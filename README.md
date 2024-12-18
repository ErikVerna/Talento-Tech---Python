# Iniciación a la Programación con Python 🤖

## Talento Tech BA
### Comision: 24215
## Profesor:  Nicolas Riquelme 
## Alumno: Erik Verna 


# Proyecto final integrador (PFI)

# Sistema de Gestión de Productos "Logística Hyrule"

## Descripción del Proyecto
Este programa implementa un sistema de gestión de inventarios llamado **Logística Hyrule**, desarrollado en Python. Permite realizar operaciones básicas como:
- Registrar nuevos productos.
- Listar productos existentes.
- Modificar información de un producto.
- Eliminar productos del inventario.
- Buscar productos por diferentes criterios.
- Identificar productos con bajo stock.

## Requisitos del Sistema
- **Python 3.8 o superior**
- Librerías necesarias:
  - `sqlite3` (incluida por defecto en Python).
  - `os` (incluida por defecto en Python).
  - `colorama` (instalable con `pip install colorama`).

## Estructura del Proyecto
El proyecto consta de los siguientes componentes principales:

### 1. **Base de Datos**
El sistema utiliza una base de datos SQLite almacenada en la carpeta `db` con el archivo `inventario.db`. La tabla `productos` tiene la siguiente estructura:
- `id`: Identificador único (entero, clave primaria, autoincremental).
- `nombre`: Nombre del producto (texto, único, requerido).
- `descripcion`: Descripción del producto (texto, requerido).
- `categoria`: Categoría del producto (texto, requerido).
- `cantidad`: Cantidad disponible en inventario (entero, requerido, no negativo).
- `precio`: Precio del producto (entero, requerido, no negativo).

### 2. **Funciones Principales**

#### a) Inicialización
- **`init_tabla_db()`**: Crea la tabla `productos` en la base de datos si no existe.

#### b) Operaciones CRUD
- **Alta de productos**:
  - Funcionalidad: Registra un nuevo producto con datos validados.
  - Funciones: `agregar_producto()`.
- **Lectura de productos**:
  - Funcionalidad: Lista todos los productos registrados.
  - Funciones: `listar_productos()`.
- **Modificación de productos**:
  - Funcionalidad: Permite editar los datos de un producto existente.
  - Funciones: `modificar_producto()`.
- **Eliminación de productos**:
  - Funcionalidad: Elimina un producto después de confirmación.
  - Funciones: `baja_producto()`.

#### c) Búsqueda y Filtrado
- **Búsqueda de productos**:
  - Funcionalidad: Permite buscar productos por ID, nombre o categoría.
  - Funciones: `busqueda_producto()`.
- **Productos con bajo stock**:
  - Funcionalidad: Lista los productos cuya cantidad es inferior a un límite especificado.
  - Funciones: `listar_bajo_stock()`.

### 3. **Interfaz de Usuario**
- Menú principal interactivo que permite al usuario seleccionar las opciones mediante números.
- Mensajes y colores proporcionados por la librería **Colorama** para mejorar la experiencia visual.

## Uso del Programa
1. Clona el repositorio o descarga los archivos del proyecto en formato zip.
2. Asegúrate de tener las siguientes dependencias instaladas:
   ```bash
   pip install colorama
   ```
3. Ejecuta el archivo principal del programa:
   ```bash
   python main.py
   ```
4. Sigue las instrucciones en el menú para realizar las operaciones deseadas.

## Ejemplo de Flujo
1. Seleccionamos la opción `1` para agregar un nuevo producto.
2. Ingresamos los datos solicitados (nombre, descripción, categoría, cantidad y precio).
3. Usamos la opción `2` para listar todos los productos y verificar que el nuevo producto se haya registrado.
4. Si se precisa editar algún producto, se utiliza la opción `3`.
5. Usamos la opción `6` para verificar productos con bajo stock.

## Personalización
Se puede modificar la estructura de la tabla o agregar nuevas funcionalidades editando las funciones correspondientes en el código fuente.

## Consideraciones
- **Validación de datos**: El programa verifica que los datos ingresados sean válidos (por ejemplo, que la cantidad y el precio sean números no negativos).
- **Control de errores**: Manejo de errores comunes como entradas no válidas o intentos de registrar productos duplicados.

---
**Autor:** Erik Tomás Verna 
**Versión:** 1.0.0
