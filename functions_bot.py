from pyautogui import *

#FUNÇÃO PARA CRIAR UM DICIONÁRIO COM DADOS
def cria_contato(nome, mensagem, data_envio):
    contato ={"Nome": nome, 
            "Mensagem": mensagem,
            "Data_Envio": data_envio}

    return contato

#FUNÇÃO PARA PESQUISAR O CONTATO NA BARRA DE NOMES
def busca_contato(name):
    x1, y1 = [211,155]

    moveTo(x1, y1)
    click()
    typewrite(name, interval=1.2)
    sleep(1)
    press('enter')
  

#FUNÇÃO PARA ENVIAR A MENSAGEM 
def envia_mensagem(msg): 
    x2, y2 = [600,680] 
    moveTo(x2, y2) 
    click() 
    sleep(1.5) 
    typewrite(msg) 
    press('enter')

#FUNÇAO QUE LIMPA O CAMPO DE BUSCA DE CONTATO
def limpa_campo():
    x3,y3 = [50,155]
    moveTo(x3, y3) 
    click() 
    sleep(1.5) 
    press('enter')
