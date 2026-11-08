
class NodoIngrediente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None


class NodoPostre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = None
        self.siguiente = None


class ListaPostres:
    def __init__(self):
        self.inicio = None

    # Buscar un postre
    def buscar(self, nombre):
        actual = self.inicio

        while actual is not None:
            if actual.nombre.lower() == nombre.lower():
                return actual
            actual = actual.siguiente

        return None

    # Registrar un postre en orden alfabetico
    def agregar_postre(self, nombre):
        if self.buscar(nombre) is not None:
            print("Ese postre ya existe.")
            return

        nuevo = NodoPostre(nombre)

        if self.inicio is None or nombre.lower() < self.inicio.nombre.lower():
            nuevo.siguiente = self.inicio
            self.inicio = nuevo
        else:
            actual = self.inicio

            while actual.siguiente is not None and actual.siguiente.nombre.lower() < nombre.lower():
                actual = actual.siguiente

            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo

        print("Postre registrado correctamente.")

    # Agregar ingredientes
    def agregar_ingrediente(self, nombre, ingrediente):
        postre = self.buscar(nombre)

        if postre is None:
            print("El postre no existe.")
            return

        actual = postre.ingredientes

        while actual is not None:
            if actual.nombre.lower() == ingrediente.lower():
                print("Ese ingrediente ya esta registrado.")
                return
            actual = actual.siguiente

        nuevo = NodoIngrediente(ingrediente)

        if postre.ingredientes is None:
            postre.ingredientes = nuevo
        else:
            actual = postre.ingredientes

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo

        print("Ingrediente agregado correctamente.")

    # Mostrar ingredientes de un postre
    def mostrar_ingredientes(self, nombre):
        postre = self.buscar(nombre)

        if postre is None:
            print("El postre no existe.")
            return

        print("\nIngredientes de", postre.nombre + ":")

        actual = postre.ingredientes

        if actual is None:
            print("Este postre no tiene ingredientes registrados.")
            return

        while actual is not None:
            print("-", actual.nombre)
            actual = actual.siguiente

    # Eliminar un ingrediente
    def eliminar_ingrediente(self, nombre, ingrediente):
        postre = self.buscar(nombre)

        if postre is None:
            print("El postre no existe.")
            return

        actual = postre.ingredientes
        anterior = None

        while actual is not None:
            if actual.nombre.lower() == ingrediente.lower():

                if anterior is None:
                    postre.ingredientes = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                print("Ingrediente eliminado correctamente.")
                return

            anterior = actual
            actual = actual.siguiente

        print("El ingrediente no existe en este postre.")

    # Dar de baja un postre
    def eliminar_postre(self, nombre):
        actual = self.inicio
        anterior = None

        while actual is not None:
            if actual.nombre.lower() == nombre.lower():

                if anterior is None:
                    self.inicio = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                print("Postre y todos sus ingredientes eliminados.")
                return

            anterior = actual
            actual = actual.siguiente

        print("El postre no existe.")

    # Mostrar todos los postres
    def mostrar_postres(self):
        actual = self.inicio

        if actual is None:
            print("No hay postres registrados.")
            return

        print("\nLISTA DE POSTRES")

        while actual is not None:
            print("-", actual.nombre)
            actual = actual.siguiente


# PROGRAMA PRINCIPAL

postres = ListaPostres()

while True:
    print("\n===== MENU DE POSTRES =====")
    print("1. Mostrar ingredientes de un postre")
    print("2. Agregar ingredientes a un postre")
    print("3. Eliminar ingredientes de un postre")
    print("4. Registrar un postre nuevo")
    print("5. Dar de baja un postre")
    print("6. Mostrar todos los postres")
    print("7. Salir")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        nombre = input("Nombre del postre: ")
        postres.mostrar_ingredientes(nombre)

    elif opcion == "2":
        nombre = input("Nombre del postre: ")
        ingrediente = input("Nuevo ingrediente: ")
        postres.agregar_ingrediente(nombre, ingrediente)

    elif opcion == "3":
        nombre = input("Nombre del postre: ")
        ingrediente = input("Ingrediente que deseas eliminar: ")
        postres.eliminar_ingrediente(nombre, ingrediente)

    elif opcion == "4":
        nombre = input("Nombre del nuevo postre: ")
        postres.agregar_postre(nombre)

        if postres.buscar(nombre) is not None:
            respuesta = input("¿Deseas agregar ingredientes? (s/n): ")

            while respuesta.lower() == "s":
                ingrediente = input("Nombre del ingrediente: ")
                postres.agregar_ingrediente(nombre, ingrediente)
                respuesta = input("¿Agregar otro ingrediente? (s/n): ")

    elif opcion == "5":
        nombre = input("Nombre del postre que deseas eliminar: ")
        postres.eliminar_postre(nombre)

    elif opcion == "6":
        postres.mostrar_postres()

    elif opcion == "7":
        print("Programa finalizado.")
        break

    else:
        print("Opcion no valida. Intenta nuevamente.")
