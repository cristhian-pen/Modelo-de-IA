import pyautogui, time
from selenium import webdriver
from selenium.webdriver.common.by import By

def OpenLAPS():
    print("It Works")

def OpenAD():
    print('feature in development')

def OpenTeams():
    pyautogui.press('win')
    time.sleep(0.3)
    pyautogui.write('teams')
    pyautogui.press('enter')

def OpenWebTools():
#Abre as ferramentas web
    jiraSolicitante = 'https://servicedesk-autoglass.atlassian.net/servicedesk/customer/portals'
    jiraAtendente = 'https://servicedesk-autoglass.atlassian.net/jira/your-work'
    outlook = 'https://outlook.office365.com/mail/inbox/'
    tabsReports = 'https://autoglass365-my.sharepoint.com/:x:/r/personal/cristhian_moura_autoglass_com_br/_layouts/15/doc2.aspx?sourcedoc=%7BC633C6BF-B8D7-46C4-9D49-EC0A57D6CCCE%7D&file=Chamados_liga%C3%A7%C3%B5es.xlsx&action=default&mobileredirect=true&DefaultItemOpen=1&ct=1739444011486&wdOrigin=OFFICECOM-WEB.START.EDGEWORTH&cid=dbf617a1-533d-47d8-891b-b0ccbbbb2c1a&wdPreviousSessionSrc=HarmonyWeb&wdPreviousSession=bd3267e7-9790-447e-9dee-c164875ab068'

    tabs = webdriver.Chrome()
#abre o chrome
    tabs.get('https://autoglass365.sharepoint.com/sites/portalcorporativo')
    time.sleep(3)
    
#autentica no portal
    """ assert "Entrar em sua conta" in tabs.title
    elem = tabs.find_element(By.ID, "i0118")
    elem.send_keys('IronMharkv10$@')
    pyautogui.press('enter') """
#tempo da autenticação
    time.sleep(3)
#autentica
    pyautogui.write('cristhian.moura@autoglass.com.br')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write('IronMharkv10$@')
    time.sleep(1)
    pyautogui.press('enter')
#abre as ferramentas em novas guias
    pyautogui.hotkey('ctrl' + 't')
    pyautogui.write(outlook)
    pyautogui.hotkey('ctrl' + 't')
    pyautogui.write(jiraAtendente)
    pyautogui.hotkey('ctrl' + 't')
    pyautogui.write(jiraSolicitante)
    pyautogui.hotkey('ctrl' + 't')
    pyautogui.write(tabsReports)

def OpenSysVendas():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('Vendas')
    time.sleep(1)
    pyautogui.press('enter')  

def OpenSysSI():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('SI')
    time.sleep(1)
    pyautogui.press('enter')

def OpenPLSQL():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('PL')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(7)
    pyautogui.write('Ironmharkv10#')

