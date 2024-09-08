def contar_a(string):
    count = string.lower().count('a')
    return f"A letra 'a' aparece {count} vezes na string."

texto = input("Informe uma string: ")
print(contar_a(texto))