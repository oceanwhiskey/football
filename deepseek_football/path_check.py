from collections import deque
from itertools import product
from brute_check import key, legal_transitions


start = "BAABAB"
target = [
    s
    for s in ("".join(c) for c in product("AB", repeat=6))
    if key(s) == key(start) and s[3:].count("A") == 0
]
print("target", target)
q = deque([(start, [])])
seen = {start}
while q:
    s, path = q.popleft()
    if s in target:
        print("path", path)
        break
    for t in legal_transitions(s):
        if t not in seen:
            seen.add(t)
            q.append((t, path + [t]))
