import sys, json

# Salvando o nome do arquivo dos personagens
CHAR_STRING1 = sys.argv[1]
CHAR_STRING2 = sys.argv[2]

# Carregar os arquivos necessários

with open("armor.json", "r") as arm:
    ARMOR = json.load(arm)

with open("weapons.json", "r") as wpn:
    WEAPONS = json.load(wpn)

with open(CHAR_STRING1, "r") as ch1:
    CHAR1 = json.load(ch1)

with open(CHAR_STRING2, "r") as ch2:
    CHAR2 = json.load(ch2)



def main():
    pass

if __name__ == '__main__':
    main()