"""
Solver for the "Football Teams" problem (see original_problem.md).

This implements the theorem proved in football.tex, translated from German
and re-verified here against brute force (see below).

Setup (1-indexed): n even, L = {1, ..., n/2-1}, R = {n/2+2, ..., n}.

football.tex proves:

  * A single transfer (i, j) is only ever possible with i in L and j in R.
    In particular, positions n/2 and n/2+1 can NEVER change teams.
    => p and q must already agree at n/2 and n/2+1 (necessary condition;
       see note below -- this is proven in the tex but not folded into
       its final theorem statement).

  * For i in L, "i is tauschbar" (exchangeable) is a condition on p alone,
    obtained by checking whether i could pair with the fixed index n.
    Symmetrically for j in R, checking against index 1.
    Tauschbar-ness is monotone: if i in L is tauschbar, every i' <= i is
    tauschbar too (mirrored for R with j' >= j). So the tauschbar set of L
    is a prefix {1..t}, and the tauschbar set of R is a suffix {s..n}.
    It is also invariant under reachability (depends only on p's
    equivalence class, not the specific string).

  * Define left/right "balance" b_L(p), b_R(p) = (#{i: p_i=1,q_i=0}
    - #{i: p_i=0,q_i=1}), restricted to L / R respectively. p is
    "balanced" iff b_L(p) == b_R(p) (every transfer changes both balances
    by the same +-1, so their difference is invariant).

  THEOREM: (n, p, q) is solvable iff
      (a) p and q agree at positions n/2 and n/2+1, AND
      (b) p is balanced (b_L == b_R), AND
      (c) every i in L with p_i != q_i is tauschbar, and every j in R
          with p_j != q_j is tauschbar.
  By monotonicity, (c) only needs checking at the extremal differing index
  in each of L and R (closest to the center) -- giving an O(n) algorithm.

Verification: implemented directly and checked against an independent
brute-force BFS over the true transfer graph, for every (p, q) pair with
n = 4, 6, 8, 10 (279,616 pairs total): 0 mismatches. Condition (a) is
included explicitly -- omitting it (as the tex's final theorem literally
states it) causes thousands of wrong answers in that same test, since it
is proven earlier in the document but not restated in the final theorem.
"""

import sys


def solve_case(n, p_str, q_str):
    # 1-indexed arrays with 1 <-> 'A', 0 <-> 'B'; index 0 unused.
    p = [0] * (n + 1)
    q = [0] * (n + 1)
    for i in range(1, n + 1):
        p[i] = 1 if p_str[i - 1] == 'A' else 0
        q[i] = 1 if q_str[i - 1] == 'A' else 0

    ones_q = sum(q[1:])
    if ones_q % 2 == 0 or (n - ones_q) % 2 == 0:
        return "NO"  # q must keep both team sizes odd, same as p

    mid1, mid2 = n // 2, n // 2 + 1
    if p[mid1] != q[mid1] or p[mid2] != q[mid2]:
        return "NO"  # the two central players can never change teams

    prefix1 = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix1[i] = prefix1[i - 1] + p[i]

    def ones_between(i, j):   # count of 1's with i < k < j
        return prefix1[j - 1] - prefix1[i]

    def zeros_between(i, j):
        return (j - i - 1) - ones_between(i, j)

    def ones_outside(i, j):   # count of 1's with k < i or k > j
        return prefix1[i - 1] + (prefix1[n] - prefix1[j])

    def zeros_outside(i, j):
        return (n - 2 - (j - i - 1)) - ones_outside(i, j)

    def tauschbar_L(i):
        o, ob = ones_between(i, n), ones_outside(i, n)
        z, zb = zeros_between(i, n), zeros_outside(i, n)
        return (o > ob + p[i] - p[n]) and (z > zb - p[i] + p[n])

    def tauschbar_R(j):
        o, ob = ones_between(1, j), ones_outside(1, j)
        z, zb = zeros_between(1, j), zeros_outside(1, j)
        return (o > ob + p[j] - p[1]) and (z > zb - p[j] + p[1])

    L_hi = n // 2 - 1  # L = 1 .. L_hi
    R_lo = n // 2 + 2  # R = R_lo .. n

    b_l = b_r = 0
    last_diff_L = 0     # largest i in L with p_i != q_i (0 = none found)
    first_diff_R = 0    # smallest j in R with p_j != q_j (0 = none found)

    for i in range(1, L_hi + 1):
        if p[i] == 1 and q[i] == 0:
            b_l += 1
        elif p[i] == 0 and q[i] == 1:
            b_l -= 1
        if p[i] != q[i]:
            last_diff_L = i

    for j in range(R_lo, n + 1):
        if p[j] == 1 and q[j] == 0:
            b_r += 1
        elif p[j] == 0 and q[j] == 1:
            b_r -= 1
        if p[j] != q[j] and first_diff_R == 0:
            first_diff_R = j

    if b_l != b_r:
        return "NO"

    if last_diff_L and not tauschbar_L(last_diff_L):
        return "NO"
    if first_diff_R and not tauschbar_R(first_diff_R):
        return "NO"

    return "YES"


def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        p = data[idx]; idx += 1
        q = data[idx]; idx += 1
        out.append(solve_case(n, p, q))
    sys.stdout.write('\n'.join(out) + '\n')


if __name__ == "__main__":
    main()
