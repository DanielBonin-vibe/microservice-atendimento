from app.database.session import conectar

class GrupoTecnicoRepository:

    def __init__(self, conectar):
        self.conectar_banco = conectar

    def criar_grupo_tecnico(self, nome, descricao):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            INSERT INTO grupos_tecnicos
            VALUES (%s, %s)
            """, (nome, descricao))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao criar grupo técnico: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()

    def listar_grupos_tecnicos(self):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM grupos_tecnicos
            """)

            resultado = cursor.fetchall()

            return resultado

        except Exception as erro:
            print(f'Erro ao listar grupos técnicos: {erro}')
            return None

        finally:
            cursor.close()
            conexao.close()

    def buscar_grupo_tecnico(self, nome):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM grupos_tecnicos
            WHERE nome ILIKE %s
            """, (f'%{nome}%',))

            resultado = cursor.fetchone()
            
            if not resultado:
                return None

            return resultado

        except Exception as erro:
            print(f'Erro ao buscar grupo técnico: {erro}')
            return None

        finally:
            cursor.close()
            conexao.close()

    def pesquisar_grupos_tecnicos(self, nome=None, descricao=None):
        conexao = self.conectar_banco()
        try:
            cursor = conexao.cursor()

            parametros = (nome, 
            f'%{nome}%' if nome else None,
            descricao, 
            f'%{descricao}%' if descricao else None )

            cursor.execute("""
            SELECT * FROM grupos_tecnicos
            WHERE (%s IS NULL OR nome ILIKE %s)
                AND (%s IS NULL OR descricao ILIKE %s)
            """, parametros)

            resultado = cursor.fetchall()

            if not resultado:
                return []

            return resultado

        except Exception as erro:
            print(f'Erro ao pesquisar grupos técnicos: {erro}')
            return []

        finally:
            cursor.close()
            conexao.close()

    def atualizar_grupo_tecnico(self, nome_inicial, nome_novo=None, descricao=None):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE grupos_tecnicos
            SET nome = COALESCE(%s, nome),
            descricao = COALESCE(%s, descricao)
            WHERE nome = %s
            """, (nome_novo, descricao, nome_inicial))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao atualizar grupo técnico: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()

    def excluir_grupo_tecnico(self, nome):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            DELETE FROM grupos_tecnicos
            WHERE nome = %s
            """, (nome,))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao excluir grupo técnico: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()

grupo_tecnico_repository = GrupoTecnicoRepository(conectar)