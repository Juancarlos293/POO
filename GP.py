import numpy as np
import csv # importamos el archivo
from EnitidadP import Pedido


class Gestorpedido:
    __listapedidio=list
    def __initi__(self):
        self.__listapedidio=[]
    def agregar(self, pedido):
        self.__listapedidio.append(pedido)
    
    def testpedido(self): #cargamos el archivo al gestor
        archivo=open("datos_Pedidos.csv",mode='r')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                "saltear cabecera"
                bandera=not bandera
            else:
                patente=fila[0]
                identificador=fila[1]
                comidas=fila[2]
                tiempo=fila[3]
                tiempor=fila[4]
                precio=float(fila[5])
                pedido=Pedido(patente,identificador,comidas,tiempo,tiempor,precio)#creamos un objeto de esa columna y la agregamos a la lista (gestor)
                self.agregar(pedido)
        archivo.close()  

    def nuevopedido(self,p): #agregamos nuevo pedido por teclado.
        i=input("ingres identificador")
        c=input("comida")
        ti=input("tiempo")
        tr=input("ingres tiempo real")
        pr=float(input("ingresar el precio"))
        crear=Pedido(p,i,c,ti,tr,pr)#creamos el objetos con los datos de la entidad
        self.agregar(crear)#agregamo el objeto a la lista

    
    
    def modifcar(self,p,ti,t):
        i=0
        while i< len(self.__listapedidio):
            if (self.__listapedidio[i].getpatente()==p) and (self.__listapedido[i].getidentificador()==ti):
                    self.__listapedidio[i].gettiemporeal=t
            else:
                print("error")
    
    def promedios(self,pate):
        acum=0
        i=0
        con=0
        while i < len(self.__listapedidio):
            if (self.__listapedidio[i].getpatente()==pate): 
                    rom+=self.__listapedidio[i].getTiemporeal()
                    con+=1
        return float(acum//con)



    def regresa_lista(self):
        return self.__lista
    def getID(self,i):
        return (self.__lista[i].getId())
    def getTr(self,i):
        return (self.__lista[i].getTr())
    def getTe(self,i):
        return(self.__lista[i].getTe())
    def getprecio(self,i):
        return(self.__lista[i].getprecio())
    def getpatente(self,i):
        return self.__lista[i].getpatente()

