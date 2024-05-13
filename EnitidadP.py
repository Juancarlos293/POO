class Pedido:
    __patente=str
    __identificador=str
    __comidas=str
    __tiempo=str
    __tiempoR=str
    __precio=float
    def __init__(self,p,i,c,t,tr,pr):
        self.__patente=p
        self.__identificador=i
        self.__comidas=c
        self.__tiempo=t
        self.__tiempoR=tr
        self.__precio=pr
    def getpatente(self):
        return self.__patente
    def getidentificador(self):
        return self.__identificador
    def getcomida(self):
        return self.__comidas
    def gettiemp(self):
        return self.__tiempo
    def gettiemporeal(self):
        return self.__tiempoR
    def getprecio(self):
        return self.__precio
    