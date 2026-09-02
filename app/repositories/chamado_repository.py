from database.session import conectar

def criar_chamado(cpf_usuario, nome_grupo, titulo, descricao, prioridade):
    conexao = conectar()

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
        """, (nome_grupo),)

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

def listar_chamados():
    conexao = conectar()

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

def buscar_chamado(id_chamado=None, titulo=None):
    conexao = conectar()

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

def pesquisar_chamados(id_usuario=None, id_tecnico=None, id_grupo_tecnico=None, titulo=None, descricao=None, status=None, prioridade=None):
    conexao = conectar()

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
        print(f'Erro ao buscar chamado: {erro}')
        return None
    
    finally:
        cursor.close()
        conexao.close()

def atualizar_info_chamado(titulo=None, descricao=None, status=None, prioridade=None):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
        SELECT * FROM chamados
        WHERE (%s )
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
