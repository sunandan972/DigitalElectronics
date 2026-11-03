def alu4(a, b, mode):
    # mode 0 = add; mode 1 = subtract
    if mode == 0:
        raw = a + b
    else:
        raw = a + ((~b) & 0xF) + 1
    return raw & 0xF, (raw >> 4) & 1

def pc_step(pc, reset, enable):
    if reset:
        return 0
    if enable:
        return (pc + 1) & 0xF
    return pc

print("4-bit ALU tests")
tests = [(5, 3, 0), (15, 1, 0), (5, 3, 1), (2, 5, 1)]
for a, b, mode in tests:
    result, carry = alu4(a, b, mode)
    op = "SUB" if mode else "ADD"
    print(f"A={a:04b} B={b:04b} M={mode} {op} -> F={result:04b} Cout={carry}")

print("\n4-bit Program Counter")
pc = 0
for edge in range(13):
    reset = 1 if edge == 0 else 0
    enable = 0 if edge in (5, 6) else 1
    pc = pc_step(pc, reset, enable)
    print(f"edge={edge:2d} reset={reset} enable={enable} PC={pc:04b} ({pc})")
