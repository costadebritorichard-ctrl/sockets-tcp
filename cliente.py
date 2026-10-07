import socket

from protocolo import HOST, PORTA, enviar, receber

def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conexao:
        conexao.connect((HOST, PORTA))

        with conexao.makefile("rb") as leitor:
            print("Digite dois inteiros separados por espaço, ou sair.")
            while True:
                entrada = input("Soma> ").strip()
                if entrada.lower() == "sair":
                    mensagem = "SAIR"

                else:
                    numeros = entrada.split()
                    if len(numeros) != 2:
                        print("Digite dois números, por exemplo: 10 20")
                        continue

                    mensagem = "SOMAR|" + "|".join(numeros)

                enviar(conexao, mensagem)
                resposta = receber(leitor)

                if resposta is None:
                    print("Conexão encerrada pelo servidor.")
                    break

                if resposta == "SAIU":
                    print("Conexão encerrada.")
                    break

                campos = resposta.split("|")

                resultado = resposta
                if len(campos) == 2 and campos[0] in ("", "OK"):
                    resultado = campos[1]

                algarismos = resultado.removeprefix("+").removeprefix("-")
                if algarismos.isascii() and algarismos.isdecimal():
                    print(resultado)
                else:
                    if len(campos) >= 3:
                        print(f"Erro ({campos[1]}: {campos[2]})")
                    else:
                        print(f"Resposta inesperada do servidor: {resposta}")

if __name__ == "__main__":
    main()
