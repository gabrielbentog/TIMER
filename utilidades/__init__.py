
def linha(n):
    print('\033[1;94m-\033[0;0m'*n) #Cria uma linha no terminal


def titulo(msg):
    linha(45)
    print("\033[1;94m", end='')
    print(f"{msg}".center(45)) #Faz um título centralizado
    print("\033[0;0m", end='')
    linha(45)


def menu(*opc):
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

def calcHora():
    from time import sleep
    tempo = float(input("\033[1;95mDigite o valor em hora: "))
    segundos = int(tempo * 3600)
    s = m = h =0
    linha(45)
    while True:
        if s == 60:
            s -= 60
            segundos -= 60
            m += 1
        if m == 60:
            m -= 60
            h += 1
        if h < 10:
            if s < 10:
                if m < 10:
                    print(f"\r0{h}:0{m}:0{s}", end='')
                else:
                    print(f"\r0{h}:{m}:0{s}", end='')
            else:
                if m < 10:
                    print(f"\r0{h}:0{m}:{s}", end='')
                else:
                    print(f"\r0{h}:{m}:{s}", end='')
        else:
            if s < 10:
                if m < 10:
                    print(f"\r{h}:0{m}:0{s}", end='')
                else:
                    print(f"\r{h}:{m}:0{s}", end='')
            else:
                if m < 10:
                    print(f"\r{h}:0{m}:{s}", end='')
                else:
                    print(f"\r{h}:{m}:{s}", end='')
        s += 1
        sleep(0.00000001)
        if s > segundos:
            break
    print()
    linha(45)


def calcMin():
    from time import sleep
    tempo = float(input("\033[1;95mDigite o valor em minutos: "))
    segundos = int(tempo * 60)
    s = m = 0
    linha(45)
    while True:
        if s == 60:
            s -= 60
            segundos -= 60
            m += 1
        if s < 10:
            if m < 10:
                print(f"\r0{m}:0{s}", end='')
            else:
                print(f"\r{m}:0{s}", end='')
        else:
            if m < 10:
                print(f"\r0{m}:{s}", end='')
            else:
                print(f"\r{m}:{s}", end='')
        s += 1
        sleep(1)
        if s > segundos:
            break
    linha(45)


def calcSeg():
    from time import sleep
    segundos = float(input("\033[1;95mDigite o valor em segundos: "))
    s = m = 0
    linha(45)
    while True:
        if s == 60:
            s -= 60
            segundos -= 60
            m += 1
        if s < 10:
            if m < 10:
                print(f"\r0{m}:0{s}", end='')
            else:
                print(f"\r{m}:0{s}", end='')
        else:
            if m < 10:
                print(f"\r0{m}:{s}", end='')
            else:
                print(f"\r{m}:{s}", end='')
        s += 1
        sleep(1)
        if s > segundos:
            break
    print()
    linha(45)