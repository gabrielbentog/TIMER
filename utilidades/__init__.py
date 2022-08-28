from time import sleep
def linha(n):
    """
    Cria uma linha de tamanho 'n'
    """
    print('\033[1;94m-\033[0;0m'*n) #Cria uma linha no terminal


def titulo(msg):
    """
    Cria um título.
    """
    linha(45)
    print("\033[1;94m", end='')
    print(f"{msg}".center(45)) #Faz um título centralizado
    print("\033[0;0m", end='')
    linha(45)


def menu(*opc):
    """
    Cria um menu com os ítens desejados.
    """
    for c in range(0, len(opc)):
        print(f"\033[1;95m{c + 1}\033[0;0m - \033[1;94m{opc[c]}\033[0;0m")#Cria um menu com os parametros colocados.
    linha(45)
    while True:
        try:
            v = int(input("\033[1;95mSua opção: \033[0;0m"))#Opção a ser escolhida nos parametros
        except:
            print("Algo deu errado. Tente novamente!")
        else:
            if v > 0 and v <= len(opc):
                break
            else:
                print("Esses valores não existem. Digite valores existentes!")
    linha(45)
    return v


##########################################

#########################################
def calcHora():
    """
    Calcula o timer em horas.
    
    """
    Hours = float(input("\033[1;95mDigite o valor em hora: "))
    seconds = int(Hours * 3600)
    min = sec = hour = 0
    linha(45)
    while True:
        if sec == 60:
            sec -= 60
            seconds -= 60
            min += 1
        if min == 60:
            min -= 60
            hour += 1
        if hour < 10: 
            if sec < 10:
                if min < 10:
                    print(f"\r0{hour}:0{min}:0{sec}", end='')
                else:
                    print(f"\r0{hour}:{min}:0{sec}", end='')
            else:
                if min < 10:
                    print(f"\r0{hour}:0{min}:{sec}", end='')
                else:
                    print(f"\r0{hour}:{min}:{sec}", end='')
        else:
            if sec < 10:
                if min < 10:
                    print(f"\r{hour}:0{min}:0{sec}", end='')
                else:
                    print(f"\r{hour}:{min}:0{sec}", end='')
            else:
                if min < 10:
                    print(f"\r{hour}:0{min}:{sec}", end='')
                else:
                    print(f"\r{hour}:{min}:{sec}", end='')
        sec += 1
        sleep(1)
        if sec > seconds:
            break
    print()
    linha(45)


def calcMin():
    """
    Calcula o timer em minutos.
    
    """
    minutes = float(input("\033[1;95mDigite o valor em minutos: "))
    seconds = int(minutes * 60)
    sec = min = 0
    linha(45)
    while True:
        if sec == 60:
            sec -= 60
            seconds -= 60
            min += 1
        if sec < 10:
            if min < 10:
                print(f"\r0{min}:0{sec}", end='')
            else:
                print(f"\r{min}:0{sec}", end='')
        else:
            if min < 10:
                print(f"\r0{min}:{sec}", end='')
            else:
                print(f"\r{min}:{sec}", end='')
        sec += 1
        sleep(1)
        if sec > seconds:
            break
    print()
    linha(45)


def calcSeg():
    """
    Calcula o timer em segundos
    """
    seconds = float(input("\033[1;95mDigite o valor em segundos: "))
    sec = min = 0
    linha(45)
    while True:
        if sec == 60:
            sec -= 60
            seconds -= 60
            min += 1
        if sec < 10:
            if min < 10:
                print(f"\r0{min}:0{sec}", end='')
            else:
                print(f"\r{min}:0{sec}", end='')
        else:
            if min < 10:
                print(f"\r0{min}:{sec}", end='')
            else:
                print(f"\r{min}:{sec}", end='')
        sec += 1
        sleep(1)
        if sec > seconds:
            break
    print()
    linha(45)