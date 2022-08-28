import playsound
import utilidades

utilidades.titulo("TIMER")
while True:
    #Escolha a ordem dos itens no menu, caso haja alteração mude nos valores dos ifs.
    esc = utilidades.menu("Em horas", "Em Minutos", "Em segundos", "Sair")
    if esc == 1:
        #Calcula em horas
        utilidades.calcHora()
        playsound("sound.mp3")
    elif esc == 2:
        #Calcula em minutos
        utilidades.calcMin()
    elif esc == 3:
        #Calcula em Segundos
        utilidades.calcSeg()
        playsound("sound.mp3")
    elif esc == 4:
        #Fecha o programa
        print("\033[1;95mOBRIGADO! TENHA UM BOM DIA\033[0;0m".center(57))
        utilidades.linha(45)
        break