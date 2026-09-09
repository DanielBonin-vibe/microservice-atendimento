from app.database.session import conectar

class ChamadoRepository:
    def __init__(self, conectar):
        self.conectar_banco = conectar

    def criar_chamado(self, cpf_usuario, nome_grupo, titulo, descricao, prioridade):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT id_usuario FROM usuarios
            WHERE cpf_usuario = %s
            """, (cpf_usuario,))

            usuario = cursor.fetchone()

            if usuario is None:
                return 0

            id_usuario = usuario[0]

            cursor.execute("""
            SELECT id_grupo_tecnico FROM grupos_tecnicos
            WHERE nome = %s
            """, (nome_grupo,))

            grupo = cursor.fetchone()

            if grupo is None:
                return 0

            id_grupo_tecnico = grupo[0]

            cursor.execute("""
            INSERT INTO chamados (id_usuario, id_grupo_tecnico, titulo, descricao, prioridade)
            VALUES (%s, %s, %s, %s, %s)
            """, (id_usuario, id_grupo_tecnico, titulo, descricao, prioridade))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao criar chamado: {erro}')
            return 0
        
        finally:
            cursor.close()
            conexao.close()

    def listar_chamados(self):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM chamados
            """)

            resultado = cursor.fetchall()

            if not resultado:
                return []

            return resultado

        except Exception as erro:
            print(f'Erro ao listar chamado: {erro}')
            return None
        
        finally:
            cursor.close()
            conexao.close()

    def buscar_chamado(self, id_chamado=None, titulo=None):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            if id_chamado is not None:
                cursor.execute("""
                SELECT * FROM chamados
                WHERE id_chamado = %s
                """, (id_chamado,))

            elif titulo is not None:
                cursor.execute("""
                SELECT * FROM chamados
                WHERE titulo = %s
                """, (titulo,))

            else:
                return None

            resultado = cursor.fetchone()

            return resultado

        except Exception as erro:
            print(f'Erro ao buscar chamado: {erro}')
            return None
        
        finally:
            cursor.close()
            conexao.close()

    def pesquisar_chamados(self, id_usuario=None, id_tecnico=None, id_grupo_tecnico=None, titulo=None, descricao=None, status=None, prioridade=None):
        conexao = self.conectar_banco()
        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM chamados 
            WHERE (%s IS NULL OR id_usuario = %s) 
                AND (%s IS NULL OR id_tecnico = %s)
                AND (%s IS NULL OR id_grupo_tecnico = %s)
                AND (%s IS NULL OR titulo ILIKE %s)
                AND (%s IS NULL OR descricao ILIKE %s)
                AND (%s IS NULL OR status = %s)
                AND (%s IS NULL OR prioridade = %s)
                """, (id_usuario, id_tecnico, id_grupo_tecnico, f'%{titulo}%', f'%{descricao}%', status, prioridade))

            resultado = cursor.fetchall()

            if not resultado:
                return []

            return resultado

        except Exception as erro:
            print(f'Erro ao pesquisar chamado: {erro}')
            return None
        
        finally:
            cursor.close()
            conexao.close()

    def atualizar_info_chamado(self, id_chamado, titulo=None, descricao=None):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE chamados 
            SET titulo = COALESCE(%s, titulo),
                descricao = COALESCE(%s, descricao),
            WHERE id_chamado = %s
            """, (titulo, descricao, id_chamado))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao atualizar as informações do chamado: {erro}')
            return 0
        
        finally:
            cursor.close()
            conexao.close()

    def atribuir_tecnico(self, id_chamado, nome):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE chamados
            SET id_tecnico = 
            (SELECT id_tecnico FROM tecnicos
            WHERE nome = %s),
            data_ultima_atualizacao = CURRENT_TIMESTAMP
            WHERE id_chamado = %s
            """, (nome, id_chamado))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao atribuir técnico ao chamado: {erro}')
            return 0
        
        finally:
            cursor.close()
            conexao.close()

    def alterar_grupo_tecnico(self, id_chamado, id_novo_grupo):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE chamados 
                SET id_grupo_tecnico = %s,
                id_tecnico = NULL,
                data_ultima_atualizacao = CURRENT_TIMESTAMP
            WHERE id_chamado = %s
            """,(id_novo_grupo, id_chamado))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao alterar grupo técnico do chamado: {erro}')
            return 0
        
        finally:
            cursor.close()
            conexao.close()

    def alterar_status_chamado(self, id_chamado, novo_status):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE chamados 
                SET status = %s,
                data_ultima_atualizacao = CURRENT_TIMESTAMP
            WHERE id_chamado = %s 
            """,(novo_status, id_chamado))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao alterar status do chamado: {erro}')
            return 0
        
        finally:
            cursor.close()
            conexao.close()

    def alterar_prioridade_chamado(self, id_chamado, nova_prioridade):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE chamados
                SET prioridade = %s,
                data_ultima_atualizacao = CURRENT_TIMESTAMP
            WHERE id_chamado = %s
            """,(nova_prioridade, id_chamado))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao alterar prioridade do chamado: {erro}')
            return 0
        
        finally:
            cursor.close()
            conexao.close()

    def solucionar_chamado(self, id_chamado, motivo_solucao):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE chamados
                SET motivo_solucao = %s,
                status = 'SOLUCIONADO',
                data_ultima_atualizacao = CURRENT_TIMESTAMP
            WHERE id_chamado = %s
            """,(motivo_solucao, id_chamado))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao solucionar o chamado: {erro}')
            return 0
        
        finally:
            cursor.close()
            conexao.close()

    def reabrir_chamado(self, id_chamado, motivo_reabrir):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE chamados
                SET motivo_reabrir = %s,
                status = 'ABERTO',
                data_ultima_atualizacao = CURRENT_TIMESTAMP
            WHERE id_chamado = %s
            """,(motivo_reabrir, id_chamado))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao reabrir o chamado: {erro}')
            return 0
        
        finally:
            cursor.close()
            conexao.close()

chamado_repository = ChamadoRepository(conectar)