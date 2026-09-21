# función con la lógica principal del programa (entry point)
def main():
    a = set([1,2,3,4])
    b = set([3,4,5,6])
    c = set([1,2,3,4])
    d = set([2,3])  
    e = set([2,2,45,6,4,4,6,43,2,1,1,3,3,5,6,6,3,3,23,2,1]) 
    AyB(a,b)
    print("Interseccion: ",Interseccion(a,b))
    print("noInterseccion: ",noInterseccion(a,b))
    print(a," es Subconjunto de ",b,"? : ",esSubconjunto(a,b),"\n ",d," es Subconjunto de ",c,"? : ",esSubconjunto(c,d))
    print("Numero de elementos de E: ",nroElementos(e)) #Devuelve 9 porque en set no se repiten valores
    
def nroElementos(a): 
    return len(a)

def Interseccion(a,b): 
    return  a&b

def noInterseccion(a,b): 
    return a^b

def AyB(a,b):
   print("a: ",a)
   print("b: ",b) 
    
def esSubconjunto(a,b):  
    return b<=a

# ejecución de la lógica principal del programa
if __name__ == "__main__":
    main() 