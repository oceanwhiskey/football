import sys


def signature(s: str):
    positions_a = []
    positions_b = []

    for index, team in enumerate(s):
        if team == "A":
            positions_a.append(index)
        else:
            positions_b.append(index)

    # Legal transfers change each team size by two, so both counts must stay odd.
    if len(positions_a) % 2 == 0 or len(positions_b) % 2 == 0:
        return None

    median_a = positions_a[len(positions_a) // 2]
    median_b = positions_b[len(positions_b) // 2]
    left = min(median_a, median_b)
    right = max(median_a, median_b)

    return left, right, s[left : right + 1]


def solve(n: int, p: str, q: str) -> bool:
    """Return whether arrangement p can be transformed into arrangement q."""
    if len(p) != n or len(q) != n:
        return False
    if p == q:
        return True

    p_signature = signature(p)
    q_signature = signature(q)
    return p_signature is not None and p_signature == q_signature


def main() -> None:
    data = sys.stdin.buffer.read().split()
    test_cases = int(data[0])
    answers = []
    cursor = 1

    for _ in range(test_cases):
        n = int(data[cursor])
        p = data[cursor + 1].decode()
        q = data[cursor + 2].decode()
        cursor += 3

        answers.append("YES" if solve(n, p, q) else "NO")

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()
