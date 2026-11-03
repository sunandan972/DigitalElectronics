# Expected Simulation Results

## ALU
- 0101 + 0011 = 1000 (5 + 3 = 8).
- 1111 + 0001 = 0000 with carry-out 1 (15 + 1 = 16).
- 0101 - 0011 = 0010 (5 - 3 = 2).
- 0010 - 0101 = 1101 (4-bit two's-complement representation of -3).

`alu_exhaustive_test_vectors.csv` lists all 512 combinations.

## Program Counter
With reset asserted at clock edge 0 and enable low at edges 5 and 6, the expected decimal sequence is:
`0, 1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10`.

See `pc_expected_sequence.png`.
