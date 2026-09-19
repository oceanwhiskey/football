def main():
    test_1()
    return
    t = int(input())
    for _ in range(t):
        read_input_and_solve()


def read_input_and_solve():
    # https://stackoverflow.com/questions/77210343/determine-whether-you-can-reach-bitstring-b-from-bitstring-a-using-specific-oper
    n = int(input())
    p = input()
    q = input()

    if solve(n, p, q): 
        print('yes')
    else:
        print('no')


def solve(n, p, q):
    try:       
        check_middle(n, p, q)
        r = find_index_right_min(n, p, q)
        l = find_index_left_max(n, p, q)
        
        if r:
            validate_switchable_1_j(p, r)
        if l:
            validate_switchable_i_n(p, l)

        check_balance(n, p, q)
        return True
    except NotSolvableException as e:
        return False


def check_balance(n, p, q):
    # left/right balance must compare 'A'/'B' characters, not the ints 1/0,
    # and both ranges must be indexed the same way (p[i], not p[i-1])
    balanced = \
    sum(1 for i in range(0, n//2-1) if p[i] == 'A' and q[i] == 'B')  \
    - sum(1 for i in range(0, n//2-1) if p[i] == 'B' and q[i] == 'A') \
    == \
    sum(1 for i in range(n//2+1, n) if p[i] == 'A' and q[i] == 'B')  \
    - sum(1 for i in range(n//2+1, n) if p[i] == 'B' and q[i] == 'A')

    if not balanced:
        raise NotSolvableException('not balanced')  
  

def check_middle(n, p, q):
    middle_indices = [n//2-1, n//2]
    if any(map(lambda i: p[i] != q[i], middle_indices)):
        raise NotSolvableException(f'indices {n//2}, {n//2 + 1} cannot switch')  
        

def find_index_right_min(n, p, q):
    for j in range(n//2-1, n):
        if p[j] != q[j]:
            return j
    else: return None
        

def find_index_left_max(n, p, q):
    for i in range(n//2-2, -1, -1):
        if p[i] != q[i]:
            return i
    else: return None


def validate_switchable_i_n(p, i):
    n = len(p)

    # strictly between i and n excludes both endpoints, i.e. p[n-1] itself
    inner_vote_A = sum(1 for k in range(i+1, n-1) if p[k] == 'A')
    outer_vote_A = sum(1 for k in range(i) if p[k] == 'A')

    if p[i] == 'A' and p[n-1] == 'B':
        outer_vote_A += 1
    if p[i] == 'B' and p[n-1] == 'A':
        outer_vote_A -= 1        

    if inner_vote_A <= outer_vote_A:
        raise NotSolvableException('transfer rejected')  

    inner_vote_B = sum(1 for k in range(i+1, n-1) if p[k] == 'B')
    outer_vote_B = sum(1 for k in range(i) if p[k] == 'B')

    if p[i] == 'A' and p[n-1] == 'B':
        outer_vote_B -= 1
    if p[i] == 'B' and p[n-1] == 'A':
        outer_vote_B += 1   

    if inner_vote_B <= outer_vote_B:
        raise NotSolvableException('transfer rejected') 
    
    
def validate_switchable_1_j(p, j):
    n = len(p)
    inner_vote_A = sum(1 for k in range(1, j) if p[k] == 'A')
    outer_vote_A = sum(1 for k in range(j+1, n) if p[k] == 'A')

    if p[j] == 'A' and p[0] == 'B':
        outer_vote_A += 1
    if p[j] == 'B' and p[0] == 'A':
        outer_vote_A -= 1        

    if inner_vote_A <= outer_vote_A:
        raise NotSolvableException('transfer rejected')  

    inner_vote_B = sum(1 for k in range(1, j) if p[k] == 'B')
    outer_vote_B = sum(1 for k in range(j+1, n) if p[k] == 'B')

    if p[j] == 'A' and p[0] == 'B':
        outer_vote_B -= 1
    if p[j] == 'B' and p[0] == 'A':
        outer_vote_B += 1   

    if inner_vote_B <= outer_vote_B:
        raise NotSolvableException('transfer rejected')     


class NotSolvableException(RuntimeError):
    pass


def test_1():
    p = 'AABA'
    q = 'BABB'
    n = len(p)
    assert solve(n, p, q) == True


def test_2():
    p = 'BAAABAAB'
    q = 'BABABBAB'
    n = len(p)
    assert solve(n, p, q) == True


def test_3():
    p = 'BAAABAABA'
    q = 'BABABBABB'
    n = len(p)
    assert solve(n, p, q) == False    


def test_4():
    p = 'BA'
    q = 'BA'
    n = len(p)
    assert solve(n, p, q) == True


def test_5():
    p = 'AAAAAAAABBBBBBBBBA'
    q = 'AAAAAAAABBBBBBBBAB'
    n = len(p)
    assert solve(n, p, q) == True


def test_6():
    p = 'ABBAABABABABABABAB'
    q = 'ABABABABABABABABAB'
    n = len(p)
    assert solve(n, p, q) == True


def test_7():
    p = 'ABBAABABABABABABAB'
    q = 'BAABBABAABBABABABA'
    n = len(p)
    assert solve(n, p, q) == True        


def test_8():
    p = 'ABBA'
    q = 'ABBA'
    n = len(p)
    assert solve(n, p, q) == True


def test_9():
    p = 'BABBAB'
    q = 'ABBBAB'
    n = len(p)
    assert solve(n, p, q) == False


def test_10():
    p = 'BABABBAB'
    q = 'ABBABBAB'
    n = len(p)
    assert solve(n, p, q) == True


def test_11():
    p = 'BABAAB'
    q = 'ABBAAB'
    n = len(p)
    assert solve(n, p, q) == True    


def test_12_reveals_check_balance_bug():
    # p and q agree at the two center indices (so check_middle passes) and
    # every individual transfer check on both sides is satisfiable, but the
    # left/right balance actually differs, so this must be unsolvable.
    # check_balance() used to compare characters to the ints 1/0 (e.g.
    # `p[i-1] == 1`), which is always False in Python, so the balance check
    # silently never rejected anything and this incorrectly returned True.
    p = 'ABBB'
    q = 'BBBA'
    n = len(p)
    assert solve(n, p, q) == False


def test_13_validate_switchable_i_n_excludes_partner_n():
    # validate_switchable_i_n(p, i) checks i in L against the fixed partner
    # n, so the "inner" (strictly-between) vote must exclude both i and n
    # itself. It used to include p[n-1] (index n-1, i.e. n) in inner_vote_A
    # / inner_vote_B via `range(i+1, n)` instead of `range(i+1, n-1)`.
    # This off-by-one never actually flips the final verdict for valid
    # inputs (both team sizes are always odd, which makes every inner/outer
    # vote comparison a strict, never-tied inequality, so shifting one side
    # by exactly 1 can't cross the pass/fail boundary) -- so no (n, p, q)
    # exists that distinguishes the buggy and fixed versions. This is a
    # plain regression test exercising that code path instead.
    p = 'BAAABAAB'
    q = 'BABABBAB'
    n = len(p)
    assert solve(n, p, q) == True


if __name__ == '__main__': main()