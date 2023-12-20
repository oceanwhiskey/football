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
    balanced = \
    sum(1 for i in range(0, n//2-1) if p[i-1] == 1 and q[i] == 0)  \
    - sum(1 for i in range(0, n//2-1) if p[i] == 0 and q[i] == 1) \
    == \
    sum(1 for i in range(n//2+1, n) if p[i] == 1 and q[i] == 0)  \
    - sum(1 for i in range(n//2+1, n) if p[i] == 0 and q[i] == 1)

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

    inner_vote_A = sum(1 for k in range(i+1, n) if p[k] == 'A')
    outer_vote_A = sum(1 for k in range(i) if p[k] == 'A')

    if p[i] == 'A' and p[n-1] == 'B':
        outer_vote_A += 1
    if p[i] == 'B' and p[n-1] == 'A':
        outer_vote_A -= 1        

    if inner_vote_A <= outer_vote_A:
        raise NotSolvableException('transfer rejected')  

    inner_vote_B = sum(1 for k in range(i+1, n) if p[k] == 'B')
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


if __name__ == '__main__': main()