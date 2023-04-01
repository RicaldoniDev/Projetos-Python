import PySimpleGUI as sg


class Gastos:

    # Inicializa a classe com o nome do arquivo para salvar, o dicionário que será salvo e a lista que 
    # vai receber os valores a serem calculados
    def __init__(self):
        
        self.save_data = {}

        self.lista_valores = []


    # Função para criar um popup de erro
    def popup(self, titulo, texto):
        _, _ = sg.Window(f'{titulo}', [[sg.Text(f'{texto}')], [sg.Yes('Ok', s=5)]], disable_close=True, modal=True).read(close=True)


    def mostrar_tabela(self, dicionario):
        tabela =''
        
        for i in  dicionario:
            tabela += f'{i} : {dicionario[i]}\n'

        
        janela_tabela = sg.Window('Gastos', layout=[[sg.Text('Esse é o valor separado de cada gasto:')],
                                                    [sg.Text(text=tabela)],
                                                    [sg.Button('Ok', s=(5))]])

        while True:
            evento, _ = janela_tabela.read()
            

            if evento == 'Ok' or evento == sg.WIN_CLOSED:
                break

        janela_tabela.close()


    def inicio(self):
        
        # Lista do combo
        gastos_lista = ['Luz', 'Agua', 'Intenet','Impostos', 'Outros',]

        sg.theme('DarkBlue4')
        
        janela = sg.Window('Cálculo de gastos', layout=[  
                 [sg.Text('Qual foi o gasto?')],
                 [sg.Combo(gastos_lista, default_value='Gastos', size=(15),readonly=True, k='-COMBO-', enable_events=True)],
                 [sg.Text('Qual?')],
                 [sg.Input(k='-TEXTO-', disabled=True, do_not_clear=False)],
                 [sg.Text('Quanto foi o valor gasto? (Digite apenas números)')],
                 [sg.Input(k='-VALOR-', do_not_clear=False), sg.Button('Adiciona')],
                 [sg.Text(k='-RESULTADO-')],
                 [sg.Button('Calcular'), sg.Button('Tabela'), sg.Button('Sair')]])

        
        
        while True:

            evento, valores = janela.read()

            # Verificar se a janela foi fechada ou o botão Sair foi apertado
            if evento == sg.WIN_CLOSED or evento == 'Sair':
                break

            # Verifica se o Combo gerou um evento e se o valor for Outros ativa a caixa    
            elif evento == '-COMBO-' and valores['-COMBO-'] == 'Outros':
                janela['-TEXTO-'].update(disabled=False)
            
            # Verifica o contrario da linha anterior para desativar a caixa novamente
            elif evento == '-COMBO-' and valores['-COMBO-'] != 'Outros':
                janela['-TEXTO-'].update(disabled=True)

            elif evento == 'Calcular':
                janela['-RESULTADO-'].update(f'O valor total dos gastos é: {self.calcular_valores()}')
                
            elif evento == 'Adiciona' and valores['-VALOR-'] != '':
                self.adiciona_gastos(valores['-VALOR-'], valores['-COMBO-'], valores['-TEXTO-'])
            
            elif evento == 'Tabela':
                self.mostrar_tabela(self.save_data)

        janela.close()

    def adiciona_gastos(self, valor_gasto, item_gasto, outros_valor):
        if item_gasto != 'Outros':
            self.save_data[item_gasto] = valor_gasto
        else:
            self.save_data[outros_valor] = valor_gasto


    def calcular_valores(self):
        resultado = 0

        if self.save_data == {}:
            self.popup('Erro!', 'Não tem números para serem calculados')
            return 0

        else:
            for i in self.save_data:
                self.lista_valores.append(self.save_data[i])

            for numero in self.lista_valores:
                resultado += float(numero)

            return resultado
            


def main():
    gastos = Gastos()
    gastos.inicio()



if __name__ == '__main__':
    main()
import PySimpleGUI as sg


class Gastos:

    # Inicializa a classe com o nome do arquivo para salvar, o dicionário que será salvo e a lista que 
    # vai receber os valores a serem calculados
    def __init__(self):
        
        self.save_data = {}

        self.lista_valores = []
       

    # Função para criar um popup de erro
    def popup(self, titulo, texto):
        _, _ = sg.Window(f'{titulo}', [[sg.Text(f'{texto}')], [sg.Yes('Ok', s=5)]], disable_close=True, modal=True).read(close=True)


    def mostrar_tabela(self, dicionario):
        tabela =''
        
        for i in  dicionario:
            tabela += f'{i} | {dicionario[i]}\n'

        
        janela_tabela = sg.Window('Gastos', layout=[[sg.Text('Esse é o valor separado de cada gasto:')],
                                                    [sg.Text(text=tabela)],
                                                    [sg.Button('Ok', s=(5))]])

        while True:
            evento, _ = janela_tabela.read()
            

            if evento == 'Ok' or evento == sg.WIN_CLOSED:
                break

        janela_tabela.close()


    def inicio(self):
        
        # Lista do combo
        gastos_lista = ['Luz', 'Agua', 'Intenet','Impostos', 'Outros',]

        sg.theme('DarkBlue4')
        
        janela = sg.Window('Cálculo de gastos', layout=[  
                 [sg.Text('Qual foi o gasto?')],
                 [sg.Combo(gastos_lista, default_value='Gastos', size=(15),readonly=True, k='-COMBO-', enable_events=True)],
                 [sg.Text('Qual?')],
                 [sg.Input(k='-TEXTO-', disabled=True, do_not_clear=False)],
                 [sg.Text('Quanto foi o valor gasto? (Digite apenas números)')],
                 [sg.Input(k='-VALOR-', do_not_clear=False), sg.Button('Adiciona')],
                 [sg.Text(k='-RESULTADO-')],
                 [sg.Button('Calcular'), sg.Button('Tabela'), sg.Button('Sair')]])

        
        
        while True:

            evento, valores = janela.read()

            # Verificar se a janela foi fechada ou o botão Sair foi apertado
            if evento == sg.WIN_CLOSED or evento == 'Sair':
                break

            # Verifica se o Combo gerou um evento e se o valor for Outros ativa a caixa    
            elif evento == '-COMBO-' and valores['-COMBO-'] == 'Outros':
                janela['-TEXTO-'].update(disabled=False)
            
            # Verifica o contrario da linha anterior para desativar a caixa novamente
            elif evento == '-COMBO-' and valores['-COMBO-'] != 'Outros':
                janela['-TEXTO-'].update(disabled=True)

            elif evento == 'Calcular':
                janela['-RESULTADO-'].update(f'O valor total dos gastos é: {self.calcular_valores()}')
                
            elif evento == 'Adiciona' and valores['-VALOR-'] != '':
                self.adiciona_gastos(valores['-VALOR-'], valores['-COMBO-'], valores['-TEXTO-'])
            
            elif evento == 'Tabela':
                self.mostrar_tabela(self.save_data)

        janela.close()

    def adiciona_gastos(self, valor_gasto, item_gasto, outros_valor):
        if item_gasto != 'Outros':
            self.save_data[item_gasto] = valor_gasto
        else:
            self.save_data[outros_valor] = valor_gasto


    def calcular_valores(self):
        resultado = 0

        if self.save_data == {}:
            self.popup('Erro!', 'Não tem números para serem calculados')
            return 'Erro!'

        else:
            for i in self.save_data:
                self.lista_valores.append(self.save_data[i])

            for numero in self.lista_valores:
                resultado += float(numero)

            return resultado
            


















def main():
    gastos = Gastos()
    gastos.inicio()



if __name__ == '__main__':
    main()
