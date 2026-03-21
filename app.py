from database import conn
from financas import registrar_transacao, ver_transacoes, excluir_transacao, nova_categoria

while True:
    print("""
----- FINANÇAS -----
1. Entrada
2. Saída
3. Ver transações
4. Excluir
5. Nova categoria
0. Sair""")

    opcao = input("\nOpção: ")

    if opcao == "1":
        registrar_transacao("entrada")
    elif opcao == "2":
        registrar_transacao("saida")
    elif opcao == "3":
        ver_transacoes()
    elif opcao == "4":
        excluir_transacao()
    elif opcao == "5":
        nova_categoria()
    elif opcao == "0":
        conn.close()
        break
    else:
        print("Opção inválida.")

    input("\nEnter para continuar...")
