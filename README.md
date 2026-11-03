# Application Mapping of Sequential Building Blocks

**Lab Assignment 6 — Digital Electronics**

This repository maps three sequential building blocks to practical systems and provides Logisim Evolution circuit projects, verification vectors, and simulation procedures.

## Project contents

```text
Sequential-Circuits-Applications/
├── 01_FlipFlop/
│   └── D_FlipFlop.circ
├── 02_Mod60_Counter/
│   └── Mod60_Counter.circ
├── 03_Shift_Register/
│   └── SIPO_Register.circ
├── tests/
│   ├── D_FlipFlop.txt
│   ├── SIPO_1011.txt
│   └── Mod60_Checklist.md
├── screenshots/
├── README.md
└── .gitignore
```

## Software

- Logisim Evolution 3.x
- Java runtime (if running the JAR distribution)
- Git

Download Logisim Evolution from its official project releases: https://github.com/logisim-evolution/logisim-evolution/releases

## 1. D flip-flop — CPU register bit

**Real system:** A CPU register stores instruction, address, and data bits. One D flip-flop stores one bit; an n-bit register is built from n storage bits sharing a clock.

**Circuit:** `01_FlipFlop/D_FlipFlop.circ`

**Simulation:** Open the file. Set D to 1, then apply a rising clock edge. Q should become 1. Change D back to 0 without a rising edge; Q should remain 1. Apply another rising edge; Q should become 0. Repeat with D=1. This demonstrates edge-triggered storage and retention.

**Expected sequence:** D=1 + rising edge → Q=1; D changes to 0 while clock is steady → Q remains 1; next rising edge → Q=0.

**Test vectors:** `tests/D_FlipFlop.txt` (load using the Test Vector feature if supported by your Logisim Evolution version).

## 2. Mod-60 counter — digital clock seconds

**Real system:** A digital clock counts seconds from 00 through 59. On the next clock event it rolls over to 00 and generates a carry to increment the minutes.

**Circuit:** `02_Mod60_Counter/Mod60_Counter.circ`

The counter is configured as a 6-bit counter with maximum value 59 (hex 0x3B). Six bits are required because 2^5 < 60 ≤ 2^6.

**Simulation:** Start the clock and use single-step/manual clock pulses for a clear demonstration. Verify the checkpoints in `tests/Mod60_Checklist.md`: 00, 01, 02, 09, 10, 58, 59, 00, 01. If the counter does not advance, inspect the component's Enable and Clear inputs in the Properties/connection view and ensure Enable is asserted and Clear is inactive. To demonstrate a full clock, cascade a second Mod-60 counter using the first counter's terminal-count/carry output.

**Important:** A practical 00–59 clock display is commonly implemented as two cascaded BCD decade stages (units 0–9 and tens 0–5), or as a 6-bit Mod-60 counter with BCD/decimal display conversion. The supplied counter demonstrates the modulo-60 state sequence; it is not a complete HH:MM:SS clock.

## 3. Shift register — serial communication

**Real system:** A serial receiver collects incoming bits one at a time and presents a parallel byte to the processor. A transmitter performs the reverse operation. UARTs commonly contain shift-register stages for serializing and deserializing data; SPI also uses shift registers.

**Circuit:** `03_Shift_Register/SIPO_Register.circ`

The four-stage SIPO circuit shifts the serial input toward the most significant stage on each rising clock edge. Shift in `1, 0, 1, 1` (one bit per rising edge). After the fourth edge, the register should contain `1011` when read as Q3 Q2 Q1 Q0.

**PISO demonstration:** In Logisim Evolution, create a second circuit named `PISO_Register`. Place a 4-bit Shift Register component from the Memory library. Set its data width to 4, enable parallel load, and expose parallel data inputs D3..D0, Shift/Load control, clock, serial output, and (if available) parallel Q outputs. Load `1011`, select shift mode, then pulse the clock four times. The serial output should emit the stored bits in the configured shift order. Record the chosen bit order in your screenshot/notes. This is the transmitter-side complement to SIPO reception.

**Test vectors:** `tests/SIPO_1011.txt`.

## How to run

1. Install and launch Logisim Evolution.
2. Open each `.circ` file using **File → Open**.
3. Use the Poke tool to change input pins and the clock controls.
4. Use **Simulate → Tick Once** (or the toolbar tick control) for manual clocking. Use **Simulate → Ticks Enabled** only when you want continuous operation.
5. Capture screenshots showing the circuit and its outputs at the key states.
6. Save screenshots in `screenshots/` and update this README with your observed results.

## Evidence to capture for submission

- `flipflop_hold.png`: D changes while clock is steady; Q holds its previous state.
- `mod60_59.png`: counter displays 59.
- `mod60_rollover.png`: next clock edge displays 00.
- `sipo_1011.png`: four serial bits have become parallel output 1011.
- `piso_serial_out.png`: PISO loaded with 1011 and shifting bits out serially.

Screenshots should come from your own Logisim run. Do not use illustrative internet images as proof of simulation.

## GitHub upload

From the parent directory of this project:

```bash
git init
git add .
git commit -m "Add Logisim sequential circuit application simulations"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/Sequential-Circuits-Applications.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. Create an empty repository on GitHub first; do not initialize it with a README if you are pushing this existing folder.

## Notes on verification status

The project files and test vectors are provided as editable Logisim Evolution project assets. The circuits have not been launched in a local Logisim GUI in this build environment. Open them in your installed Logisim Evolution version, verify the pin connections and counter control pins, and save the resulting screenshots as evidence before submitting. The PISO circuit is specified as a reproducible build step rather than included as a pre-verified `.circ` file.
