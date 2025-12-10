# Challenges of reimplementing Loco

Participants: Sebastien Joly, Benat ...., Waheedullah Sulaiman Khail, Markus Ries, Pierre Schnizer
Date: 9. December 2025

## Main outcome

* Fit per se considered working as provided by the Levenberg Marquardt fit (Trusted region ?)?
* Have fine control of which fit parameters are used at the current fitting step
* Results depend heavily of fit targets
* Minimise wait time for the user e.g.
  * computation of FIT parameters: 
    Verify: MML computes one after the other
  * provide import of used / computed Jacobian
  * provide import of used / computed model info
* Focus on providing debug information / simplifying debugging: not necessarily code implementation
  * identifying malfunctioning devices
  * incomplete / inadequate model: e.g. wavelength shifter missing
* Good documentation always helpful


## Preparation or qualification of the machine

* Machine is set to a different state:
  * e.g. a steerer current is changed

* Ensure for measurement
  1. Measurements are preformed at "steady state": i.e. all
     settings have stabilised with sufficient accuracy
  2. Minimize the overall measurement time: e.g. wait and  
     check device response or have good estimates of slew rate
     etc...
    
## Input required by Loco    

* Differential orbits produced by the different actuators
  (Todo: can one only fit if the actuator was used in the model ?)
* Jacobian for parameter dependence: be aware it needs to be
  normalised
  

### Extensions
Use other observables than only beam position data: e.g. phase advance

* (post meeting comment: curly H? measure of local emittance? )
* (resonance driving terms= )

## What does Loco provide

* Many different options: 
  * but standard: 
    * new "K" parameters for the quadrupoles 
    * and new "BPM" gains
    * BPM offsets: typically by Beam Based Alignment

* Additionally:
  * e.g. skew quadrupole conversion factors
  * (skew quadrupole offsets)
  * 

## Options for fitting the model to the response matrix measurement

* user shall be able to select different parameters to fit
* Jacobian should be able to provide more than actually required for the current fit
* general fit parameters:
  * rtol relative tolerance, 
  * atol absolute tolerance
  * ftol tolerance on function variation
  * max iter maximum number of iterations
  * Levenberg Marquardt Lambda
  * constraint fit: i.e. parameters are only allowed to vary in a certain range


## Extensions

* Provide extension to non-linear effects
* e.g. noise of beam position monitors:
  * not (only) as single measurement, which estimates (stability of the machine)
  * but as weights for the individual measurements

## When iterations are performed

Iteration
1. Setup
   1. configuration: control system interface
   3. machine reaction description: by sufficient device supervision
      or model of slew rates and assosiated wait times
   4. machine preparation: get it ready for measurement
2. measure response matrix
   3. selection of a set of parameters 
   4. associated ranges or values of these parameters
2. execute FIT of parameters
   1. selection of model
   2. selection of fit parameters (a sub set of the ones used for measuring response matrix)
3. FIT result: evaluation of quality
    1. recheck of used model: e.g. wavelength shifter  (WLS) not in model but in machine
       check by adding WLS into ring or comparison measurement without shifter
4. update model (typically small corrections to the original parameter set)
4. (post meeting comment: update machine settings)
5. start at point 1.

When iterations are done, use different set of parameters for 
different fits 


## Data inspections

### 3D Plots

* Response matrix and Jacobian
* correlation between the fit parameters: 
  similar to [confusion matrix](https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html#sphx-glr-auto-examples-model-selection-plot-confusion-matrix-py)

* Effect of different actuators:
  * e.g. dispersion of model vs measured dispeersion

## Overview of fit space

E.g. for BESSY II

* 144 quadrupoles K-values
* 100 correctors strength
* 100 bpm (gains)



## Not mentioned: preliminary considerations made writing the minutes

* Architecture should provide access to data at many different levels
* Data documented in well understandable formats