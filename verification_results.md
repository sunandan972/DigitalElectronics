# Verification Results

The reference verification checks all 16 possible combinations of two 2-bit inputs.

For each pair:
1. Compute `G = (A > B)`.
2. Select `C = A` if G=1, else `C = B`.
3. Compare against the expected unsigned maximum.

Expected result: 16/16 combinations pass.

Representative results:
| A | B | G | C |
|---|---|---:|---|
| 00 | 00 | 0 | 00 |
| 01 | 10 | 0 | 10 |
| 10 | 01 | 1 | 10 |
| 11 | 00 | 1 | 11 |
| 11 | 11 | 0 | 11 |
