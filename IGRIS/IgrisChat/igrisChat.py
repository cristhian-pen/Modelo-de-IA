import pyautogui

def CustomChat(message):
    pyautogui.alert(text=f'{message}', title='IGRIS')

def FirstInteractionLocked():
    pyautogui.alert(text="Oi eu sou o IGRIS e voce esta tentando acessar a maquina do meu criador.... o teclado esta bloqueado e a chave e uma sequencia de letras que deve ser digitada beeeem lentamente, mas tenho a certeza de que você não consegue :)", title="IGRIS")

def SeccondInteractionLocked():
    pyautogui.alert(text="E não e meu nome rssrsrs", title="IGRIS")

def ThirdInteractionLocked():
    pyautogui.alert(text="Mais uma tentativa e eu aviso o administrador de rede ainda vou informar ao meu criador que voce tentou usar a maquina dele!!!", title="IGRIS") 

def FinalInteractionLocked():
    pyautogui.alert(text="Tentativa de acesso não autorizado no patrimonio N132784!, possível violação de segurança o evento será enviado ao administrador de rede!", title="IGRIS")
