import random as rd

maiusculo = input("Deseja letras maiusculas na senha? [S/N] ")
maiusculo = maiusculo.lower()

numero = input("Deseja numeros na senha? [S/N] ")
numero = numero.lower()

especial = input("Desja caracteres especias na senha? [S/N] ")
especial = especial.lower()

quantidade = int(input("Quantos caracteres na senha? "))
print(" ")

letra_min = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letra_mai = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
carac_esp = ["!","@","#","$","%","&","*","-","+","/"]
num = ["0","1","2","3","4","5","6","7","8","9"]

senha = []

if maiusculo == "n" and numero == "n" and especial == "n":

    for i in range(quantidade):
        n = rd.choice(letra_min)
        senha.append(n)

elif maiusculo == "s" and numero == "n" and especial == "n":

    escolha_senha = [letra_mai, letra_min]

    for i in range(quantidade):
        esc = rd.choice(escolha_senha)
        n = rd.choice(esc)
        senha.append(n)

elif maiusculo == "n" and numero == "s" and especial == "n":

    escolha_senha = [num, letra_min]

    for i in range(quantidade):
        esc = rd.choice(escolha_senha)
        n = rd.choice(esc)
        senha.append(n)

elif maiusculo == "n" and numero == "n" and especial == "s":

    escolha_senha = [carac_esp, letra_min]

    for i in range(quantidade):
        esc = rd.choice(escolha_senha)
        n = rd.choice(esc)
        senha.append(n)        

elif maiusculo == "s" and numero == "s" and especial == "n":

    escolha_senha = [num, letra_mai, letra_min]

    for i in range(quantidade):
        esc = rd.choice(escolha_senha)
        n = rd.choice(esc)
        senha.append(n)

elif maiusculo == "s" and numero == "n" and especial == "s":

    escolha_senha = [letra_mai, carac_esp, letra_min]

    for i in range(quantidade):
        esc = rd.choice(escolha_senha)
        n = rd.choice(esc)
        senha.append(n)

elif maiusculo == "n" and numero == "s" and especial == "s":

    escolha_senha = [num, carac_esp, letra_min]

    for i in range(quantidade):
        esc = rd.choice(escolha_senha)
        n = rd.choice(esc)
        senha.append(n)

elif maiusculo == "s" and numero == "s" and especial == "s":

    escolha_senha = [letra_mai, num, carac_esp, letra_min]

    for i in range(quantidade):
        esc = rd.choice(escolha_senha)
        n = rd.choice(esc)
        senha.append(n)

senha = ''.join(senha)

print("Seua senha: ")
print(senha)