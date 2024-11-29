def soma_pares_impares(numeros):
  
    soma_pares = sum(n for n in numeros if n % 2 == 0)
    soma_impares = sum(n for n in numeros if n % 2 != 0)
    return soma_pares, soma_impares


entrada = [1, 2, 3, 4, 5]
resultado = soma_pares_impares(entrada)
resultado
