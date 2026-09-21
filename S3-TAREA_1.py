class Calificador:
    def __init__(self):
        self.notas = []
    def validar_nota(self, nota):
        return 0 <= nota <= 100
    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas
    def promedio(self):
        return sum(self.notas) / len(self.notas)
c = Calificador()
print(c.cargar_notas(85, 92, 110, 78, -5, 88))
print(c.promedio())

class AnalizadorTexto:
    def __init__(self):
        self.palabras_unicas = set()
        self.orden_palabras = []
    def agregar_palabra(self, palabra):
        if palabra not in self.palabras_unicas:
            self.palabras_unicas.add(palabra)
            self.orden_palabras.append(palabra)
    def contar_palabras(self):
        return len(self.palabras_unicas)
    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)
at = AnalizadorTexto()
at.agregar_multiples("hola","mundo","hola")
print(at.contar_palabras())

class CarroCompras:
    def __init__(self):
        self.articulos = {}
    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio
    def total_carrito(self):
        return sum(self.articulos.values())
    def articulos_por_rango(self, precio_min, precio_max):
        resultado = []
        for nombre, precio in self.articulos.items():
            if precio_min <= precio <= precio_max:
                resultado.append(nombre)
        return resultado
c = CarroCompras()
c.agregar_articulo("pan",2.50)
c.agregar_articulo("leche",3.00)
print(c.total_carrito())

class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida = []
        indice = len(lista) - 1
        while indice >= 0:
            invertida.append(lista[indice])
            indice -= 1
        return invertida
    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            original = tuple(lista)
            invertida = self.invertir_lista(lista)
            resultado[original] = invertida
        return resultado
inv = InversorSecuencia()
print(inv.invertir_lista([1,2,3]))

class AnalizadorNumeros:
    def __init__(self):
        self.pares = []
        self.impares = []
    def es_par(self, numero):
        return numero % 2 == 0
    def separar(self, *numeros):
        self.pares = []
        self.impares = []
        for numero in numeros:
            if self.es_par(numero):
                self.pares.append(numero)
            else:
                self.impares.append(numero)
        return {
            "pares": self.pares,
            "impares": self.impares
        }
    def cantidad_pares_impares(self):
        return len(self.pares), len(self.impares)
an = AnalizadorNumeros()
print(an.separar(1,2,3,4,5))

class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []
    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)
    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)
    def minima(self):
        return min(self.temperaturas)
    def maxima(self):
        return max(self.temperaturas)
    def promedio(self):
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)
gt = GestorTemperatura()
gt.registrar_multiples(20, 25, 18, 30)
print(gt.promedio())

class GestorPersonas:
    def __init__(self):
        self.personas = {}
    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad
    def personas_mayores(self, edad_minima):
        resultado = []
        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                resultado.append(nombre)
        return resultado
    def edad_promedio(self):
        if len(self.personas) == 0:
            return 0
        return sum(self.personas.values()) / len(self.personas)
gp = GestorPersonas()
gp.agregar_persona("Ana",28)
gp.agregar_persona("Bob",17)
print(gp.personas_mayores(18))

class Equipos:
    def __init__(self):
        self.equipos = {}
    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []
    def agregar_jugador(self, equipo, jugador):
        if equipo in self.equipos:
            self.equipos[equipo].append(jugador)
    def equipo_mayor_integrantes(self):
        if len(self.equipos) == 0:
            return None
        equipo_mayor = None
        mayor_cantidad = 0
        for equipo, jugadores in self.equipos.items():
            if len(jugadores) > mayor_cantidad:
                mayor_cantidad = len(jugadores)
                equipo_mayor = equipo
        return equipo_mayor
eq = Equipos()
eq.crear_equipo("A")
eq.crear_equipo("B")
eq.agregar_jugador("A","Juan")
eq.agregar_jugador("A","Pedro")

class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""
    def solo_vocales(self, letra):
        return letra.lower() in "aeiouáéíóú"
    def contar_por_tipo(self, texto):
        conteo = {
            "vocales": 0,
            "consonantes": 0,
            "digitos": 0
        }
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto
        for letra in texto:
            if self.solo_vocales(letra):
                conteo["vocales"] += 1
            elif letra.isdigit():
                conteo["digitos"] += 1
            elif letra.isalpha():
                conteo["consonantes"] += 1
        return conteo
astr = AnalizadorString()
print(astr.contar_por_tipo("Hola123"))

class Tareas:
    def __init__(self):
        self.tareas = []
    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))
    def tareas_prioritarias(self):
        resultado = []
        for tarea in self.tareas:
            if tarea[1].lower() == "alta":
                resultado.append(tarea)
        return resultado
    def eliminar_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                return True
        return False
t = Tareas()
t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
print(t.tareas_prioritarias())

class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias = {}
    def agregar_elemento(self, elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] += 1
        else:
            self.frecuencias[elemento] = 1
    def elemento_mas_frecuente(self):
        if len(self.frecuencias) == 0:
            return None
        elemento_mayor = None
        mayor = 0
        for elemento, frecuencia in self.frecuencias.items():
            if frecuencia > mayor:
                mayor = frecuencia
                elemento_mayor = elemento
        return elemento_mayor
    def frecuencia_elemento(self, elemento):
        return self.frecuencias.get(elemento, 0)
cf = ContadorFrecuencia()
cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")
print(cf.elemento_mas_frecuente())

class SelectorRango:
    def crear_rango(self, inicio, fin):
        numeros = []
        for numero in range(inicio, fin + 1):
            numeros.append(numero)
        return tuple(numeros)
    def elementos_en_multiples_rangos(self, *rangos):
        elementos = set()
        for rango in rangos:
            inicio = rango[0]
            fin = rango[1]
            numeros = self.crear_rango(inicio, fin)
            for numero in numeros:
                elementos.add(numero)
        return sorted(list(elementos))
sr = SelectorRango()
print(sr.crear_rango(1, 3))
print(sr.elementos_en_multiples_rangos((1, 3), (2, 4)))

class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        mayor = max(len(lista1), len(lista2))
        for i in range(mayor):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado
    def intercalar_multiples(self, *listas):
        if len(listas) == 0:
            return []
        resultado = list(listas[0])
        for i in range(1, len(listas)):
            resultado = self.intercalar(resultado, listas[i])
        return resultado
cl = CombinadorListas()
print(cl.intercalar([1,2], [3,4]))

class RegistroNotas:
    def __init__(self):
        self.notas = {}
    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota
    def estudiantes_aprobados(self, nota_minima):
        aprobados = []
        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                aprobados.append(estudiante)
        return aprobados
    def mejor_estudiante(self):
        if len(self.notas) == 0:
            return None
        mejor_nombre = None
        mejor_nota = None
        for estudiante, nota in self.notas.items():
            if mejor_nota is None or nota > mejor_nota:
                mejor_nombre = estudiante
                mejor_nota = nota
        return mejor_nombre, mejor_nota
rn = RegistroNotas()
rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
print(rn.mejor_estudiante())

class DivisorFinder:
    def encontrar_divisores(self, numero):
        divisores = []
        if numero <= 0:
            return tuple(divisores)
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return tuple(divisores)
    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        suma = 0
        for divisor in divisores:
            if divisor != numero:
                suma += divisor
        return suma == numero
    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)
        return resultado
df = DivisorFinder()
print(df.encontrar_divisores(12))

class CodificadorCesar:
    def __init__(self):
        self.historial = {}
    def codificar_letra(self, letra, desplazamiento):
        if not letra.isalpha():
            return letra
        if letra.islower():
            inicio = ord('a')
        else:
            inicio = ord('A')
        codigo = ord(letra) - inicio
        nuevo_codigo = (codigo + desplazamiento) % 26
        return chr(nuevo_codigo + inicio)
    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""
        for letra in palabra:
            resultado += self.codificar_letra(letra, desplazamiento)
        self.historial[palabra] = resultado
        return resultado
cc = CodificadorCesar()
print(cc.codificar_palabra("hola", 3))

class AgrupadorEdades:
    def __init__(self):
        self.categorias = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }
    def clasificar_edad(self, edad):
        if edad < 13:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 65:
            return "adulto"
        else:
            return "mayor"
    def agrupar_por_categoria(self, *edades):
        self.categorias = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            self.categorias[categoria].append(edad)
        return self.categorias
    def edad_promedio_categoria(self, categoria):
        if categoria not in self.categorias:
            return 0
        edades = self.categorias[categoria]
        if len(edades) == 0:
            return 0
        return sum(edades) / len(edades)
ae = AgrupadorEdades()
print(ae.agrupar_por_categoria(5, 15, 30, 70))

class CalculadorDistancia:
    def __init__(self):
        self.distancias = []
    def distancia_euclidiana(self, p1, p2):
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        distancia = (
            (x2 - x1) ** 2 +
            (y2 - y1) ** 2
        ) ** 0.5
        self.distancias.append(distancia)
        return distancia
    def punto_mas_cercano(self, referencia, *puntos):
        if len(puntos) == 0:
            return None
        punto_cercano = None
        menor_distancia = None
        for punto in puntos:
            distancia = self.distancia_euclidiana(
                referencia,
                punto
            )
            if menor_distancia is None or distancia < menor_distancia:
                menor_distancia = distancia
                punto_cercano = punto
        return punto_cercano
cd = CalculadorDistancia()
print(cd.distancia_euclidiana((0,0), (3,4)))

class Inventario:
    def __init__(self):
        self.productos = {}
    def agregar_stock(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad
    def restar_stock(self, producto, cantidad):
        if producto not in self.productos:
            return False
        if self.productos[producto] < cantidad:
            return False
        self.productos[producto] -= cantidad
        return True
    def productos_bajo_stock(self, minimo):
        resultado = []
        for producto, cantidad in self.productos.items():
            if cantidad < minimo:
                resultado.append(producto)
        return resultado
inv = Inventario()
inv.agregar_stock("pan", 50)
print(inv.restar_stock("pan", 30))
print(inv.productos_bajo_stock(15))

class AnalizadorPatrones:
    def __init__(self):
        self.palabras = []
    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        resultado = []
        for palabra in palabras:
            if palabra.lower().startswith(patron.lower()):
                resultado.append(palabra)
        return resultado
    def agrupar_por_longitud(self, texto):
        resultado = {}
        for palabra in texto.split():
            longitud = len(palabra)
            if longitud not in resultado:
                resultado[longitud] = []
            resultado[longitud].append(palabra)
        return resultado
    def palabras_unicas(self):
        return set(self.palabras)
    def cargar_texto(self, texto):
        palabras = texto.split()
        for palabra in palabras:
            self.palabras.append(palabra)
ap = AnalizadorPatrones()
print(ap.agrupar_por_longitud("el gato está aquí"))

# Ejercicios nuevos
class TallerMecanico:
    def __init__(self):
        self.reparaciones = []
    def registrar_reparacion(self, placa, falla, costo):
        self.reparaciones.append({"placa": placa, "falla": falla, "costo": costo})
    def costo_total_placa(self, placa):
        total = 0
        for r in self.reparaciones:
            if r["placa"] == placa:
                total += r["costo"]
        return total
    def fallas_caras(self, minimo):
        resultado = []
        for r in self.reparaciones:
            if r["costo"] >= minimo:
                resultado.append(r["falla"])
        return resultado
tm = TallerMecanico()
tm.registrar_reparacion("ABC123", "frenos", 80)
tm.registrar_reparacion("ABC123", "aceite", 25)
tm.registrar_reparacion("XYZ9", "motor", 400)
print(tm.costo_total_placa("ABC123"))
print(tm.fallas_caras(50))


class Cafeteria:
    def __init__(self):
        self.ordenes = []
    def tomar_orden(self, cliente, bebida, precio):
        self.ordenes.append({"cliente": cliente, "bebida": bebida, "precio": precio})
    def total_cliente(self, cliente):
        total = 0
        for o in self.ordenes:
            if o["cliente"] == cliente:
                total += o["precio"]
        return total
    def bebidas_unicas(self):
        resultado = set()
        for o in self.ordenes:
            resultado.add(o["bebida"])
        return resultado
cf = Cafeteria()
cf.tomar_orden("Ana", "latte", 3.5)
cf.tomar_orden("Ana", "muffin", 2.0)
cf.tomar_orden("Luis", "espresso", 2.5)
print(cf.total_cliente("Ana"))
print(cf.bebidas_unicas())


class EstacionClima:
    def __init__(self):
        self.registros = {}
    def registrar_ciudad(self, ciudad, humedad, viento):
        self.registros[ciudad] = {"humedad": humedad, "viento": viento}
    def ciudad_mas_humeda(self):
        if len(self.registros) == 0:
            return None
        mayor_ciudad = None
        mayor = -1
        for ciudad, datos in self.registros.items():
            if datos["humedad"] > mayor:
                mayor = datos["humedad"]
                mayor_ciudad = ciudad
        return mayor_ciudad
    def ciudades_viento_alto(self, minimo):
        resultado = []
        for ciudad, datos in self.registros.items():
            if datos["viento"] >= minimo:
                resultado.append(ciudad)
        return resultado
ec = EstacionClima()
ec.registrar_ciudad("Lima", 80, 12)
ec.registrar_ciudad("Cusco", 55, 20)
ec.registrar_ciudad("Arequipa", 40, 25)
print(ec.ciudad_mas_humeda())
print(ec.ciudades_viento_alto(18))


class ClubLectura:
    def __init__(self):
        self.lecturas = {}
    def registrar_lectura(self, socio, libro, paginas):
        if socio not in self.lecturas:
            self.lecturas[socio] = []
        self.lecturas[socio].append({"libro": libro, "paginas": paginas})
    def paginas_socio(self, socio):
        if socio not in self.lecturas:
            return 0
        total = 0
        for lectura in self.lecturas[socio]:
            total += lectura["paginas"]
        return total
    def socio_mas_lector(self):
        if len(self.lecturas) == 0:
            return None
        mayor_socio = None
        mayor = -1
        for socio in self.lecturas:
            paginas = self.paginas_socio(socio)
            if paginas > mayor:
                mayor = paginas
                mayor_socio = socio
        return mayor_socio
cl = ClubLectura()
cl.registrar_lectura("Ana", "1984", 328)
cl.registrar_lectura("Ana", "Fahrenheit", 158)
cl.registrar_lectura("Bob", "Dune", 412)
print(cl.paginas_socio("Ana"))
print(cl.socio_mas_lector())


class Granja:
    def __init__(self):
        self.animales = {}
    def agregar_lote(self, especie, cantidad):
        if especie in self.animales:
            self.animales[especie] += cantidad
        else:
            self.animales[especie] = cantidad
    def vender(self, especie, cantidad):
        if especie not in self.animales:
            return False
        if self.animales[especie] < cantidad:
            return False
        self.animales[especie] -= cantidad
        return True
    def especies_escasas(self, minimo):
        resultado = []
        for especie, cantidad in self.animales.items():
            if cantidad < minimo:
                resultado.append(especie)
        return resultado
gr = Granja()
gr.agregar_lote("gallinas", 40)
gr.agregar_lote("vacas", 8)
gr.vender("gallinas", 10)
print(gr.especies_escasas(15))


class RelojMundial:
    def __init__(self):
        self.zonas = {}
    def agregar_zona(self, ciudad, diferencia):
        self.zonas[ciudad] = diferencia
    def hora_en(self, ciudad, hora_base):
        if ciudad not in self.zonas:
            return None
        hora = (hora_base + self.zonas[ciudad]) % 24
        return hora
    def ciudades_adelantadas(self):
        resultado = []
        for ciudad, diferencia in self.zonas.items():
            if diferencia > 0:
                resultado.append(ciudad)
        return resultado
rw = RelojMundial()
rw.agregar_zona("Lima", -5)
rw.agregar_zona("Madrid", 1)
rw.agregar_zona("Tokyo", 9)
print(rw.hora_en("Tokyo", 10))
print(rw.ciudades_adelantadas())


class Museo:
    def __init__(self):
        self.obras = {}
    def agregar_obra(self, titulo, artista, anio):
        self.obras[titulo] = {"artista": artista, "anio": anio}
    def obras_de_artista(self, artista):
        resultado = []
        for titulo, datos in self.obras.items():
            if datos["artista"].lower() == artista.lower():
                resultado.append(titulo)
        return resultado
    def obra_mas_antigua(self):
        if len(self.obras) == 0:
            return None
        antigua = None
        anio_min = None
        for titulo, datos in self.obras.items():
            if anio_min is None or datos["anio"] < anio_min:
                anio_min = datos["anio"]
                antigua = titulo
        return antigua
mu = Museo()
mu.agregar_obra("Guernica", "Picasso", 1937)
mu.agregar_obra("Las Meninas", "Velázquez", 1656)
mu.agregar_obra("El viejo guitarrista", "Picasso", 1903)
print(mu.obras_de_artista("Picasso"))
print(mu.obra_mas_antigua())


class LigaFutbol:
    def __init__(self):
        self.equipos = {}
    def registrar_equipo(self, nombre):
        if nombre not in self.equipos:
            self.equipos[nombre] = {"puntos": 0, "goles": 0}
    def sumar_partido(self, nombre, puntos, goles):
        if nombre in self.equipos:
            self.equipos[nombre]["puntos"] += puntos
            self.equipos[nombre]["goles"] += goles
    def lider(self):
        if len(self.equipos) == 0:
            return None
        mejor = None
        max_puntos = -1
        for nombre, datos in self.equipos.items():
            if datos["puntos"] > max_puntos:
                max_puntos = datos["puntos"]
                mejor = nombre
        return mejor
    def equipos_con_goles(self, minimo):
        resultado = []
        for nombre, datos in self.equipos.items():
            if datos["goles"] >= minimo:
                resultado.append(nombre)
        return resultado
lf = LigaFutbol()
lf.registrar_equipo("A")
lf.registrar_equipo("B")
lf.sumar_partido("A", 3, 2)
lf.sumar_partido("B", 1, 1)
lf.sumar_partido("A", 1, 0)
print(lf.lider())
print(lf.equipos_con_goles(2))


class Farmacia:
    def __init__(self):
        self.medicinas = {}
    def agregar_medicina(self, nombre, precio, stock):
        self.medicinas[nombre] = {"precio": precio, "stock": stock}
    def vender(self, nombre, cantidad):
        if nombre not in self.medicinas:
            return False
        if self.medicinas[nombre]["stock"] < cantidad:
            return False
        self.medicinas[nombre]["stock"] -= cantidad
        return True
    def medicinas_baratas(self, precio_max):
        resultado = []
        for nombre, datos in self.medicinas.items():
            if datos["precio"] <= precio_max:
                resultado.append(nombre)
        return resultado
far = Farmacia()
far.agregar_medicina("paracetamol", 2.5, 40)
far.agregar_medicina("ibuprofeno", 3.8, 10)
print(far.vender("paracetamol", 5))
print(far.medicinas_baratas(3))


class DiarioViaje:
    def __init__(self):
        self.ciudades = []
    def visitar(self, ciudad, dias, gasto):
        self.ciudades.append({"ciudad": ciudad, "dias": dias, "gasto": gasto})
    def gasto_total(self):
        total = 0
        for c in self.ciudades:
            total += c["gasto"]
        return total
    def ciudad_mas_dias(self):
        if len(self.ciudades) == 0:
            return None
        mayor = self.ciudades[0]
        for c in self.ciudades:
            if c["dias"] > mayor["dias"]:
                mayor = c
        return mayor["ciudad"]
dv = DiarioViaje()
dv.visitar("Cusco", 4, 180)
dv.visitar("Arequipa", 2, 90)
dv.visitar("Lima", 3, 150)
print(dv.gasto_total())
print(dv.ciudad_mas_dias())


class EscuelaMusica:
    def __init__(self):
        self.alumnos = {}
    def inscribir(self, nombre, instrumento):
        self.alumnos[nombre] = instrumento
    def alumnos_de_instrumento(self, instrumento):
        resultado = []
        for nombre, inst in self.alumnos.items():
            if inst.lower() == instrumento.lower():
                resultado.append(nombre)
        return resultado
    def instrumentos_unicos(self):
        return set(self.alumnos.values())
em = EscuelaMusica()
em.inscribir("Ana", "piano")
em.inscribir("Luis", "guitarra")
em.inscribir("Eva", "piano")
print(em.alumnos_de_instrumento("piano"))
print(em.instrumentos_unicos())


class EstacionamientoBicis:
    def __init__(self):
        self.bicis = {}
    def estacionar(self, codigo, color, horas):
        self.bicis[codigo] = {"color": color, "horas": horas}
    def retirar(self, codigo):
        if codigo in self.bicis:
            del self.bicis[codigo]
            return True
        return False
    def bicis_por_color(self, color):
        resultado = []
        for codigo, datos in self.bicis.items():
            if datos["color"].lower() == color.lower():
                resultado.append(codigo)
        return resultado
    def mas_tiempo(self):
        if len(self.bicis) == 0:
            return None
        mayor_codigo = None
        mayor = -1
        for codigo, datos in self.bicis.items():
            if datos["horas"] > mayor:
                mayor = datos["horas"]
                mayor_codigo = codigo
        return mayor_codigo
eb = EstacionamientoBicis()
eb.estacionar("B1", "rojo", 2)
eb.estacionar("B2", "azul", 5)
eb.estacionar("B3", "rojo", 1)
print(eb.bicis_por_color("rojo"))
print(eb.mas_tiempo())


class CatalogoCelulares:
    def __init__(self):
        self.modelos = {}
    def agregar_modelo(self, nombre, marca, bateria):
        self.modelos[nombre] = {"marca": marca, "bateria": bateria}
    def modelos_de_marca(self, marca):
        resultado = []
        for nombre, datos in self.modelos.items():
            if datos["marca"].lower() == marca.lower():
                resultado.append(nombre)
        return resultado
    def mayor_bateria(self):
        if len(self.modelos) == 0:
            return None
        mejor = None
        mayor = -1
        for nombre, datos in self.modelos.items():
            if datos["bateria"] > mayor:
                mayor = datos["bateria"]
                mejor = nombre
        return mejor
ccel = CatalogoCelulares()
ccel.agregar_modelo("Pixel 8", "Google", 4500)
ccel.agregar_modelo("Galaxy S24", "Samsung", 4000)
ccel.agregar_modelo("Pixel 9", "Google", 4700)
print(ccel.modelos_de_marca("Google"))
print(ccel.mayor_bateria())


class CineClub:
    def __init__(self):
        self.asistencias = {}
    def registrar_asistencia(self, socio, pelicula):
        if socio not in self.asistencias:
            self.asistencias[socio] = []
        self.asistencias[socio].append(pelicula)
    def peliculas_socio(self, socio):
        return self.asistencias.get(socio, [])
    def socio_mas_asistencias(self):
        if len(self.asistencias) == 0:
            return None
        mayor_socio = None
        mayor = -1
        for socio, pelis in self.asistencias.items():
            if len(pelis) > mayor:
                mayor = len(pelis)
                mayor_socio = socio
        return mayor_socio
cclub = CineClub()
cclub.registrar_asistencia("Ana", "Dune")
cclub.registrar_asistencia("Ana", "Matrix")
cclub.registrar_asistencia("Luis", "Dune")
print(cclub.peliculas_socio("Ana"))
print(cclub.socio_mas_asistencias())


class Pizzeria:
    def __init__(self):
        self.pizzas = {}
    def agregar_pizza(self, nombre, ingredientes, precio):
        self.pizzas[nombre] = {"ingredientes": list(ingredientes), "precio": precio}
    def pizzas_con(self, ingrediente):
        resultado = []
        for nombre, datos in self.pizzas.items():
            if ingrediente.lower() in [i.lower() for i in datos["ingredientes"]]:
                resultado.append(nombre)
        return resultado
    def pizza_mas_cara(self):
        if len(self.pizzas) == 0:
            return None
        cara = None
        mayor = -1
        for nombre, datos in self.pizzas.items():
            if datos["precio"] > mayor:
                mayor = datos["precio"]
                cara = nombre
        return cara
pz = Pizzeria()
pz.agregar_pizza("margarita", ["tomate", "queso", "albahaca"], 12)
pz.agregar_pizza("hawaiana", ["tomate", "queso", "piña", "jamón"], 15)
print(pz.pizzas_con("queso"))
print(pz.pizza_mas_cara())


class Observatorio:
    def __init__(self):
        self.estrellas = {}
    def registrar_estrella(self, nombre, magnitud, constelacion):
        self.estrellas[nombre] = {"magnitud": magnitud, "constelacion": constelacion}
    def estrellas_de(self, constelacion):
        resultado = []
        for nombre, datos in self.estrellas.items():
            if datos["constelacion"].lower() == constelacion.lower():
                resultado.append(nombre)
        return resultado
    def mas_brillante(self):
        if len(self.estrellas) == 0:
            return None
        mejor = None
        menor_mag = None
        for nombre, datos in self.estrellas.items():
            if menor_mag is None or datos["magnitud"] < menor_mag:
                menor_mag = datos["magnitud"]
                mejor = nombre
        return mejor
ob = Observatorio()
ob.registrar_estrella("Sirio", -1.46, "Can Mayor")
ob.registrar_estrella("Betelgeuse", 0.42, "Orión")
ob.registrar_estrella("Rigel", 0.13, "Orión")
print(ob.estrellas_de("Orión"))
print(ob.mas_brillante())


class Lavanderia:
    def __init__(self):
        self.servicios = []
    def registrar_servicio(self, cliente, kilos, precio_kilo):
        self.servicios.append({
            "cliente": cliente,
            "kilos": kilos,
            "precio_kilo": precio_kilo
        })
    def total_cliente(self, cliente):
        total = 0
        for s in self.servicios:
            if s["cliente"] == cliente:
                total += s["kilos"] * s["precio_kilo"]
        return total
    def kilos_totales(self):
        total = 0
        for s in self.servicios:
            total += s["kilos"]
        return total
lv = Lavanderia()
lv.registrar_servicio("Ana", 4, 2.5)
lv.registrar_servicio("Ana", 2, 3.0)
lv.registrar_servicio("Luis", 6, 2.5)
print(lv.total_cliente("Ana"))
print(lv.kilos_totales())


class AgenciaAutos:
    def __init__(self):
        self.autos = {}
    def publicar(self, modelo, anio, precio):
        self.autos[modelo] = {"anio": anio, "precio": precio}
    def autos_por_presupuesto(self, maximo):
        resultado = []
        for modelo, datos in self.autos.items():
            if datos["precio"] <= maximo:
                resultado.append(modelo)
        return resultado
    def auto_mas_nuevo(self):
        if len(self.autos) == 0:
            return None
        nuevo = None
        anio_max = -1
        for modelo, datos in self.autos.items():
            if datos["anio"] > anio_max:
                anio_max = datos["anio"]
                nuevo = modelo
        return nuevo
aa = AgenciaAutos()
aa.publicar("Civic", 2018, 12000)
aa.publicar("Corolla", 2021, 15000)
aa.publicar("Spark", 2016, 7000)
print(aa.autos_por_presupuesto(13000))
print(aa.auto_mas_nuevo())


class Guarderia:
    def __init__(self):
        self.ninos = {}
    def inscribir(self, nombre, edad, aula):
        self.ninos[nombre] = {"edad": edad, "aula": aula}
    def ninos_de_aula(self, aula):
        resultado = []
        for nombre, datos in self.ninos.items():
            if datos["aula"] == aula:
                resultado.append(nombre)
        return resultado
    def edad_promedio(self):
        if len(self.ninos) == 0:
            return 0
        return sum(d["edad"] for d in self.ninos.values()) / len(self.ninos)
gd = Guarderia()
gd.inscribir("Lucía", 4, "A")
gd.inscribir("Mateo", 5, "A")
gd.inscribir("Sofía", 3, "B")
print(gd.ninos_de_aula("A"))
print(gd.edad_promedio())


class TiendaSemillas:
    def __init__(self):
        self.semillas = {}
    def agregar(self, nombre, tipo, stock):
        self.semillas[nombre] = {"tipo": tipo, "stock": stock}
    def vender(self, nombre, cantidad):
        if nombre not in self.semillas:
            return False
        if self.semillas[nombre]["stock"] < cantidad:
            return False
        self.semillas[nombre]["stock"] -= cantidad
        return True
    def por_tipo(self, tipo):
        resultado = []
        for nombre, datos in self.semillas.items():
            if datos["tipo"].lower() == tipo.lower():
                resultado.append(nombre)
        return resultado
ts = TiendaSemillas()
ts.agregar("tomate", "hortaliza", 30)
ts.agregar("girasol", "flor", 12)
ts.agregar("lechuga", "hortaliza", 20)
print(ts.vender("tomate", 5))
print(ts.por_tipo("hortaliza"))
