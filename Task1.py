def valid_password(pswrd: str) -> str:
    if len(pswrd) < 8:
        return 'Password Invalid'
    has_num, has_upper, has_lower, has_spec = False, False, False, False
    symbols = r"""!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"""
    for i in pswrd:
        if i.isupper():
            has_upper = True
        if i.islower():
            has_lower = True
        if i.isdigit():
            has_num = True
        if i in symbols:
            has_spec = True
        if i.isspace():
            return 'Password Invalid'
        if not i.isascii():
            return 'Password Invalid'
    lst = [has_lower, has_upper, has_spec, has_num]
    if False in lst:
        return 'Password Invalid'
    else:
        return 'Password Valid'
