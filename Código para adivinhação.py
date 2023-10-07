print("**Jogo da adivinhação**")
import random

while True:
    numero = int(input("Escolha um número de 0 a 10: "))
    numero_computador = random.randint(0, 10)
    resultado = numero_computador
    if numero == resultado:
        print(f"Acertou mizeravi, a máquina escolheu:", resultado, "Você Ganhou!!!")
    else:
        print(f'Você perdeu, o número escolhido pela máquina foi', resultado, 'Você Perdeu!!!')
    vl = input("Quer tentar novamente? [S] ou [N]: ").lower()  # Converter para minúsculas
    if vl == 's':
        pass  # Continuar o loop
    else:
        break
