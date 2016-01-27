# conversor

Converter valor numerico (String) para o seu Extenso

numeros = ['0','1','9','10','14','99','100','101','357','1000','1001','1034','1589','125967','10000']
for i in range(0,len(numeros)):
    print("Numero "+ numeros[i]+ "->" + ConvertCurrencyToPortuguese(numeros[i],False))

Resultado:
Numero 0->ZERO
Numero 1->UM
Numero 9->NOVE
Numero 10->DEZ
Numero 14->QUATORZE
Numero 99->NOVENTA E NOVE
Numero 100->CEM
Numero 101->CENTO E UM
Numero 357->TREZENTOS E CINQUENTA E SETE
Numero 1000->MIL
Numero 1001->MIL E UM
Numero 1034->MIL E TRINTA E QUATRO
Numero 1589->MIL E QUINHENTOS E OITENTA E NOVE
Numero 125967->CENTO E VINTE E CINCO MIL E NOVECENTOS E SESSENTA E SETE
Numero 10000->DEZ MIL
