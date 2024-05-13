
import csv # importamos el archivo
from EntidadM import Moto

class Gestormoto:
    __listmoto=list
    def __init__(self):
        self.__listmoto=[]
    def agregarmoto(self, moto): #agregamos objeto a la lista
        self.__listmoto.append(moto)

    def testmotos(self):#cargamos el archivo al gestor
        archivo=open("datos_Motos.csv",mode='r')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                "saltear cabecera"
                bandera=False
            else:
                patente=fila[0]
                marca=fila[1]
                nombre=fila[2]
                apellido=fila[3]
                kilometraje=float(fila[4])
                moto=Moto(patente,marca,nombre,apellido,kilometraje) #creamos un objeto de esa columna y la agregamos a la lista (gestor)
                self.agregarmoto(moto)
        archivo.close()

    def buscarpatente(self,p):# sirve para buscar un elemento en la lista osea en el gestor y de ahi lo extrae de la entidad
        i=0 # p valor que vamos a buscar en la lista. i se usa como un contador para recorrer la lista.
        posicion=None  # se utiliza para almacenar el indece donde se encontro el valor
        bandera=False #sirve para conrolar el bucle while
        while not bandera and i<len(self.__listmoto):
            #      false      o         ej: 10 objetos
            if self.__listmoto[i].getpatente()==p:
                bandera=True
                posicion=i # se encontro en dicha posicion 
            else:
                i+=1 #si no vamos a la siguiente poscion de la lista osea al siguiente objeto
        return posicion #retorna la pocision donde se enconto el objeto (refiriendose el numero de moto que se encontro o objeto)

    def promedio(self,pate):
        i=0
        posicioin=None
        bandera=False
        while not bandera and i<len(self.__listmoto):
            if(self.__listmoto[i].getpatente()==pate):
                print(self.__listmoto[i].getpatente(),self.__listmoto[i].getmarca(),self.__listmoto[i].getnombre(),self.__listmoto[i].getapellido(),self.__listmoto[i].kilometraje())
                print(promedios(pate))
            i+=1
            
