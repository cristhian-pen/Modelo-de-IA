import datetime
from IGRIS.IgrisChat.igrisChat import *
from IGRIS.IgrisActions.actions import *
import IGRIS.IgrisInteractions.IgrisInteractions


#get time
morning = "06:00"
aftNoon = "12:00"
evening = "18:00"
night = "23:59"
dawn = "05:00"
getTime =  datetime.datetime.now()
formatTime = getTime.strftime( "%H:%M" )

def Main():
#validações de horario

    if (formatTime >= morning) and (formatTime < aftNoon):
        IGRIS.IgrisInteractions.IgrisInteractions.Alerts('Bom dia senhor cristhian!, estou configurando sua maquina!')      

    elif (formatTime >= aftNoon) and (formatTime < evening):
        IGRIS.IgrisInteractions.IgrisInteractions.Alerts('Boa Tarde senhor cristhian!, seja bem vindo a sua maquina, tenha uma boa utilização!')

        dayWork = pyautogui.confirm(text="Hoje e dia de trabalho?",title="IGRIS", buttons=["Sim", "Não"])

        if dayWork == "Sim":
            OpenTeams()
            OpenWebTools()
        else:
            CustomChat('Deixarei sua maquina livre, qualquer coisa me acione estarei por aqui!')

    elif (formatTime >= evening) and (formatTime < night):
        IGRIS.IgrisInteractions.IgrisInteractions.Alerts('Boa noite senhor crishian!, seja bem vindo a sua maquina, tenha uma boa utilização!')
        OpenWebTools()
    elif (formatTime >= night) and (formatTime < dawn): 
        IGRIS.IgrisInteractions.IgrisInteractions.Alerts('estranho, esse horario??? o acesso esta fora do padrão, me diga, o que estou pensando agora????')
    else:
        IGRIS.IgrisInteractions.IgrisInteractions.Alerts("Someting wrong! IA system is failure, please check your code or contact you administrator!")

def Code(): 
    code = input('O que voce quer que eu faça senhor? ')
    IGRIS.IgrisInteractions.IgrisInteractions.DomainChek()

Main()
#Code()
