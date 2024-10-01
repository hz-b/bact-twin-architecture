from dataclasses import dataclass


@dataclass(eq=True)
class StandardIdentifier:
    """Is that the standard approach for MML
    """
    # name: str
    family_name : str
    child_number : int


