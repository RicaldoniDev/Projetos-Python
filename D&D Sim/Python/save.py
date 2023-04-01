# print('teste')
# nome_formatado = remove_white_space(values['-NAME-']).lower()
# personagem_basico = {
#     values['-NAME-']:{
#             'armor': values['-ARM-'],
#             'weapon': values['-WPN-'],
#     }
# }
# # Se a chave do elemento do escudo for sim, cheque se a arma é de 2 mãos
# if values['-SIM-']:
#     if any('2-hand' in i for i in WEAPONS[values['-WPN-']]['props']):
#         sg.popup('Erro!', 'Você não pode usar um escudo com uma arma de 2 mãos')
#     else:
#         personagem_basico[values['-NAME-']]['shield'] = True
# else:
#     personagem_basico[values['-NAME-']]['shield'] = False

# # Tentar criar o arquivo com o nome do personagem. Se já existir, dê um aviso
# try:
#     open(f'JSON/{nome_formatado}.json', 'x')
# except FileExistsError:
#     sg.popup('Erro!', 'O personagem que você está tentando criar já existe')
#     continue

# with open(f'JSON/{nome_formatado}.json', 'r+') as f:
#     json.dump(personagem_basico, f)

# window.close()
# atributos()


# [
#          [sg.Text('Pontos restantes:', size=(15, 1))],
#          [sg.Text('Força:', k='-STR-', size=(15, 1))],
#          [sg.Text('Destreza:', k='-DEX-', size=(15, 1))],
#          [sg.Text('Constituição:', k='-HP-', size=(15, 1))]]
# [
#         [sg.Text()],
#         [sg.Text('0', k='-STR_PT-', size=(15, 1))],
#         [sg.Text('0', k='-DEX_PT-', size=(15, 1))],
#         [sg.Text('0', k='-HP_PT-', size=(15, 1))]])]