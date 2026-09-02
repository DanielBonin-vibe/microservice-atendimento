from database.session import conectar

def criar_tecnico(id_grupo_tecnico, nome, cpf_tecnico, email):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
        INSERT INTO tecnicos (id_grupo_tecnico, nome, cpf_tecnico, email)
        VALUES (%s, %s, %s, %s)
        """, (id_grupo_tecnico, nome, cpf_tecnico, email))

        resultado = cursor.rowcount

        if resultado > 0:
            conexao.commit()
            return resultado

        conexao.rollback()
        return 0

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao criar técnico: {erro}')
        return 0

    finally:
        cursor.close()
        conexao.close()

def listar_tecnicos():
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
        SELECT * FROM tecnicos
        """)

        resultado = cursor.fetchall()

        return resultado

    except Exception as erro:
        print(f'Erro ao listar técnicos: {erro}')
        return None

    finally:
        cursor.close()
        conexao.close()

def buscar_tecnico(cpf_tecnico):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
        SELECT * FROM tecnicos
        WHERE cpf_tecnico = %s
        """, (cpf_tecnico,))

        resultado = cursor.fetchall()

        return resultado

    except Exception as erro:
        print(f'Erro ao buscar técnico: {erro}')
        return None

    finally:
        cursor.close()
        conexao.close()

def pesquisar_tecnicos(nome=None, id_grupo_tecnico=None):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        if nome is not None:
            cursor.execute("""
                SELECT * FROM tecnicos
                WHERE nome ILIKE %s
            """, (f'%{nome}%',))

        else:
            cursor.execute("""
                SELECT * FROM tecnicos
                WHERE id_grupo_tecnico = %s
            """, (id_grupo_tecnico,))

        resultado = cursor.fetchall()

        return resultado

    except Exception as erro:
        print(f'Erro ao pesquisar técnicos: {erro}')
        return None

    finally:
        cursor.close()
        conexao.close()

def atualizar_tecnico(cpf_tecnico_inicial, nome=None, cpf_tecnico=None, email=None):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
        UPDATE tecnicos 
        SET nome = COALESCE(%s, nome), 
        cpf_tecnico = COALESCE(%s, cpf_tecnico),
        email = COALESCE(%s, email)
        WHERE cpf_tecnico_inicial = %s
        """, (nome, cpf_tecnico, email, cpf_tecnico_inicial))

        resultado = cursor.rowcount

        if resultado > 0:
            conexao.commit()
            return resultado

        conexao.rollback()
        return 0

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao atualizar técnico: {erro}')
        return 0

    finally:
        cursor.close()
        conexao.close()

def excluir_tecnico(cpf_tecnico):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
        DELETE FROM tecnicos
        WHERE cpf_tecnico = %s
        """, (cpf_tecnico,))

        resultado = cursor.rowcount

        if resultado > 0:
            conexao.commit()
            return resultado

        conexao.rollback()
        return 0

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao excluir técnico: {erro}')
        return 0

    finally:
        cursor.close()
        conexao.close()

