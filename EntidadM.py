class Moto:
    __patente=str
    __marca=str
    __nombre=str
    __apellido=str
    __kilometraje=float
    def __inti__(self,pat,mar,nom,ape,kil):
        self.__patente=pat
        self.__marca= mar
        self.__nombre=nom
        self.__apellido=ape
        self.__kilometraje=kil
    def getpatente(self):
        return self.__patente
    def getmarca(self):
        return self.__marca
    def getnombre(self):
        return self.__nombre
    def getapellido(self):
        return self.__apellido
    def getkilometraje(self):
        return self.__kilometraje