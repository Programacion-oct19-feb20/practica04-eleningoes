'''
   @autor: eleningoes
   nombre: ejercicio7.py
   descripción: ...

   Lenin Toledo 21
   Su suma de notas es: 30
   Su promedio es:15
'''
# System.out.println("Igrese su nombre")
# nombre = entrada.nextLine()

nombre = input("Ingrese su nombre: \n\t")
edad = input("Ingrese su edad: \n\t")
nota1 = input("Ingrese el valor de su nota 1: \n\t")
nota2 = input("Ingrese el valor de su nota 2: \n\t")

suma = int(nota1) + int(nota2);
promedio = int(suma)/2;

print("%s -- %s\n Su suma de notas es: \n\t%s\n Su promedio es: \n\t%s\n" % (nombre, edad, suma, promedio))
