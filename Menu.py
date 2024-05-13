from GM import Gestormoto
from GP import Gestorpedido

if __name__ =='__main__':
    i=int(input(" Menu (ingrese la opcion que desea ralizar) \n 1. Leer los datos de la motos \n 2. Leer los datos de los pedidos \n 3. Cargar nuevo pedido \n 4. Ingresar numero de patente \n 5. Ingresar numero de patente de una moto \n 6. Generar un listado por cada moto, para el pago de comicion \n 0 Salir\n"))
    while i!=0:
        if i==1:
            moto=Gestormoto()
            moto.testmotos()
        elif i==2:
            pedido=Gestorpedido()
            pedido.testpedido()
            pedido.ordenar()
        elif i==3:
            print("ingrese numerpo de pantente")
            pat=input("Ingrese la patente del pedido\n")
            Pan=moto.buscarpatente(pat) #comprobamos que la patente que buscamos este en la lista del gestor.
            if Pan!=0:
                while Pan!=True:
                    print("No se encontro la patente\n")
                    pat=input("Ingrese la patente del pedido\n")
                    Pan=moto.buscarpatente(pat)
                pedido.nuevopedido(pat)#agregamos a la lista de patentes
        elif i==4:
            patente=input("Ingrese la patente del pedido\n")
            ti=input("Ingrese numero identificador del pedido\n")
            treal=input("Ingrese el tiempo real a modificar \n")
            pedido.modifica(patente,ti,treal)

        elif i==5:
            pate=input("ingrese patnete de moto\n")
            moto.promedio(pate)
        elif i==6:
            pedido.Ordenar()
            p=pedido.regresa_lista()
            m=moto.regresa_lista()
            for i in range (len(m)):
                print("\nPatente de Moto:{}\nConductor:{}".format(moto.regresapatente(i),moto.regresaconductor(i)))
                print("Indentificador de Pedido   Tiempo Estimado   Tiempo real   Precio")
                for l in range (len(p)):
                    cant=0
                    acum=0.0
                    band=False
                    if (moto.regresapatente(i)==pedido.getpatente(l)):
                        band=True
                        print("     {}                        {}                {}        {}".format(pedido.getID(l),pedido.getTe(l),pedido.getTr(l),pedido.getprecio(l)))
                            #5,24,16,8 espacio
                        cant+=1
                        acum+=pedido.getprecio(l)
                    if band==True:
                        print("\nComision:${}(20 del total)\n".format(acum*20/100))
        else:
            p=1

        i=int(input(" Menu (ingrese la opcion que desea ralizar) \n 1. Leer los datos de la motos \n 2. Leer los datos de los pedidos \n 3. Cargar nuevo pedido \n 4. Ingresar numero de patente \n 5. Ingresar numero de patente de una moto \n 6. Generar un listado por cada moto, para el pago de comicion \n 0 Salir"))
    print("fin del programa")