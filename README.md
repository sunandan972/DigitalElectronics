# Lab Assignment 8 — 4-bit Mini-ALU and Program Counter

## Project contents
- `Design/alu_architecture.png`: shared-adder ALU architecture.
- `Design/code_to_hardware_mapping.png`: mapping from code to hardware blocks.
- `Simulation_Outputs/alu_exhaustive_test_vectors.csv`: all 512 ALU input combinations.
- `Simulation_Outputs/pc_expected_sequence.png`: expected PC sequence with reset and enable.
- `Simulation_Outputs/expected_results.md`: representative expected results and edge cases.
- `Code/simulate_assignment8.py`: runnable Python reference simulator.
- `Logisim/BUILD_IN_LOGISIM.md`: component-level construction guide for Logisim Evolution.

**Important:** These are reference simulations and expected-output artifacts. This package does not contain a verified, executable Logisim `.circ` file or screenshots captured from a running Logisim session. Build the circuits using the included Logisim guide, then replace/add genuine Logisim screenshots before submission if your instructor requires them.

## Quick start
```bash
python3 Code/simulate_assignment8.py
```
