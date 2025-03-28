import psycopg2


def conectar_bd():
    """Função para conectar ao banco de dados"""
    return psycopg2.connect(
        dbname="teste_nivelamento",
        user="postgres",
        password="3570",
        host="localhost",
        port="5432"
    )


def executar_script_sql(arquivo_sql):
    """Executa o script SQL a partir de um arquivo e exibe resultados de SELECT"""
    conn = conectar_bd()
    cursor = conn.cursor()

    try:
        # Verificando se o caminho do arquivo está correto
        with open(arquivo_sql, "r", encoding="utf-8") as f:
            script = f.read()
            print("Conteúdo do arquivo SQL:")
            print(script)  # Para verificar o conteúdo do arquivo antes de executar
            cursor.execute(script)

        # Se o script for uma consulta SELECT, obtenha e exiba os resultados
        if script.strip().lower().startswith('select'):
            resultados = cursor.fetchall()
            if resultados:
                print("Resultados da consulta:")
                for resultado in resultados:
                    print(resultado)  # Exibe cada linha de resultado
            else:
                print("Nenhum registro encontrado.")

        conn.commit()  # Commit (necessário apenas para modificações no DB, mas não prejudica)

    except Exception as e:
        print(f"Erro ao executar o script: {e}")

    finally:
        # Fecha o cursor e a conexão
        cursor.close()
        conn.close()


if __name__ == "__main__":
    # Caminho para o seu script SQL
    arquivo_sql = "../Database/sql_scripts/analytics.sql"
    executar_script_sql(arquivo_sql)
