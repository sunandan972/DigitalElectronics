# Build the circuits in Logisim Evolution

Create two circuits: `ALU4` and `ProgramCounter4`.

## A. ALU4

### Pins
Inputs: A3..A0, B3..B0, M.
Outputs: F3..F0, Cout.

### Components
- One 4-bit adder (Arithmetic → Adder; set Data Bits to 4).
- Four 2-input XOR gates.
- One constant or wire for the adder carry-in controlled by M.
- Splitters to route the four B bits through XOR gates and into the adder.
- LEDs/probes for F3..F0 and Cout.

### Connections
1. Connect A directly to adder input A.
2. Connect each B bit to one XOR gate.
3. Connect M to the other input of all four XOR gates.
4. Connect XOR outputs to adder input B.
5. Connect M to adder carry-in.
6. Observe sum output as F and carry output as Cout.

If your Logisim version's adder exposes carry-in as a separate pin, connect M there. If it does not, construct the adder from full-adder stages.

## B. ProgramCounter4

### Pins
Inputs: CLK, RESET, EN.
Outputs: Q3..Q0.

### Components
- Four D flip-flops, each configured for rising-edge triggering.
- A 4-bit incrementer (or a 4-bit adder with constant 0001).
- A 2:1 mux for each D input, or equivalent gates.
- A reset-priority path.

### Required next-state logic
`D = RESET ? 0000 : (EN ? Q + 0001 : Q)`

Connect the same clock to all four D flip-flops. Connect each D output to its corresponding Q output. Use RESET to select zero first; otherwise EN selects incremented value or feedback Q. Probe Q3..Q0.

## Simulation
- ALU: toggle M and enter the test values from `Design/test_plan.md`.
- PC: pulse the clock after setting RESET and EN. Test reset, count, hold and wraparound.
- Save screenshots from your own running Logisim window; do not label reference diagrams as actual Logisim captures.
