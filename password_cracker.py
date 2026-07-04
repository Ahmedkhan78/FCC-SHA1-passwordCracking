import hashlib


def load_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f]


passwords = load_file("top-10000-passwords.txt")
salts = load_file("known-salts.txt")


def sha1(text):
    return hashlib.sha1(text.encode()).hexdigest()


def crack_sha1_hash(hash, use_salts=False):
    # Step 1: normal dictionary attack
    for password in passwords:
        if sha1(password) == hash:
            return password

    # Step 2: salted attack
    if use_salts:
        for salt in salts:
            for password in passwords:

                if sha1(salt + password) == hash:
                    return password

                if sha1(password + salt) == hash:
                    return password

    return "PASSWORD NOT IN DATABASE"
