from database.session import conectar

def criar_grupo_tecnico(nome, descricao):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
        INSERT INTO grupos_tecnicos
        VALUES (%s, %s)
        """, (nome, descricao))

        resultado = cursor.rowcoun 

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

def listar_grupos_tecnicos():
    conexao = conectar()

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

def buscar_grupo_tecnico(nome):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
        SELECT * FROM grupos_tecnicos
        WHERE nome ILIKE %s
        """, (f'%{nome}%',))

        resultado = cursor.fetchall()
        
        conexao.commit()
        return resultado

    except Exception as erro:
        print(f'Erro ao buscar grupo técnico: {erro}')
        return None

    finally:
        cursor.close()
        conexao.close()

def pesquisar_grupos_tecnicos(nome=None, descricao=None):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        parametros = (nome, 
        f'%{nome}%' if nome else None,
        descricao, 
        f'%{descricao}%' if descricao else None )

        cursor.execute("""
        SELECT * FROM grupos_tecnicos
        WHERE (%s IS NULL OR nome ILIKE %s)
            OR (%s IS NULL OR descricao ILIKE %s)
        """, (parametros))

        resultado = cursor.fetchall()
        
        conexao.commit()
        return resultado

    except Exception as erro:
        print(f'Erro ao pesquisar grupos técnicos: {erro}')
        return None

    finally:
        cursor.close()
        conexao.close()

def atualizar_grupo_tecnico(nome_inicial, nome_novo=None, descricao=None):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
        UPDATE grupos_tecnicos
        SET nome = COALESCE(%s, nome) AND descricao = COALESCE(%s, descricao)
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

def excluir_grupo_tecnico(nome):
    conexao = conectar()

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