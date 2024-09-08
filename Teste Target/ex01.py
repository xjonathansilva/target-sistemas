def pertence_fibonacci(num):
    a = 0
    b =  1
    while b < num:
        
        aux = b
        b = a + b
        a = aux

    if b == num:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} NÃO pertence à sequência de Fibonacci."

numero = int(input("Informe um número: "))
print(pertence_fibonacci(numero))