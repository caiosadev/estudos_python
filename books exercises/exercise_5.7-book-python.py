numb_one = int(input("Tabuada de: "))
numb_two = int(input("Até o número: "))

x = numb_one

while x <= numb_two:
    print(f"{numb_one} + {x} = {numb_one + x}") #variavel dentro de string
    x += 1




#variável /resultado/ com o conteúdo de print.
numb_one = int(input("Tabuada de: "))
numb_two = int(input("Até o número: "))

x = numb_one

while x <= numb_two:
    resultado = (f"{numb_one} + {x} = {numb_one + x}")
    print(resultado)
    x += 1
