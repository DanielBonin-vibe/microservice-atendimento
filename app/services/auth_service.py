from repositories import usuario_repository, tecnico_repository
from security.hash import verificar_senha
from security.token import gerar_token

def login_service(cpf, senha):
    usuario = usuario_repository.buscar_usuario_cpf(cpf)

    if usuario:
        senha_hash = usuario[5]

        if not verificar_senha(senha, senha_hash):
            return 'CPF ou senha inválido(s).'
        # "Verifique se a senha que a pessoa digitou corresponde ao hash salvo no banco"
        
        token = gerar_token(cpf, 'usuario') # Gera o JWT

        return {
            'acess_token': token, 
            'tipo': 'usuario'     
        }
        # Esse return serve para o sistema saber qual o tipo do usuário e o token


    tecnico = tecnico_repository.buscar_tecnico(cpf)

    if tecnico:
        senha_hash = tecnico[5]

        if not verificar_senha(senha, tecnico['senha_hash']):
            return 'CPF ou senha inválido(s).'

        token = gerar_token(cpf, 'tecnico')

        return {
            'acess_token': token,
            'tipo': 'tecnico'
        }

    return 'CPF ou senha inválido(s).'