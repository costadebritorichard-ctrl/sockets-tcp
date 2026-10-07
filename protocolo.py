"""Definição do IP e da porta onde o serviço estará rodando"""

HOST = "127.0.0.1"
PORTA = 5000

# Converte e envia mensagens em byte conforme protocolo TCP
def enviar(conexao, mensagem):
    conexao.sendall((mensagem + "\n").encode("utf-8"))

def receber(leitor):

    #le os bytes até encontrar o \n que define o final da mensagem
    dados = leitor.readline()

    #Caso a mensagem não tenha o \n definindo o final da mensagem ou não tenha recebido nenhuma mensagem retorna None
    if not dados or not dados.endswith(b"\n"): 
        return None 

    #retorna os dados enviados pela conexão agora em string(decodificado) e sem o /n no final.
    return dados[:-1].decode("utf-8")


def inteiro_valido(texto):
    # Remove um único sinal opcional antes de verificar os algarismos.
    if texto.startswith("+") or texto.startswith("-"):
        texto = texto[1:]
    # Limitamos os operandos a 12 algarismos ASCII; decimais não são aceitos.
    return 1 <= len(texto) <= 12 and texto.isascii() and texto.isdecimal()

def responder(mensagem):

    #verifica se a mensagem recebida é o comando de SAIR, caso seja sai da função retornando a string "SAIU".
    if mensagem == "SAIR":
        return "SAIU"


    #divide a string da mensagem em um array considerando os caracteres "|".
    campos = mensagem.split("|")


    #se o primeiro item do array que é o comando for diferente de "SOMAR" e também diferente de "SAIR" retorna um erro.
    if campos[0] != "SOMAR":
        return "ERRO|COMANDO|Use SOMAR ou SAIR."

    #se o array com a mensagem tiver menos ou mais de 3 itens, significa que não está respeitando o formato do protocolo, logo, retorna um erro.
    if len(campos) != 3:
        return "ERRO|FORMATO|Use SOMAR|<numero1>|<numero2>"

    if not inteiro_valido(campos[1]) or not inteiro_valido(campos[2]):
        return "ERRO|NUMERO_INVALIDO|Use inteiros com até 12 algarismos."

    a = int(campos[1])
    b = int(campos[2])
    return str(a + b)
