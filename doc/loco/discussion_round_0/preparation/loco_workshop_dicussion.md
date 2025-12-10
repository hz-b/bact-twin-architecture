# 1. Recommended Workshop Type & Structure

Since this is a lightweight first discussion aimed at discovering workflows, sub-processes, challenges, and human-in-the-loop points — and your participants are accelerator physicists — the best format is:

# Workshop Type:

“Process-Mapping & Pain-Point Discovery Workshop” (1.5–2 hours)**

This style focuses on uncovering:

* What LOCO actually looks like in practice
* How physicists think through each step
* Where decision points happen
* What parts break or require manual interventions
* Where variability occurs between users
* What needs to be modular in the new architecture

# Suggested Agenda

## 0. Intro (5 min)
Explain: the goal is not to redesign LOCO now, but to understand its components, workflow, and user pain points.

## 1. Collaborative Mapping of the LOCO Pipeline (25–30 min)

Use a whiteboard or digital board.
Prompt them to describe the steps from ORM acquisition → model setup → fitting → corrections → validation.

You and software engineers only facilitate and document.

## 2. Identifying Human-in-the-Loop Points (20 min)
Highlight each step where users currently adjust, tune, repeat, or “trust judgment.”

## 3. Identifying “Black Boxes” and Sources of Confusion (20 min)
Ask where the algorithm is opaque or unpredictable.

## 4. Pain-Point Harvesting (15–20 min)
Physicists state frustration points with the current implementation — even subjective ones.

## 5. Architecture-Relevant Reflections (10–15 min)
Ask what flexibility they would want in a redesign.

## 6. Wrap-up (5 min)
Summarize what was learned and what will be extracted for architectural design.

# 2. Key Questions to Ask Participants (High-Value, Architecture-Oriented)

These questions are carefully chosen to extract information your software architects actually need.

## A. Understanding the LOCO workflow as practiced

* What are the exact steps you follow when you run LOCO today?
 (Let them enumerate organically; you map it.)
* Where does the workflow branch depending on lattice conditions or operation mode?
* Which steps must run online, and which can comfortably run offline?
* What inputs do you prepare manually before running LOCO?
* What outputs do you inspect manually afterward?

## B. Identifying modular components

* If LOCO were made of Lego blocks, what blocks would you expect?
(ORM acquisition, preprocessing, fit engine, parameter groups, correction generation…)
* Are there parts you frequently tweak or replace?
(BPM gains, skew quadrupoles, dispersion handling, coupling model…)
*  Which parts feel too tightly coupled in the current implementation?

## C. Human-in-the-loop points

* Where in the workflow do you make manual decisions?
 (Example: parameter weighting, bad BPM rejection, fit parameter selection.)
* What criteria do you use to decide whether the fit is “good enough”?
* Which steps rely on experience or intuition rather than automation?
* Which parts would benefit from automation, and which should stay manual?

## D. Defining pain points & constraints

* What do you find most frustrating or limiting in the current LOCO system?
  (Speed, readability, reliability, tuning difficulty, model mismatch…)
* What has historically gone wrong when running LOCO?
* Are there physics effects that the current tool doesn’t handle well?
* When the fit fails: what actions do you typically take?

## E. Desired flexibility in a reimplementation

* If you could change one thing about how LOCO is structured, what would it be?
* How important is it to be able to plug in different fitting engines (SVD, LM, etc.)?
* Do you expect to experiment with new model formulations or constraints?
* How should the new framework interact with lattice models (AT, Elegant,…)?
* Would you prefer a single coherent LOCO pipeline or multiple interchangeable workflows?

## F. Usage expectations

* How often do you expect to run LOCO (daily, weekly, only after major changes)?
* Should the new LOCO be operator-friendly, or primarily for beam physicists?
* Do you want quick-iteration “light LOCO” modes vs. full high-accuracy modes?

## Outcome of this workshop

By the end you will have a clear understanding of:

* the physics-side expectations of modularity
* the true pipeline of LOCO as used in your environment
* where decision points exist (needed for architecture)
* what should be pluggable, configurable, or replaceable
* the problems your architecture must solve
* initial requirements for a sustainable, extensible Python-friendly LOCO framework

If you want, I can also provide:

* a template slide deck for running the workshop
* a full process-map draft for typical LOCO workflows
* a preliminary modular software architecture based on common LOCO implementations
* a follow-up workshop plan for deep-dive technical sessions