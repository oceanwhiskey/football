import sys


def key_for(s: str):
    """Canonical invariant of a valid state, or None for invalid parity."""
    total_a = s.count("A")
    total_b = len(s) - total_a
    if total_a % 2 == 0 or total_b % 2 == 0:
        return None

    seen_a = seen_b = 0
    pos_a = pos_b = -1
    median_a = total_a // 2
    median_b = total_b // 2

    for i, ch in enumerate(s):
        if ch == "A":
            if seen_a == median_a:
                pos_a = i
            seen_a += 1
        else:
            if seen_b == median_b:
                pos_b = i
            seen_b += 1

    left = min(pos_a, pos_b)
    right = max(pos_a, pos_b)
    return left, right, s[left : right + 1]


def can_transform(p: str, q: str) -> bool:
    key_p = key_for(p)
    key_q = key_for(q)
    return key_p is not None and key_p == key_q


def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    it = iter(data)
    t = int(next(it))
    out = []

    for _ in range(t):
        _ = int(next(it))
        p = next(it).decode()
        q = next(it).decode()
        out.append("YES" if can_transform(p, q) else "NO")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
