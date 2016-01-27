# coding=utf-8
__author__ = 'Nuno Gouveia'

from string_functions import *

def posDecimal(v):
    try:
        i=v.index(".")
    except ValueError:
        i=-1
    return i

def fUnidades(valor,currency=False):
    digitos = {'0':'ZERO','1':'UM',
               '2':'DOIS','3':'TRÊS',
               '4':'QUATRO','5':'CINCO',
               '6':'SEIS','7':'SETE',
               '8':'OITO','9':'NOVE'}

    retorno =""

    if ( currency == True ):
        num = int(valor)
        if num == 0:
            retorno = ""
        else:
            retorno = digitos.get(valor)
    else:
        retorno = digitos.get(valor)

    return retorno

def fDezenas(valor,currency=False):
    dict1 = {'10':'DEZ','11':'ONZE','12':'DOZE','13':'TREZE','14':'QUATORZE','15':'QUINZE',
             '16':'DEZASSEIS','17':'DEZASSETE','18':'DEZOITO','19':'DEZANOVE'}
    dict2 = {'2':'VINTE','3':'TRINTA',
             '4':'QUARENTA','5':'CINQUENTA',
             '6':'SESSENTA','7':'SETENTA',
             '8':'OITENTA','9':'NOVENTA'}

    result = ""
    done = False
    # Se o valor estiver entre 10 e 19
    num = int(valor[0])
    if  num == 1:
        result = dict1.get(valor)
        done = True
    else: # Se o valor estiver entre 20 e 99
        result = dict2.get(valor[0])

    if (done == False ):
        num = int(valor[1])
        if  num != 0  :
            result = result + " E " + fUnidades(valor[1], currency)
        else:
            result = result + fUnidades(valor[1], currency)

    return result

def fCentenas(valor,currency = False):
    dict1 = { '1':'CEM','10':'CENTO'}
    dict2 = { '2':'DUZENTOS',
              '3':'TREZENTOS','4':'QUATROCENTOS',
              '5':'QUINHENTOS','6':'SEISCENTOS',
              '7':'SETECENTOS','8':'OITOCENTOS','9':'NOVECENTOS'
              }

    result = ""

    num = int(valor)
    v = str(num)

    if len(v) < 3:
        num = 0
        try:
            num = int(v)
        except ValueError:
            pass
        if num < 10:
           result = fUnidades(v,currency)
        else:
            result = fDezenas(v,currency)
    else:
        num = int(v)
        if num == 100:
            result = dict1.get(v[0])
        else:
            num1 = int(v[0:2])
            num2 = int(v[2])
            if  num1 == 10 and  num2 > 0:
                result = dict1.get(v[0:2]) + " E " + fUnidades(v[2], currency)
            else:
                num1 = int(v[1])
                num2 = int(v[2])
                if int(v[1]) >= 1  and int(v[2]) >= 0:
                    result = dict1.get('10') + " E " + fDezenas(v[1:3], currency)

        num = int(v)
        if  num >= 200:
            result = dict2.get(v[0])
            num1 = int(v[1])
            num2 = int(v[2])
            if num1 > 0:
                result = dict2.get(v[0]) + " E " + fDezenas(v[1:3], currency)
            elif num1 == 0 and  num2 > 0:
                result = dict2.get(v[0]) + " E " + fUnidades(v[1:3], currency)

    return result

def ConvertCurrencyToPortuguese(valor,currency=False):
    singular = [" "," MIL ", " MILHÃO ", " BILIÃO "]
    plural   = [" "," MIL ", " MILHÕES ", " BILIÕES "]
    centimos = ""
    euros = ""
    cents = ""
    tmp = ""
    extenso = ""

    if currency:
        euros = " EUROS "
        cents = " CÊNTIMOS"
    else:
        cents = " CENTÉSIMAS"

    v = valor

    # Verificar se Existe Decimais
    pos = posDecimal(v)
    if (pos != -1):
        tmp = v[pos+1:len(v)]
        num = int(tmp)
        if( num >= 10 ):
            centimos = fDezenas(tmp,currency)
        else:
            centimos = fUnidades(tmp,currency)
        # retira ao valor o valor decimal
        v = mid(v,0,pos)

    # Prosseguir com o restante
    pos = len(v)-3

    if pos < 0:
        pos = 0
    count = 0
    tmp = ""
    while (len(v) != 0):
        tmp = mid(v,pos,3)
        num = int(tmp)
        tmp = fCentenas(tmp,currency)

        if trim(extenso) == "ZERO":
            extenso = ""

        if num == 1 and count == 1:
            tmp = singular[count]

        if num == 1 and count > 1:
            tmp = tmp + singular[count]

        if num > 1 and count == 1:
            tmp = tmp + singular[count]

        if num > 1 and count > 1:
            tmp = tmp + plural[count]

        extenso = trim(extenso)
        if len(extenso) != 0:
            extenso = trim(tmp) + " E " + extenso
        else:
            extenso = extenso + trim(tmp)

        v = v[0:pos]
        pos = len(v)-3
        if (pos < 0):
            pos = 0
        elif (pos == 0):
            pos = 0
        count += 1

    if currency:
        if len(centimos) != 0:
            extenso = extenso + euros + " E " + centimos + cents
        else:
            extenso = extenso + euros
    else:
        if len(centimos) != 0:
            extenso = extenso + " E " + centimos + cents

    extenso = extenso
    return extenso


numeros = ['0','1','9','10','14','99','100','101','357','1000','1001','1034','1589','125967','10000']
for i in range(0,len(numeros)):
    print("Numero "+ numeros[i]+ "->" + ConvertCurrencyToPortuguese(numeros[i],False))
