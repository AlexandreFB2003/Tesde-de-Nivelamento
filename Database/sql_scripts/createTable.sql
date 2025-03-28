CREATE TABLE operadoras (
    registro_ans INT PRIMARY KEY,
    cnpj VARCHAR(18) NOT NULL,
    razao_social VARCHAR(255) NOT NULL,
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(255),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf CHAR(2),
    cep VARCHAR(10),
    ddd CHAR(2),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(255),
    regiao_comercializacao VARCHAR(255),
    data_registro_ans DATE
);



CREATE TABLE demonstracoes_contabeis (
    data DATE NOT NULL,
    reg_ans INT NOT NULL,
    cd_conta_contabil VARCHAR(50) NOT NULL,
    descricao TEXT NOT NULL,
    vl_saldo_inicial NUMERIC(18,2),
    vl_saldo_final NUMERIC(18,2),
    FOREIGN KEY (reg_ans) REFERENCES operadoras(registro_ans)
);

