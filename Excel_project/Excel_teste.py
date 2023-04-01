import win32com.client as win32

def limpar_tabela(ws):
    for tabelas in ws.PivotTables():
        tabelas.TableRange2.Clear()

def iserir_campo_td_set1(td):
    campo_linhas = {}
    campo_linhas['situação'] = td.PivotFields('Situação')
    campo_linhas['modelo'] = td.PivotFields('Modelo')

    campo_valores = {}
    campo_valores['tipo'] = td.PivotFields('Tipo')

    # Inserir campos de linha no design da TD
    campo_linhas['situação'].Orientation = 1
    campo_linhas['situação'].Position = 1

    campo_linhas['modelo'].Orientation = 1
    campo_linhas['modelo'].Position = 2

    #Inserir campos de dados no design
    campo_valores['tipo'].Orientation = 4
    campo_valores['tipo'].Function = -4112
    campo_valores['tipo'].NumberFormat = '#'
    

# Abrir a aplicação do Excel
xl = win32.Dispatch('Excel.Application')
xl.Visible = True

# Criar a pasta de trabalho (Workbooks)
wb = xl.Workbooks.Open('C:\\Users\\juliano.melo\\Documents\\Teste.xlsx')

# Referenciar as planilhas (WorkSheets) dentro da pasta de trabalho (wb)
ws_dados = wb.Worksheets('Dados')
ws_tabela = wb.Worksheets('Tabela')

# Limpar todas as tabelas anteriores
limpar_tabela(ws_tabela)

# Criar conexão com o cache de TD (Para salvar os dados de uma Tabela Dinâmica)
td_cache = wb.PivotCaches().Create(1, ws_dados.Range('A1').CurrentRegion)

# Criar a TD
td = td_cache.CreatePivotTable(ws_tabela.Range('B2'), 'Inventário')

# Ligar/Desligar totais
td.ColumnGrand = True
td.RowGrand = False

# Mudar a localização do subtotal
td.SubtotalLocation(2) # Baixo (1 == Cima)

# Mudar o layout
td.RowAxisLayout(1)

# Estilo da TD
td.TableStyle2 = 'PivotStyleMedium9'

# Criar o report
iserir_campo_td_set1(td)