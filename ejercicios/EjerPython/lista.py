
lista =[5,15,20,35]

suma = 0
for elemento in lista:
    suma += elemento


promedio  = suma / len(lista)

print(suma)
print(promedio)

nuevaLista =[] 
for elemento in lista:
    if(elemento > 10):
        nuevaLista.append(elemento)
        
print(nuevaLista)

print(sum([elemento for elemento in lista if elemento > 10]))
print(min([elemento for elemento in lista if elemento > 10]))

lista2 = [{"nombre" : "JI" , "edad" : 44} ,{"nombre" : "MI", "edad" : 10} ]


longitudMayores = len([elemento for elemento in lista2 if elemento["edad"] >=18])
print(sum([elemento["edad"] for elemento in lista2 if elemento["edad"] >=18]) / longitudMayores)

