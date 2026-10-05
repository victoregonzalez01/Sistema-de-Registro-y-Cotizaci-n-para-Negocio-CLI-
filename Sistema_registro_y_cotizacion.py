#Librerias
import json

#FUNCIONES
def mostrar_menu():
	menu = print("""--- INVENTORYMAX: MENÚ PRINCIPAL ---
1. Agregar nuevo artículo
2. Mostrar inventario
3. Crear cotización
4. Salir y Guardar
------------------------------------""")
	return menu
#REGISTRAR PIEZA
def agregar_articulo(lista_destino):
	nombre_pieza = str(input("Nombre: "))
	while True:
		try:
			precio_pieza = float(input("Precio: "))
		except ValueError:
			print("Error: Entrada inválida. Por favor, ingresa solo números.")
			continue
		break
	lista_destino.append({"nombre": nombre_pieza, "precio": precio_pieza})
	print("Pieza registrada con éxito")
#MUESTRA INVENTARIO
def mostrar_inventario(lista_destino):
	print("Cantidad de piezas en inventario: ",len(lista_destino))
	for articulo in lista_destino:
		print(f"- Pieza: {articulo['nombre']} | Costo: ${articulo['precio']}")
	
#GUARDAR DATOS
def guardar_datos(lista_destino):
	print("Guardando inventario...")

	# Abrimos un archivo llamado 'datos.json' en modo 'w' (write / escritura)
	with open("inventario_piezas.json", "w") as archivo:
		# El traductor toma tu lista 'inventario' y la escribe en el 'archivo'
		json.dump(lista_destino, archivo)

	print("Cerrando InventoryMax...")

def agregar_indices(lista_destino):
	# 1. Creamos una lista vacía para ir guardando los resultados
	lista_nueva = []
	
	# 2. Medimos cuántos elementos hay para saber cuántas veces iterar
	total_elementos = len(lista_destino)
	
	# 3. El ciclo "for" va a contar desde 0 hasta el total de elementos
	for i in range(total_elementos):
		# Tomamos el objeto original usando su posición [i]
		objeto_original = lista_destino[i]
		
		# Creamos un nuevo diccionario, poniendo primero el 'id'
		objeto_con_id = {
			"id": i,
			"nombre": objeto_original["nombre"],
			"precio": objeto_original["precio"]
		}
		
		# Agregamos este nuevo objeto a nuestra lista_nueva
		lista_nueva.append(objeto_con_id)
		
	# 4. Al terminar el ciclo, regresamos la lista completa
	return lista_nueva
def mostrar_lista_cotizacion(lista_destino):
	lista_indexada = agregar_indices(lista_destino)
	for producto in lista_indexada:
		numero_lista = producto['id'] + 1
		print(f"{numero_lista}. {producto['nombre']} ~~~ ${producto['precio']}")

def crear_cotizacion(lista_destino):
	# 1. Verificamos si hay piezas en el inventario antes de hacer algo
	if len(lista_destino) == 0:
		print("\nEl inventario está vacío. Agrega piezas primero.\n")
		return # Esto cancela la función y nos regresa al menú principal

	# 2. El "freno de mano": Pedimos el número (ID) de la pieza
	while True:
		try:
			opcion_id = int(input("\nIngresa el número de la pieza que deseas cotizar (o 0 para cancelar): "))
		except ValueError:
			print("Error: Ingresa un número válido.")
			continue
				
		# Validamos si quiere cancelar
		if opcion_id == 0:
			return
					
		# Validamos que el número exista en la lista (que no ponga 10 si solo hay 3 artículos)
		if opcion_id < 1 or opcion_id > len(lista_destino):
			print("Ese número no está en la lista. Intenta de nuevo.")
			continue
					
		break # Si es un número válido y existe, rompemos este mini-ciclo

	# 3. Traducimos el ID visual al índice real de Python (que empieza en 0)
	indice_real = opcion_id - 1
	pieza_elegida = lista_destino[indice_real]

	# 4. Pedimos la cantidad que el cliente quiere cotizar
	while True:
		try:
			cantidad = int(input(f"¿Cuántas piezas de '{pieza_elegida['nombre']}' necesitas? "))
		except ValueError:
			print("Error: Ingresa una cantidad válida.")
			continue
		break

	# 5. Calculamos e imprimimos el ticket
	total = pieza_elegida['precio'] * cantidad
	print("\n" + "="*30)
	print("      COTIZACIÓN INVENTORYMAX      ")
	print("="*30)
	print(f"Producto:        {pieza_elegida['nombre']}")
	print(f"Precio unitario: ${pieza_elegida['precio']}")
	print(f"Cantidad:        {cantidad}")
	print("-" * 30)
	print(f"TOTAL A PAGAR:   ${total}")
	print("="*30 + "\n")
	

#OPCION INGRESADA POR EL USUARIO
def opcion_user():
	opcion = int(input("Ingresa una opcion del menu principal: "))
	return opcion


# Ritual de apertura: Intentar cargar datos previos
try:
	# Abrimos en modo 'r' (read / lectura)
	with open("inventario_piezas.json", "r") as archivo:
		inventario_piezas = json.load(archivo) # json.load hace lo opuesto a json.dump
		print("--- Inventario cargado desde el disco duro ---")
except FileNotFoundError:
	# Si es la primera vez que se corre y no hay archivo, iniciamos vacío
	inventario_piezas = []
	print("--- Base de datos nueva. Iniciando inventario vacío ---")

while True:
	mostrar_menu()
	try:
		opcion = opcion_user()
	except ValueError:
		print("Error: Entrada inválida. Por favor, ingresa solo números.")
		continue # Esto hace que se salte todo lo de abajo y vuelva a imprimir el menú
		

	if opcion == 1:
		agregar_articulo(inventario_piezas)
	elif opcion == 2:
		mostrar_inventario(inventario_piezas)
	elif opcion == 3:
		mostrar_lista_cotizacion(inventario_piezas)	
		crear_cotizacion(inventario_piezas)
	elif opcion == 4:
		guardar_datos(inventario_piezas)
		break
	else:
		print("Opcion no valida. intenta de nuevo")