#Autor: Braulio Arturo Rodriguez Hernandez
#Fecha: 07/Septiembre/2021

#importamos las librerias necesarias
import json #esta biblioteca la utilizaremos para la gestion de credenciales de los usuarios
import lifestore_file as datos #importamos los datos contenidos en el archivo y lo nombramos como datos
from prettytable import PrettyTable #biblioteca para imprimir tablas mas esteticas
from colorama import init, Fore, Back, Style #biblioteca para imprimir en color



# ***************************** funciones de procesamiento de datos *****************************
#importamos las listas de el archivo lifestore_file.py y los asignamos a las variables
"""
    lifestore_searches = [id_search, id product]
    lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
    lifestore_products = [id_product, name, price, category, stock]
"""
#asiganamos los valores de las listas a las variables
productos = datos.lifestore_products
ventas = datos.lifestore_sales
busquedas= datos.lifestore_searches

#metodo para imprimir la listas en tablas
def imprime_tabla(lista_productos, tipo):
    """Esta funcion es la encargada de recibir una lista y el tipo de tabla a imprimir"""
    #1= lista de productos mas vendidos
    #2= lista de productos mas buscados
    #3= lista de productos mas buscados por un usuario
    init(autoreset=True)#inicializamos la biblioteca colorama
    #creamos una variable con guarde el id de la posicion del producto en la tabla
    posicion= 0
    #creamos una variable de tipo tabla
    tabla = PrettyTable()
    if tipo == 1:
        #se le agrega una cabecera a la tabla
        tabla.field_names = ["Posicion","ID del producto", "Nombre", "Cantidad de ventas"]
        #solo se imprimen los primeros 20 productos
        for producto in lista_productos[:30]:
            #se incrementa la posicion
            posicion += 1
            #se agrega a la tabla el id del producto, su nombre y su cantidad de ventas
            tabla.add_row([posicion, producto[0], producto[1], producto[2]])
        #se imprime la tabla de color azul
        print(Fore.LIGHTBLUE_EX + str(tabla))
    elif tipo == 2:
        #se le agrega una cabecera a la tabla
        tabla.field_names = ["Posicion","ID del producto", "Nombre", "Cantidad de busquedas"]
        #solo se imprimen los primeros 20 productos
        for producto in lista_productos[:30]:
            #se incrementa la posicion
            posicion += 1
            #se agrega a la tabla el id del producto, su nombre y su cantidad de busquedas
            tabla.add_row([posicion, producto[0], producto[1], producto[2]])
        #se imprime la tabla de color magenta
        print(Fore.LIGHTBLUE_EX  + str(tabla))
    elif tipo == 3:
        #se le agrega una cabecera a la tabla
        tabla.field_names = ["Posicion","ID del producto", "Nombre", "Cantidad de ventas"]
        #solo se imprimen los primeros 20 productos
        for productos in lista_productos[:20]:
            #imprimimos el nomnbre del categoria colo amarillo, y la letra capitalizada
            titulo=productos[0]
            print(Fore.YELLOW + titulo.upper())
            for producto in productos[1]:
                #se incrementa la posicion
                posicion += 1
                #se agrega a la tabla el id del producto, su nombre y su cantidad de ventas
                tabla.add_row([posicion, producto[0], producto[1], producto[5]])
            #se imprime la tabla de color verde
            print(Fore.GREEN + str(tabla))
            #se reinicia la tabla
            tabla.clear_rows()
    elif tipo == 4:
        #se le agrega una cabecera a la tabla
        tabla.field_names = ["Posicion","ID del producto", "Nombre", "Cantidad de busquedas"]
        #solo se imprimen los primeros 20 productos
        for productos in lista_productos[:20]:
            #imprimimos el nomnbre del categoria colo amarillo, y la letra capitalizada
            titulo=productos[0]
            print(Fore.YELLOW + titulo.upper())
            for producto in productos[1]:
                #se incrementa la posicion
                posicion += 1
                #se agrega a la tabla el id del producto, su nombre y su cantidad de ventas
                tabla.add_row([posicion, producto[0], producto[1], producto[5]])
            #se imprime la tabla de color verde
            print(Fore.GREEN + str(tabla))
            #se reinicia la tabla
            tabla.clear_rows()
    elif tipo == 5:
        #se le agrega una cabecera a la tabla
        tabla.field_names = ["Posicion","ID_Producto", "Nombre", "Frecuencia","Promedio de rese??a"]
        for producto in lista_productos:
                #se incrementa la posicion
                posicion += 1
                #se agrega a la tabla el id del producto, su nombre y su cantidad de ventas
                tabla.add_row([posicion, producto[0], producto[1], producto[2], producto[3]])
            #se imprime la tabla de color verde
        print(Fore.CYAN + str(tabla))
        #se reinicia la tabla
    elif tipo == 6:
        #agragamos una cabecera a la tabla con total de ingresos
        tabla.field_names = ["Total de ingresos"]
        total_ingresos=lista_productos
        #el total de ingresos lo convertimos a un formato de moneda con simbolo de pesos
        total_ingresos= "${:,}".format(total_ingresos)
        #se agrega a la tabla el total de ingresos
        tabla.add_row([total_ingresos])
        #se imprime la tabla de color verde
        print(Fore.GREEN + str(tabla))
    elif tipo == 7:
        #creamos un diccionario con los el numero del mes y su nombre
        meses = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}
        #agragamos una cabecera a la tabla  mese y total de ingresos
        tabla.field_names = ["Mes", "Total de ingresos"]
        ventas_mensuales=lista_productos
        #con un ciclo for se recorre la lista de ventas mensuales
        for mes,total in ventas_mensuales.items():
            #se agrega a la tabla el mes y el total de ingresos
            #del diccionario meses se obtiene el nombre del mes
            tabla.add_row([meses[mes], "${:,}".format(total)])
        #se imprime la tabla de color azul
        print(Fore.LIGHTBLUE_EX + str(tabla))
    elif tipo == 8:
        tabla.field_names = ["A??o", "Total de ingresos"]
        ventas_anuales=lista_productos
        #con un ciclo for se recorre la lista de ventas mensuales
        for year,total in ventas_anuales.items():
            #se agrega a la tabla el mes y el total de ingresos
            #del diccionario meses se obtiene el nombre del mes
            tabla.add_row([year, "${:,}".format(total)])
        #se imprime la tabla de color azul
        print(Fore.LIGHTBLUE_EX + str(tabla))
    elif tipo == 9:
        #se le agrega una cabecera a la tabla
        tabla.field_names = ["Posicion","ID del producto", "Nombre", "Cantidad de stock"]
        #solo se imprimen todos los productos de la lista
        for productos in lista_productos:
            #imprimimos el nomnbre del categoria colo amarillo, y la letra capitalizada
            titulo=productos[0].upper()
            print(Fore.YELLOW + titulo)
            for producto in productos[1]:
                #se incrementa la posicion
                posicion += 1
                #se agrega a la tabla el id del producto, su nombre y su cantidad de ventas
                tabla.add_row([posicion, producto[0], producto[1], producto[4]])
            #se imprime la tabla de color verde
            print(Fore.CYAN + str(tabla))
            #se reinicia la tabla
            tabla.clear_rows()
      


#________________________________________________Productos m??s vendidos y productos rezagados________________________________________________
#funcion para crear una lista de productos clasifcados por categoria
def lista_productos_por_categoria():
    """Esta funcion crea una lista llena de listas de productos clasificados por categorias"""
    lista_categorias = []
    #creamos una copy de la productos
    productos_copy = productos.copy()
    #utilizamos el ciclo for para extraer las categorias existentes sin repetir
    for producto in productos_copy:
        #si la categoria no esta en la lista
        if producto[3] not in lista_categorias:
            #se agrega a la lista
            lista_categorias.append(producto[3])
    
    lista_productos = []
    #utilizamos el ciclo for para enfocarnos en las categorias
    for categoria in lista_categorias:
        #creamos una lista vacia donde se almacenaran los productos de la categoria
        lista_productos_categoria = []
        #utilizamos el ciclo for para enfocarnos en las categorias
        for producto in productos_copy:
            #si la categoria es igual a la categoria actual
            if producto[3] == categoria:
                #se agrega a la lista de la categoria
                lista_productos_categoria.append(producto)
        lista_productos.append([categoria,lista_productos_categoria])
    #retornamos la lista de productos clasificados por categorias y despues la vaciamos
    return lista_productos

        

#metodo para obtener los productos mas vendidos 
def produc_mas_vendidos():
    """Esta funcion es la encargada de mostrar los productos mas venidos"""
    #creamos una variable que contenga la cantidad de repeticiones de un producto dentro de la lista de ventas
    cant_repeticiones = 0
    #declaramos una lista vacia
    lista_productos = []
    #utilizamos un ciclo for para enfocarnos en el ID de los productos
    for producto in productos:
        #se reinicia la variable de repeticiones
        cant_repeticiones = 0
        #utilizamos un ciclo for para enfocarnos en las ventas
        for venta in ventas:
            #si el ID de la venta es igual al ID del producto
            if venta[1] == producto[0]:
                #se suma una repeticion
                cant_repeticiones += 1
        #incrementamos la posicion
        #se agrega a la lista la posicion,ID del producto, su nombre y su cantidad de repeticiones
        lista_productos.append([producto[0], producto[1], cant_repeticiones])
    #se ordena la lista de mayor a menor
    lista_productos.sort(key=lambda x: x[2], reverse=True)
    #se manda a llamar a la funcion imprime_productos
    imprime_tabla(lista_productos,1)          
#metodo para obtener los productos mas buscados 
def produc_mas_buscados():
    """Esta funcion es la encargada de mostrar los productos mas buscados"""
    #creamos una variable que contenga la cantidad de repeticiones de un producto dentro de la lista de busquedas
    cant_repeticiones = 0
    #declaramos una lista vacia
    lista_productos = []
    #utilizamos un ciclo for para enfocarnos en el ID de los productos
    for producto in productos:
        #se reinicia la variable de repeticiones
        cant_repeticiones = 0
        #utilizamos un ciclo for para enfocarnos en las busquedas
        for busqueda in busquedas:
            #si el ID de la busqueda es igual al ID del producto
            if busqueda[1] == producto[0]:
                #se suma una repeticion
                cant_repeticiones += 1
        #incrementamos la posicion
        #se agrega a la lista la posicion,ID del producto, su nombre y su cantidad de repeticiones
        lista_productos.append([producto[0], producto[1], cant_repeticiones])
    #se ordena la lista de mayor a menor
    lista_productos.sort(key=lambda x: x[2], reverse=True)
    #se manda a llamar a la funcion imprime_productos
    imprime_tabla(lista_productos,2)
#metodo para obtener los productos menos vendidos por categoria
def produc_menos_vendidos_categoria():
    """Esta funcion es la encargada de mostrar los productos menos vendidos por categoria"""
   #llamamos a la funcion lista_productos_por_categoria para obtenemos una lista de listas de productos clasificados por categoria
    lista_productos = lista_productos_por_categoria()    
    #utilizamos un ciclo for para enfocarnos en las listas de productos y organizarlos acorde a las ventas
    for productos in lista_productos:
        for producto in productos[1]:
            #se reinicia la variable de repeticiones
            cant_repeticiones = 0
            #utilizamos un ciclo for para enfocarnos en las ventas
            for venta in ventas:
                #si el ID de la venta es igual al ID del producto
                if venta[1] == producto[0]:
                    #se suma una repeticion
                    cant_repeticiones += 1
            #verificamos si no existe el indice 5 
            if len(producto) == 5:
                #agregamos cantidad de repeticiones al producto
                producto.append(cant_repeticiones)
            else:
                #si existe el indice 5, se reemplaza
                producto[5] = cant_repeticiones
        #orderamos la lista de mayor a menor
        productos[1].sort(key=lambda x: x[5])
    #se manda a llamar a la funcion imprime_productos
    imprime_tabla(lista_productos,3)
#metodo para obtener los productos menos buscados por categoria
def produc_menos_buscados_categoria(): 
    """Esta funcion es la encargada de mostrar los productos menos buscados por categoria"""
    #llamamos a la funcion lista_productos_por_categoria para obtenemos una lista de listas de productos clasificados por categoria
    lista_productos = lista_productos_por_categoria()
    #utilizamos el ciclo for para extrare la lista de productos por categoria
    for productos in lista_productos:
        for producto in productos[1]:
            #se reinicia la variable de repeticiones
            cant_repeticiones = 0
            #utilizamos un ciclo for para enfocarnos en las busquedas
            for busqueda in busquedas:
                #si el ID de la busqueda es igual al ID del producto
                if busqueda[1] == producto[0]:
                    #se suma una repeticion
                    cant_repeticiones += 1
            #verificamos si no existe el indice 5 
            if len(producto) == 5:
                #agregamos cantidad de repeticiones al producto
                producto.append(cant_repeticiones)
            else:
                #si existe el indice 5, se reemplaza
                producto[5] = cant_repeticiones
        #orderamos la lista de mayor a menor
        productos[1].sort(key=lambda x: x[5])
    #se manda a llamar a la funcion imprime_productos
    imprime_tabla(lista_productos,4)
#____________________________________________________Productos por rese??a en el servicio____________________________________________________
#metodo para obtener los productos con las mejores rese??as
def productos_rese??as(orden):
    """Esta funcion es la encargada de mostrar los productos con las mejores rese??as"""
    #creamos una variable que contenga la sumatoria de las rese??as de un producto dentro de la lista de rese??as
    suma_rese??as = 0
    cant_repeticiones = 0
    #declaramos una lista vacia
    lista_productos = []
    #utilizamos un ciclo for para enfocarnos en el ID de los productos
    for producto in productos:
        #se reinicia la variable de repeticiones
        cant_repeticiones = 0
        #utilizamos un ciclo for para enfocarnos en las ventas
        for venta in ventas:
            #si el ID de la venta es igual al ID del producto
            if venta[1] == producto[0]:
                #se suma una repeticion
                cant_repeticiones += 1
                #se suma la cantidad de rese??as al producto
                suma_rese??as += venta[2]
        #calculamos el promedio de rese??as y verificamos que la cantidad de repeticiones sea mayor a 0
        if cant_repeticiones > 0:
            promedio_rese??as = suma_rese??as/cant_repeticiones
            lista_productos.append([producto[0], producto[1], cant_repeticiones, promedio_rese??as])
        suma_rese??as = 0
    #orderamos la lista de mayor a menor por promedio de rese??as y por cantidad de repeticiones
    #si el parametro de orden es igual a 1
    if orden == 1:
        #ordena de menor a mayor por promedio de rese??as y por cantidad de repeticiones
        lista_productos.sort(key=lambda x: (x[3], x[2]), reverse=True)
    #si el parametro de orden es igual a 2
    elif orden == 2:
        #ordena de mayor a menor por promedio de rese??as y por cantidad de repeticiones
        lista_productos.sort(key=lambda x: (x[3], x[2]))
    #se manda a llamar a la funcion imprime_productos
    imprime_tabla(lista_productos,5)
    #se ordena la lista de mayor a menor

#______________________________________Total de ingresos y ventas promedio mensuales, total anual y meses con m??s ventas al a??o_______________________
#metodo para obtener el total de ingresos
def total_ingresos(accion):
    """ Esta funcion calculara el total de ingresos"""
    #verificaremos cuales ventas no tienen devoluciones y en base a ello calculamos el total de ingresos
    if accion == 1:
        #si se ejecuta la accion 1 se calcula el total de ingresos sin devoluciones
        total_ingresos = 0
        #utilizamos un ciclo for para enfocarnos en los productos
        for producto in productos:
            #utilizamos el ciclo for para comparar el ID de los productos con los ID del producto en las ventas
            for venta in ventas:
                #si el id del producto en la venta es igual al id del producto y la devolucion es igual a 0
                if producto[0] == venta[1] and venta[4] == 0:
                    #suma el precio del producto a la variable total de ingresos
                    total_ingresos += producto[2]
        #llamamos a la funcion imprime_tabla
        imprime_tabla(total_ingresos,6)
    elif accion == 2:
        #si la accion es igual a 2 se calcula el total de ingresos por mes
        #creamos una lista con los meses del a??o en numeros
        meses = [1,2,3,4,5,6,7,8,9,10,11,12]
        #creamos una diccionario donde la clave sera el mes y el valor sera el total de ingresos
        total_ingresos_mes = {}
        #utilizamos un ciclo for para enfocarnos en los productos
        for producto in productos:
            #utilizamos el ciclo for para comparar el ID de los productos con los ID del producto en las ventas
            for venta in ventas:
                #si el id del producto en la venta es igual al id del producto y la devolucion es igual a 0
                if producto[0] == venta[1] and venta[4] == 0:
                    #extraemos la fecha de la venta
                    fecha = venta[3]
                    #extraemos el mes de la venta con el formato MM y lo convertimos a entero
                    mes = int(fecha[3:5])
                    if mes in meses:
                        #si el mes esta dentro de la lista de meses, recuperamos el valor del diccionario y le sumamos el precio del producto
                        total_ingresos_mes[mes] = total_ingresos_mes.get(mes,0) + producto[2]
        #llamamos a la funcion imprime_tabla
        imprime_tabla(total_ingresos_mes,7) 
    elif accion == 3:
        #si la accion es igual a 3 se calcula el total de ingresos por a??o
        #creamos una lista con los a??os
        a??os = [2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000]
        #creamos una diccionario donde la clave sera el a??o y el valor sera el total de ingresos
        total_ingresos_a??o = {}
        #utilizamos un ciclo for para enfocarnos en los productos
        for producto in productos:
            #utilizamos el ciclo for para comparar el ID de los productos con los ID del producto en las ventas
            for venta in ventas:
                #si el id del producto en la venta es igual al id del producto y la devolucion es igual a 0
                if producto[0] == venta[1] and venta[4] == 0:
                    #extraemos la fecha de la venta
                    fecha = venta[3]
                    #extraemos el a??o de la venta 
                    a??o = int(fecha[6:10])                    
                    if a??o in a??os:
                        #si el a??o esta dentro de la lista de a??os, recuperamos el valor del diccionario y le sumamos el precio del producto
                        total_ingresos_a??o[a??o] = total_ingresos_a??o.get(a??o,0) + producto[2]
        #llamamos a la funcion imprime_tabla
        imprime_tabla(total_ingresos_a??o,8)

#metodo para obtener los productos que recomendaria vender de inmediato
def conclusion():
    #este metodo imprimira la conclusion del programa y decir que producto son los mas vendidos, con las mejores rese??as y con los menos vendidos y peores rese??as
    #variable para contar la cantidad de productos vendidos
    cantidad_productos = 0
    #variable para almacenar la sumatoria de las busquedas
    suma_rese??as= 0
    #prodcuto no vendidos
    producto_no_vendidos = []
    #variable para almacenar la sumatoria de las busquedas
    suma_busquedas = 0
    #creamos una lista con los resultados
    resultados = []
    #creamos una lista con llamada resultados_productos
    productos_vendidos = []
    #relacionamos los productos con rese??as con el id de los productos en las ventas
    for producto in productos:
        #for para comparar el id de los productos con los id de los productos en las ventas
        for venta in ventas:
            #si el id del producto en la venta es igual al id del producto
            if producto[0] == venta[1]:
                #agregamos el producto a la lista de productos vendidos
                productos_vendidos.append(producto)
        #si el producto no coenicide con los prodcuctos vendidos
        if producto not in productos_vendidos:
            #agregamos el producto a la lista de productos no vendidos
            producto_no_vendidos.append(producto)
    #ahora que ya tenemos los productos que no se venden, veremos si tiene algunas busquedas
    for producto in producto_no_vendidos:
        #for para comparar el id de los productos con los id de los productos en las busquedas
        for busqueda in busquedas:
            #si el id del producto en la busqueda es igual al id del producto
            if producto[0] == busqueda[1]:
                #sumamos las busquedas
                suma_busquedas += 1
        #si las busquedas son menores a 10
        if suma_busquedas < 50:
            #agregamos el producto a la lista de resultados
            resultados.append(producto)
    #ahora vamos a clasificar los productos por su categoria
    #creamos una lista con las categorias
    categorias = []
    #for para recorrer los productos
    for producto in productos:
        #si la categoria no esta en la lista de categorias
        if producto[3] not in categorias:
            #agregamos la categoria a la lista de categorias
            categorias.append(producto[3])
    #creamos una lista con los resultados
    resultados_categorias = []
    #lista temporal para almacenar los productos
    productos_temporal = []
    #for para recorrer las categorias
    for categoria in categorias:
        #for para recorrer los productos
        for producto in resultados:
            #si la categoria del producto es igual a la categoria
            if producto[3] == categoria:
                #agregamos el producto a la lista de resultados
                productos_temporal.append(producto)
        #antes de agregar los productos a la lista de resultados, ordenamos los productos por la cantidad de stock de mayor a menor
        productos_temporal.sort(key=lambda x: x[4], reverse=True)
        #agregamos la categoria y la lista de resultados a la lista de resultados_ctaegorias
        resultados_categorias.append([categoria,productos_temporal])
        #limpiamos la lista temporal
        productos_temporal = []
        
    #llamamos a la funcion imprime_tabla
    imprime_tabla(resultados_categorias,9)

                             
#abrimos el archivo json de usuarios, lo leemos y lo guardamos en la variable usuarios
with open("usuarios.json", "r") as archivo:
    #lo guardamos en una variable, en este caso usaurios sera la lista con los usuarios actuales
    usuarios = json.load(archivo)
#****************************** login y registro de usuarios *****************************
def login():
    """Esta funcion es la encargada de logear al usuario"""
    #variable de iteracion
    intentos_logeo = 0
    estatus=False
    #creamos un while que se repita 3 veces
    while estatus==False and intentos_logeo < 3:
        #se le pide al usuario que ingrese su nombre de usuario
        input_user = input("Usuario: ")
        #se le pide al usuario que ingrese su contrase??a
        input_pass = input("Password: ")
        #crea una lista con los datos ingresados
        datos_ingresados = [input_user, input_pass]
        #utilizamos un ciclo for que busque en usuarios si existe el usuario ingresado
        for usuario in usuarios:
            #si existe el usuario se cierra el ciclo
            if datos_ingresados == usuario:
                #se imprime un mensaje de bienvenida y el nombre del usuario
                print("["+Fore.GREEN+ "OK" +Fore.RESET+"] Login exitoso, Bienvenido: "+ Fore.LIGHTBLUE_EX+ str(datos_ingresados[0]+Fore.RESET))
                return True #se retorna un valor booleano True si el usuario se encontro
            else:
                continue #se vuelve a iterar el ciclo
        #si no existe el usuario se suma un intento y muestra un mensaje de error
        intentos_logeo += 1
        print("["+Fore.RED+ "Error" +Fore.RESET+"] Usuario o contrase??a incorrecta: "+Fore.GREEN+ str(3-intentos_logeo) +Fore.RESET+" Intentos" )
def registro():
    """En esta funcion la utilizaremos para registrar un nuevo usuario y tambien validar si ya esta registrado"""
    #variable que controla el cilo while
    registro_exitoso = False
    #intentos para poder registrar un usuario
    intentos = 0
    #creamos un ciclo que se repita hasta que el usuario ingrese un usuario valido
    while registro_exitoso != True and intentos < 3:
        #le pedimos al usuario que ingrese su nombre
        input_user = input("Usuario: ")
        #verificamos que no exista el usuario ingresado y solo tiene
        for usuario in usuarios:
            if usuario[0] == input_user:
                intentos += 1
                print("["+Fore.RED+ "Error" +Fore.RESET+"] Usuario existente, intenta con otro, Restan: "+Fore.GREEN+ str(3-intentos) +Fore.RESET+" Intentos" )
                registro_exitoso=False
                break
            else:
                registro_exitoso=True
                continue
        #si el usuario no existe se crea una lista con los datos ingresados
        if registro_exitoso == True:
            datos_ingresados = [input_user, input("Password: ")]
            #se agrega la lista a la lista de usuarios
            usuarios.append(datos_ingresados)
            #se guarda el archivo json con los datos ingresados
            with open("usuarios.json", "w") as archivo:
                json.dump(usuarios, archivo)
            #imprimimos un mensaje de  usuario registrado  color verde
            print("["+Fore.GREEN+ "OK" +Fore.RESET+"] Usuario registrado con exito")
            break
# ***************************** imprimir menus *****************************
def menu():
    """Esta funcion es la encargada de mostrar el menu"""
    #vaiable para iniciar una tabla
    tabla = PrettyTable()
    #se le agrega un titulo a la tabla
    tabla.title = "Menu"
    #se le agrega una lista con los titulos de las columnas
    tabla.field_names = ["Opcion", "Descripcion"]
    #se le agrega una lista con los datos de las columnas
    tabla.add_row(["1", "Registrar usuario"])
    tabla.add_row(["2", "Login"])
    tabla.add_row(["3", "Salir"])
    #se imprime la tabla color verde
    print(Fore.LIGHTGREEN_EX+str(tabla)+Fore.RESET)
def submenu():
    """Esta funcion es la encargada de mostrar el submenu"""
    #vaiable para iniciar una tabla
    tabla = PrettyTable()
    #se le agrega un titulo a la tabla
    tabla.title = "Submenu"
    #se le agrega una lista con los titulos de las columnas
    tabla.field_names = ["Opcion", "Descripcion"]
    #se le agrega una lista con los datos de las columnas
    tabla.add_row(["1", "Top 30 de los productos con mas ventas"])
    tabla.add_row(["2", "Top 30 de los productos con mayor busquedas"])
    tabla.add_row(["3", "Tops de productos rezagados por categoria"])
    tabla.add_row(["4", "Tops de productos con menos busquedas por categoria"])
    tabla.add_row(["5", "Tops de productos con peores rese??as"])
    tabla.add_row(["6", "Tops de productos con mejores rese??as"])
    tabla.add_row(["Nota:","Para las siguentes opciones no se toman en cuentra productos devueltos"])
    tabla.add_row(["7.", "Total de ventas"])
    tabla.add_row(["8.", "Total de ventas por mes"])
    tabla.add_row(["9.", "Total de ventas por a??o"])
    tabla.add_row(["10.", "Mi conclusion"])
    tabla.add_row(["11.", "Volver al menu y logout"])
    #se imprime la tabla color verde
    print(Fore.CYAN+str(tabla)+Fore.RESET)


    
#****************************** funcion principal *****************************
def main():
    """Esta funcion es la principla de la aplicacion y se encarga de llamar a las demas funciones"""
    #mostramos el menu en un loop hasta sea interrumpido por el usuario
    while True:
        menu()
        #se le pasa la opcion que el usuario desea realizar
        option = input("Ingrese una opcion: ")
        #se valida que la opcion sea un numero
        if option.isdigit():
            #se le asigna el valor ala opcion
            option = int(option)
            #se valida que la opcion sea correcta
            if option == 1:
                #se llama a la funcion registro
                registro()
            elif option == 2:
                login_valido = login()
                #mienstras el login sea true se ejecutara el submenu
                while login_valido == True:
                    submenu()
                    #se le pasa la opcion que el usuario desea realizar
                    opcion = input("Ingrese una opcion: ")
                    #se valida que la opcion sea un numero
                    if opcion.isdigit():
                        #se le asigna el valor ala opcion
                        opcion = int(opcion)
                        if opcion == 1:
                            produc_mas_vendidos()
                        elif opcion == 2:
                            produc_mas_buscados()
                        elif opcion == 3:
                            produc_menos_vendidos_categoria()
                        elif opcion == 4:
                            produc_menos_buscados_categoria()
                        elif opcion == 5:
                            #le enviamos un parametro que determianara como sera el orden es decir de menor a mayor o de mayor a menor
                            #si el paraemetro es 2 el orden sera de mayor a menor
                            productos_rese??as(2)
                        elif opcion == 6:
                            #se le pasa un parametro que determianara como sera el orden es decir de menor a mayor o de mayor a menor
                            #si el paraemetro es 1 el orden sera de menor a mayor
                            productos_rese??as(1)
                        elif opcion == 7:
                            #se manda a llamar la funcion total ingresoa y se le envia un parametro que determina que se quiere mostrar
                            #si es total de ventas se manda el valor 1
                            total_ingresos(1)
                        elif opcion == 8:
                            #si las opcion es 8 se manda a llamar la funcion total ingrsos con el parametro 2 que mostrara el total de ventas por mes
                            total_ingresos(2)
                        elif opcion == 9:
                            #si las opcion es 9 se manda a llamar la funcion total ingrsos con el parametro 3 que mostrara el total de ventas por a??o
                            total_ingresos(3)
                        elif opcion == 10:
                            #Mensaje de conclusion para la empresa en color rojon
                            print(Fore.RED+"Mi conclusion:"+Fore.RESET)
                            #texto de conclusion en color azul
                            print(Fore.BLUE+"La empresa tiene los siguientes productos en stock, sin ventas y con una cantidad de busquedas muy bajas\n es por ello que recomiendo que se enfoquen vender estos productos con alguna estrategi\n que les permita reducir productos que esten estaticos como ofertas, 2*1, descuentos en segundas compras, paquetes entre otras"+Fore.RESET)
                            conclusion()   
                        elif opcion == 11:
                            break
                        else:
                            print("["+Fore.RED+ "Error" +Fore.RESET+"] Opcion incorrecta ingresa un numero entre 1 y 11")
                    else:
                        print("["+Fore.RED+ "Error" +Fore.RESET+"] Caracter incorrecto, ingresa un nuemro entero")  
            elif option == 3:
                print("["+Fore.GREEN+ "OK" +Fore.RESET+"] Aplicacion finalizada exitosamente")
                break
            else:
                print("["+Fore.RED+ "Error" +Fore.RESET+"] Opcion incorrecta ingresa un numero entre 1 y 3")
        else:
             print("["+Fore.RED+ "Error" +Fore.RESET+"] Caracter incorrecto, ingresa un nuemro entero") 
#si existe la funcion main ejecutala
if __name__ == "__main__":
    main()