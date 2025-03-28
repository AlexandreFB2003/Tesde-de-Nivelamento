SELECT 
    d.reg_ans,
	d.descricao,
    o.razao_social,
    SUM(d.vl_saldo_final) AS total_despesas
FROM 
    demonstracoes_contabeis d
JOIN 
    operadoras o ON d.reg_ans = o.registro_ans
WHERE 
    LOWER(REGEXP_REPLACE(d.descricao, '\s+', ' ', 'g')) LIKE '%eventos/ sinistros conhecidos ou avisados de assistência a saúde medico hospitalar%'
    AND d.data BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY 
    d.reg_ans, o.razao_social, d.descricao
ORDER BY 
    total_despesas DESC
LIMIT 10;



SELECT 
    d.reg_ans,
	d.descricao,
    o.razao_social,
    SUM(d.vl_saldo_final) AS total_despesas
FROM 
    demonstracoes_contabeis d
JOIN 
    operadoras o ON d.reg_ans = o.registro_ans
WHERE 
    LOWER(REGEXP_REPLACE(d.descricao, '\s+', ' ', 'g')) LIKE '%eventos/ sinistros conhecidos ou avisados de assistência a saúde medico hospitalar%'
    AND d.data BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY 
    d.reg_ans, o.razao_social, d.descricao
ORDER BY 
    total_despesas DESC
LIMIT 10;


