TOKEN = "fd579b77da974b62bf7b75ba2dde566cc621b20921dbb363fcc4220cd087e4b12eb211390df7d13fdd749"


introduction = ""
with open('introduction.txt', 'r', encoding="utf8") as f:
    introduction = f.read()


help = ""
with open('help.txt', 'r', encoding="utf8") as f:
    help= f.read()

unknown = "Неизвестная команда, напишите 'помощь', чтобы посмотреть список доступных команд"