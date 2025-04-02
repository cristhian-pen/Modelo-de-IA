import pyautogui, keyboard, time, IGRIS.IgrisChat.igrisChat
from pynput.mouse import Controller, Listener


def Alerts(message):

    pyautogui.alert(text=f'{message}', title="IGRIS")
    pyautogui.PAUSE = 0.5 
    pyautogui.press('enter')

def DomainChek():

#Variaveis e verificações
    IaName = [ 'i', 'g', 'r', 'i', 's' ]
    correctSequence = [ 'j', 'a', 'r', 'v', 'i', 's' ]
    sequence = [ ]
    activeKeys = [ 'j', 'a', 'r', 'v', 'i', 's', 'g' ]
    blockKeys = ['1','2','3','4','5','6','7','8','9','0','-','=','q','w','e','r','t','y','u','i','o','p','a','s','d','f','h','j','k','l','ç', 'win', 'ctrl', 'shift', 'del', 'alt', 'fn', 'tab', 'esc']
    count=0

#Bloqueia teclas
    for key in blockKeys:
        if key not in blockKeys:
            keyboard.block_key(key)

#valida sequencia digitada
    while True:
        event = keyboard.read_event(suppress=True)

        if event.name in activeKeys:
            time.sleep(0.3)
            sequence.append(event.name)

#Faz a Primeira interação com o usuario que errou a sequencia
            if count == 7:
                IGRIS.IgrisChat.igrisChat.FirstInteractionLocked()
                sequence = [ ]
#Segunda interação
            if sequence == IaName:
                IGRIS.IgrisChat.igrisChat.SeccondInteractionLocked()
                sequence = [ ]
                count - 7
#Terceira interação
            if count == 12:
                IGRIS.IgrisChat.igrisChat.ThirdInteractionLocked()
                sequence = [ ]
#Interação Final
            if count >= 21:
                IGRIS.IgrisChat.igrisChat.FinalInteractionLocked()
                sequence= [ ]
                count=0

            if sequence == correctSequence:
                print('Sequencia correta, desbloqueando teclado!')
                break
            else:
                count+=1 
    
#Desbloqueia Teclas
    keyboard.unhook_all()
    Alerts("Aparelho desbloqueado!")

#Mensagem da IA
    if count > 7:
        Alerts("Senhor tentaram acessar sua maquina sem sua permissão, verifique se voce deixou o equipamento desbloqueado!")
            