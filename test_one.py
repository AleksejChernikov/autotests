def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


def test_massiv():
    assert 1 in [2, 3, 4]


def test_uslovie():
    a = 2
    b = 3
    assert a < b


def test_stroka():
    assert 'fizz' not in 'fizzbuzz'
