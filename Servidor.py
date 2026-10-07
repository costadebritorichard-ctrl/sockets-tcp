import socket

from protocolo import HOST, PORTA, enviar, receber, responder

def atender(conexao, endereco):
    print("Cliente conectado:", endereco, flush=True)

    with conexao.makefile("rb") as leitor:
        while True:
            mensagem = receber(leitor)
            if mensagem is None:
                break

            print("Recebido:", mensagem, flush=True)

            resposta = responder(mensagem)

            enviar(conexao, resposta)

            print("Enviado:", resposta, flush=True)

            if resposta == "SAIU":
                break

        print("Cliente desconectado:", endereco, flush=True)


def main():

    #AF_INET representa o IPV4 e o SOCK_STREAM o protocolo TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind((HOST, PORTA)) # Reserva o IP e a porta do serviço.
        servidor.listen(1) # Habilita o servidor a aceitar conexões, o parâmetro representa o limite de conexões.

        print(f"Servidor ouvindo em {HOST}:{PORTA}. Ctrl+C para parar.", flush=True)

        while True:
            # accept espera um cliente e devolve um NOVO socket para atende-lo.
            # O socket servidor permanece aberto para próximas conexões.
            conexao, endereco = servidor.accept()
            with conexao:
                atender(conexao, endereco)


if __name__ == "__main__":
    main()