from app.repositories import grupo_tecnico_repository


class GrupoTecnicoService:
    def __init__(self, grupo_tecnico_repository):
        self.grupo_tecnico_repository = grupo_tecnico_repository

    def criar_grupo_tecnico(self, nome, descricao):

        grupo_tecnico = self.grupo_tecnico_repository.buscar_grupo_tecnico(nome)

        if grupo_tecnico is not None:
            return 'Já existe um grupo técnico com esse nome.'

        resultado = self.grupo_tecnico_repository.criar_grupo_tecnico(nome, descricao)

        if resultado == 0:
            return 'Não foi possível criar o grupo técnico.'

        return resultado

    def listar_grupos_tecnicos(self):
        resultado = self.grupo_tecnico_repository.listar_grupos_tecnicos()

        if not resultado:
            return 'Não há nada a listar em grupos técnicos.'

        return resultado

    def buscar_grupo_tecnico(self, nome):

        resultado = self.grupo_tecnico_repository.buscar_grupo_tecnico(nome)

        if not resultado:
            return 'Não foi possível localizar nenhum grupo técnico.'

        return resultado

    def pesquisar_grupos_tecnicos(self, nome=None, descricao=None):

        resultado = self.grupo_tecnico_repository.pesquisar_grupos_tecnicos(nome, descricao)

        if not resultado:
            return 'Nenhuma grupo técnico foi localizado.'

        return resultado

    def atualizar_grupo_tecnico(self, nome_inicial, nome_novo=None, descricao=None):
        if nome_inicial is None or not nome_inicial.strip():
            return 'Preencha o campo Nome Inicial.'

        grupo_tecnico_1 = self.grupo_tecnico_repository.buscar_grupo_tecnico(nome_inicial)

        if not grupo_tecnico_1:
            return 'O nome informado não se relaciona a nenhum grupo técnico cadastrado.'
        

        if nome_novo is not None:
            grupo_tecnico_2 = self.grupo_tecnico_repository.buscar_grupo_tecnico(nome_novo)

            if grupo_tecnico_2 is not None:
                return 'Já existe um grupo técnico com esse nome..'


        resultado = self.grupo_tecnico_repository.atualizar_grupo_tecnico(nome_inicial, nome_novo, descricao)

        if resultado == 0:
            return 'Não foi possível atualizar o grupo técnico.'

        return resultado 

    def excluir_grupo_tecnico(self, nome):

        grupo_tecnico = self.grupo_tecnico_repository.buscar_grupo_tecnico(nome)

        if not grupo_tecnico:
            return 'O nome informado não se relaciona a nenhum grupo técnico cadastrado.'

        resultado = self.grupo_tecnico_repository.excluir_grupo_tecnico(nome)

        if resultado == 0:
            return 'Não foi possível excluir o grupo técnico.'

        return resultado

grupo_tecnico_service = GrupoTecnicoService(grupo_tecnico_repository)