# Test Plan

## ALU representative tests

| A | B | M | Expected operation | F | Cout |
|---|---|---:|---|---|---:|
| 0101 | 0011 | 0 | 5 + 3 | 1000 | 0 |
| 1111 | 0001 | 0 | 15 + 1 | 0000 | 1 |
| 0101 | 0011 | 1 | 5 - 3 | 0010 | 1 |
| 0010 | 0101 | 1 | 2 - 5 | 1101 | 0 |
| 0111 | 0111 | 0 | 7 + 7 | 1110 | 0 |
| 0000 | 0001 | 1 | 0 - 1 | 1111 | 0 |

The CSV file contains every combination of A, B and M (16 × 16 × 2 = 512 tests).

## Program counter tests

1. RESET=1 at a rising edge: PC -> 0000.
2. RESET=0, EN=1: PC increments by one.
3. RESET=0, EN=0: PC holds its value.
4. PC=1111 and EN=1: PC wraps to 0000.
5. RESET and EN both 1: reset takes priority.
