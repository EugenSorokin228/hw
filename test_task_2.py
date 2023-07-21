import Task2


def test_too_big():
    result = Task2.create_number()
    assert result > 1000 == False


def test_too_small():
    result = Task2.create_number()
    assert result < 0 == False
