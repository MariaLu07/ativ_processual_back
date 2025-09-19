from collections import Counter

texto = input("Digite um texto: ")

palavras = texto.split()
num_palavras = len(palavras)
palavra_mais_longa = max(palavras, key=len)
contagem = Counter(palavras)
palavra_mais_frequente, freq = contagem.most_common(1)[0]

print(f'Número de palavras: {num_palavras}')
print(f'Palavra mais longa: {palavra_mais_longa}')
print(f'Palavra que mais aparece: "{palavra_mais_frequente}" ({freq} vezes)')
