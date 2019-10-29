'''
   @autor: eleningoes
   nombre: ejercicio5.py
   descripción: ...
'''
# System.out.println("Igrese su nombre")
# nombre = entrada.nextLine()

nombre = input("Ingrese su nombre: \n")
edad = input("Ingrese su edad: \n")
nota1 = input("Ingrese el valor de su nota 1: \n")
nota2 = input("Ingrese el valor de su nota 2: \n")

suma = int(nota1) + int(nota2);

print("%s -- %s\n Su suma de notas es %s" % (nombre, edad, suma))
