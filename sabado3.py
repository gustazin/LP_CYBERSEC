soma_pares = int 
soma_impares = int
numero = int 

soma_pares = 0 
soma_impares = 0 

numero = int (input("digite um número positivo para classificar ou um negativo para sair  : "))
print (numero)
while numero >= 0 :
    if numero % 2 == 0 : 
        soma_pares = soma_pares + numero 
        print ("numero", numero , "É par ") 
    else:
        soma_impares = soma_impares + numero
        print ("numero" , numero , "é impar")
    numero = int(input("digite outro numero positivo para classificar ou negativo para sair " ) )
    print ("processo encerrado")
    print ("soma total dos numeros pares:", soma_pares)
    print ("soma total dos mumeros impares : " , soma_impares)