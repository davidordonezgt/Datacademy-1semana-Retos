#Reto de la 1ra-Semana del Datacademy

menu = """
Que haremos hoy, ingrese lo que haras:
1. Hallar el area de un triangulo
2. Jugar papel o tijera
3. covertidor de millas a kilometros
4. Hallar el volumen cilindro
5. Hacer comparaciones
6. Para terminar
"""

def area_triangulo ():
    valor_area = int(input("Ingrese la base  "))
    valor_altura = int(input("Ingrese la altura  "))
    area_triangulo = ((valor_area * valor_altura)/2)
    area_triangulo = str(area_triangulo)
    print("El area del triangulo es " + area_triangulo)
    
def triangulo():
    lado1 = int(input("Ingrese el primer lado "))
    lado2 = int(input("Ingrese el segundo lado "))
    lado3 = int(input("ingrese el tercer lado  "))
    if (lado1 == lado2 == lado3):
        print("Triangulo equilatero, es lado equilatero por que tiene todo los lados iguales")
    elif((lado1 == lado2 !=lado3) or (lado2 == lado3 !=lado1) or (lado3 == lado1 !=lado2)):
        print("Triangulo isoseles:  Es triangulo isoseles por que dos lados son iguales")
    elif(lado1 != lado2) or (lado2 !=lado3) or (lado1 != lado3):
        print("Triángulo escaleno: es triangulo escaleno por que todos sus lados son distintos")

def juego():
    menu_juego= """
    Juego de piedra, papel, o tijera. Se termina quien gane dos veces
    1. Piedra
    2. papel
    3. tijera
    """
    cpu = random.randint(1, 3)
    usuario = int(input(menu_juego))
    vida_cpu=0
    vida_usuario=0

    while True:
        if usuario == cpu:
            print( "Empate", usuario, cpu)
        elif usuario == 1 and cpu == 2: 
            print(usuario,' Piedra ',' Perdiste ',cpu,' Papel ')
            vida_cpu = vida_cpu + 1
        elif usuario == 1 and cpu == 3:
            print(usuario,' Piedra ',' Ganaste ',cpu, ' Tijeras ' )
            vida_usuario = vida_usuario +1
        elif usuario == 2 and cpu == 1:
            print(usuario,' Papel ',' Ganaste ',cpu,' Piedra ')
            vida_usuario = vida_usuario +1
        elif usuario == 2 and cpu == 3:
            print(usuario,' Papel ',' Perdiste ',cpu,' Tijeras ')
            vida_cpu = vida_cpu +1
        elif usuario == 3 and cpu == 1:
            print(usuario,' Tijera ',' Perdiste ',' Piedra ', cpu)
            vida_cpu = vida_cpu +1
        elif usuario == 3 and cpu == 2:
            print(usuario,' Tijeras ',' Ganaste ',' Papel ', cpu)
            vida_usuario = vida_usuario +1
        else:
            print("Numero incorrecto")

        if vida_cpu == 2:
            print("Gano la maquina")
            break
        if vida_usuario == 2:
            print("Ganaste")
            break

        cpu = random.randint(1, 3)
        usuario = int(input(menu_juego))

def maraton():
    menu_maraton = """
    Bienvenido al maraton de programacion, aqui puedes convertir tus millas en kilometroo kilometro en millas. Ingrese la opcion deseada
    1. Kilometro a milla
    2. Milla a kilometro
    3. Terminar la operacion
    """   

    menu_maraton_usuario = int(input(menu_maraton))

    while menu_maraton_usuario != 3:

        if menu_maraton_usuario == 1:
            kilometro = float(input(" Ingrese la cantidad de kilometro que hizo "))
            convertidor_kilometro = (kilometro / 1.609344)
            convertidor_kilometro = float(convertidor_kilometro)
            print("La cantidad de kilometro es", convertidor_kilometro)
        if menu_maraton_usuario == 2:
            milla =  float(input(" Ingrese la cantidad de millas "))
            convertido_milla = (milla*1.609344)
            convertido_milla = float(convertido_milla)
            print("La cantidad de milla es ",convertido_milla)

        menu_maraton_usuario = int(input(menu_maraton))

def Ecuaciones_figuras():
    menu_figura= """
    Bienvenido al calculador de figura, podra saber el volumen de un cilindro, Paralelogramo, Cubo: No hay presupuesto para otra figura de
    Ingrese la opcion:
    1.Volumen del  cilindro
    2.Volumen Paralelogramo
    3.Volumen cubo
    4.Terminar la operacion
    """
    menu_volumen=int(input(menu_figura))

    while menu_volumen !=4:
        if menu_volumen == 1:
            altura_cilindro = int(input("Ingrese la altura del cilindro "))
            radio_cilindro = int(input("Ingrese el radio "))
            volumen_cilindro = (3.1416*(radio_cilindro**2)*altura_cilindro)
            volumen_cilindro = float(volumen_cilindro)
            print("El volumen del cilindro es ",volumen_cilindro)
        if menu_volumen == 2:
            lado1 = int(input("Ingrese el primer lado: "))
            lado2 = int(input("Ingrese el segundo lado "))
            altura_paralelogramo =int(input("Ingrese la altura del paralelogramo "))
            volumen_paralelogramo = ((lado1*lado2)*altura_paralelogramo)
            volumen_paralelogramo = int(volumen_paralelogramo)
            print("Volumen del paralologramo ",volumen_paralelogramo)
        if menu_volumen == 3:
            lado_cubo= int(input("Ingrese el lado del cubo "))
            volumen_cubo=(lado_cubo*lado_cubo*lado_cubo)
            volumen_cubo=int(volumen_cubo)
            print("El volumen del cubo es: ", volumen_cubo)
        menu_volumen=int(input(menu_figura))

def limites():
      
    limite_inferior = int(input("Ingrese el limite inferior "))
    limite_superior = int(input("Ingrese el limite superior "))
    limite_comparacion= int(input("Ingrese el limite de comparacion "))

    while True:
        if limite_comparacion > limite_inferior and limite_comparacion < limite_superior:
            print("Esta en el rango ")
            break 
        if limite_comparacion > limite_superior and limite_comparacion < limite_inferior:
            print("Esta en el rango ")
            break 
        print("No esta en el rango, ingrese otra vez el limite de comparacion ")
        limite_comparacion= int(input("Ingrese el limite de comparacion "))
        
def run():
    opciones = int(input(menu))
    while opciones != 6:
        if opciones == 1:
            area_triangulo()
            menu_triangulo ="""
            Quieres saber si un triangulo es isósceles, equilátero o escaleno, 
            1: Si
            2: No
            """
            opciones_triangulo= int(input(menu_triangulo))
            if opciones_triangulo == 1:
                triangulo()
            elif opciones_triangulo == 2:
                pass
            else:
                print("Ingrese bien el dato")
            
        elif opciones == 2:
            juego()
            
        elif opciones == 3:
            maraton()
            
        elif opciones == 4:
            Ecuaciones_figuras()
            
        elif opciones == 5:
            limites()
        else :
            print("No tenemos mas opciones")
        opciones = int(input(menu))
    print("Hasta luego")
    
if __name__ == '__main__':
    run()
