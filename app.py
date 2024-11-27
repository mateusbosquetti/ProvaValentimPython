#1
a = 5
b = 3
print(a + b)

#2
x = "Python"
print(x.__len__())

#3
y = 8
print(y-3)

#4
nome = "Mateus Henrique Bosquetti"
print(len(nome))

#5
print(15/3)

#6
print(29 % 4)

#7
print(7*6+10)

#8
print((25-50) / 5)

#9
if(10 > 5):
    print("Maior")


#10
idade = 19
if (idade >= 18):
    print("Adulto")
    
#11
nota = 7
if (nota >= 7):
    print("Aprovado")
else:
    print("Reprovado")
    
#12
x = 11
y = 23
if (x < 10 and y > 20):
    print("Condicao Atendida")
else:
    print("Condicao nao Atendida")
    
#13
for i in range(1, 6):
    print(i)
    
#14
for i in range(2, 10):
    if (i % 2 == 0):
        print(i)

#15
contador = 1
while (contador <= 5):
    print(contador)
    contador = contador + 1
    
#16
for i in range(1, 10):
    print(i, " + " , (i + 1) , " = " , (i + i + 1))

#17
frutas = ["maca", "banana", "laranja"]
print(frutas)

#18
frutas.append("uva")
print(frutas)

#19
frutas.pop(1)
print(frutas)

#20
print(frutas[0])

#21
def saudacao(nome):
    print("Ola, " + nome)
    
saudacao("Mateus")

#22
def soma(a, b):
    return(a + b)

print(soma(2, 3))