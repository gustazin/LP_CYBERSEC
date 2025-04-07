

while True:
        print ("MENU")
        print ("1.NOVO SALÁRIO")
        print ("2.FÉRIAS")
        print ("3.DÉCIMO TERCEIRO")
        print ("4. Sair")
        entrada = input ("ESCOLHA UMA OPÇÃO ! : " )
        if entrada == "4":
            print ("Saindo do programa..." )
            break
        if entrada == "1":
            s1= float(input("Digite aqui seu salário para consultar acrécimo : "))
            if s1 <= 350.00:
                s1 = s1+ (s1* 15 / 100)
                print ("Seu salário com acrécimos é:" , s1 )
            elif s1 >=350.00 and s1 <= 600.00 : 
                 s1 = s1+ (s1 * 10 / 100)
                 print ("Seu salário com acrécimos é:" , s1 )
            elif s1 > 600.00 :
                 s1 = s1+(s1* 5 /100)
                 print ("Seu salário com acrécimos é:" , s1 )
        elif entrada == "2":
             s1 = float(input("Digite o seu salário para calcular as suas férias: "))
             s1 = s1 +(s1 / 2 )
             print ("O valor das suas férias é : " , s1 )
        elif entrada == "3": 
             s1 = float(input("Digite o seu salário para consultar o seu décimo terceiro : " ))
             print (s1)
             meses_trabalhados = int(input("Digite aqui o numero de meses trabalhados para efeturar o cálculo"))
             print (meses_trabalhados)
             s1 = s1 + (s1 * meses_trabalhados ) / 12 
             print ("o valor do seu décimo terceiro : " , s1 ) 