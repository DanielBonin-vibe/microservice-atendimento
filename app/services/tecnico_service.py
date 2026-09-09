from app.repositories import tecnico_repository
from app.security.hash import gerar_hash, verificar_senha

class TecnicoService:
    def __init__(self, tecnico_repository):
        self.tecnico_repository = tecnico_repository

    def criar_tecnico(self, id_grupo_tecnico, nome, cpf_tecnico, email, senha):
        if id_grupo_tecnico is None:
            return 'Preencha o campo ID do grupo técnico.'

        tecnico = self.tecnico_repository.buscar_tecnico(cpf_tecnico)

        if tecnico is not None:
            return 'O CPF informado já está vinculado a outro técnico.'
        
        senha_hash = gerar_hash(senha)

        resultado = self.tecnico_repository.criar_tecnico(nome, cpf_tecnico, email, senha_hash)

        if resultado == 0:
            return 'Erro ao cadastrar técnico.'

        return resultado

    def listar_tecnicos(self):
        resultado = self.tecnico_repository.listar_tecnicos()

        if not resultado:
            return 'Não há nenhum técnico a listar.'

        return resultado

    def buscar_tecnico(self, cpf_tecnico):

        resultado = self.tecnico_repository.buscar_tecnico(cpf_tecnico)

        if not resultado:
            return 'Técnico não encontrado.'

        return resultado

    def pesquisar_tecnicos(self, nome=None, id_grupo_tecnico=None):

        resultado = self.tecnico_repository.pesquisar_tecnicos(nome=nome, id_grupo_tecnico=id_grupo_tecnico)

        if not resultado:
            return 'Não foi possível localizar nenhum técnico.'

        return resultado 

    def atualizar_tecnico(self, cpf_tecnico_inicial, nome=None, cpf_tecnico=None, email=None):
        if cpf_tecnico_inicial is None or not cpf_tecnico_inicial.strip():
            return 'Preencha o campo CPF Técnico inicial.'

        tecnico = self.tecnico_repository.buscar_tecnico(cpf_tecnico_inicial)

        if not tecnico:
            return 'Não foi possível localizar nenhum técnico vinculado ao CPF informado.'


        resultado = self.tecnico_repository.atualizar_tecnico(cpf_tecnico_inicial, nome=nome, cpf_tecnico=cpf_tecnico, email=email)

        if resultado == 0:
            return 'Não foi possível atualizar as informações de cadastro técnico.'

        return resultado

    def alterar_senha_tecnico(self, cpf_tecnico, senha_atual, senha_nova):

        tecnico = self.tecnico_repository.buscar_tecnico(cpf_tecnico)

        if not tecnico:
            return 'Não há nenhum técnico vinculado ao CPF infromado.'
        

        senha_hash_atual = tecnico[5]

        senha_correta = verificar_senha(senha_atual, senha_hash_atual)

        if not senha_correta:
            return 'Senha atual incorreta'
        

        senha_hash_nova = gerar_hash(senha_nova)    


        resultado = self.tecnico_repository.alterar_senha_tecnico(cpf_tecnico, senha_hash_nova)

        if resultado == 0:
            return 'Erro ao alterar a senha do técnico.'
        

        return resultado

    def excluir_tecnico(self, cpf_tecnico):

        tecnico = self.tecnico_repository.buscar_tecnico(cpf_tecnico)

        if not tecnico:
            return 'Não foi possível localizar nenhum técnico vinculado ao CPF informado.'


        resultado = self.tecnico_repository.excluir_tecnico(cpf_tecnico)

        if resultado == 0:
            return 'não foi possível excluir técnico.'

        return resultado

tecnico_service = TecnicoService(tecnico_repository)