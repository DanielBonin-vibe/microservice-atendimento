from app.repositories import usuario_repository
from app.security.hash import gerar_hash, verificar_senha

def cadastro_usuario_service(nome, cpf_usuario, email, telefone, senha):

    usuario = usuario_repository.buscar_usuario(cpf_usuario)

    if usuario is not None:
        return 'Esse CPF já está vinculado a um usuário.'

    usuario = usuario_repository.buscar_usuario(email)

    if usuario is not None:
        return 'Esse Email já está vinculado a um usuário.'

    usuario = usuario_repository.buscar_usuario(telefone)

    if usuario is not None:
        return 'Esse Telefone já está vinculado a um usuário.'


    senha_hash = gerar_hash(senha)


    resultado = usuario_repository.cadastro_usuario(nome, cpf_usuario, email, telefone, senha_hash)

    if resultado == 0:
        return 'Não foi possível cadastrar o usuário.'

    return resultado

def listar_usuario_service():
    resultado = usuario_repository.listar_usuarios()

    if not resultado:
        return 'Não há nenhum usuário a listar.'

    return resultado

def buscar_usuario_service(busca):
    if busca is None or not busca.strip():
        return 'Preencha o campo de Busca.'

    resultado = usuario_repository.buscar_usuario(busca)

    if not resultado:
        return 'Usuário não encontrado.'

    return resultado

def pesquisar_usuarios_service(nome=None, cpf_usuario=None, email=None, telefone=None):
    resultado = usuario_repository.pesquisar_usuario(nome=nome, cpf_usuario=cpf_usuario, email=email, telefone=telefone)

    if not resultado:
        return 'Não foi possível localizar nenhum usuário.'

    return resultado

def atualizar_usuario_service(cpf_usuario_inicial, nome=None, cpf_usuario_novo=None, email=None, telefone=None):

    usuario = usuario_repository.buscar_usuario(cpf_usuario_inicial)

    if usuario is None:
        return 'O CPF informado não está vinculado a nenhum usuário.'
    

    if cpf_usuario_novo is not None:
        usuario_cpf = usuario_repository.buscar_usuario(cpf_usuario_novo)

        if usuario_cpf is not None:
            return 'Esse CPF já está vinculado a um usuário.'

    if email is not None:
        usuario_email = usuario_repository.buscar_usuario(email)

        if usuario_email is not None:
            return 'Esse Email já está vinculado a um usuário.'

    if telefone is not None:
        usuario_telefone = usuario_repository.buscar_usuario(telefone)

        if usuario_telefone is not None:
            return 'Esse Telefone já está vinculado a um usuário.'

        
    resultado = usuario_repository.atualizar_usuario(cpf_usuario_inicial, nome=nome, cpf_usuario_novo=cpf_usuario_novo, email=email, telefone=telefone)

    if resultado == 0:
        return 'Não foi possível atualizar o cadastro do usuário.'

    return resultado

def alterar_senha_service(cpf_usuario, senha_atual, senha_nova):
    usuario = usuario_repository.buscar_usuario_cpf(cpf_usuario)

    if usuario == 0:
        return 'Não foi possível localizar nenhum usuário.'
    

    senha_hash_atual = usuario[5]

    senha_correta = verificar_senha(senha_atual, senha_hash_atual)

    if not senha_correta:
        return 'Senha atual incorreta.'


    senha_hash_nova = gerar_hash(senha_nova)


    resultado = usuario_repository.alterar_senha_usuario(senha_hash_nova, cpf_usuario)

    if resultado == 0:
        return 'Não foi possível alterar a senha do usuário.'

    return resultado

def excluir_usuario_service(cpf_usuario):
    if cpf_usuario is None or not cpf_usuario.strip():
        return 'Preencha o campo de CPF.'

    usuario = usuario_repository.buscar_usuario(cpf_usuario)

    if not usuario:
        return 'O CPF informado não está vinculado a nenhum usuário.'

    resultado = usuario_repository.excluir_usuario(cpf_usuario)

    if resultado == 0:
        return 'Não foi possível excluir o usuário.'

    return resultado
