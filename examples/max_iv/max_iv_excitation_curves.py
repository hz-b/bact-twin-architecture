import json
import jsons
import pprint
from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, Sequence, Union, Literal, List

from bact_twin_architecture.data_model.conversion_info import CurvePoint
from bact_twin_architecture.data_model.harmonic_id import Harmonic
from bact_twin_architecture.data_model.location import SectorCellBasedLocationName


@dataclass
class MaxIVR1ExcitationMetaData:
    trl: str
    loc: SectorCellBasedLocationName


@dataclass
class MaxIVR1ExcitationDataImport:
    harmonic : Harmonic
    md: MaxIVR1ExcitationMetaData
    curve: Sequence[CurvePoint]


@dataclass
class MaxIVR1ExcitationDataSingleCurve:
    harmonic: Harmonic
    curve: Sequence[CurvePoint]


@dataclass
class MaxIVExcitationData:
    md: MaxIVR1ExcitationMetaData
    curves: Sequence[MaxIVR1ExcitationDataSingleCurve]


def create_curve_points(d: Dict[str, Union[str, float]]) -> Sequence[CurvePoint]:
    col_pairs = [(f"I_{cnt:03d}", f"h_{cnt:03d}") for cnt in range (1, 12 +1)]
    return [CurvePoint(d.pop(cp[0]), d.pop(cp[1])) for cp in col_pairs]


def create_model_for_record(d: Dict[str, Union[str, float]]) -> MaxIVR1ExcitationDataImport:
    cp = create_curve_points(d)
    sector = int(d.pop("sector"))
    cell = int(d.pop("cell"))
    subcell = int(d.pop("subcell"))
    hnum = int(d.pop("harmonic"))
    for col in range(3):
        assert d.pop(f"empty_{col:03d}") is None
    r = MaxIVR1ExcitationDataImport(
        md=MaxIVR1ExcitationMetaData(
            trl=d.pop("trl"),
            loc=SectorCellBasedLocationName(
                sector=sector,
                cell=cell,
                subcell=subcell,
            ),
        ),
        harmonic=Harmonic(type="unknown", number=hnum),
        curve=cp,
    )
    assert d == {}
    return r


def combined_model(data: Sequence[MaxIVR1ExcitationDataImport]) -> MaxIVExcitationData:
    # make sure that all refer to the same location
    md = data[0].md
    for datum in data[1:]:
        assert datum.md == md

    r =  MaxIVExcitationData(
        md=md,
        curves=[MaxIVR1ExcitationDataSingleCurve(harmonic=d.harmonic, curve=d.curve) for d in data]
    )
    return r


def fix_curve_data(data: Sequence[CurvePoint]) -> Sequence[CurvePoint]:
    """remove empty excitation points"""
    r: List[CurvePoint] = []
    for point in data:
        if point.indep is None or point.dep is None:
            if not (point.indep is None and point.dep is None):
                print(f"{point=} contains only part" )
                # assert point.indep is None and point.dep is None
            continue
        r.append(point)
    return r

def fix_harmonic_types(data: MaxIVExcitationData) -> MaxIVExcitationData:
    return MaxIVExcitationData(
        md=data.md,
        curves=[
            MaxIVR1ExcitationDataSingleCurve(
                harmonic=Harmonic(type="normal", number=c.harmonic.number),
                curve=fix_curve_data(c.curve)
            )
            for c in data.curves
        ]
    )


def main(filename):
    with open(filename) as fp:
        data = json.load(fp)

    tmp = []
    failed = []
    for line_cnt, d in enumerate(data):
        try:
            t = create_model_for_record(d.copy())
        except:
            failed.append(dict(line=line_cnt, data=d))
            continue
        tmp.append(t)

    del d

    print("Failed to convert")
    pprint.pprint(failed)

    lut2_ = defaultdict(list)
    for info in tmp:
        lut2_[info.md.trl].append(info)
    #pprint.pprint(lut)
    lut1_ = {trl : combined_model(d) for trl, d in lut2_.items() }
    lut  = {trl : fix_harmonic_types(d) for trl, d in lut1_.items()  }
    d = jsons.dump(lut)

    with open("maxiv_r1_excitation_curves.json", "wt") as fp:
        json.dump(d, fp, indent=2)


if __name__ == "__main__":
    main("../mml-exported-data-sets/maxiv/r1/maxiv_excitation_curves_from_excel.json")
