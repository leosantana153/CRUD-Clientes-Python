import mysql.connector


def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="87654321",
        database="crud_clientes"
    )


def adicionar_cliente(nome, email, telefone):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(
            "INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)",
            (nome, email, telefone)
        )
        conexao.commit()
        print("Cliente adicionado com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao adicionar cliente: {erro}")
    finally:
        cursor.close()
        conexao.close()


def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("SELECT * FROM clientes")
        resultados = cursor.fetchall()
        print("Lista de Clientes:")
        for cliente in resultados:
            print(f"ID: {cliente[0]}, Nome: {cliente[1]}, Email: {cliente[2]}, Telefone: {cliente[3]}")
    except mysql.connector.Error as erro:
        print(f"Erro ao listar clientes: {erro}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_cliente(id_cliente, nome=None, email=None, telefone=None):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        atualizacoes = []
        valores = []

        if nome:
            atualizacoes.append("nome=%s")
            valores.append(nome)
        if email:
            atualizacoes.append("email=%s")
            valores.append(email)
        if telefone:
            atualizacoes.append("telefone=%s")
            valores.append(telefone)

        valores.append(id_cliente)

        sql = f"UPDATE clientes SET {', '.join(atualizacoes)} WHERE id=%s"
        cursor.execute(sql, valores)
        conexao.commit()

        if cursor.rowcount > 0:
            print("Cliente atualizado com sucesso!")
        else:
            print("Nenhum cliente encontrado com o ID fornecido.")
    except mysql.connector.Error as erro:
        print(f"Erro ao atualizar cliente: {erro}")
    finally:
        cursor.close()
        conexao.close()


def excluir_cliente(id_cliente):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM clientes WHERE id=%s", (id_cliente,))
        conexao.commit()

        if cursor.rowcount > 0:
            print("Cliente excluído com sucesso!")
        else:
            print("Nenhum cliente encontrado com o ID fornecido.")
    except mysql.connector.Error as erro:
        print(f"Erro ao excluir cliente: {erro}")
    finally:
        cursor.close()
        conexao.close()


def menu():
    while True:
        print("\n--- Sistema de Cadastro de Clientes ---")
        print("1. Adicionar Cliente")
        print("2. Listar Clientes")
        print("3. Atualizar Cliente")
        print("4. Excluir Cliente")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")
            telefone = input("Digite o telefone do cliente: ")
            adicionar_cliente(nome, email, telefone)

        elif opcao == "2":
            listar_clientes()

        elif opcao == "3":
            id_cliente = int(input("Digite o ID do cliente a ser atualizado: "))
            nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
            email = input("Digite o novo email (ou pressione Enter para manter o atual): ")
            telefone = input("Digite o novo telefone (ou pressione Enter para manter o atual): ")

            nome = nome if nome else None
            email = email if email else None
            telefone = telefone if telefone else None

            atualizar_cliente(id_cliente, nome, email, telefone)

        elif opcao == "4":
            id_cliente = int(input("Digite o ID do cliente a ser excluído: "))
            excluir_cliente(id_cliente)

        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o sistema
if __name__ == "__main__":
    menu()
