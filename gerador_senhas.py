import random
import string

nome = input("Digite seu nome: ")

caracteres = string.ascii_letters + string.digits + string.punctuation
senha = "".join(random.choice(caracteres) for i in range(20 - len(nome)))

meio = len(senha) // 2
senha = senha[:meio] + nome + senha[meio:]

print("Senha gerada:", senha)
