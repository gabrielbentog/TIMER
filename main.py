from time import sleep
import utilidades

utilidades.titulo("TIMER")
while True:
    esc = utilidades.menu("Em horas", "Em Minutos", "Em segundos", "Sair")
    if esc == 1:
        utilidades.calcHora()
    elif esc == 2:
        utilidades.calcMin()
    elif esc == 3:
        utilidades.calcSeg()
    elif esc == 4:
        print("OBRIGADO! TENHA UM BOM DIA".center(45))
        utilidades.linha(45)
        break