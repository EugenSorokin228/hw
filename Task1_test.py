import Task1

def test_is_not_ascii():
    result = Task1.valid_password('абвгдєйке')
    assert result == 'Password Invalid'


def test_password_too_short():
    result = Task1.valid_password('123qwE@')
    assert result == 'Password Invalid'


def test_has_not_upper():
    result = Task1.valid_password('123qwe@5')
    assert result == 'Password Invalid'


def test_has_not_lower():
    result = Task1.valid_password('123QWE@5')
    assert result == 'Password Invalid'


def test_has_space():
    result = Task1.valid_password('123 qw@rtY')
    assert result == 'Password Invalid'


def test_has_not_spec():
    result = Task1.valid_password('123qwEEE')
    assert result == 'Password Invalid'


def test_has_not_digit():
    result = Task1.valid_password('@@@qwEEE')
    assert result == 'Password Invalid'
