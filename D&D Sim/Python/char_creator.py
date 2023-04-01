import json, re, random, PySimpleGUI as sg
from char import Personagem

def remove_white_space(text):
    return re.sub('\s', '-', text)


def principal():
    sg.theme('DarkAmber')   # Dar um pouco de cor ao programa

    # Carregar os arquivos necessários
    with open('Info/armor.json', 'r') as arm:
        ARMOR = json.load(arm)
    with open('Info/weapons.json', 'r') as wpn:
        WEAPONS = json.load(wpn)
    # ----------------------------------------------
    
    # Salvar as chaves dos dicionários em listas
    armor_list = list(ARMOR.keys())
    weapon_list = list(WEAPONS.keys())
    
    # Criar da janela principal
    window = sg.Window(title='Criador de personagem', layout=[
        [sg.Text('Nome do personagem:', size=(16,1)), sg.InputText(key='-NAME-')],
        [sg.Text('Arma:', size=(16,1)), sg.InputCombo((weapon_list), key='-WPN-', readonly=True)],
        [sg.Text('Armadura:', size=(16,1)), sg.InputCombo((armor_list), key='-ARM-', readonly=True)],
        [sg.Text('O personagem tem escudo? ', size=(21,1)), sg.Radio('Sim', 'shield', key='-SIM-'), sg.Radio('Não', 'shield', key='-NAO-')],
        [sg.Button('Criar personagem'), sg.Button('Sair')]])
    # ----------------------------------------------
    
    # Loop que ouve constantemente por eventos na janela
    while True:
        event, values = window.read()

        # Se clicar no 'X' ou em 'Sair' sai do loop e fecha a janela
        if event == sg.WIN_CLOSED or event == 'Sair':
            break
        # ------------------------------------------

        if event == 'Criar personagem':

            # Salvar os equipamentos dos personagens
            char_equip = {
                "name": values['-NAME-'],
                "armor": values['-ARM-'],
                "weapon": values['-WPN-']
            }
            # --------------------------------------

            # Checar se o personagem tem um escudo
            if values['-SIM-']:

                # Se a arma dele tiver a propriedade 2-hand, ele não será capaz de usar um escudo
                if '2-hand' in WEAPONS[values['-WPN-']]['props']:
                    sg.popup('Erro!', 'Você não pode usar um escudo com uma arma de 2 mãos')
                    continue
                else:
                    char_equip['shield'] = True
                # -------------------------------
            else:
                char_equip['shield'] = False
        window.close()
        atributos()


def atributos():
    sg.theme('Dark Amber')

    atr_window = sg.Window('Escolha seus atributos', [[sg.Column([
        [sg.Text('Pontos restantes:', size=(15, 1))],
        [sg.Text('Força:', k='-STR-', size=(15, 1))],
        [sg.Text('Destreza:', k='-DEX-', size=(15, 1))],
        [sg.Text('Constituição:', k='-HP-', size=(15, 1))]]), sg.VSeparator(), sg.Column([
        [sg.pin(sg.Text(size=(8, 1), k='-NUM-',visible=False)),
        sg.pin(sg.Button('Rolar', k='-BTN-', visible=True))],
        [sg.Text('0', k='-STR_PT-', size=(15, 1))],
        [sg.Text('0', k='-DEX_PT-', size=(15, 1))],
        [sg.Text('0', k='-HP_PT-', size=(15, 1))]]),
        sg.Column([
            [sg.Text()],
            [sg.Button('+', k='-ADD_STR-', size=(1,1))],
            [sg.Button('+', k='-ADD_DEX-',size=(1,1))],
            [sg.Button('+', k='-ADD_HP-',size=(1,1))],
            ])],
        [sg.Button('Confirmar'), sg.Cancel('Sair')]], modal=True)

    while True:
        event, values = atr_window.read()

        if event == sg.WIN_CLOSED or event == 'Sair':
            break

        elif event == '-BTN-':
            sorte = random.randint(0, 4)
            pontos = random.randint(0, 20) + sorte
            atr_window['-BTN-'].Update(visible=False)
            atr_window['-NUM-'].Update(visible=True)
            atr_window['-NUM-'].Update(str(pontos))
            




def main():
    principal()

if __name__ == '__main__':
    main()
