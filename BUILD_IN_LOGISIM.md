# Build the circuit in Logisim Evolution

This folder contains the implementation recipe rather than a falsely-labelled simulator screenshot or unverified `.circ` file.

1. Create a circuit named `Parking_Barrier_Controller`.
2. Place two rising-edge D flip-flops. Label their Q outputs `Q1` and `Q0`.
3. Add input pins `V`, `P`, `T`, `O`, and `RESET`; add one shared clock.
4. Build the two next-state networks from the equations in `README.md`.
5. Connect `D1` and `D0` to the D inputs.
6. Connect RESET to asynchronous clear (verify polarity), or implement synchronous reset by forcing D1=D0=0 when RESET=1.
7. Build the four output equations from `README.md`.
8. Add LEDs/output pins for MO, MC, G, C.
9. Use the test sequences in `Simulation_Outputs/expected_results.md`.
10. Save as `Parking_Barrier_Controller.circ` and capture genuine screenshots from the running Logisim window.

Important: the timer-complete signal `T` is manually driven in this basic model. A practical timed controller needs a timer circuit that restarts on entry to each phase.
