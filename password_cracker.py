import hashlib

with open("top-10000-passwords.txt", "r", encoding="utf-8") as f:
    passwords = [line.strip() for line in f.readlines()]

with open("Known-salts.txt", "r", encoding="utf-8") as f:
    salts = [line.strip() for line in f]


def crack_sha1_hash(hash, use_salts=False):
    for password in passwords:
        if hashlib.sha1(password.encode()).hexdigest() == hash:
            return password

    if use_salts:
        for salt in salts:
            for password in passwords:

                if hashlib.sha1((salt + password).encode()).hexdigest() == hash:
                    return password

                if hashlib.sha1((password + salt).encode()).hexdigest() == hash:
                    return password

    return "PASSWORD NOT IN DATABASE"
