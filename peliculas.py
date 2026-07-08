
## Actividad: Diccionario Películas

#                               0            1
# peliculas = 'codigo': [título película, género, ]

peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False]
}


cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
}

########################################################################################################################################

# Funciones

def cupos_genero(genero):
    total_cupos = 0
    for clave, valor in peliculas.items():
        if valor[1].lower() == genero.lower():
            total_cupos += cartelera[clave][1]
    if total_cupos == 0:
        print("No hay cupos para ese género...")
    else:
        print(f"Hay {total_cupos} cupos en total para el género {genero}")

def busqueda_precio(p_min , p_max):
    lista = []
    for clave, valor in cartelera.items():
        if valor[0] >= p_min and valor[0] <= p_max and valor[1] >= 0:
            titulo = peliculas[clave][0]
            lista.append(titulo + "-" + clave)
    if len(lista) == 0:
        print("No se encontró en la lista...")
    else:
        lista.sort
        print(lista)

def actualizar_precio(codigo , nuevo_precio):
    if codigo in cartelera:
        cartelera[codigo][0] = nuevo_precio
        return True
    return False

def eliminar_pelicula(codigo):
    if codigo in cartelera:
        del cartelera[codigo]
        del peliculas[codigo]
        return True
    return False

def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos):
    if codigo in peliculas:
        return False
    if es_3d == "s":
        CAL = True
    else:
        CAL = False
    
    peliculas[codigo] = [titulo, genero, int(duracion), clasificacion, idioma, CAL]
    cartelera[codigo] = [int(precio), int(cupos)]
    return True

#######################################################################################################################################

# Validaciones 

def validaCodigo(codigo):
    if len(codigo.strip()) > 0:
        return True
    return False

def validaTitulo(titulo):
    if len(titulo.strip()) > 0:
        return True
    return False

def validaGenero(genero):
    if len(genero.strip()) > 0:
        if genero in ('drama', 'acción', 'documental', 'comedia', 'thriller', 'ciencia ficción'):
            return True
        return False
    return False

def validaDuracion(duracion):
    try:
        d = int(duracion)
        if d > 0:
            return True
        return False
    except:
        return False

def validaClasificacion(clasificacion):
    if clasificacion in ('A', 'B', 'C'):
        return True
    return False

def validaIdioma(idioma):
    if len(idioma.strip()) > 0:
        return True
    return False

def valida3D(es_3d):
    if es_3d in ('s', 'n'):
        return True
    return False

def validaPrecio(precio):
    try:
        p = int(precio)
        if p > 0:
            return True
        return False
    except:
        return False

def validaCupos(cupos):
    try:
        c = int(cupos)
        if c > 0:
            return True
        return False
    except:
        return False



#######################################################################################################################################


# Menu

def menu():
    print("====== MENÚ PRINCIPAL ======")
    print("1. Cupos por género")
    print("2. Búsqueda de películas por rango de precio")
    print("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")
    print("=" * 30)

def seleccione():
    try:
        op = int(input("Seleccione: "))
        return op
    except:
        return 0

while True:
    menu()
    opcion = seleccione()
    match opcion:
        case 1:
            while True:
                genero = input("Ingrese el género: ")
                cupos_genero(genero)
                resp = input("¿Desea continuar (s/n)?: ").lower()
                if resp == "n":
                    break
        case 2:
            while True:
                try:
                    p_min = int(input("Ingrese el precio mínimo: "))
                    p_max = int(input("Ingrese el precio máximo: "))
                    if p_min <= p_max and p_min >= 0:
                        busqueda_precio(p_min,p_max)
                    else:
                        print("El precio mínimo debe ser menor al máximo...")
                except BaseException as error:
                    print("Debe ingresar valores enteros", error)
                resp = input("¿Desea continuar (s/n)?: ").lower()
                if resp == "n":
                    break
        case 3:
            while True:
                try: 
                    codigo = input("Ingrese el codigo que quiere actualizar: ").upper()
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                    if nuevo_precio > 0:
                        resp = actualizar_precio(codigo , nuevo_precio)
                        if resp == True:
                            print("Se actualizó el precio...")
                        else:
                            print("Error de actualización...")
                    else:
                        print("El precio debe ser mayor a 0")
                except BaseException as error:
                    print("Debe ingresar el código existente y precio numérico...",error)
                resp = input("¿Desea continuar (s/n)?: ").lower()
                if resp == "n":
                    break
        case 4:
            while True:
                codigo = input("Ingrese el nuevo codigo: ").upper()
                if validaCodigo(codigo) == False:
                    print("El código no debe estar vacío y tampoco existente...")
                    continue
                titulo = input("Ingrese el título de la película: ")
                if validaTitulo(titulo) == False:
                    print("El título no debe estar vacío y tampoco espacios en blanco...")
                    continue
                genero = input("Ingrese el género de la película: ")
                if validaGenero(genero) == False:
                    print("El género no debe tener espacios en blanco y tampoco en vacio...")
                    continue
                duracion = input("Ingrese la duración de la película: ")
                if validaDuracion(duracion) == False:
                    print("Debe ser un número mayor a cero...")
                    continue
                clasificacion = input("Ingrese la clasificación de su película: ").upper()
                if validaClasificacion(clasificacion) == False:
                    print("La clasificación debe estar entre A, B o C...")
                    continue
                idioma = input("Ingrese el idioma de la película: ")
                if validaIdioma(idioma) == False:
                    print("El idioma no debe estar vacío, tampoco tener espacios en blanco...")
                    continue
                es_3d = input("¿Su película es 3D (s/n)?: ").lower()
                if valida3D(es_3d) == False:
                    print("Debe ser s o n para que se confirme el 3D...")
                    continue
                precio = input("Ingrese el precio de la película: ")
                if validaPrecio(precio) == False:
                    print("El precio debe ser un número entero mayor a cero...")
                    continue
                cupos = input("Ingrese los cupos de la película: ")
                if validaCupos(cupos) == False:
                    print("Los cupos deben ser un número entero mayor a cero...")
                    continue
                resp = agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos)
                if resp == True:
                    print("Película agregada...")
                else:
                    print("El código ya existe...")
                resp = input("¿Desea continuar (s/n)?: ").lower()
                if resp == "n":
                    break
        case 5:
            while True:
                codigo = input("Ingrese el código a eliminar: ").upper()
                resp = eliminar_pelicula(codigo)
                if resp == True:
                    print("Película eliminada...")
                else:
                    print("El código no existe...")
                resp = input("¿Desea continuar (s/n)?: ").lower()
                if resp == "n":
                    break
        case 6:
            print("Programa finalizado...")
            break