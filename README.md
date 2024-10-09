# Accelerator digital twin architecture: data models and interfaces

**NB**: accelerator is here a short form for
particle accelerators.


This package shall collect data models and interfaces that
are required to

* interact with a digital twin of an accelerator
* provide the infrastructure that the same applications can
  talk to the accelerator as much as to the underlying twin.


## Guideline

* An accelerator design consists of a *a sequence of lattice elements*.
* *Devices* are designed, built and tested to provide.
  the expected *lattice element performance* in the *real world*.
* They are assembled together to realise the *accelerator*.
* The accelerator is then commissioned to provide its expected performance.


## Implementation concepts
### Observation

The concept is built on the observation that at least two different spaces
exist:

1. How an accelerator lattice is designed and developed: it describes
   the lattice as a sequence of elements. The parameters of the elements
   are independent of the beam energy: at least for the magnets; some
   codes treat the energy as a parameter of the beam, others implement
   cavities with scaled voltages.
   Furthermore, some codes allow for placing "artificial kicks" at e.g.
   quadrupole or sextupole magnets.
2. The parameters or *process variables* a real world accelerator provides.
   These are typically currents supplied to the magnets, frequency or voltage
   of the RF power supplies.

The first world is often called the `physics space`
while the second one is called the  `engineering space`. So if one e.g. wants
to translate a quadrupole gradient, one would change the 'K'-value of the
corresponding quadrupole in the lattice, while one would change the
current of the power converter of the power supply that drives it.

This requires the following steps:
* one recognices that setting the 'K' involves a command with the following values:
  (name of the quadrupole, property, value)
* these have to be translated to
  (name of the quadrupole power converter, property value)

In this particular case the translation would be for BESSY II:

* from physics space: ('q1m1d1r', 'K', 1.2)
* to engineering space ('q1p1d1r', 'current', 240)

So one realises that the tuple of (name, property) have to be translated to
another tuple of (name, property). Furthermore, the value has to be mapped
from on space to the other.

Steerer magnets are commonly cowound on the sextupole magnets for BESSY II
or other light sources. In this case the follow would have to be mapped

* from physics space: ('s1m1d1r', 'y_kick', 1e-4)
* to engineering space ('vs1m1dr', 'current', 0.1)


### Realisation

This functionality is realised by:
 * `IdentifierPropertyTransformer`: this transforms the identifier and property
    from one space. The `forward` method transforms from physics space to
    engineering space.
 * `State conversion`: this transforms the value.

Please note: these two objects work on single (name, property) tuples.
