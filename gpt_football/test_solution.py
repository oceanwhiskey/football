from solution import solve


def test_1():
    p = "AABA"
    q = "BABB"
    n = len(p)
    assert solve(n, p, q) is True


def test_2():
    p = "BAAABAAB"
    q = "BABABBAB"
    n = len(p)
    assert solve(n, p, q) is True


def test_3():
    p = "BAAABAABA"
    q = "BABABBABB"
    n = len(p)
    assert solve(n, p, q) is False


def test_4():
    p = "BA"
    q = "BA"
    n = len(p)
    assert solve(n, p, q) is True


def test_5():
    p = "AAAAAAAABBBBBBBBBA"
    q = "AAAAAAAABBBBBBBBAB"
    n = len(p)
    assert solve(n, p, q) is True


def test_6():
    p = "ABBAABABABABABABAB"
    q = "ABABABABABABABABAB"
    n = len(p)
    assert solve(n, p, q) is True


def test_7():
    p = "ABBAABABABABABABAB"
    q = "BAABBABAABBABABABA"
    n = len(p)
    assert solve(n, p, q) is True


def test_8():
    p = "ABBA"
    q = "ABBA"
    n = len(p)
    assert solve(n, p, q) is True


def test_9():
    p = "BABBAB"
    q = "ABBBAB"
    n = len(p)
    assert solve(n, p, q) is False


def test_10():
    p = "BABABBAB"
    q = "ABBABBAB"
    n = len(p)
    assert solve(n, p, q) is True


def test_11():
    p = "BABAAB"
    q = "ABBAAB"
    n = len(p)
    assert solve(n, p, q) is True


def test_12():
    p = "ABBB"
    q = "BBBA"
    n = len(p)
    assert solve(n, p, q) is False


def test_13():
    p = "BAAABAAB"
    q = "BABABBAB"
    n = len(p)
    assert solve(n, p, q) is True
