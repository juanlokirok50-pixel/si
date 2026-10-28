# 🚀 Guía Práctica y Catálogo de Tkinter en Python

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![GUI Library](https://img.shields.io/badge/GUI-Tkinter-yellow.svg)](https://docs.python.org/3/library/tkinter.html)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Este repositorio es una colección educativa estructurada de ejemplos prácticos y proyectos en Python diseñados para aprender a desarrollar interfaces gráficas de usuario (**GUI**) modernas e interactivas utilizando la biblioteca nativa **Tkinter**.

Desde los conceptos más elementales (ventanas, botones, etiquetas) hasta temas avanzados como animación en lienzos gráficos, gestión de eventos y una aplicación completa **CRUD** con persistencia de datos.

---

## 📑 Tabla de Contenidos

1. [¿Qué es Tkinter?](#-qué-es-tkinter)
2. [Requisitos e Instalación](#-requisitos-e-instalación)
3. [Estructura del Proyecto](#-estructura-del-proyecto)
4. [Detalle de los Archivos de Código](#-detalle-de-los-archivos-de-código)
   - [01 - Hola Mundo y Widgets Básicos](#01_hola_mundo_y_basicospy)
   - [02 - Gestores de Geometría (pack, grid, place)](#02_gestores_de_geometriapy)
   - [03 - Widgets Interactivos y Variables Reactivas](#03_widgets_interactivospy)
   - [04 - Estilos Modernos y Widgets ttk](#04_estilos_y_ttkpy)
   - [05 - Diálogos Nativos y Ventanas Toplevel](#05_dialogos_y_ventanas_emergentespy)
   - [06 - Menús, Barras de Herramientas y Atajos](#06_menus_y_barras_de_herramientaspy)
   - [07 - Lienzo Gráfico (Canvas) y Animaciones con after()](#07_canvas_y_animacionespy)
   - [08 - Inspector de Eventos del Ratón y Teclado](#08_eventos_y_atajospy)
   - [09 - Proyecto Integral: Gestor de Tareas CRUD](#09_aplicacion_completa_crudpy)
5. [Buenas Prácticas en Tkinter](#-buenas-prácticas-en-tkinter)
6. [Cómo Publicar este Repositorio en GitHub](#-cómo-publicar-este-repositorio-en-github)

---

## 💡 ¿Qué es Tkinter?

**Tkinter** (*Tk interface*) es la biblioteca estándar de Python para la creación de interfaces gráficas. Viene preinstalada con la mayoría de distribuciones oficiales de Python y proporciona un enlace directo con el kit de herramientas **Tcl/Tk**.

### Ventajas principales:
- **Nativa y ligera:** No necesitas instalar bibliotecas externas pesadas mediante `pip`.
- **Multiplataforma:** El mismo código funciona en Windows, macOS y distribuciones GNU/Linux.
- **Rápida curva de aprendizaje:** Sintaxis intuitiva y excelente para prototipado y aplicaciones de escritorio profesionales.
- **Soporte temático moderno:** A través del submódulo `tkinter.ttk`, que proporciona widgets nativos y estilizados.

---

## 🛠 Requisitos e Instalación

### 1. Python 3.8 o superior
Comprueba si tienes Python instalado en tu terminal o PowerShell:

```bash
python --version
```

- **Windows / macOS:** Descarga el instalador oficial desde [python.org](https://www.python.org/downloads/). En Windows, asegúrate de marcar la casilla **"Add python.exe to PATH"** e instalar la opción **"tcl/tk and IDLE"** (marcada por defecto).
- **Linux (Ubuntu / Debian):** Si Tkinter no está disponible, instálalo con:
  ```bash
  sudo apt-get update
  sudo apt-get install python3-tk
  ```
- **Linux (Fedora):**
  ```bash
  sudo dnf install python3-tkinter
  ```
- **Linux (Arch):**
  ```bash
  sudo pacman -S tk
  ```

---

## 📂 Estructura del Proyecto

```text
libreria-tkinter/
├── main.py                             # Lanzador visual interactivo de todos los ejemplos
├── 01_hola_mundo_y_basicos.py          # Ventana base, Button, Label, Entry, Frame
├── 02_gestores_de_geometria.py         # Comparativa de pack(), grid() y place()
├── 03_widgets_interactivos.py          # Checkbutton, Radiobutton, Scale, Spinbox, Listbox
├── 04_estilos_y_ttk.py                 # Temas ttk, Style, Treeview y Progressbar
├── 05_dialogos_y_ventanas_emergentes.py# messagebox, filedialog, colorchooser y Toplevel
├── 06_menus_y_barras_de_herramientas.py# Menu, submenús, clic derecho, toolbar y atajos
├── 07_canvas_y_animaciones.py          # Primitivas de Canvas, rebote 60 FPS y dibujo libre
├── 08_eventos_y_atajos.py              # Event binding (<Button>, <Key>) e inspector en vivo
├── 09_aplicacion_completa_crud.py      # App completa: Gestor de Tareas con JSON
├── subir_a_github.bat                  # Script automatizado para publicar en GitHub en 1 clic
├── .gitignore                          # Exclusiones de archivos para Git
├── LICENSE                             # Licencia libre MIT
├── README.md                           # Documentación completa del repositorio
└── requirements.txt                    # Notas de compatibilidad y dependencias
```

---

## 🔍 Detalle de los Archivos de Código

---

### `01_hola_mundo_y_basicos.py`
> **Objetivo:** Comprender el ciclo de vida de una ventana en Tkinter y los widgets esenciales.

- **Conceptos cubiertos:**
  - Creación de la instancia principal `root = tk.Tk()`.
  - Configuración de propiedades de la ventana: `.title()`, `.geometry("520x420")`, `.minsize()`, `.resizable()` y `.configure(bg=...)`.
  - Widgets fundamentales:
    - `tk.Label`: Presentación de texto informativo con formatos de fuentes y colores.
    - `tk.Entry`: Entrada de datos por parte del usuario.
    - `tk.Button`: Botones interactivos asociados a funciones ejecutoras (`command=...`).
    - `tk.Frame`: Contenedores rectangulares para organizar la vista en bloques visuales independientes.
  - Bucle de eventos con `.mainloop()`.
- **Cómo ejecutar:**
  ```bash
  python 01_hola_mundo_y_basicos.py
  ```

---

### `02_gestores_de_geometria.py`
> **Objetivo:** Dominar los tres métodos para organizar y maquetar widgets en la pantalla.

- **Conceptos cubiertos:**
  - **`pack()`**: Disposición secuencial y automática alrededor de los bordes. Se analizan parámetros clave como `side` (`'top'`, `'bottom'`, `'left'`, `'right'`), `fill` (`'x'`, `'y'`, `'both'`), `expand` y espaciado (`padx`, `pady`).
  - **`grid()`**: Sistema de maquetación matricial (filas y columnas), el más recomendado para formularios complejos. Configuración de `row`, `column`, `columnspan`, `sticky` (`'nsew'`) y la asignación de pesos responsivos mediante `columnconfigure(col, weight=1)`.
  - **`place()`**: Posicionamiento directo mediante píxeles fijos (`x`, `y`, `width`, `height`) o coordenadas proporcionales (`relx`, `rely`, `relwidth`, `relheight`).
  - Navegación entre ejemplos utilizando un contenedor de pestañas `ttk.Notebook`.
- **Cómo ejecutar:**
  ```bash
  python 02_gestores_de_geometria.py
  ```

---

### `03_widgets_interactivos.py`
> **Objetivo:** Conocer los controles de formulario avanzados y las variables de control reactivas.

- **Conceptos cubiertos:**
  - **Variables de control de Tkinter:** `BooleanVar`, `StringVar`, `IntVar` y `DoubleVar`.
  - **Trazado reactivo (`trace_add`):** Cómo suscribir observadores que reaccionan automáticamente cuando el valor de una variable cambia.
  - Controles incluidos:
    - `tk.Checkbutton`: Casillas de selección múltiple (ej. configuración de notificaciones o modo nocturno).
    - `tk.Radiobutton`: Botones de selección excluyente única (ej. planes de suscripción).
    - `tk.Scale`: Control deslizante (slider) continuo para ajustar valores numéricos con arrastre.
    - `tk.Spinbox`: Selector de números enteros con flechas incrementales.
    - `tk.Listbox` + `tk.Scrollbar`: Lista de opciones con barra de desplazamiento vertical y botones para agregar o eliminar elementos en caliente.
- **Cómo ejecutar:**
  ```bash
  python 03_widgets_interactivos.py
  ```

---

### `04_estilos_y_ttk.py`
> **Objetivo:** Modernizar la apariencia de las interfaces utilizando el motor de temas `tkinter.ttk`.

- **Conceptos cubiertos:**
  - Clase `ttk.Style`: Modificación de apariencias, fuentes, rellenos y asignación dinámica de temas globales (`clam`, `alt`, `default`, `classic`, `vista`).
  - Widgets avanzados de `ttk`:
    - `ttk.Treeview`: Creación de tablas de datos estructuradas con columnas con encabezados, alineaciones y selección de filas.
    - `ttk.Progressbar`: Barras de estado en modo **determinado** (porcentajes de 0% a 100%) e **indeterminado** (animación continua para cargas asíncronas).
    - `ttk.Combobox`: Desplegables modernos con modo solo lectura (`readonly`).
    - `ttk.Separator`: Divisores horizontales y verticales.
- **Cómo ejecutar:**
  ```bash
  python 04_estilos_y_ttk.py
  ```

---

### `05_dialogos_y_ventanas_emergentes.py`
> **Objetivo:** Gestionar cuadros de diálogo del sistema y ventanas hijas secundarias.

- **Conceptos cubiertos:**
  - Submódulo `tkinter.messagebox`:
    - Notificaciones: `showinfo()`, `showwarning()`, `showerror()`.
    - Cuadros de decisión: `askyesno()`, `askokcancel()`.
  - Submódulo `tkinter.filedialog`:
    - Exploración y selección de archivos: `askopenfilename()`.
    - Diálogo de guardado: `asksaveasfilename()`.
    - Selector de directorios: `askdirectory()`.
  - Submódulo `tkinter.colorchooser`:
    - Selector de color nativo `askcolor()` que retorna códigos RGB y Hexadecimal.
  - Ventanas secundarias con `tk.Toplevel`:
    - Creación de ventanas flotantes no modales.
    - Creación de **ventanas modales** que bloquean la interacción con la ventana padre mediante `modal.grab_set()` y `modal.transient(root)`.
- **Cómo ejecutar:**
  ```bash
  python 05_dialogos_y_ventanas_emergentes.py
  ```

---

### `06_menus_y_barras_de_herramientas.py`
> **Objetivo:** Construir una interfaz típica de software de escritorio con menús jerárquicos y accesos rápidos.

- **Conceptos cubiertos:**
  - Barra de menú superior (`Menu`): Menús en cascada (`add_cascade`), comandos (`add_command`), separadores (`add_separator`) y casillas de verificación integradas (`add_checkbutton`).
  - Menú contextual emergente: Activación de menú con clic derecho (`<Button-3>`) usando `.post(x, y)`.
  - Barra de herramientas rápida (*Toolbar*): Botones de acción directa con efectos hover.
  - Barra de estado (*Status Bar*): Actualización reactiva con conteo de palabras y caracteres en tiempo real.
  - Atajos de teclado vinculados globalmente (`bind_all`): `Ctrl+N`, `Ctrl+O`, `Ctrl+S`, `Ctrl+Q`.
  - Widget `tk.Text`: Área de texto multilínea con soporte de deshacer/rehacer (`undo=True`).
- **Cómo ejecutar:**
  ```bash
  python 06_menus_y_barras_de_herramientas.py
  ```

---

### `07_canvas_y_animaciones.py`
> **Objetivo:** Dibujar figuras vectoriales y ejecutar animaciones suaves en 2D sin bloquear la interfaz.

- **Conceptos cubiertos:**
  - Dibujo de primitivas con `tk.Canvas`:
    - `create_line()` (líneas con grosor y extremos de flecha).
    - `create_rectangle()` (rectángulos y bordes estilizados).
    - `create_oval()` (círculos y elipses).
    - `create_polygon()` (figuras geométricas complejas como estrellas y triángulos).
    - `create_arc()` (arcos y sectores circulares).
    - `create_text()` (renderizado de tipografía en el lienzo).
  - Animación fluida (~60 FPS) mediante llamadas recursivas con `root.after(16, bucle)`.
  - Simulación física de múltiples pelotas rebotando con detección de colisión contra los bordes de la ventana.
  - Pizarra interactiva para pintar a mano alzada usando eventos `<Button-1>` y `<B1-Motion>`.
  - Arrastrar y soltar (*drag & drop*) de objetos geométricos sobre el lienzo.
- **Cómo ejecutar:**
  ```bash
  python 07_canvas_y_animaciones.py
  ```

---

### `08_eventos_y_atajos.py`
> **Objetivo:** Comprender en profundidad el sistema de enlaces y captura de eventos de Tkinter.

- **Conceptos cubiertos:**
  - Sintaxis formal de descriptores de eventos: `<modificador-tipo-detalle>`.
  - Eventos de ratón:
    - `<Button-1>` (clic izquierdo), `<Button-2>` (clic central), `<Button-3>` (clic derecho).
    - `<Double-Button-1>` (doble clic).
    - `<Enter>` y `<Leave>` (detección de paso del cursor / hover).
    - `<MouseWheel>` (desplazamiento con la rueda).
  - Eventos de teclado:
    - `<KeyPress>`, `<KeyRelease>`, combinaciones con `<Control>` y teclas especiales (`<Return>`, `<Escape>`).
  - Eventos de ventana: `<FocusIn>`, `<FocusOut>` y `<Configure>`.
  - **Inspector interactivo en vivo:** Visualiza las propiedades del objeto `event` (`x`, `y`, `keysym`, `char`, `keycode`, `widget`) en una tabla en tiempo real conforme interactúas con la pantalla.
- **Cómo ejecutar:**
  ```bash
  python 08_eventos_y_atajos.py
  ```

---

### `09_aplicacion_completa_crud.py`
> **Objetivo:** Integrar todos los conceptos en una aplicación de producción lista para usar.

- **Características principales:**
  - **Arquitectura Orientada a Objetos (POO):** Código limpio, desacoplado y mantenible.
  - **Operaciones CRUD completas:**
    - **C (Crear):** Formulario con validación para registrar tareas con título, categoría, prioridad, fecha límite y notas.
    - **R (Leer):** Visualización tabular en `ttk.Treeview` con indicadores de estado.
    - **U (Actualizar):** Modificación de campos precargando datos y alternancia rápida del estado (Pendiente / Completada).
    - **D (Eliminar):** Borrado individual de tareas con ventana de confirmación (`askyesno`).
  - **Persistencia de datos:** Lectura y escritura automática en un archivo `tareas.json` local.
  - **Filtros y Búsqueda en vivo:** Filtrado instantáneo por texto y por estado (Todas / Pendientes / Completadas).
  - **Panel de estadísticas:** Contador de tareas totales, pendientes, completadas y porcentaje de progreso.
- **Cómo ejecutar:**
  ```bash
  python 09_aplicacion_completa_crud.py
  ```

---

## 📌 Buenas Prácticas en Tkinter

1. **Evita `time.sleep()`:** En aplicaciones gráficas, `time.sleep()` congela el bucle de eventos (`mainloop`), provocando que la ventana no responda. Utiliza siempre `root.after(milisegundos, callback)`.
2. **Usa Programación Orientada a Objetos (POO):** Encapsular la lógica en clases (`class MiApp: def __init__(self, root): ...`) previene el uso de variables globales y mejora la reutilización del código.
3. **No mezcles `pack()` y `grid()` en el mismo contenedor:** Puedes usar `pack()` en la ventana principal y `grid()` dentro de un `Frame`, pero jamás apliques ambos directamente sobre los mismos hijos de un contenedor.
4. **Utiliza `ttk` para interfaces modernas:** Prefiere los widgets de `tkinter.ttk` frente a los clásicos cuando busques coherencia con el tema visual nativo del sistema operativo.
5. **Configura pesos de redimensionado:** Al usar `grid()`, añade `contenedor.columnconfigure(col, weight=1)` para que los campos de texto y tablas se expandan al cambiar el tamaño de la ventana.

---

## 🌐 Cómo Publicar este Repositorio en GitHub

Sigue estos sencillos pasos para subir este proyecto a tu cuenta de GitHub:

### Opción A: Usando la Terminal / Git CLI

1. **Abre tu terminal o PowerShell** en la carpeta donde se encuentra este proyecto:
   ```bash
   cd "ruta/a/libreria tkinter"
   ```

2. **Inicializa el repositorio local de Git:**
   ```bash
   git init
   ```

3. **Agrega todos los archivos al área de preparación:**
   ```bash
   git add .
   ```

4. **Crea el primer commit:**
   ```bash
   git commit -m "feat: repositorio inicial con ejemplos y proyectos prácticos de Tkinter"
   ```

5. **Crea un nuevo repositorio en [GitHub](https://github.com/new)** (deja las casillas de README y .gitignore desmarcadas para evitar conflictos).

6. **Vincula tu repositorio local con GitHub y súbelo:**
   ```bash
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
   git push -u origin main
   ```

---

### Opción B: Usando GitHub Desktop

1. Abre **GitHub Desktop**.
2. Ve al menú superior: **File** > **Add Local Repository...**
3. Selecciona la carpeta `libreria tkinter` y haz clic en **Add Repository**. Si te pregunta si deseas inicializarlo con Git, presiona **Create a repository**.
4. En el campo de resumen escribe: `Primer commit con catálogo de Tkinter`.
5. Haz clic en **Commit to main**.
6. Presiona el botón superior **Publish repository** para crearlo en tu cuenta de GitHub automáticamente.

---

### Opción C: Usando la CLI oficial de GitHub (`gh`)

Si tienes instalada la herramienta `gh`:

```bash
git init
git add .
git commit -m "feat: ejemplos de Tkinter y proyecto CRUD"
gh repo create libreria-tkinter --public --source=. --push
```

---

## 📄 Licencia

Este proyecto está bajo la Licencia [MIT](LICENSE). Eres libre de usar, modificar y distribuir este material para fines personales, educativos o comerciales.
