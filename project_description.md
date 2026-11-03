# Project Description

## Real-world system
An automatic parking barrier controls vehicle entry into a parking facility. A vehicle sensor detects arrival, a payment-valid signal authorizes entry, a timer controls the opening/hold/closing phases, and an obstruction sensor prevents the barrier from continuing to close when an object is detected.

## Why an FSM?
The controller must remember which phase of operation it is in. A Moore FSM stores the current phase in two D flip-flops and generates motor/indicator outputs from the stored state.

## Constraints and assumptions
- One vehicle transaction is handled at a time.
- Payment is represented by a single Boolean input.
- Timer completion is supplied externally as `T`.
- Timer restart and duration generation are outside this FSM.
- Obstruction detection inhibits the closing motor immediately and requests reopening at the next clock edge.
- The design is a teaching model, not a safety-certified real-world controller.

## Combinational and sequential design
The two state flip-flops are the sequential portion. The next-state equations and output equations are combinational logic.
