from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

password_hasher = PasswordHasher()

def gerar_hash(senha: str):
    return password_hasher.hash(senha)


def verificar_senha(senha: str, senha_hash: str):
    try:
        return password_hasher.verify(senha_hash, senha)
    except VerifyMismatchError:
        return False