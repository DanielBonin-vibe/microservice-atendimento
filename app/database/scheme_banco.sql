CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    cpf_usuario VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(50) NOT NULL UNIQUE,
    telefone VARCHAR(25) NOT NULL,
    data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS grupos_tecnicos (
    id_grupo_tecnico INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY
    nome VARCHAR(100) NOT NULL UNIQUE, 
    descricao VARCHAR(300) NOT NULL,
    data_criacao TIMESTAMP NOT NULl DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE IF NOT EXISTS tecnicos (
    id_tecnico INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_grupo_tecnico INTEGER NOT NULL,
    nome VARCHAR(150) NOT NULL, 
    cpf_tecnico VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (id_grupo_tecnico) REFERENCES grupos_tecnicos(id_grupo_tecnico)
);

CREATE TABLE IF NOT EXISTS chamados (
    id_chamado INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_usuario INTEGER NOT NULL,
    id_tecnico INTEGER,
    id_grupo_tecnico INTEGER NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    descricao VARCHAR(300) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'ABERTO'
        CHECK (status IN ('ABERTO', 'PENDENTE', 'SOLUCIONADO')),
    prioridade VARCHAR(10) NOT NULL DEFAULT 'BAIXA'
        CHECK (status IN ('BAIXO', 'MEDIA', 'ALTA', 'URGENTE'))
    motivo_pendencia VARCHAR(1000) NOT NULL,
    motivo_solucao VARCHAR(1000) NOT NULL,
    data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    data_ultima_atualizacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    data_resolucao TIMESTAMP,

    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_tecnico) REFERENCES tecnicos(id_tecnico),
    FOREIGN KEY (id_grupo_tecnico) REFERENCES grupos_tecnicos(id_grupo_tecnico)
);

