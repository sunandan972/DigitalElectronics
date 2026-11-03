# Lab Assignment 9 — AI-Assisted Code-to-Gate Explainer

## Chosen code
```c
if (a > b)
    c = a;
else
    c = b;
```

## Hardware interpretation
A 2-bit unsigned magnitude comparator generates `G = (A > B)`. The signal G controls a 2:1, 2-bit-wide multiplexer:
- G=1 selects A.
- G=0 selects B.

The selected MUX output is C. The complete truth table contains all 4 × 4 = 16 input pairs.

## Package contents
- `Design/`: labelled block diagram, comparator logic diagram, equations and write-up.
- `Simulation_Outputs/complete_truth_table.csv`: exhaustive 16-row truth table.
- `Simulation_Outputs/verification_results.md`: test summary and representative cases.
- `Code/verify_circuit.py`: runnable Python reference verification.
- `Logisim/BUILD_IN_LOGISIM.md`: steps to construct and test the circuit.

**Transparency note:** The diagrams are reference design diagrams, not screenshots from a running Logisim session. This package does not include a verified executable `.circ` file. Build it in Logisim using the included guide and capture genuine screenshots if required by your instructor.

## Run verification
```bash
python3 Code/verify_circuit.py
```
