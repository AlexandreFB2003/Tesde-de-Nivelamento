import psycopg2


def conectar_bd():
    return psycopg2.connect(
        dbname="teste_nivelamento",
        user="postgres",
        password="3570",
        host="localhost",
        port="5432"
    )


def executar_script_sql(arquivo_sql):
    conn = conectar_bd()
    cursor = conn.cursor()

    try:
        with open(arquivo_sql, "r", encoding="utf-8") as f:
            script = f.read()
            print("Conteúdo do arquivo SQL:")
            print(script)
            cursor.execute(script)

        if script.strip().lower().startswith('select'):
            resultados = cursor.fetchall()
            if resultados:
                print("Resultados da consulta:")
                for resultado in resultados:
                    print(resultado)  # Exibe cada linha de resultado
            else:
                print("Nenhum registro encontrado.")

    except Exception as e:
        print(f"Erro ao executar o script: {e}")

    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    arquivo_sql = "analytics.sql"
    executar_script_sql(arquivo_sql)
