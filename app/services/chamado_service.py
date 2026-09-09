from app.repositories import chamado_repository, usuario_repository, grupo_tecnico_repository, tecnico_repository

class ChamadoService:
    def __init__(self, chamado_repository, usuario_repository, grupo_tecnico_repository, tecnico_repository):
        self.chamado_repository = chamado_repository
        self.usuario_repository = usuario_repository
        self.grupo_tecnico_repository = grupo_tecnico_repository
        self.tecnico_repository = tecnico_repository

    def criar_chamado(self, cpf_usuario, nome_grupo, titulo, descricao, prioridade):

        usuario = self.usuario_repository.buscar_usuario(cpf_usuario)

        if not usuario:
            return 'O CPF não está vinculado a nenhum usuário.'


        grupo = self.grupo_tecnico_repository.buscar_grupo_tecnico(nome_grupo)

        if not grupo:
            return 'O Nome do Grupo Técnico informado não está vinculado a nenhum grupo técnico cadastrado.'


        resultado = self.chamado_repository.criar_chamado(cpf_usuario, nome_grupo, titulo, descricao, prioridade)

        if resultado == 0:
            return 'Não foi possível criar o chamado.'

        return resultado

    def listar_chamados(self):
        resultado = self.chamado_repository.listar_chamados()

        if not resultado:
            return 'Não há nenhum chamado existente.'

        return resultado

    def buscar_chamado(self, id_chamado=None, titulo=None):

        resultado = self.chamado_repository.buscar_chamado(id_chamado, titulo)

        if not resultado:
            return 'Não foi possível localizar nenhum chamado em específico.'

        return resultado

    def pesquisar_chamados(self, id_usuario=None, id_tecnico=None, id_grupo_tecnico=None, titulo=None, descricao=None, status=None, prioridade=None):

        resultado = self.chamado_repository.pesquisar_chamados(id_usuario, id_tecnico, id_grupo_tecnico, titulo, descricao, status, prioridade)

        if not resultado:
            return 'Não foi possível localizar nenhum chamado com os filtros usados.'

        return resultado

    def atualizar_info_chamado(self, id_chamado, titulo=None, descricao=None):
        
        chamado = self.chamado_repository.buscar_chamado(id_chamado)

        if not chamado:
            return 'O ID informado não está vinculado a nenhum chamado.'
        

        resultado = self.chamado_repository.atualizar_info_chamado(id_chamado, titulo, descricao)

        if resultado == 0:
            return 'Não foi possível atualizar as infromações do chamado.'

        return resultado

    def atribuir_tecnico(self, id_chamado, nome):

        if nome is None or not nome.strip():
            return 'Preencha o campo Nome do técnico.'
        

        chamado = self.chamado_repository.buscar_chamado(id_chamado)

        if not chamado:
            return 'O ID informado não é relacionado a nenhum chamado.'


        tecnico = self.tecnico_repository.buscar_tecnico(nome)

        if not tecnico:
            return 'O técnico informado não existe.'
        

        resultado = self.chamado_repository.atribuir_tecnico(id_chamado, nome)

        if resultado == 0:
            return 'Não foi possível atribuir técnico ao chamado.'

        return resultado

    def alterar_grupo_tecnico(self, id_chamado, id_novo_grupo):

        if id_novo_grupo is None:
            return 'Preencha o campo ID do Grupo Técnico.'
        

        chamado = self.chamado_repository.buscar_chamado(id_chamado)

        if not chamado:
            return 'O ID informado não está vinculado a nenhum chamado.'


        resultado = self.chamado_repository.alterar_grupo_tecnico(id_chamado, id_novo_grupo)

        if resultado == 0:
            return 'Erro ao alterar o grupo técnico.'

        return resultado

    def alterar_status_chamado(self, id_chamado, novo_status):

        if novo_status is None or not novo_status.strip():
            return 'Preencha o campo Novo Status.'

        chamado = self.chamado_repository.buscar_chamado(id_chamado)

        if not chamado:
            return 'O ID informado não está vinculado a nenhum chamado.'

        resultado = self.chamado_repository.alterar_status_chamado(id_chamado, novo_status)

        if resultado == 0:
            return 'Não foi possível alterar o status do chamado.'

        return resultado

    def alterar_prioridade_chamado(self, id_chamado, nova_prioridade):

        if nova_prioridade is None or not nova_prioridade.strip():
            return 'Preencha o campo Nova Prioridade.'
        

        chamado = self.chamado_repository.buscar_chamado(id_chamado)

        if not chamado:
            return 'O ID informado não está vinculado a nenhum chamado.'

        resultado = self.chamado_repository.alterar_prioridade_chamado(id_chamado, nova_prioridade)


        if resultado == 0:
            return 'Não foi possível alterar a prioridade do chamado.'

        return resultado

    def solucionar_chamado(self, id_chamado, motivo_solucao):

        if motivo_solucao is None or not motivo_solucao.strip():
            return 'Preencha o campo Motivo da Solução.'

        
        chamado = self.chamado_repository.buscar_chamado(id_chamado)

        if not chamado:
            return 'O ID informado não está vinculado a nenhum chamado.'
        

        resultado = self.chamado_repository.solucionar_chamado(id_chamado, motivo_solucao)

        if resultado == 0:
            return 'Não foi possível solucionar o chamado.'

        return resultado

    def reabrir_chamado(self, id_chamado, motivo_reabrir):

        if motivo_reabrir is None or not motivo_reabrir.strip():
            return 'Preencha o campo Motivo da Reabertura.'

        chamado = self.chamado_repository.buscar_chamado(id_chamado)

        if not chamado:
            return 'O ID informado não está vinculado a nenhum chamado.'
        

        resultado = self.chamado_repository.reabrir_chamado(id_chamado, motivo_reabrir)

        if resultado == 0:
            return 'Não foi possível reabrir o chamado.'

        return resultado

chamado_service = ChamadoService(chamado_repository, usuario_repository, grupo_tecnico_repository, tecnico_repository)