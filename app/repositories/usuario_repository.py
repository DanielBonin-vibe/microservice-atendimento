from database.session import conectar

def cadastro_usuario(nome, cpf_usuario, email, telefone):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
        INSERT INTO usuarios (nome, cpf_usuario, email, telefone)
        VALUES (%s, %s, %s, %s)
        """, (nome, cpf_usuario, email, telefone))

        resultado = cursor.rowcount

        if resultado > 0:
            conexao.commit()
            return resultado

        conexao.rollback()
        return 0

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao cadastrar usuário: {erro}')
        return 0
    finally:
        cursor.close()
        conexao.close()

def listar_usuarios():
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
        SELECT * FROM usuarios
        """)

        resultado = cursor.fetchall()

        return resultado

    except Exception as erro:
        print(f'Erro ao cadastrar usuário: {erro}')
        return None
    
    finally:
        cursor.close()
        conexao.close()

def buscar_usuario(busca):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
        SELECT * FROM usuarios
        WHERE nome ILIKE %s
            OR cpf_usuario ILIKE %s
            OR email ILIKE %s
            OR telefone ILIKE %s
        """, (f'%{busca}%'), (f'%{busca}%'), (f'%{busca}%'), (f'%{busca}%'))

        resultado = cursor.fetchall()

        return resultado

    except Exception as erro:
        print(f'Erro ao buscar usuário: {erro}')
    finally:
        cursor.close()
        conexao.close()

def pesquisar_usuarios(nome=None, cpf_usuario=None, email=None, telefone=None):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        parametros = (
        nome, f'%{nome}%' if nome else None,
        cpf_usuario, f'%{cpf_usuario}%' if cpf_usuario else None,
        email, f'%{email}%' if email else None,
        telefone, f'%{telefone}%' if telefone else None)   

        cursor.execute("""
        SELECT * FROM usuarios
        WHERE (%s IS NULL OR nome ILIKE %s)
            AND (%s IS NULL OR cpf_usuario ILIKE %s)
            AND (%s IS NULL OR email ILIKE %s)
            AND (%s IS NULL OR telefone ILIKE %s)
            """, (parametros))

        resultado = cursor.fetchall()

        return resultado

    except Exception as erro:
        print(f'Erro ao pesquisar usuário: {erro}')
        return None
    
    finally:
        cursor.close()
        conexao.close()


def atualizar_usuario(cpf_usuario_inicial, nome=None, cpf_usuario_novo=None, email=None, telefone=None):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
        UPDATE usuarios
        SET nome = COALESCE(%s, nome),
            cpf_usuario_novo = COALESCE(%s, cpf_usuario_novo),
            email = COALESCE(%s, email),
            telefone = COALESCE(%s, telefone)
        WHERE cpf_usuario = %s
        """, (nome, cpf_usuario_novo, email, telefone, cpf_usuario_inicial))

        resultado = cursor.rowcount

        if resultado > 0:
            conexao.commit()
            return resultado

        conexao.rollback()
        return 0

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao atualizar usuário: {erro}')
        return 0
    
    finally:
        cursor.close()
        conexao.close()

def excluir_usuario(cpf_usuario):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
        REMOVE FROM usuarios
        WHERE cpf = %s
        """, (cpf_usuario,))

        resultado = cursor.rowcount

        if resultado > 0:
            conexao.commit()
            return resultado

        conexao.rollback()
        return 0

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao excluir usuário: {erro}')
        return 0
    
    finally:
        cursor.close()
        conexao.close()