import jwt
import datetime

payload = {
    "my_name": "Eugen",
    "password": "123qWE@@",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * 15),
    "iat": datetime.datetime.utcnow()
}


def encode_jwt(payload_):
    encoded_jwt = jwt.encode(payload=payload, key='secret', algorithm="HS256")

    return encoded_jwt


def decode_jwt(encoded_jwt_):
    try:
        decoded = jwt.decode(encoded_jwt_, 'secre5t', algorithms=['HS256'])
    except jwt.exceptions.InvalidSignatureError:
        return False
    return decoded



