expr = str(input("Digite sua expressão: "))
paratense = []
for para in expr:
    if para == "(":
        paratense.append("(")
    elif para == ")":
        if len(paratense) > 0:
            paratense.pop()
        else:
            paratense.append(")")
            break
if not paratense:
    print("Essa expressao exta correta")
else:
    print("Essa expressão esta errada")