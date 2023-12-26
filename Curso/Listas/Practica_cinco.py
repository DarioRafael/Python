#Si el numero es divisible entre 3, cambia el numero y que ponga PATO
#Si el numero es divisible entre 5, cambia el numero y que ponga chido
#Si el numero es divisible entre 3 y 5, cambia el numero y que ponga PATO CHIDO

numero = [7,4,23,1,15,5,3,30,75,0]
numero.sort()


for numerito in numero:
    if numerito == 0:
        continue
    elif numerito % 3 == 0 and numerito % 5 == 0:
        print(numerito , "PATO CHIDO")
    elif numerito % 3 == 0:
        print(numerito , "PATO")
    elif numerito % 5 == 0:
        print(numerito , "CHIDO")
        
print(" ")
print(" ")
        
#numero = [numerito for numerito in numero if numerito != 0]

numero = [
          "PATOCHIDO" if numerito % 5 == 0 and numerito % 3 == 0 else 
          "CHIDO" if numerito % 5 == 0 else 
          "PATO" if numerito % 3 == 0 else 
          numerito for numerito in numero if numerito != 0
          ]


print(numero)

