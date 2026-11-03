# Lab Assignment 7 — Mini Automation System
## Automatic Parking Barrier Controller (Logisim Evolution)

This repository contains the design package for a four-state Moore FSM parking-barrier controller.

### Inputs
- `V`: vehicle detected
- `P`: payment valid
- `T`: current phase timer complete
- `O`: obstruction detected
- `RESET`: active-high controller reset

### Outputs
- `MO`: opening motor command
- `MC`: closing motor command (inhibited immediately by obstruction)
- `G`: gate fully-open indicator
- `C`: gate fully-closed indicator

### State encoding
| State | Q1 Q0 | Meaning |
|---|---|---|
| CLOSED | 00 | Waiting for a valid vehicle/payment |
| OPENING | 01 | Opening motor active |
| OPEN | 10 | Gate held open |
| CLOSING | 11 | Closing motor active unless obstructed |

### FSM transition rules
- CLOSED: go to OPENING when `V=1` and `P=1`; otherwise stay CLOSED.
- OPENING: stay OPENING while `T=0`; go to OPEN when `T=1`.
- OPEN: stay OPEN while `T=0` or `O=1`; go to CLOSING when `T=1` and `O=0`.
- CLOSING: go to OPENING whenever `O=1`; otherwise stay CLOSING while `T=0`, and go to CLOSED when `T=1`.

### Next-state equations
For `Q1+ = D1`, `Q0+ = D0`:

`D1 = (~Q1 & Q0 & T) | (Q1 & ~Q0) | (Q1 & Q0 & ~O & ~T)`

`D0 = (~Q1 & ~Q0 & V & P) | (~Q1 & Q0 & ~T) | (Q1 & ~Q0 & T & ~O) | (Q1 & Q0 & (O | ~T))`

### Output equations
- `MO = ~Q1 & Q0`
- `MC = Q1 & Q0 & ~O`
- `G = Q1 & ~Q0`
- `C = ~Q1 & ~Q0`

The motor commands are mutually exclusive by construction. The closing motor is combinationally inhibited whenever `O=1`; the FSM returns to OPENING on the next active clock edge.

### Timer interface
`T` is a phase-complete input from an external timer. In a physical implementation, the timer must be restarted on entry to each timed phase (OPENING, OPEN, CLOSING). For a simple Logisim demonstration, drive `T` manually using an input pin and apply clock edges.

### Simulation
See `Simulation_Outputs/expected_results.md` and the PNG reference diagrams. These are expected logical outputs, not screenshots captured from a running Logisim session.

### Logisim implementation note
Create a Logisim Evolution circuit named `Parking_Barrier_Controller` with:
1. Two rising-edge-triggered D flip-flops storing `Q1` and `Q0`.
2. Combinational gates implementing `D1` and `D0` above.
3. Output logic implementing `MO`, `MC`, `G`, and `C`.
4. A shared clock and reset connected to both state flip-flops.
5. Input pins for `V`, `P`, `T`, and `O`.

For reset, use the flip-flops' clear input if available and configure its active polarity correctly. If using a synchronous reset instead, implement `D1=0`, `D0=0` whenever RESET=1.

### Safety and scope
This is an educational logic model, not a certified barrier controller. A real installation needs independent safety-rated obstruction sensing, motor limit switches, emergency stop, fault detection, watchdogs, and hardware interlocks.
