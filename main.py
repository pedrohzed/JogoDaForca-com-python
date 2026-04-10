from random import choice
import sys

FILENAME = "palavras.txt"

try:
    with open(FILENAME, encoding="utf-8") as texto:
        palavras = [linha.strip().lower() for linha in texto if linha.strip()]
except FileNotFoundError:
    print(f"Erro: arquivo '{FILENAME}' não encontrado.")
    sys.exit(1)

if not palavras:
    print(f"Erro: arquivo '{FILENAME}' está vazio.")
    sys.exit(1)

palavra = choice(palavras)

tentativas = 6
exibicao = ["_"] * len(palavra)
letras_tentadas = []

while tentativas > 0 and "_" in exibicao:
    print("\nPalavra:", " ".join(exibicao))
    print(f"Tentativas restantes: {tentativas}")
    if letras_tentadas:
        print("Letras tentadas:", " ".join(letras_tentadas))
    else:
        print("Letras tentadas: (nenhuma)")

    try:
        chute = input("Chute uma letra: ").lower().strip()
    except EOFError:
        print("\nEntrada finalizada. Encerrando o jogo.")
        break

    if len(chute) != 1 or not chute.isalpha():
        print("Entrada inválida. Digite apenas uma letra.")
        continue

    if chute in letras_tentadas:
        print("Você já tentou essa letra. Tente outra.")
        continue

    letras_tentadas.append(chute)

    if chute in palavra:
        for indice, letra in enumerate(palavra):
            if letra == chute:
                exibicao[indice] = chute
        print(f"Acertou! A letra '{chute}' está na palavra.")
    else:
        tentativas -= 1
        print(f"Errou! A letra '{chute}' não está na palavra.")

if "_" not in exibicao:
    print("\nVocê ganhou!")
    print("Palavra completa:", palavra)
else:
    print("\nVocê perdeu!")
    print("A palavra era:", palavra)
