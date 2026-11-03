def circuit_model(a, b):
    # Unsigned 2-bit comparator
    g = 1 if a > b else 0

    # 2-bit-wide 2:1 multiplexer
    if g == 1:
        c = a
    else:
        c = b

    return g, c

def main():
    passed = 0
    total = 0
    print("A  B  G  C  RESULT")
    for a in range(4):
        for b in range(4):
            g, c = circuit_model(a, b)
            expected = a if a > b else b
            ok = (c == expected)
            total += 1
            passed += int(ok)
            print(f"{a:02b} {b:02b}  {g}  {c:02b}  {'PASS' if ok else 'FAIL'}")
    print(f"\nVerification: {passed}/{total} cases passed.")

if __name__ == "__main__":
    main()
