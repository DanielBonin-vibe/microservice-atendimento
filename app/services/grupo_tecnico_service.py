from repositories import grupo_tecnico_repository

def criar_grupo_tecnico_service(nome, descricao):
    if nome is None or not nome.strip():
        return 'Preencha o campo Nome.'

    if descricao is None or not descricao.strip():
        return 'Preencha o campo Descrição.'

    grupo_tecnico = grupo_tecnico_repository.buscar_grupo_tecnico(nome)

    if grupo_tecnico is not None:
        return 'Já existe um grupo técnico com esse nome.'

    resultado = grupo_tecnico_repository.criar_grupo_tecnico(nome, descricao)

    if resultado == 0:
        return 'Não foi possível criar o grupo técnico.'

    return resultado

def listar_grupos_tecnicos_service():
    resultado = grupo_tecnico_repository.listar_grupos_tecnicos()

    if not resultado:
        return 'Não há nada a listar em grupos técnicos.'

    return resultado

def buscar_grupo_tecnico_service(nome):
    if nome is None or not nome.strip():
        return 'Preencha o campo Nome.'

    resultado = grupo_tecnico_repository.buscar_grupo_tecnico(nome)

    if not resultado:
        return 'Não foi possível localizar nenhum grupo técnico.'

    return resultado

def pesquisar_grupos_tecnicos_service(nome=None, descricao=None):
    if (nome is None or not nome.strip()) and (descricao is None or not descricao.strip()):
        return 'Ao menos uma informação deve ser passada nos campos.'

    resultado = grupo_tecnico_repository.pesquisar_grupos_tecnicos(nome, descricao)

    if not resultado:
        return 'Nenhuma grupo técnico foi localizado.'

    return resultado

def atualizar_grupo_tecnico_service(nome_inicial, nome_novo=None, descricao=None):
    if nome_inicial is None or not nome_inicial.strip():
        return 'Preencha o campo Nome Inicial.'

    if (nome_novo is None or not nome_novo.strip()) and (descricao is None or not descricao.strip()):
        return 'Ao menos uma modificação deve ser informada.'

    grupo_tecnico = grupo_tecnico_repository.buscar_grupo_tecnico(nome_inicial)

    if not grupo_tecnico:
        return 'O nome informado não se relaciona a nenhum grupo técnico cadastrado.'

    resultado = grupo_tecnico_repository.atualizar_grupo_tecnico(nome_inicial, nome_novo, descricao)

    if resultado == 0:
        return 'Não foi possível atualizar o grupo técnico.'

    return resultado 

def excluir_grupo_tecnico_service(nome):
    if nome is None or not nome.strip():
        return 'Preencha o campo Nome.'
    
    grupo_tecnico = grupo_tecnico_repository.buscar_grupo_tecnico(nome)

    if not grupo_tecnico:
        return 'O nome informado não se relaciona a nenhum grupo técnico cadastrado.'

    resultado = grupo_tecnico_repository.excluir_grupo_tecnico(nome)

    if resultado == 0:
        return 'Não foi possível excluir o grupo técnico.'

    return resultado
