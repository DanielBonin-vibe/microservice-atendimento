from repositories import chamado_repository, usuario_repository, grupo_tecnico_repository

def criar_chamado_service(cpf_usuario, nome_grupo, titulo, descricao, prioridade):
    if cpf_usuario is None or cpf_usuario.strip():
        return 'Preencha o campo CPF do usuário.'

    if nome_grupo is None or nome_grupo.strip():
        return 'Preencha o campo Nome do grupo.'

    if titulo is None or titulo.strip():
        return 'Preencha o campo titulo do chamado.'

    if descricao is None or descricao.strip():
        return 'Preencha o campo Descrição do Chamado.'

    if prioridade is None or prioridade.strip():
        return 'Preencha o campo Prioridade.'
    

    usuario = usuario_repository.buscar_usuario(cpf_usuario)

    if not usuario:
        return 'O CPF não está vinculado a nenhum usuário.'


    grupo = grupo_tecnico_repository.buscar_grupo_tecnico(nome_grupo)

    if not grupo:
        return 'O Nome do Grupo Técnico informado não está vinculado a nenhum grupo técnico cadastrado.'


    resultado = chamado_repository.criar_chamado(cpf_usuario, nome_grupo, titulo, descricao, prioridade)

    if resultado == 0:
        return 'Não foi possível criar o chamado.'

    return resultado

def listar_chamados_service():
    resultado = chamado_repository.listar_chamados()

    if not resultado:
        return 'Não há nenhum chamado existente.'

    return resultado

def buscar_chamado_service(id_chamado=None, titulo=None):
    if id_chamado is None and (titulo is None or titulo.strip()):
        return 'Ao menos um filtro deve ser informado.'

    resultado = chamado_repository.buscar_chamado(id_chamado, titulo)

    if not resultado:
        return 'Não foi possível localizar nenhum chamado em específico.'

    return resultado

def pesquisar_chamados(id_usuario=None, id_tecnico=None, id_grupo_tecnico=None, titulo=None, descricao=None, status=None, prioridade=None):
    if id_usuario is None and id_tecnico is None and id_grupo_tecnico is None and (titulo is None or not titulo.strip()) and (descricao is None or not descricao.strip()) and (status is None or not status.strip()) and (prioridade is None or not prioridade.strip()):
        return 'Ao menos um filtro deve ser informado.'

    resultado = chamado_repository.pesquisar_chamados(id_usuario, id_tecnico, id_grupo_tecnico, titulo, descricao, status, prioridade)

    if not resultado:
        return 'Não foi possível localizar nenhum chamado com os filtros usados.'

    return resultado

def atualizar_info_chamado(id_chamado, titulo=None, descricao=None, status=None, prioridade=None):
    if id_chamado is None:
        return 'Preencha o campo ID do chamado.'

    if (titulo is None or not titulo.strip()) and (descricao is None or not descricao.strip()) and (status is None or not status.strip()) and (prioridade is None or not prioridade.strip()):
        return 'Informe ao menos uma informação para atualizar.'

    chamado = chamado_repository.buscar_chamado(id_chamado)

    if not 