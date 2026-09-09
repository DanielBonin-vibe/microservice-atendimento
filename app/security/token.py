from datetime import datetime, timedelta, timezone
import jwt

CHAVE_SECRETA = 'B@nin18052006'
ALGORITMO = 'HS256'
TEMPO_EXPIRACAO_MINUTOS = 60

def gerar_token(cpf: str, tipo: str): # Passamos os parâmetros que serão utilizados
    expiracao = datetime.now(timezone.utc) + timedelta(minutos=TEMPO_EXPIRACAO_MINUTOS)
    # Pegamos a hora atual e somamos com o tempo de expiração

    dados = {
        'sub': cpf,      # Subject -> Quem é o dono do 'sub', Ex.: 709.399.954-92
        'tipo': tipo,    # Serve para identificar qual o perfil do usuário (Usuário ou Técnico)
        'exp': expiracao # Literalmente o tempo de expiração.
    }

    return jwt.encode(dados, CHAVE_SECRETA, algorithm=ALGORITMO)
    # Retorna um string de token (Vários números e letras juntos)

def validar_token(token: str):
    try:
        return jwt.decode(
            token,
            CHAVE_SECRETA,
            algorithms=[ALGORITMO]
        )

    except jwt.InvalidTokenError:
        return None