# Design Equations and Explanation

## 1. Code-to-hardware mapping

Code:
```c
if (a > b)
    c = a;
else
    c = b;
```

Assume `a` and `b` are unsigned 2-bit values, from 0 to 3.

- Comparator: evaluates `A > B`.
- Multiplexer: selects A when comparator output G=1, otherwise selects B.
- Output C: receives the selected 2-bit value.
- Registers: in a clocked processor, operand registers hold A and B, and a destination register stores C. The combinational comparator/MUX alone does not provide storage.

## 2. Comparator equations

Let A = A1A0 and B = B1B0.

Define:
- `HGT = A1 AND NOT(B1)`
- `HEQ = A1 XNOR B1`
- `LGT = A0 AND NOT(B0)`

Then:

`G = HGT OR (HEQ AND LGT)`

This is lexicographic comparison: the most significant bit decides unless equal, in which case the least significant bit decides.

## 3. Multiplexer equations

For each output bit i:

`Ci = (G AND Ai) OR (NOT(G) AND Bi)`

Therefore:
- if A > B, G=1 and C=A.
- if A <= B, G=0 and C=B.

When A=B, either MUX input has the same value, so the code's `else` branch is represented correctly.

## 4. Reflection / AI correction

An initial AI explanation might say only “use a comparator and a MUX.” That is a correct block-level idea, but incomplete for implementation:
1. It must specify operand width and whether values are signed or unsigned.
2. A 2-bit comparator must compare the most significant bit first, then the lower bit only when the upper bits are equal.
3. The MUX must be 2 bits wide, not a 1-bit MUX.
4. Equality must select B because the source code uses `if (a > b)`, not `if (a >= b)`. The output is numerically identical when A=B, but the select signal differs.
5. The combinational circuit does not store variables. Registers are needed to hold operands and the destination value in a sequential CPU datapath.

The corrected design uses an unsigned 2-bit comparator and a 2-bit-wide MUX.
