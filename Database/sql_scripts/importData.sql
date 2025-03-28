
COPY operadoras
FROM '../Dados/Relatorio_.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');


COPY demonstracoes_contabeis
FROM '../Dados/1T2023/1T2023.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');

COPY demonstracoes_contabeis
FROM '../Dados/2T2023/2T2023.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');

COPY demonstracoes_contabeis
FROM '../Dados/3T2023/3T2023.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');

COPY demonstracoes_contabeis
FROM '../Dados/4T2023/4T2023.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');

COPY demonstracoes_contabeis
FROM '../Dados/1T2024/1T2024.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');

COPY demonstracoes_contabeis
FROM '../Dados/2T2024/2T2024.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');

COPY demonstracoes_contabeis
FROM '../Dados/3T2024/3T2024.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');

COPY demonstracoes_contabeis
FROM '../Dados/4T2024/4T2024.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');
