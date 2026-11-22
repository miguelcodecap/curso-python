# Recetario · Sesión 4 — Slicing y texto (en curso)

Consulta rápida de lo visto el 18-nov-2026 (parte 1) y el 21-nov-2026 (parte 2). **Sesión en curso:** se completará con `.split()`, `.replace()`, `in` y `len()` en texto cuando se cierre la sesión.

---

## 1. Slicing: cortar una lista

**Qué es:** sacar un pedazo de una lista con `lista[inicio:fin]`.
**Para qué sirve:** quedarte con los primeros días, los últimos días o un tramo del historial.

**Regla clave:** el `inicio` **sí** se incluye; el `fin` **no** se incluye.

```python
precios = [158.40, 160.25, 157.90, 161.30, 163.75, 162.10]
#  índice:    0       1       2       3       4       5
# negativo:  -6      -5      -4      -3      -2      -1

precios[1:4]    # [160.25, 157.90, 161.30] → índices 1, 2 y 3 (el 4 no)
```

**Truco:** `fin - inicio` = cuántos elementos salen (`4 - 1` = 3).

**Variantes:**

```python
precios[:3]     # los 3 primeros         → desde el inicio hasta el índice 2
precios[2:]     # desde el índice 2 hasta el final
precios[-3:]    # los 3 últimos
precios[-4:]    # los 4 últimos
precios[:]      # la lista completa
```

**Índice vs slicing:**

| | Ejemplo | Devuelve |
| --- | --- | --- |
| Índice | `precios[0]` | Un **valor** suelto: `158.40` |
| Slicing | `precios[0:1]` | Una **lista**: `[158.40]` (aunque tenga un solo elemento) |

**Receta: promedio de los últimos días**

```python
ultimos_3 = precios[-3:]
promedio_3 = sum(ultimos_3) / len(ultimos_3)
```

**Ojo:**
- El slicing lee siempre **de izquierda a derecha**. `precios[-1:-5]` y `precios[-5:0]` devuelven `[]` (lista vacía): el inicio está a la derecha del fin.
- Para llegar **hasta el final incluyendo el último**, el `fin` se deja vacío: `[-4:]`. Con `[-5:-1]` el último queda fuera.
- Un slicing sin `=` no guarda nada: `precios[0:]` solo, en una línea, no hace nada.

---

## 2. Orden de operaciones

**Qué es:** el orden en que Python resuelve una cuenta.

1. Paréntesis `()`
2. Potencia `**`
3. Multiplicación y división `*` `/` (de izquierda a derecha)
4. Suma y resta `+` `-` (de izquierda a derecha)

**Por qué importa:** sin paréntesis, el resultado puede salir mal **sin ningún error**.

```python
compra = 158.40
actual = 168.30

actual - compra / compra * 100      # ❌ hace primero compra / compra * 100 → 68.30
(actual - compra) / compra * 100    # ✅ 6.25
```

**Variantes para que salga bien:**

```python
# A) Paréntesis
rendimiento = (actual - compra) / compra * 100

# B) Separar el paso en su propia variable (más fácil de leer y revisar)
ganancia = actual - compra
rendimiento = ganancia / compra * 100
```

---

## 3. `.upper()`

**Qué es:** método de texto que devuelve el texto en **mayúsculas**.
**Para qué sirve:** dejar uniformes los tickers aunque el usuario los escriba en minúsculas.

```python
ticker = "scco"
print(ticker.upper())   # SCCO
```

**Por qué con punto y paréntesis:** es un método del texto (`texto.metodo()`). Los `()` lo **ejecutan** y van **vacíos**: el método ya sabe sobre qué texto trabajar (el que está antes del punto).

**Variantes:**

```python
# Guardar el resultado (la variable original NO cambia sola)
ticker = ticker.upper()

# Usarlo directo dentro de un f-string (solo sirve para ese print)
print(f"Ticker: {ticker.upper()}")

# Aplicarlo al input en la misma línea
ticker = input("Ticker: ").upper()
```

**Ojo:**
- `ticker.upper()` no modifica `ticker`; devuelve un texto **nuevo**. Para conservarlo, hay que asignarlo: `ticker = ticker.upper()`. Python lee esa línea de derecha a izquierda: calcula, y guarda en la variable de la izquierda.
- A la **izquierda** del `=` solo va un nombre de variable. `ticker.upper = "BAP"` da error.
- `ticker.upper(ticker)` da **TypeError**: `.upper()` no recibe nada dentro de los paréntesis.
- Sin `()`: `print(ticker.upper)` muestra `<built-in method upper ...>` en vez del texto.
- Entre comillas (`"ticker.upper()"`) es solo texto, no se ejecuta.
- Dentro del `print` vs con `=`: `print(ticker.upper())` muestra `BAP`, pero `ticker` sigue en minúsculas. Si vas a usar el ticker varias veces, guárdalo una vez.

---

## 4. `.lower()`

**Qué es:** método de texto que devuelve el texto en **minúsculas**. Es el espejo de `.upper()` y se escribe igual.
**Para qué sirve:** dejar uniformes correos, dominios, URLs y nombres de usuario.

```python
correo = "Soporte@BANCO.com"
correo = correo.lower()
print(correo)   # soporte@banco.com
```

**Por qué existe si ya hay `.upper()`:** cada dato tiene su convención.

| Dato | Convención | Método |
| --- | --- | --- |
| Tickers | MAYÚSCULAS (`SCCO`, `BAP`) | `.upper()` |
| Correos, dominios, URLs, usuarios | minúsculas (`banco.com`) | `.lower()` |

**Variantes:**

```python
# Guardar el resultado
usuario = usuario.lower()

# Directo en el print (solo para ese print)
print("Pago-USD 500".lower())        # pago-usd 500

# En la misma línea del input
correo = input("¿Cuál es el correo? ").lower()
```

**Solo cambian las letras:** números, símbolos y espacios quedan igual.

```python
"BCP-2026 @Lima".lower()   # "bcp-2026 @lima"
```

### Normalizar

**Qué es:** dejar todos los datos en el **mismo formato** antes de compararlos o analizarlos. Depende del dato: para un ticker, normalizar es `.upper()`; para un usuario o correo, `.lower()`; para quitar espacios sobrantes, `.strip()` (sección 5).

**Por qué en ciberseguridad:** para Python, `"Admin"`, `"ADMIN"` y `"admin"` son tres textos distintos.

```python
intento_1 = "Admin"
intento_1 = intento_1.lower()
intento_2 = "ADMIN"
intento_2 = intento_2.lower()
intento_3 = "admin"
intento_3 = intento_3.lower()
print(f"Intentos: {intento_1}, {intento_2}, {intento_3}")   # Intentos: admin, admin, admin
```

- Sin normalizar: parecen 3 usuarios con 1 intento cada uno (nada raro).
- Normalizado: **1 usuario con 3 intentos** (posible ataque a la cuenta `admin`).

**Cuándo SÍ y cuándo NO normalizar:**

| Caso | ¿`Admin` = `admin`? | ¿Normalizar? |
| --- | --- | --- |
| Windows, cuentas corporativas, correos, dominios | Sí, es lo mismo | ✅ Sí |
| Linux (usuarios) | No: pueden ser dos cuentas | ❌ No |
| Contraseñas | No: `Clave123` ≠ `clave123` | ❌ Nunca (la debilitarías) |

Regla: se normaliza lo que el sistema trata igual; no se toca lo que debe ser exacto. Antes de normalizar, saber cómo trata el sistema las mayúsculas.

### Ojo: `.lower()` no funciona en listas

```python
intentos = ["Admin", "ADMIN", "admin"]
intentos.lower()
# AttributeError: 'list' object has no attribute 'lower'
```

Cada tipo tiene sus propios métodos:

| Tipo | Tiene | No tiene |
| --- | --- | --- |
| `str` | `.upper()`, `.lower()`, `.strip()` | `.append()` |
| `list` | `.append()` | `.upper()`, `.lower()`, `.strip()` |

**Trampa: convertir la lista a texto con `str()`**

```python
intentos_texto = str(intentos).lower()
print(intentos_texto)        # ['admin', 'admin', 'admin']  ← parece lista, pero es texto
print(type(intentos_texto))  # <class 'str'>
print(intentos_texto[0])     # [  ← en un texto, cada posición es UN carácter
len(intentos_texto)          # 27 caracteres, no 3 intentos
```

`str(lista)` es como una **foto** de una tabla de Excel: sirve para **verla**, no para **trabajar** con ella (contar, separar, agregar). Para limpiar cada elemento y que siga siendo lista se necesitan **bucles** (semana 3).

---

## 5. `.strip()`

**Qué es:** método de texto que quita los espacios del **inicio** y del **final**. Los del medio no los toca.
**Para qué sirve:** limpiar lo que el usuario escribe (espacios que se cuelan al copiar y pegar) y las líneas de registros y archivos, que suelen traer espacios o saltos de línea al final.

```python
ticker = "   scco   "
ticker = ticker.strip()
print(f"[{ticker}]")   # [scco]
```

**Truco de los corchetes:** los espacios no se ven en pantalla. Poner `[ ]` alrededor del valor en la f-string muestra dónde empieza y termina el texto.

**Qué quita:** espacios, saltos de línea `\n` y tabulaciones `\t` de los extremos.

```python
linea_log = "  ACCESO FALLIDO user=jperez  \n"
linea_log = linea_log.strip()
print(f"[{linea_log}]")   # [ACCESO FALLIDO user=jperez]
```

**No cambia** los espacios entre palabras, ni letras, ni tildes:

```python
"  Banco de Crédito  ".strip()   # "Banco de Crédito"
```

**Variantes:**

```python
texto = "  BCP  "

texto.strip()    # "BCP"      → ambos lados
texto.lstrip()   # "BCP  "    → solo la izquierda (left)
texto.rstrip()   # "  BCP"    → solo la derecha (right)
```

**Quitar otros caracteres:** se ponen entre comillas dentro de los paréntesis.

```python
precio_texto = "$$$165.40$$"
precio_texto = precio_texto.strip("$")     # "165.40"
precio = float(precio_texto)               # 165.4 (ahora es número)
cantidad_de_acciones = 25
compra = precio * cantidad_de_acciones
print(f"El precio de la acción es ${precio:.2f}")
print(f"El valor total por las {cantidad_de_acciones} acciones es de ${compra:.2f}")
```

**Ojo:**
- Igual que `.upper()` y `.lower()`: sin `=` no se guarda. `usuario.strip()` solo, deja `usuario` igual.
- Después de limpiar un precio en texto, hay que convertirlo con `float()` para poder calcular.

---

## 6. Encadenar métodos

**Qué es:** poner un método tras otro en la misma línea. Python los aplica **de izquierda a derecha**.
**Para qué sirve:** limpiar un dato en un solo paso.

```python
ticker = input("¿Cuál es el ticker? ").strip().upper()
# Usuario escribe: "   sCcO  "
# 1) input()  → "   sCcO  "
# 2) .strip() → "sCcO"
# 3) .upper() → "SCCO"

correo = input("¿Cuál es el correo? ").strip().lower()
# "  Alertas@BCP.com   " → "alertas@bcp.com"

ticker = "   bvn  "
ticker = ticker.strip().upper()   # "BVN"
```

**Por qué primero `.strip()`:** primero se limpia y después se normaliza. (Con estos dos métodos el orden no cambia el resultado, pero es la costumbre.)

---

## 7. Detalles de `input()` vistos hoy

```python
ticker = input("¿Cuál es el ticker? ")
#              └─ mensaje: lo escribes TÚ en el código → lleva comillas
# ticker ← respuesta: la escribe el USUARIO en la terminal → no lleva comillas, input() la devuelve como str
```

- El `¿` y las tildes son válidos **dentro** de las comillas. Fuera de ellas dan `SyntaxError: invalid character '¿'`.
- Deja un espacio al final del mensaje, dentro de las comillas: `"¿Cuál es el ticker? "`. Si no, la respuesta sale pegada (`¿Cuál es el ticker?sCcO`).
- Para probar un programa con `input()`, al ejecutarlo escribe a propósito datos "sucios" (mayúsculas mezcladas, espacios). Si la salida sale limpia, el código funciona.

---

## 8. Estilo (PEP 8) visto hoy

- Nombres de variables **todo en minúsculas** con guiones bajos: `cantidad_de_acciones`, `ticker_usuario`. No `Cantidad_de_acciones` ni `Ticker2`.
- Nombres que digan qué guardan: `compra` o `valor_total` (dólares), no `acciones_25`.
- Números que pueden cambiar, en su propia variable (`cantidad_de_acciones = 25`) y usados en el texto con `{}`.
- No convertir lo que ya tiene el tipo correcto: `int(25)` sobra.
- Espacio después de cada coma, también dentro de las f-strings: `{a}, {b}, {c}`.
