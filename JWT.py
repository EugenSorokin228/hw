import jwt
import datetime

payload = {
    "my_name": "Eugen",
    "password": "123qWE@@",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * 15),
    "iat": datetime.datetime.utcnow()
}
encoded_jwt = jwt.encode(payload=payload, key='secret', algorithm="HS256")
decoded = jwt.decode(encoded_jwt, 'secret', algorithms=['HS256'])
