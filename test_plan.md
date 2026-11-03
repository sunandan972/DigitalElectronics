# Test Plan

Test every pair A,B in {0,1,2,3}. The complete set is in `Simulation_Outputs/complete_truth_table.csv`.

Important edge cases:
- A=B: G=0, C=B (same value as A).
- A=0, B=3: G=0, C=3.
- A=3, B=0: G=1, C=3.
- A=2, B=1: G=1, C=2.
- A=1, B=2: G=0, C=2.

Expected property for every row: `C = max(A,B)` for unsigned two-bit values.
