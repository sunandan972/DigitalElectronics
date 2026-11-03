# Build in Logisim Evolution

Create a circuit named `Max_Selector_2bit`.

## Inputs and outputs
Inputs: `A1`, `A0`, `B1`, `B0`.
Outputs: `G`, `C1`, `C0`.

## Comparator
Implement:
`G = (A1 AND NOT B1) OR ((A1 XNOR B1) AND A0 AND NOT B0)`

Use:
- NOT gates for `B1` and `B0`.
- AND gate for `A1 AND NOT B1`.
- XNOR gate for `A1` and `B1`.
- AND gate for `A0 AND NOT B0`.
- AND gate for `HEQ AND LGT`.
- OR gate to combine `HGT` and the second term.

## Two-bit MUX
For each bit i=0,1:
`Ci = (G AND Ai) OR (NOT G AND Bi)`

Build each MUX bit from two AND gates and one OR gate, sharing the inverter for G.

## Testing
Use Logisim input pins or switches for A1,A0,B1,B0. Attach probes or LEDs to G,C1,C0. Test all 16 combinations from the CSV truth table. Capture screenshots from your own Logisim session.

## Width and signedness
Set the inputs as unsigned 2-bit values. If you choose a wider bus or signed values, the comparator implementation must be changed accordingly.
