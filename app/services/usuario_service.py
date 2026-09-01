from repositories import usuario_repository

def cadastro_usuario_service(nome, cpf_usuario, email, telefone):

    if nome is None or not nome.strip():
        return 'Preencha o campo de Nome.'
    
    if cpf_usuario is None or not cpf_usuario.strip():
        return 'Preencha o campo de CPF.'

    if email is None or not email.strip():
        return 'Preencha o campo de Email.'

    if telefone is None or not telefone.strip():
        return 'Preencha o campo de Telefone.'

    usuario = usuario_repository.buscar_usuario(cpf_usuario)

    if usuario is not None:
        return 'Esse CPF já está vinculado a um usuário.'

    usuario = usuario_repository.buscar_usuario(email)

    if usuario is not None:
        return 'Esse Email já está vinculado a um usuário.'

    usuario = usuario_repository.buscar_usuario(telefone)

    if usuario is not None:
        return 'Esse Telefone já está vinculado a um usuário.'


    resultado = usuario_repository.cadastro_usuario(nome, cpf_usuario, email, telefone)

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

    if cpf_usuario_inicial is None or not cpf_usuario_inicial.strip():
        return 'Preencha o campo CPF.'

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
