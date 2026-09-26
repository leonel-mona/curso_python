
def main():
    print("\nTest Division")
    a,b = 12,0
    print("dividiendo ",a," por ",b)
    print(division(a,b)) 
    
    a,b = 22,2
    print("dividiendo ",a," por ",b)
    print("Resultado: ", division(a,b))
    
    print("----------------------------")
    
    print("\nTest suma")
    n,s = 10,"test"
    print("sumando ",n," y ",s)
    print( suma(n,s)) 
    
    n,s = 23,2
    print("sumando ",n," y ",s)
    print("Resultado: ", suma(n,s)) 
    
    print("----------------------------")  
    print("\nTest Diccionario")
    dict = {"nombre":"Leo","edad":26}
    print("Obtener key TEST")
    print(getKey(dict,"TEST"))
    print("Obtener key Leo")
    print(getKey(dict,"nombre"))
    
    print("----------------------------")  
    print("\nTest input division")
    a =  "test"
    b = 321
    print("\ndiviendo: ", a," por ", b)
    print(divisionValue(a,b))
    a =  2
    b = 0
    print("\ndiviendo: ", a," por ", b)
    print(divisionValue(a,b))
    a =  1
    b = 2
    print("\ndiviendo: ", a," por ", b)
    print(divisionValue(a,b))
    
    print("----------------------------")  
    print("\nTest abrir archivo")
    abrirArchivo("./","test.txt") 
    
 
def division(a,b):
    try:
        return a/b
  
    except ZeroDivisionError:
        return "ZeroDivisionError: No se puede dividir por cero"

def divisionValue(a,b):
    try: 
        return int(a)/int(b)
    except ValueError:
        return "ValueError: El 1er valor no es un numero"
    except ZeroDivisionError:
            return "ZeroDivisionError: No se puede dividir por cero"
        

def suma(a,b):
    try:
        return a+b
    except TypeError:
        return "TypeError: Los valores a sumar deben ser numericos"

def getKey(dict,k):
    try:
        return dict[k]
    except KeyError:
        return "KeyError: key invalida"
    
def abrirArchivo(ruta,nombre): 
    try:
        open(ruta+nombre)
    except FileNotFoundError:
        print( "FileNotFoundError: Archivo no encontrado, generando uno")
        try:
            open(ruta+nombre,"x")
        except:
            return "No se pudo crear el archivo en la ruta ",ruta
        else:
            print("Archivo creado, volviendo a abrir...")
            abrirArchivo(ruta,nombre)
    else:
        print("Archivo ",ruta+nombre," encontrado")

    

# ejecución de la lógica principal del programa
if __name__ == "__main__":
    main() 