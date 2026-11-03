# Design Notes

## 1. Four-bit ALU

Inputs: `A[3:0]`, `B[3:0]`, mode `M`.
Outputs: `F[3:0]`, `Cout`.

- `M=0`: addition, `F = A + B` (modulo 16).
- `M=1`: subtraction, `F = A - B` (modulo 16).

Use one 4-bit adder:
`F = A + (B XOR {4{M}}) + M`

The mode bit controls four XOR gates and the adder carry-in. For subtraction, `Cout=1` means no borrow in this two's-complement implementation. The 4-bit result wraps around modulo 16.

Examples:
- A=0101 (5), B=0011 (3), M=0 -> F=1000 (8).
- A=0101 (5), B=0011 (3), M=1 -> F=0010 (2).
- A=0010 (2), B=0101 (5), M=1 -> F=1101 (13), representing -3 in 4-bit two's complement.

## 2. Four-bit Program Counter

Inputs: `CLK`, active-high synchronous `RESET`, `EN`.
Output: `PC[3:0]`.

At each rising clock edge:
- RESET=1 -> PC becomes 0000.
- RESET=0 and EN=1 -> PC increments by one.
- RESET=0 and EN=0 -> PC holds its previous value.

The counter wraps from 1111 to 0000.

## 3. Mapping code to hardware

For `c = a + b;`:
- Register A holds `a`.
- Register B holds `b`.
- The ALU performs addition with M=0.
- A destination/result register stores `c` on the clock edge.

For `for (i=0; i<8; i++)`:
- The PC represents the address of the next instruction, not the loop variable itself.
- The PC advances to the next instruction each instruction cycle.
- A comparison/branch decision and control logic implement the loop condition and jump back to the loop body.
- A separate register stores `i`; an incrementer/ALU updates `i`.
- This assignment's 4-bit PC is a simplified sequencing model. A real CPU PC usually increments by instruction length and can be loaded with a branch target.

## 4. Scope
This is an educational functional model, not a complete CPU. It omits instruction decoding, memory, branch-target calculation, and pipeline control.
