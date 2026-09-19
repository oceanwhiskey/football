# Football Teams

There are $n$ football players, each belonging to either team A or team B. Each team has an **odd number** of players, and before the tournament the following process occurs an arbitrary number of times:

Players $i$ and $j$ ($1 \le i < j \le n$) on the **same team** want to switch to the other team. The other players then vote on whether this transfer should take place. For each $1 \le x \le n$:

- Player $x$ will vote *Yes* if $i < x < j$, and *No* otherwise.
- Players $i$ and $j$ do not vote.

The transfer is successful if and only if **both** teams had more *Yes* than *No* votes. Both players move to the other team if the transfer occurs.

Currently the teams are represented by the string $p$, where $p_i$ is the team of the $i$-th player.

Each player would really like to be in team $q_i$. Is it possible for some sequence of transfers to occur such that at the end, the team of the $i$-th player is $q_i$ for all $1 \le i \le n$?

## Input

Each test contains multiple test cases. The first line contains the number of test cases $t$ ($1 \le t \le 10^4$). The description of the test cases follows.

The first line of each test case contains a single integer $n$ ($2 \le n \le 2 \cdot 10^5$) — the number of players.

The second line of each test case contains a string $p$ with $n$ characters consisting only of the uppercase Latin letters `A` and `B` — the initial arrangement of teams.

The third line of each test case contains a string $q$ with $n$ characters consisting only of the uppercase Latin letters `A` and `B` — the desired arrangement of teams.

It is guaranteed that the sum of $n$ over all test cases does not exceed $2 \cdot 10^5$, and that each team has an **odd number** of players initially (so as a result, each team has at least $1$ player, and $n$ is always even).

## Output

For each test case, output a single line. Print `YES` if it is possible for the $i$-th player's team to reach $q_i$ after some exchanges. Otherwise output `NO`.

You can output the answer in any case (upper or lower). For example, the strings `"yEs"`, `"yes"`, `"Yes"`, and `"YES"` will be recognized as positive responses.
