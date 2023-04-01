import PySimpleGUI as sg
import re
import webbrowser

def popup(titulo, texto):
    _, _ = sg.Window(f'{titulo}', [[sg.Text(f'{texto}')], [sg.Yes('Ok', s=5)]], disable_close=True, modal=True).read(close=True)


def enviar(numero):
    if re.search('[a-zA-Z]', numero):
        popup('Erro!', 'O número não pode conter letras')
        return

    numero = re.sub('[\s()-]', '', numero)
    webbrowser.open(f'https://api.whatsapp.com/send?phone=55{numero}')


def window():

    sg.theme('SystemDefaultForReal')

    window = sg.Window('Insira um numero', layout=[
        [sg.Text('Insira o numero que você quer mandar mensagem'), sg.Input(k='-NUM-', do_not_clear=False)],
        [sg.Button('Enviar', bind_return_key=True), sg.Button('Sair')]])

    while True:
        evento, valores = window.read()

        if evento == sg.WIN_CLOSED or evento == 'Sair':
            break
        
        elif evento == 'Enviar':
            enviar(valores['-NUM-'])


    window.close()

def main():
    window()

if __name__ == '__main__':
    main()