from app.repositories import usuario_repository
from app.security.hash import gerar_hash, verificar_senha

class UsuarioService:

    def __init__(self, usuario_repository):
        self.usuario_repository = usuario_repository

    def cadastro_usuario(self, nome, cpf_usuario, email, telefone, senha):

        usuario = self.usuario_repository.buscar_usuario(cpf_usuario)

        if usuario is not None:
            return 'Esse CPF já está vinculado a um usuário.'

        usuario = self.usuario_repository.buscar_usuario(email)

        if usuario is not None:
            return 'Esse Email já está vinculado a um usuário.'

        usuario = self.usuario_repository.buscar_usuario(telefone)

        if usuario is not None:
            return 'Esse Telefone já está vinculado a um usuário.'

        senha_hash = gerar_hash(senha)
        

        resultado = self.usuario_repository.cadastro_usuario(nome, cpf_usuario, email, telefone, senha_hash)

        if resultado == 0:
            return 'Não foi possível cadastrar o usuário.'

        return resultado

    def listar_usuario(self):
        resultado = self.usuario_repository.listar_usuarios()

        if not resultado:
            return 'Não há nenhum usuário a listar.'

        return resultado

    def buscar_usuario(self, busca):
        if busca is None or not busca.strip():
            return 'Preencha o campo de Busca.'

        resultado = self.usuario_repository.buscar_usuario(busca)

        if not resultado:
            return 'Usuário não encontrado.'

        return resultado

    def pesquisar_usuarios(self, nome=None, cpf_usuario=None, email=None, telefone=None):
        resultado = self.usuario_repository.pesquisar_usuarios(nome=nome, cpf_usuario=cpf_usuario, email=email, telefone=telefone)

        if not resultado:
            return 'Não foi possível localizar nenhum usuário.'

        return resultado

    def atualizar_usuario(self, cpf_usuario_inicial, nome=None, cpf_usuario_novo=None, email=None, telefone=None):

        usuario = self.usuario_repository.buscar_usuario(cpf_usuario_inicial)

        if usuario is None:
            return 'O CPF informado não está vinculado a nenhum usuário.'
        

        if cpf_usuario_novo is not None:
            usuario_cpf = self.usuario_repository.buscar_usuario(cpf_usuario_novo)

            if usuario_cpf is not None:
                return 'Esse CPF já está vinculado a um usuário.'

        if email is not None:
            usuario_email = self.usuario_repository.buscar_usuario(email)

            if usuario_email is not None:
                return 'Esse Email já está vinculado a um usuário.'

        if telefone is not None:
            usuario_telefone = self.usuario_repository.buscar_usuario(telefone)

            if usuario_telefone is not None:
                return 'Esse Telefone já está vinculado a um usuário.'

            
        resultado = self.usuario_repository.atualizar_usuario(cpf_usuario_inicial, nome=nome, cpf_usuario_novo=cpf_usuario_novo, email=email, telefone=telefone)

        if not resultado:
            return 'Não foi possível atualizar o cadastro do usuário.'

        return resultado

    def alterar_senha(self, cpf_usuario, senha_atual, senha_nova):
        usuario = self.usuario_repository.buscar_usuario_cpf(cpf_usuario)

        if usuario == 0:
            return 'Não foi possível localizar nenhum usuário.'
        

        senha_hash_atual = usuario[5]

        senha_correta = verificar_senha(senha_atual, senha_hash_atual)

        if not senha_correta:
            return 'Senha atual incorreta.'


        senha_hash_nova = gerar_hash(senha_nova)


        resultado = self.usuario_repository.alterar_senha_usuario(senha_hash_nova, cpf_usuario)

        if not resultado:
            return 'Não foi possível alterar a senha do usuário.'

        return resultado

    def excluir_usuario(self, cpf_usuario):
        if cpf_usuario is None or not cpf_usuario.strip():
            return 'Preencha o campo de CPF.'

        usuario = self.usuario_repository.buscar_usuario_cpf(cpf_usuario)

        if not usuario:
            return 'O CPF informado não está vinculado a nenhum usuário.'

        resultado = self.usuario_repository.excluir_usuario(cpf_usuario)

        if resultado == 0:
            return 'Não foi possível excluir o usuário.'

        return resultado

usuario_service = UsuarioService(usuario_repository)
