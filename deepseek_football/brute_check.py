from collections import defaultdict
from itertools import product


def legal_transitions(s):
    n = len(s)
    a = s.count("A")
    b = n - a
    ka = (a - 1) // 2
    kb = (b + 1) // 2
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] != s[j]:
                continue
            inside = s[i + 1 : j]
            ia = inside.count("A")
            ib = inside.count("B")
            if s[i] == "A":
                ok = ia >= ka and ib >= kb
            else:
                ok = ia >= (a + 1) // 2 and ib >= (b - 1) // 2
            if ok:
                chars = list(s)
                other = "B" if s[i] == "A" else "A"
                chars[i] = chars[j] = other
                yield "".join(chars)


def key(s):
    a = s.count("A")
    b = len(s) - a
    if a % 2 == 0 or b % 2 == 0:
        return None
    ka = a // 2
    kb = b // 2
    pa = pb = None
    ca = cb = 0
    for idx, ch in enumerate(s):
        if ch == "A":
            if ca == ka:
                pa = idx
            ca += 1
        else:
            if cb == kb:
                pb = idx
            cb += 1
    left = min(pa, pb)
    right = max(pa, pb)
    return left, right, s[left : right + 1]


for n in range(2, 13, 2):
    states = [
        "".join(chars)
        for chars in product("AB", repeat=n)
        if sum(c == "A" for c in chars) % 2 == 1
    ]
    graph = {s: list(legal_transitions(s)) for s in states}
    visited = set()
    comps = []
    for s in states:
        if s in visited:
            continue
        stack = [s]
        visited.add(s)
        comp = []
        while stack:
            x = stack.pop()
            comp.append(x)
            for y in graph[x]:
                if y not in visited:
                    visited.add(y)
                    stack.append(y)
        comps.append(comp)

    keys = {s: key(s) for s in states}
    bad = []
    for comp in comps:
        k = keys[comp[0]]
        for s in comp:
            if keys[s] != k:
                bad.append((comp, s, k, keys[s]))

    bykey = defaultdict(list)
    for s, k in keys.items():
        bykey[k].append(s)
    for k, arr in bykey.items():
        root = None
        vis = set()
        stack = [arr[0]]
        while stack:
            x = stack.pop()
            if x in vis:
                continue
            vis.add(x)
            stack.extend(graph[x])
        if len(vis) != len(arr):
            bad.append(("disconnected key", k, len(vis), len(arr)))

    print("n", n, "states", len(states), "components", len(comps), "bad", bad[:1])
