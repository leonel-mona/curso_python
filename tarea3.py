
def main():
    a,b = input("Primer valor: "), input("Segundo valor: ")
    print("El mayor es:", conseguir_mayor(a,b)) 
     
    diccionario = set(["Test","Hola","Todo","Bien"])
    palabra_buscada = input("Ingrese la palabra a buscar: ")
    print( conseguir_palabra(palabra_buscada,*diccionario)) 
    
    a,b = 2,1
    print(es_par(a))
    print(es_par(b))
    
    lista = set([1,2,4])
    
    print("Promedio: ", promedio(*lista))
    
    print(sin_argumentos())
    arg_test = {"valor"}
    print(sin_argumentos(*arg_test))
 
def conseguir_mayor(a,b):
    try:
        return (int)(a) if a>b else (int)(b)
  
    except ValueError:
        return "ValueError: El valor no es un numero"

def conseguir_palabra(buscado, *diccionario):
    if len(diccionario) == 0:
            return "Error: no se pasaron suficientes argumentos"
        
    for palabra in diccionario:  
        if palabra == buscado:
            return "Palabra encontrada: "+ buscado
          
    return "Error: palabra '"+buscado+"' no encontrada"
 
def es_par(a):
    try:
        if (int)(a)%2==0:
            return a,"es par"
        else:
            return a,"es impar"
    except ValueError:
        return "ValueError: El valor no es un numero"
    
def promedio(*args):
    if len(args) == 0:
            return "Error: no se pasaron suficientes argumentos"
    suma =0 
    for nro in args:
        suma += nro
    
    return suma/len(args)

def sin_argumentos(*args): 
    if len(args) == 0:
        return "Error: no se pasaron suficientes argumentos"
    else:
        return "Argumentos suficientes"

if __name__ == "__main__":
    main() 