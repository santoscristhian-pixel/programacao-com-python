import re
codigo = input("Digite um codigo!")
if re.fullmatch(r"[a-z0-9]{5}", codigo):
    print("codigo valido!")
else:
    print("codigo invalido!")

