# Football Team Transfers

There are $n$ football players, each belonging to either team A or team B. Each team has an **odd** number of players, and before the tournament the following process occurs an arbitrary number of times:

Players $i$ and $j$ ($1 \le i < j \le n$) on the **same team** want to switch to the other team. The other players then vote on whether this transfer should take place. For each $1 \le x \le n$:

- Player $x$ votes `Yes` if $i < x < j$, and `No` otherwise.
- Players $i$ and $j$ do not vote.

The transfer is successful if and only if **both teams** have more `Yes` than `No` votes. If the transfer occurs, both players move to the other team.

Currently, the teams are represented by the string $p$, where $p_i$ is the team of the $i$-th player.

Each player would really like to be in team $q_i$. Is it possible for some sequence of transfers to occur such that, at the end, the team of the $i$-th player is $q_i$ for every $1 \le i \le n$?

## Input

Each test contains multiple test cases. The first line contains the number of test cases $t$ ($1 \le t \le 10^4$). The test cases follow.

The first line of each test case contains a single integer $n$ ($2 \le n \le 2 \cdot 10^5$) — the number of players.

The second line contains a string $p$ of $n$ characters, consisting only of uppercase Latin letters `A` and `B` — the initial arrangement of teams.

The third line contains a string $q$ of $n$ characters, consisting only of uppercase Latin letters `A` and `B` — the desired arrangement of teams.

It is guaranteed that the sum of $n$ over all test cases does not exceed $2 \cdot 10^5$, and that each team initially has an **odd** number of players. Consequently, each team initially has at least one player and $n$ is even.

## Output

For each test case, output a single line. Print `YES` if it is possible to reach the desired arrangement after some transfers. Otherwise, print `NO`.

The answer may be printed in any letter case.

## Solution and proof

We use one-based indices throughout the proof. For an arrangement $s$ and a
team $c\in\{A,B\}$, write

$$
P_c(s)=\{k\in\{1,\ldots,n\}:s_k=c\}.
$$

Both sets have odd cardinality. If $|P_c(s)|=2h_c+1$, define $m_c(s)$ to be
the position of the $(h_c+1)$-st occurrence of $c$. We call this player the
**median of team $c$**.

Define

$$
L(s)=\min(m_A(s),m_B(s)),\qquad
R(s)=\max(m_A(s),m_B(s))
$$

and define the **median signature**

$$
\Sigma(s)=\bigl(L(s),R(s),s_{L(s)}s_{L(s)+1}\cdots s_{R(s)}\bigr).
$$

We prove that this signature characterizes reachability exactly.

### Lemma 1: every successful interval contains both medians

Suppose a successful transfer changes the equal endpoints $s_i=s_j$, where
$i<j$. Then

$$
i<m_A(s)<j
\quad\text{and}\quad
i<m_B(s)<j.
$$

#### Proof

First consider the team $c$ to which the endpoints belong. Let
$|P_c(s)|=2h+1$, and let the endpoint occurrences have ranks $r<t$ among all
occurrences of $c$. The number of `Yes` votes from team $c$ is $t-r-1$ and
the number of `No` votes is

$$
(r-1)+(2h+1-t).
$$

The transfer is accepted by this team only if

$$
t-r-1>(r-1)+(2h+1-t),
$$

which implies $t-r\ge h+1$. Hence $r<h+1<t$: the median occurrence of $c$
lies strictly between the endpoints.

For the other team $d$, all $2h_d+1$ players vote. A strict majority requires
at least $h_d+1$ of them to lie in $(i,j)$. Any set of $h_d+1$ consecutive
occurrences contains the median occurrence, so $m_d(s)\in(i,j)$ as well.
$\square$

### Lemma 2: the median signature is invariant

If one successful transfer changes $s$ into $s'$, then

$$
\Sigma(s')=\Sigma(s).
$$

#### Proof

By Lemma 1, both medians lie strictly between the changed endpoints. For the
team losing the endpoints, one occurrence is removed to the left of its median
and one to the right. For the team gaining the endpoints, one occurrence is
added on each side of its median. Thus each old median still has equally many
members of its team on its left and right, so both median positions remain
unchanged.

Moreover,

$$
i<L(s)\le R(s)<j.
$$

Consequently no position in $[L(s),R(s)]$ changes. Both the endpoints of the
median interval and every character inside it are invariant. $\square$

Every transfer is reversible: after the endpoints switch teams, all voters
and all their votes are unchanged, so the reverse transfer is accepted too.
It follows already that

$$
p\sim q\quad\Longrightarrow\quad\Sigma(p)=\Sigma(q).
$$

It remains to prove the converse.

### Lemma 3: transfers assisted by a boundary player

Fix an arrangement $s$ with median interval $[L,R]$.

- If $i<L$ and $s_i=s_n$, then $(i,n)$ is a successful transfer.
- If $j>R$ and $s_1=s_j$, then $(1,j)$ is a successful transfer.

#### Proof

We prove the first statement; the second is symmetric. Let the common endpoint
team contain $2h+1$ players. Because $i$ is strictly before its median, at most
$h-1$ other members of that team occur before $i$. All its remaining
$2h-1$ voters occur between $i$ and $n$. Thus at most $h-1$ vote `No` and at
least $h$ vote `Yes`.

For the other team, containing $2k+1$ players, at most $k$ occur before $i$
because $i$ is also before that team's median. None is an endpoint. Therefore
at most $k$ vote `No` and at least $k+1$ vote `Yes`. Both teams approve the
transfer. $\square$

### Lemma 4: the boundary gadget

Let $i<L$ and $j>R$. If $s_i=s_j$, there is a sequence of at most three
successful transfers whose net effect is to toggle exactly $s_i$ and $s_j$.
Every other position is restored to its original value.

#### Proof

If $i=1$ or $j=n$, Lemma 3 gives the required transfer directly. Assume now
$1<i<L\le R<j<n$, and put $x=s_i=s_j$. Denote a transfer at endpoints $a,b$
by $\tau_{a,b}$. According to the two boundary values, use the following
sequence from left to right:

| Boundary values | Transfer sequence |
|---|---|
| $s_1=s_n=x$ | $\tau_{i,n},\ \tau_{1,j},\ \tau_{1,n}$ |
| $s_1=s_n\ne x$ | $\tau_{1,n},\ \tau_{i,n},\ \tau_{1,j}$ |
| $s_1\ne s_n$ and $s_n=x$ | $\tau_{i,n},\ \tau_{1,n},\ \tau_{1,j}$ |
| $s_1\ne s_n$ and $s_1=x$ | $\tau_{1,j},\ \tau_{1,n},\ \tau_{i,n}$ |

At every step, the displayed endpoints are equal. Lemma 3 therefore makes
each transfer legal. Lemma 2 ensures that the same median interval is available
at every intermediate state. Direct inspection shows that positions $1$ and
$n$ are restored, while precisely positions $i$ and $j$ are toggled. $\square$

### Lemma 5: a binary balancing lemma

Let $I$ and $J$ be two nonempty, disjoint sets of binary positions. Permit the
following abstract operation: choose $i\in I$ and $j\in J$ with equal current
values and toggle both. Two assignments $u$ and $v$ are connected by these
operations if and only if

$$
\#A_I(u)-\#A_J(u)=\#A_I(v)-\#A_J(v).
$$

#### Proof

Each operation changes both numbers of A's by $+1$ or both by $-1$, so their
difference is invariant.

Conversely, compare a current assignment with $v$. If two mismatching
positions on opposite sides currently have the same value, toggle them; both
mismatches disappear.

If one side contains two mismatches of opposite current values, choose any
position on the other side as a temporary buffer. Toggle the mismatch equal to
the buffer together with the buffer, and then toggle the other mismatch with
the buffer. Both mismatches are fixed and the buffer is restored.

If neither reduction is possible while mismatches remain, all mismatches on
each side have one current value, and the two sides have opposite current
values. Their contributions to the displayed invariant then have opposite
nonzero signs, contradicting equality of the invariant. Hence one of the two
reductions is always possible until all mismatches are removed. $\square$

### Theorem: complete characterization

For two arrangements $p$ and $q$ in which both teams have odd size,

$$
p\sim q
\quad\Longleftrightarrow\quad
\Sigma(p)=\Sigma(q).
$$

#### Proof

Necessity is Lemma 2.

For sufficiency, suppose the signatures are equal. Write their common median
interval as $[L,R]$ and their common median substring as $C$. Let

$$
I=\{1,\ldots,L-1\},
\qquad
J=\{R+1,\ldots,n\}.
$$

We first show that the invariant from Lemma 5 has the same value for $p$ and
$q$. Suppose, for example, that the A-median is at $L$. The number of A's to
the left and right of this median is equal, so for every arrangement $s$ with
this signature,

$$
\#A_I(s)=\bigl(\#A_C-1\bigr)+\#A_J(s).
$$

Therefore

$$
\#A_I(s)-\#A_J(s)=\#A_C-1,
$$

which depends only on the common substring $C$. If the A-median is at $R$, the
same argument gives

$$
\#A_I(s)-\#A_J(s)=1-\#A_C.
$$

Thus $p$ and $q$ satisfy the equality required by Lemma 5.

If both $I$ and $J$ are nonempty, Lemma 5 supplies a sequence of abstract
equal-value pair toggles transforming the positions outside $C$ from $p$ to
$q$. Lemma 4 realizes each such toggle by successful football transfers,
without changing $C$. Hence $p\sim q$.

Finally, suppose $I$ is empty. The team whose median is at position $1$ has no
member before its median. It must therefore contain exactly one player, so it
cannot occur in $J$. The entire suffix $J$ is consequently forced to consist
of the other team. Thus the common signature already implies $p=q$. The case
where $J$ is empty is symmetric. This completes the proof. $\square$

### Algorithm

For each string $s$:

1. Record the positions occupied by A and by B.
2. Select the middle position from each list.
3. Let $L$ and $R$ be the smaller and larger median positions.
4. Return $(L,R,s[L\ldots R])$.

Print `YES` exactly when the signatures of $p$ and $q$ are equal. A transfer
changes each team size by two, so if either team has even size in $q$, the
answer is immediately `NO`.

### Complexity

Each string is scanned once. The time complexity is $O(n)$ per test case and
$O(\sum n)$ overall. The implementation uses $O(n)$ auxiliary space.
