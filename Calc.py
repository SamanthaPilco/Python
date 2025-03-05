# #Estoy definiendo la variable num1 = 5
# num1 = 5
# #Estoy definiendo la variable num2 = 3
# num2 = 3
# #Estoy imprimiendo la suma de num1 y num2
# print(num1 + num2)

print ("\tEjercicio Semana 11")
print ("\nCalculadora\n")

num1= float(input("Ingrese el primer número: ")) #Se solicita ingresar el primer número
num2= float(input("Ingrese el segundo número: ")) #Se solicita ingresar el segundo número
print()

def suma(num1,num2):
    # return (num1 + num2)
    print("La suma de ",num1, "+",num2,"=",num1 + num2)

suma(num1, num2) #Se llama a la función suma
print ()

def resta(num1,num2):
    print("La resta de ",num1, "-",num2,"=",num1 - num2)

resta(num1, num2) #Se llama a la función resta
print()

def division(num1,num2):
    if num2==0:
        print("No se puede dividir por cero")
    else:
        print("La división de ",num1, "/",num2,"=",num1 / num2)

division(num1, num2) #Se llama a la función división
print ()

def multiplicacion(num1,num2):
    print("La multiplicación de ",num1, "*",num2,"=",num1 * num2)

multiplicacion(num1, num2) #Se llama a la función multiplicación
    
# print("La suma de ",num1, "+",num2,"=",num1 + num2)
# print("La resta de ",num1, "-",num2,"=",num1 - num2)
# print("La multiplicación de ",num1, "*",num2,"=",num1 * num2)
# print("La división de ",num1, "/",num2,"=",num1 / num2)
# if num2==0:
#     print("No se puede dividir por cero")
# else:
#     print("La división entera de ",num1, "//",num2,"=",num1 // num2)
#     print("El residuo de ",num1, "%",num2,"=",num1 % num2)



