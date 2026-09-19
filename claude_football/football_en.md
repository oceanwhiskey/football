# Football Teams — Full Solution (English)

This is the English markdown version of `football_en.tex` / `football.tex`: a full, formal solution (statement, theorem, and proof) for the reachability problem described in [original_problem.md](original_problem.md).

## 1. The Problem

Let $n\in\mathbb{N}$ with $n\geq 2$. We define the index set $N=\{1, 2,\dots, n\}$ and two vectors $p = (p_1, p_2, \dots, p_n)$, $q = (q_1, q_2, \dots, q_n)$ with $p_i, q_i \in \{0, 1\}$ for $i\in N$ (think $1 \leftrightarrow$ team A, $0 \leftrightarrow$ team B).

For $i,j \in N$ with $i<j$ let

$$
\mathrm{one}_i^j(p) = \#\{ k \mid i< k < j,\ p_k=1 \}, \qquad
\overline{\mathrm{one}}_i^j(p) = \#\{ k \mid 1\leq k<i,\ p_k=1 \} + \#\{ k \mid j< k\leq n,\ p_k=1 \}
$$

$$
\mathrm{zero}_i^j(p) = \#\{ k\mid i< k < j,\ p_k=0 \}, \qquad
\overline{\mathrm{zero}}_i^j(p) = \#\{ k\mid 1\leq k < i,\ p_k=0 \} + \#\{ k\mid j< k \leq n,\ p_k=0 \}
$$

**Definition.** Let the tuple $(n, p, q)$ be as above. If there exist $i, j \in N$ with $i<j$, $p_i = p_j$, and

$$
\mathrm{one}_i^{j}(p) > \overline{\mathrm{one}}_i^{j}(p), \qquad \mathrm{zero}_i^{j}(p) > \overline{\mathrm{zero}}_i^{j}(p), \tag{1}
$$

then the following transformation, called a **swap**, may be performed for $(i,j)$:

$$
\tau_{ij}(p) = (p_1, \dots, p_{i-1}, 1-p_i, p_{i+1},\dots, p_{j-1}, 1-p_j, p_{j+1},\dots, p_n).
$$

If some $q$ can be reached from $p$ by a finite sequence of $m$ swaps, i.e.

$$
(\tau_{i_mj_m} \circ \cdots \circ \tau_{i_2j_2}\circ \tau_{i_1j_1}) (p) = q, \tag{2}
$$

we write $p\sim q$.

**Definition.** Let $(n, p, q)$ be given with $\#\{ i \in N\mid p_i=1 \}$ and $\#\{ i \in N\mid p_i=0 \}$ both odd. If $p\sim q$, we call $(n, p, q)$ **solvable**.

The question: given $(n, p, q)$, is it solvable?

## 2. Solution

**Proposition.** $n$ is even.

*Proof.* $n$ is the sum of two odd numbers ($\#\{p_i=1\}$ and $\#\{p_i=0\}$), hence even. $\blacksquare$

**Proposition.** For every swap $(i,j)$,

$$
j - i \geq \frac{n}{2} + 1, \tag{3}
$$

i.e. the number of indices strictly between $i$ and $j$ must be at least $\frac{n}{2}$.

*Proof.* As a necessary condition for a swap, (1) gives $\mathrm{one}_i^j(p)+\mathrm{zero}_i^j(p) \geq \overline{\mathrm{one}}_i^j(p) + \overline{\mathrm{zero}}_i^j(p) + 2$. Combined with the balance identities

$$
\mathrm{one}_i^j(p)+\mathrm{zero}_i^j(p) + \overline{\mathrm{one}}_i^j(p)+\overline{\mathrm{zero}}_i^j(p) = n - 2, \qquad
\mathrm{one}_i^j(p) + \mathrm{zero}_i^j(p) = j - i - 1,
$$

this yields $2(j-i-1) \geq n$, i.e. $j - i \geq \frac{n}{2} + 1$. $\blacksquare$

**Definition.** $L = \{1,\dots, \frac{n}{2}-1\}$ and $R = \{\frac{n}{2}+2,\dots, n\}$.

**Corollary.** The indices $\{\frac{n}{2}, \frac{n}{2}+1\}$ can *never* swap. Every swap $(i,j)$ has $i \in L$ and $j \in R$.

This is a direct consequence of (3): $j - i \ge \frac n2 + 1$ forces $i$ strictly left of $\frac n2$ and $j$ strictly right of $\frac n2 + 1$.

**Definition.** $(n,p,q)$ is **center-equal** if $p_{n/2}=q_{n/2}$ and $p_{n/2+1}=q_{n/2+1}$.

**Corollary (center invariance).** If $(n,p,q)$ is solvable, then it is center-equal &mdash; immediate from the preceding corollary: every swap leaves positions $n/2, n/2+1$ untouched, so by induction on the number of swaps in (2), every $\bar p \sim p$ (in particular $\bar p = q$) agrees with $p$ there.

**Definition (swappable).** $i \in L$ is **swappable** if

$$
\mathrm{one}_i^{n}(p) > \overline{\mathrm{one}}_i^{n}(p) + p_i-p_n
\quad\text{and}\quad
\mathrm{zero}_i^{n}(p) > \overline{\mathrm{zero}}_i^{n}(p) - p_i+p_n. \tag{4}
$$

Symmetrically, $j \in R$ is swappable if

$$
\mathrm{one}_1^{j}(p) > \overline{\mathrm{one}}_1^{j}(p) + p_j-p_1
\quad\text{and}\quad
\mathrm{zero}_1^{j}(p) > \overline{\mathrm{zero}}_1^{j}(p) - p_j+p_1. \tag{5}
$$

$(n,p,q)$ is swappable if every $i \in L$ with $p_i \neq q_i$ and every $j \in R$ with $p_j \neq q_j$ is swappable. Intuitively: $(i,n)$ *could* swap as soon as $p_n$ takes on the value of $p_i$; $(1,j)$ *could* swap as soon as $p_1$ takes on the value of $p_j$.

**Proposition.** If $i \in L$ and $j \in R$ can actually swap with each other, both are individually swappable (against $n$, resp. $1$).

*Proof sketch.* Case $j = n$ is immediate from (1). For $j < n$, split $\mathrm{one}_i^n(p)$ across $[i,j]$ and $[j,n]$ and use (1) to bound it below by $\overline{\mathrm{one}}_i^n(p) + p_i - p_n$; the zero-count bound is symmetric, and swappability of $j$ follows by the mirrored argument. $\blacksquare$

**Proposition (monotonicity).**
- If $i \in L$ is *not* swappable, then no $i' \geq i$ in $L$ can swap.
- If $i \in L$ *is* swappable, then every $i' \leq i$ in $L$ is swappable.
- (Symmetric statements hold for $R$, with the inequality directions reversed.)

*Proof.* Direct algebraic manipulation of (4), shifting the reference index from $i$ to $i'$ and tracking how $\mathrm{one}_i^n$/$\overline{\mathrm{one}}_i^n$ change by at most $p_{i}$ or $p_{i'}$ per step. $\blacksquare$

So the swappable indices of $L$ form a *prefix* $\{1,\dots,t\}$, and the swappable indices of $R$ form a *suffix* $\{s,\dots,n\}$.

**Lemma (swappability is a class invariant).** $i \in N$ is swappable for $(n,p,q)$ iff it is swappable for every $(n,p',q)$ with $p' \sim p$.

*Proof.* Show swappability (and separately, non-swappability) of a fixed $i \in L$ survives an arbitrary single swap $(i',j)$, by case analysis on whether $i' \lessgtr i$ and whether $j = n$ or $j < n$ (four cases each way), each resolved by direct algebraic substitution using (4) and the fact that $(i',j)$ itself satisfies (1). By symmetry the same holds for $i \in R$. $\blacksquare$

**Corollary.** If $(n,p,q)$ is swappable, then so is every $(n,p',q)$ with $p'\sim p$.

**Definition (balance).** For $(n,p,q)$, define the **left balance** and **right balance**

$$
b_L(p) = \#\{i\in L \mid p_i=1, q_i=0\} - \#\{i\in L \mid p_i=0, q_i=1\}, \qquad
b_R(p) = \#\{j\in R \mid p_j=1, q_j=0\} - \#\{j\in R \mid p_j=0, q_j=1\}.
$$

$p$ is **balanced** if $b_L(p) = b_R(p)$.

**Lemma.** A solvable $(n,p,q)$ must be balanced.

*Proof.* Every swap uses one index from $L$ and one from $R$ (Corollary above), so it changes $b_L$ and $b_R$ by exactly the same amount ($\pm 1$) simultaneously — their difference is invariant. Since $b_L(q) = b_R(q) = 0$ trivially, and $p \sim q$ preserves $b_L - b_R$, $p$ must already be balanced. $\blacksquare$

**Definition.** $\sigma(n,p,q) = \#\{i \in N \mid p_i \neq q_i\}$.

**Lemma (progress).** If $(n,p,q)$ is swappable and balanced with $\sigma(n,p,q) > 0$, there is $(n,p',q)$ swappable with $p' \sim p$, $\sigma(n,p,q) \geq \sigma(n,p',q)$, and swappable $i \in L$, $j \in R$ with $p_i = p_j \neq q_i = q_j$.

*Proof.* WLOG some $i \in L$ has $p_i=0, q_i=1$. By balance, there is either a matching $j \in R$ with $p_j=0,q_j=1$ (done immediately), or an $i' \in L$ with $p_{i'}=1,q_{i'}=0$ — in which case $i,i'$ (both swappable) can be paired via $n$. $\blacksquare$

### Main Theorem

**Theorem.** $(n,p,q)$ is solvable **if and only if** it is **center-equal**, **balanced**, and **swappable**.

*Proof.* Necessity of each condition is the center-invariance corollary, the balance lemma, and the swappable-is-a-class-invariant corollary, respectively.

For sufficiency, assume $(n,p,q)$ is center-equal, balanced, and swappable, but (for contradiction) not solvable. Take the reachable $\bar p \sim p$ minimizing the number of "stuck" swaps; then $\sigma(n,\bar p, q) > 0$, and $(n,\bar p,q)$ is still swappable. Because $(n,p,q)$ is center-equal and center-values are invariant along $\bar p \sim p$, $\bar p$ and $q$ also agree at $n/2, n/2+1$ — so the mismatch causing $\sigma(n,\bar p,q)>0$ must lie in $L \cup R$. This is exactly what the progress lemma needs: it produces swappable $i \in L, j \in R$ with $p_i=p_j\neq q_i=q_j$, and (via one of two short compositions of swaps through $1$ and $n$, depending on whether $\bar p_1 = \bar p_n$) a new $p'$ with strictly smaller $\sigma(n,p',q)$ — contradicting minimality. $\blacksquare$

> **Note on the omitted center-agreement condition.** The original document's theorem statement said only "balanced and swappable," omitting the center-equal condition (even though it is proved as a corollary earlier in the document). Without it, "balanced and swappable" can hold *vacuously* whenever $p$ and $q$ differ *only* at the two center positions — since then $L$ and $R$ have no differing indices at all — while the pair is still unsolvable, because those two positions can never change teams. A minimal counterexample: $n=4$, $p = 0100$, $q=0010$ (in the football notation: $p=\texttt{BABB}$, $q=\texttt{BBAB}$) — they agree everywhere except the center, so balance and swappability hold trivially, yet no sequence of swaps connects them.

### Corollary (Algorithm)

**Corollary.** Solvability of $(n,p,q)$ can be decided in $O(n)$ time.

*Proof.* By the theorem, check:
1. **Center-equal**: compare $p_{n/2},q_{n/2}$ and $p_{n/2+1},q_{n/2+1}$ — $O(1)$.
2. **Balanced**: compute $b_L, b_R$ in one $O(n)$ pass and compare.
3. **Swappable**: by monotonicity, it suffices to check swappability of $\max\{i \in L : p_i \neq q_i\}$ against $n$, and of $\min\{j \in R : p_j \neq q_j\}$ against $1$ — each an $O(1)$ check given $O(n)$ prefix sums. $\blacksquare$

See [football_solver.py](football_solver.py) for a verified Python implementation of this algorithm.
