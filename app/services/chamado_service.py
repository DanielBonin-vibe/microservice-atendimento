from repositories import chamado_repository, usuario_repository, grupo_tecnico_repository, tecnico_repository

def criar_chamado_service(cpf_usuario, nome_grupo, titulo, descricao, prioridade):
    if cpf_usuario is None or not cpf_usuario.strip():
        return 'Preencha o campo CPF do usuário.'

    if nome_grupo is None or not nome_grupo.strip():
        return 'Preencha o campo Nome do grupo.'

    if titulo is None or not titulo.strip():
        return 'Preencha o campo titulo do chamado.'

    if descricao is None or not descricao.strip():
        return 'Preencha o campo Descrição do Chamado.'

    if prioridade is None or not prioridade.strip():
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
    if id_chamado is None and (titulo is None or not titulo.strip()):
        return 'Ao menos um filtro deve ser informado.'

    resultado = chamado_repository.buscar_chamado(id_chamado, titulo)

    if not resultado:
        return 'Não foi possível localizar nenhum chamado em específico.'

    return resultado

def pesquisar_chamados_service(id_usuario=None, id_tecnico=None, id_grupo_tecnico=None, titulo=None, descricao=None, status=None, prioridade=None):
    if id_usuario is None and id_tecnico is None and id_grupo_tecnico is None and (titulo is None or not titulo.strip()) and (descricao is None or not descricao.strip()) and (status is None or not status.strip()) and (prioridade is None or not prioridade.strip()):
        return 'Ao menos um filtro deve ser informado.'

    resultado = chamado_repository.pesquisar_chamados(id_usuario, id_tecnico, id_grupo_tecnico, titulo, descricao, status, prioridade)

    if not resultado:
        return 'Não foi possível localizar nenhum chamado com os filtros usados.'

    return resultado

def atualizar_info_chamado_service(id_chamado, titulo=None, descricao=None, status=None, prioridade=None):
    if id_chamado is None:
        return 'Preencha o campo ID do chamado.'

    if (titulo is None or not titulo.strip()) and (descricao is None or not descricao.strip()) and (status is None or not status.strip()) and (prioridade is None or not prioridade.strip()):
        return 'Informe ao menos uma informação para atualizar.'
    

    chamado = chamado_repository.buscar_chamado(id_chamado)

    if not chamado:
        return 'O ID informado não está vinculado a nenhum chamado.'
    

    resultado = chamado_repository.atualizar_info_chamado(id_chamado, titulo, descricao, status, prioridade)

    if resultado == 0:
        return 'Não foi possível atualizar as infromações do chamado.'

    return resultado

def atribuir_tecnico_service(id_chamado, nome):
    if id_chamado is None:
        return 'Preencha o campo ID do Chamado.'

    if nome is None or not nome.strip():
        return 'Preencha o campo Nome do técnico.'
    

    chamado = chamado_repository.buscar_chamado(id_chamado)

    if not chamado:
        return 'O ID informado não é relacionado a nenhum chamado.'


    tecnico = grupo_tecnico_repository.buscar_tecnico(nome)

    if not tecnico:
        return 'O técnico informado não existe.'
    

    resultado = chamado_repository.atribuir_tecnico(id_chamado, nome)

    if resultado == 0:
        return 'Não foi possível atribuir técnico ao chamado.'

    return resultado

def alterar_grupo_tecnico_service(id_chamado, id_novo_grupo):
    if id_chamado is None:
        return 'Preencha o campo ID do Chamado.'

    if id_novo_grupo is None:
        return 'Preencha o campo ID do Grupo Técnico.'
    

    chamado = chamado_repository.buscar_chamado(id_chamado)

    if not chamado:
        return 'O ID informado não está vinculado a nenhum chamado.'


    resultado = chamado_repository.alterar_grupo_tecnico(id_chamado, id_novo_grupo)

    if resultado == 0:
        return 'Erro ao alterar o grupo técnico.'

    return resultado

def alterar_status_chamado_service(id_chamado, novo_status):
    if id_chamado is None:
        return 'Preencha o campo ID do Chamado.'

    if novo_status is None or not novo_status.strip():
        return 'Preencha o campo Novo Status.'

    chamado = chamado_repository.buscar_chamado(id_chamado)

    if not chamado:
        return 'O ID informado não está vinculado a nenhum chamado.'

    resultado = chamado_repository.alterar_status_chamado(id_chamado, novo_status)

    if resultado == 0:
        return 'Não foi possível alterar o status do chamado.'

    return resultado

def alterar_prioridade_chamado_service(id_chamado, nova_prioridade):
    if id_chamado is None:
        return 'Preencha o campo ID do Chamado.'

    if nova_prioridade is None or not nova_prioridade.strip():
        return 'Preencha o campo Nova Prioridade.'
    

    chamado = chamado_repository.buscar_chamado(id_chamado)

    if not chamado:
        return 'O ID informado não está vinculado a nenhum chamado.'

    resultado = chamado_repository.alterar_prioridade_chamado(id_chamado, nova_prioridade)


    if resultado == 0:
        return 'Não foi possível alterar a prioridade do chamado.'

    return resultado

def solucionar_chamado_service(id_chamado, motivo_solucao):
    if id_chamado is None:
        return 'Preencha o campo ID do Chamado.'

    if motivo_solucao is None or not motivo_solucao.strip():
        return 'Preencha o campo Motivo da Solução.'

    
    chamado = chamado_repository.buscar_chamado(id_chamado)

    if not chamado:
        return 'O ID informado não está vinculado a nenhum chamado.'
    

    resultado = chamado_repository.solucionar_chamado(id_chamado, motivo_solucao)

    if resultado == 0:
        return 'Não foi possível solucionar o chamado.'

    return resultado

def reabrir_chamado_service(id_chamado, motivo_reabrir):
    if id_chamado is None:
        return 'Preencha o campo ID do Chamado.'

    if motivo_reabrir is None or not motivo_reabrir.strip():
        return 'Preencha o campo Motivo da reabertura.'

    chamado = chamado_repository.buscar_chamado(id_chamado)

    if not chamado:
        return 'O ID informado não está vinculado a nenhum chamado.'
    

    resultado = chamado_repository.reabrir_chamado(id_chamado, motivo_reabrir)

    if resultado == 0:
        return 'Não foi possível reabrir o chamado.'

    return resultado