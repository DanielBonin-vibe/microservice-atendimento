from repositories import tecnico_repository

def criar_tecnico_service(id_grupo_tecnico, nome, cpf_tecnico, email):
    if id_grupo_tecnico is None:
        return 'Preencha o campo ID do grupo técnico.'

    if nome is None or not nome.strip():
        return 'Preencha o campo Nome.'

    if cpf_tecnico is None or not cpf_tecnico.strip():
        return 'Preencha o campo CPF do Técnico.'

    if email is None or not email.strip():
        return 'Preencha o campo email.'
    

    tecnico = tecnico_repository.buscar_tecnico(cpf_tecnico)

    if tecnico is not None:
        return 'O CPF informado já está vinculado a outro técnico.'
    

    resultado = tecnico_repository.criar_tecnico(nome, cpf_tecnico, email)

    if resultado == 0:
        return 'Erro ao cadastrar técnico.'

    return resultado

def listar_tecnicos_service():
    resultado = tecnico_repository.listar_tecnicos()

    if not resultado:
        return 'Não há nenhum técnico a listar.'

    return resultado

def buscar_tecnico_service(cpf_tecnico):
    if cpf_tecnico is None or not cpf_tecnico.strip():
        return 'Prencha o campo CPF do Técnico.'

    resultado = tecnico_repository.buscar_tecnico(cpf_tecnico)

    if not resultado:
        return 'Técnico não encontrado.'

    return resultado

def pesquisar_tecnicos_service(nome=None, id_grupo_tecnico=None):
    if (nome is None or not nome.strip()) and (id_grupo_tecnico is None):
        return 'Ao menos um filtro deve ser selecionado.'

    resultado = tecnico_repository.pesquisar_tecnicos(nome=None, id_grupo_tecnico=None)

    if not resultado:
        return 'Não foi possível localizar nenhum técnico.'

    return resultado 

def atualizar_tecnico_servic(cpf_tecnico_inicial, nome=None, cpf_tecnico=None, email=None):
    if cpf_tecnico_inicial is None or not cpf_tecnico_inicial.strip():
        return 'Preencha o campo CPF Técnico inicial.'

    if (nome is None or not nome.strip()) and (cpf_tecnico is None or not cpf_tecnico.strip()) and (email is None is email.strip()):
        return 'Preencha ao menos um campo para atualizar.'

    tecnico = tecnico_repository.buscar_tecnico(cpf_tecnico_inicial)

    if not tecnico:
        return 'Não foi possível localizar nenhum técnico vinculado ao CPF informado.'


    resultado = tecnico_repository.atualizar_tecnico(cpf_tecnico_inicial, nome=nome, cpf_tecnico=cpf_tecnico, email=email)

    if resultado == 0:
        return 'Não foi possível atualizar as informações de cadastro técnico.'

    return resultado

def excluir_tecnico_service(cpf_tecnico):
    if cpf_tecnico is None or not cpf_tecnico.strip():
        return 'Preencha o campo CPF Técnico.'

    tecnico = tecnico_repository.buscar_tecnico(cpf_tecnico)

    if not tecnico:
        return 'Não foi possível localizar nenhum técnico vinculado ao CPF informado.'


    resultado = tecnico_repository.excluir_tecnico(cpf_tecnico)

    if resultado == 0:
        return 'não foi possível excluir técnico.'

    return resultado