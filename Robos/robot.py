import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import xlrd
import re





def start_robot(dominio):
    driver = webdriver.Chrome(service=Service('C:\\Users\\juliano.melo\\Documents\\VSCode\\my_shared_codes\\Robos\\chromedriver.exe'))
    driver.get('https://registro.br/')

    pesquisa = driver.find_element(by=By.ID, value= 'is-avail-field')
    pesquisa.clear()

    pesquisa.send_keys(dominio)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(1)

    resultado = driver.find_elements(by= By.TAG_NAME, value='strong')
    
    

    if resultado[4].text == 'disponível':
       
        # janela_de_compra(driver)
        sg.Window('Cadastrar ')
        sg.popup(f'O domínio {dominio} está disponível para compra')

    else:
        sg.popup(f'O domínio {dominio} não está disponível para compra', title='Aviso!')

    driver.close()


def janela_de_compra(driver):
    pass


def tela_inicial():
    sg.theme('Default1')

    janela = sg.Window('Robot', layout=[
        [sg.T('Insira o domínio que quer validar:'), sg.Input(k='-DOMAIN-')],
        [sg.Button('Procurar'), sg.Button('Sair')]])

    while True:
        evento, valores = janela.read()

        if evento == sg.WIN_CLOSED or evento == 'Sair':
            break

        if evento == 'Procurar':
            if not re.search('\.com$|\.com\.br$|.', valores['-DOMAIN-']):
                sg.popup('O domínio que você está procurando não é um domínio válido', title='Error')
            else:
                start_robot(valores['-DOMAIN-'])
    
    janela.close()

def main():
    tela_inicial()

if __name__ == '__main__':
    main()