from functions_bot import*
from pyautogui import *
from datetime import *
import json

print("\n---- WhatsBot ----\n")
lista_registro = []
decisao = str("S").upper()


while decisao == str("S").upper():

    contato = str(input("\nDigite o contato: "))
    msg = str(input("\nDigite a mensagem a ser encaminhada: "))

    data_hora = datetime.now()
    data = data_hora.strftime('%H:%M:%S do dia %d/%m/%y')
    dado = cria_contato(contato,msg, data)
    lista_registro.append(dado)
    print(lista_registro)

    #CRIA UM HISTÓRICO DE MENSAGENS EM FORMATO JSON
    json_object=json.dumps(lista_registro, indent=3)
    with open("historico.json", "w") as historico:
         historico.write(json_object)

    decisao = str(input("Deseja enviar mensagem para outro contato? S || N -->  ")).upper()

    

    if decisao == str("N").upper():
        for dados in lista_registro:
            nome = dados['Nome']
            mensagem = dados['Mensagem']
            data_envio = dados['Data_Envio']
            busca_contato(nome)
            envia_mensagem(mensagem)
            limpa_campo()
            print(f"\nMensagem encaminhada para {nome.upper()} às {data_envio} ")

            

       
        exit()



    """"
    contato=cria_contato(nome, msg) #C1 CRIA UM NOVO CONTATO
    json_object = json.dumps(contato)
    arch=open('contatos.json','a')
    arch.write("\n"+str(json_object)+"\n") #salva os dados do contato no arquivo contato.json
    arch.close()

    historico_mensagem = open('contatos.json','r') #ABERTURA E LEITURA DO ARQUIVO 
    json_load = json.load(historico_mensagem)
    print(json_load)
    print("\n")
    print(json_load["Contato"])
    print(json_load["Mensagem"])"""
        
        
        
        

      
                            
                    
""""


time.sleep(1)

busca_contato(nome)
envia_mensagem(msg)

print(f"\nMensagem encaminhada com sucesso para {nome.upper()} !\n")
   """
        

   
   

