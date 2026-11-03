# Expected Simulation Results

These are hand-derived expected results for validating the FSM in Logisim. They are not screenshots or captured simulator traces.

## Test 1 — Normal entry
Start CLOSED (00). Apply V=1, P=1 and clock: OPENING (01).
Apply T=1 and clock: OPEN (10).
Apply T=1, O=0 and clock: CLOSING (11).
Apply T=1, O=0 and clock: CLOSED (00).

Expected output progression:
| State | MO | MC | G | C |
|---|---:|---:|---:|---:|
| CLOSED 00 | 0 | 0 | 0 | 1 |
| OPENING 01 | 1 | 0 | 0 | 0 |
| OPEN 10 | 0 | 0 | 1 | 0 |
| CLOSING 11, O=0 | 0 | 1 | 0 | 0 |
| CLOSED 00 | 0 | 0 | 0 | 1 |

## Test 2 — Invalid payment
CLOSED with V=1, P=0. After any clock edge, state remains 00. Expected outputs: MO=0, MC=0, G=0, C=1.

## Test 3 — Obstruction while closing
Reach CLOSING (11). Set O=1. MC must immediately become 0 due to the output interlock. At the next clock edge the state becomes OPENING (01).

## Test 4 — Timer not complete
In OPENING with T=0, remain 01. In CLOSING with O=0 and T=0, remain 11.

## Test 5 — Obstruction while open
In OPEN (10), set O=1 and T=1. Remain OPEN (10); do not begin closing.

## Test 6 — Reset
Assert RESET. Both state bits must clear to 00 (check the chosen flip-flop clear polarity).

## Motor interlock check
For every state/input combination, MO and MC must never both be 1. MC is additionally forced low whenever O=1.
