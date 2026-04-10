from random import randint

tentativas = 6
linha = randint(0, 4)
with open("palavras.txt") as texto:
    for _ in range(linha):
        texto.readline()
    palavra = texto.readline().strip().lower()  # Palavra secreta em minúsculas

# Inicializa a exibição com underscores
exibicao = ["_"] * len(palavra)

print("Palavra:", " ".join(exibicao))
print(f"Tentativas restantes: {tentativas}")

while tentativas > 0 and "_" in exibicao:
    chute = input("Chute uma letra: ").lower()
    if len(chute) != 1 or not chute.isalpha():
        print("inválido. Digite uma letra.")
        continue
    
    if chute in palavra:
        for i in range(len(palavra)):
            if palavra[i] == chute:
                exibicao[i] = chute
        print("Acertou!", " ".join(exibicao))
    else:
        tentativas -= 1
        print("Errou!", " ".join(exibicao))
        print(f"Tentativas restantes: {tentativas}")

if "_" not in exibicao:
    print("Você ganhou!")
else:
    print(f"Você perdeu! A palavra era: {palavra}")
