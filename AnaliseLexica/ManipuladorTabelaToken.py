import pandas as pd

palavrasReservadas = {
    "while": "laco",
    "if": "if",
    "else": "else",
    "int" : "tipo",
    "bool": "tipo",
    "funcao": "funcao",
    "return": "return",
    "print": "print",
    "procedimento": "procedimento",
    "break": "auxLaco",
    "continue": "auxLaco",
    "true": "bool",
    "false": "bool"
}

def verificarToken(lexema, numeroLinha):
    if(lexema == ''):
        return ''
    else:
        tokens = palavrasReservadas.get(lexema)
        if tokens:
            return tokens
        elif lexema[:3] == 'var':
            return 'idVariavel'
        elif lexema[:4] == 'func':
            return 'idFuncao'
        elif lexema[:4] == 'proc':
            return 'idProcedimento'
        else:
            try:
                constante = int(lexema)
                return "constante"
            except:
                print("="*25)
                print("Erro lexico na linha "+ str(numeroLinha))
                print("Lexema '"+ lexema +"' invalido.")
                print("="*25)
                exit()

# Salva o token na tabela
def inserirToken(lexema, tabelaDeTokens, numeroDaLinhaAtual, token=None):
    if lexema:
        if not token:
            token = verificarToken(lexema, numeroDaLinhaAtual)
        tabelaDeTokens.loc[len(tabelaDeTokens)] = [token, lexema, numeroDaLinhaAtual]
    lexema = ""