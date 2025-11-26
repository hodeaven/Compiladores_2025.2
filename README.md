# 📘 Projeto de Compiladores  
Disciplina de Compiladores, ministrada pela professora **Maria Sibaldo**, na **UFAPE**, referente ao período **2025.2**.

---

# 📝 Sobre o projeto  
O projeto consiste na **implementação de um compilador**, utilizando uma linguagem de programação de livre escolha e baseado em uma **gramática preditiva LL(1)**.

A linguagem adotada para o desenvolvimento foi **Python 3.9.5**.

---

# 🎯 Objetivo  
Colocar em prática os conhecimentos teóricos abordados em sala, validando a aprendizagem dos conceitos fundamentais da construção de compiladores.

---

# 📒 Sobre a gramática  
A gramática utilizada deve obedecer ao padrão **LL(1)**, ou seja, precisa atender aos seguintes critérios:

- ✔️ Estar **fatorada à esquerda**;  
- ✔️ Não possuir **recursão à esquerda**;  
- ✔️ Utilizar **apenas 1 símbolo de look-ahead**;  
- ✔️ Ser adequada para um **parser descendente recursivo**.

---

# 📖 Sobre a linguagem implementada  
A linguagem definida para o compilador contempla:

1. Declaração de variáveis dos tipos **inteiro** e **booleano**;  
2. Declaração de **procedimentos** e **funções** (com e sem parâmetros);  
3. **Atribuições** de variáveis;  
4. Chamadas de **funções** e **procedimentos**;  
5. Estruturas condicionais **if / else**;  
6. Estruturas de repetição **while**;  
7. **Retorno de valor** em funções;  
8. Comandos de desvio incondicional: **break** e **continue**;  
9. Comando de impressão de constantes e variáveis;  
10. Expressões **aritméticas**: `+`, `-`, `*`, `/`;  
11. Expressões **booleanas**: `==`, `!=`, `>`, `>=`, `<`, `<=`.

---

# 👥 Integrantes  
- [Eduarda Interaminense](https://github.com/hodeaven)  
- [Gabriel Melo](https://github.com/Bielmelo6)

---

# ▶️ Como executar  
1. Utilize Python **3.9.5 ou superior**.  
2. Instale as dependências:  

```bash
pip install pandas
pip install tabulate
````
3. Execute o arquivo **Main.py**.

---

# 🧪 Testes realizados  
- [x] Uso de operadores de comparação  
- [x] Erros de digitação (ex.: *whle*, *it*, *bolean*)  
- [x] Teste com `if x > 0 or and y < 10`  
- [x] Teste com `if x > y + z:`  
- [x] Inserção de vírgulas aleatórias em funções, procedimentos e laços  
- [x] Inversão da ordem dos parâmetros: `declaracaoDeFuncao(variavel tipo)`  
- [x] Chamada incorreta de função: `chamadaDeFuncao(int)` (em vez de literal ou identificador)  
- [x] Uso de múltiplos pontos e vírgulas  
- [x] Declaração de variável sem ponto e vírgula  
- [x] Atribuição com operador unário irregular: `int vA = + 10;`  
- [x] Erros em expressões: `int vA = 2 + * 5;`  
- [x] Tokens fora de ordem: `int vA = 10 2 +;`
