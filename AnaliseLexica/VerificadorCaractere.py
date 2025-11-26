# Tipos de tokens
caracteres = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 
    ";", "(", ")", "{", "}", " ", "\n", ">", "<", 
    "=", "!", "+", "-", "*", "/", ","
]

def getOperadoresLogicos():
    return [">=", ">", "<", "<=", "!=", "=="]

def getOperadoresAritmeticos():
    return ["+", "-", "*", "/"]


#Funções de verificação de caracteres 

# Indica se a linguagem aceita o caractere informado
def ehCaractereValido(caractere):
    return caractere in caracteres

# Identifica se o caractere encontrado é um espaço ou uma quebra de linha
def ehEspacoOuQuebraDeLinha(caractere):
    return (caractere == " ") or (caractere == "\n")

# Identifica se o lexema é um operador aritmético, uma atribuição ou uma vírgula
def identificarTipoAritmeticoAtribuicaoOuVirgula(lexema):
    if lexema == "=":
        return "atribuicao"
    elif lexema == ";":
        return "pontoEVirgula"
    elif lexema == ",":
        return "virgula"
    elif lexema in getOperadoresAritmeticos():
        return "operadorAritmetico"

# Identifica se o lexema é um operador lógico    
def identificarTipoOperadorLogico(lexema):
    if lexema in getOperadoresLogicos():
        return "operadorLogico"

def ehAritmeticoAtribuicaoOuVirgula(caractere):
    if caractere == "=":
        return True
    elif caractere == ";" or caractere == ",":
        return True
    elif caractere in getOperadoresAritmeticos():
        return True

    return False

# Identifica se é parentese, chave ou ponto e vírgula
def ehParenteseChavePontoEVirgula(caractere):
    return caractere in set("(){};")

# Converte o caractere parentese, chave ou ponto e vírgula em uma string
def traduzParenteseChaveOuPontoEVirgula(caractere):
    caracteres = {
        "(": "abreParentese",
        ")": "fechaParentese",
        "{": "abreChave",
        "}": "fechaChave",
        ";": "pontoEVirgula"
    }
    return caracteres.get(caractere)

# Identifica se é uma atribuição ou um operador lógico aritmético
def identificarAritmeticoOuAtribuicao(caractere, proximoCaractere, indice):
    if (caractere == ">") or (caractere == "<"):
        return (indice + 1 if proximoCaractere == '=' else indice)

    elif ((caractere == "=" or caractere == "!") and proximoCaractere == '='):
            return indice + 1
    
    else:
        return -1 # Não reconheceu