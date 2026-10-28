"""
=============================================================================
main.py - Lanzador Principal del Catálogo de Tkinter
=============================================================================
Menú interactivo con interfaz gráfica para explorar y ejecutar
cualquiera de los 9 módulos de ejemplo con un solo clic.
=============================================================================
"""

import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import sys
import os

# Lista de módulos del catálogo
EJEMPLOS = [
    {
        "archivo": "01_hola_mundo_y_basicos.py",
        "titulo": "1. Hola Mundo y Widgets Básicos",
        "desc": "Ventana principal, Label, Entry, Button, Frame y bucle de eventos.",
        "icono": "👋",
        "categoria": "Básico"
    },
    {
        "archivo": "02_gestores_de_geometria.py",
        "titulo": "2. Gestores de Geometría",
        "desc": "Comparativa práctica entre pack(), grid() responsivo y place().",
        "icono": "📐",
        "categoria": "Diseño"
    },
    {
        "archivo": "03_widgets_interactivos.py",
        "titulo": "3. Widgets Interactivos y Variables",
        "desc": "Checkbutton, Radiobutton, Scale, Spinbox, Listbox y trace_add().",
        "icono": "🎛️",
        "categoria": "Formularios"
    },
    {
        "archivo": "04_estilos_y_ttk.py",
        "titulo": "4. Estilos Modernos y Widgets ttk",
        "desc": "Temas visuales, ttk.Style, ttk.Treeview y ttk.Progressbar.",
        "icono": "🎨",
        "categoria": "Estilos"
    },
    {
        "archivo": "05_dialogos_y_ventanas_emergentes.py",
        "titulo": "5. Diálogos Nativos y Toplevel",
        "desc": "messagebox, filedialog, colorchooser y ventanas modales.",
        "icono": "🪟",
        "categoria": "Diálogos"
    },
    {
        "archivo": "06_menus_y_barras_de_herramientas.py",
        "titulo": "6. Menús, Toolbar y Atajos",
        "desc": "Menú en cascada, clic derecho contextual, toolbar y atajos Ctrl+S.",
        "icono": "📋",
        "categoria": "Navegación"
    },
    {
        "archivo": "07_canvas_y_animaciones.py",
        "titulo": "7. Canvas y Animaciones a 60 FPS",
        "desc": "Figuras vectoriales, rebote físico con after() y pizarra de dibujo.",
        "icono": "⚽",
        "categoria": "Gráficos"
    },
    {
        "archivo": "08_eventos_y_atajos.py",
        "titulo": "8. Inspector de Eventos en Vivo",
        "desc": "Captura de eventos de ratón, teclado y ventana en tiempo real.",
        "icono": "⚡",
        "categoria": "Eventos"
    },
    {
        "archivo": "09_aplicacion_completa_crud.py",
        "titulo": "9. Proyecto Integral: Gestor CRUD",
        "desc": "Gestor de tareas profesional con POO, filtros y persistencia JSON.",
        "icono": "💼",
        "categoria": "Proyecto"
    }
]


class LanzadorApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Lanzador - Catálogo de Ejemplos Tkinter")
        self.root.geometry("780x640")
        self.root.minsize(700, 560)
        self.root.configure(bg="#f8fafc")

        self.directorio_base = os.path.dirname(os.path.abspath(__file__))

        self.crear_interfaz()

    def crear_interfaz(self):
        # Encabezado
        header = tk.Frame(self.root, bg="#1e293b", padx=20, pady=15)
        header.pack(fill="x")

        tk.Label(
            header,
            text="🚀 Catálogo Interactivo de Tkinter",
            font=("Segoe UI", 16, "bold"),
            fg="#ffffff",
            bg="#1e293b"
        ).pack(side="left")

        tk.Label(
            header,
            text="Selecciona y ejecuta cualquier módulo",
            font=("Segoe UI", 9),
            fg="#94a3b8",
            bg="#1e293b"
        ).pack(side="right")

        # Contenedor con scroll para los ejemplos
        contenedor = tk.Frame(self.root, bg="#f8fafc", padx=15, pady=15)
        contenedor.pack(fill="both", expand=True)

        canvas = tk.Canvas(contenedor, bg="#f8fafc", highlightthickness=0)
        scrollbar = ttk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
        self.scroll_frame = tk.Frame(canvas, bg="#f8fafc")

        self.scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw", width=730)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Permitir scroll con la rueda del ratón
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

        # Tarjetas de cada módulo
        for item in EJEMPLOS:
            self.crear_tarjeta_ejemplo(self.scroll_frame, item)

    def crear_tarjeta_ejemplo(self, parent, item):
        tarjeta = tk.Frame(parent, bg="#ffffff", bd=1, relief="solid", padx=12, pady=10)
        tarjeta.pack(fill="x", pady=6)

        # Icono + Título + Categoría
        fila_sup = tk.Frame(tarjeta, bg="#ffffff")
        fila_sup.pack(fill="x")

        tk.Label(
            fila_sup,
            text=f"{item['icono']}  {item['titulo']}",
            font=("Segoe UI", 11, "bold"),
            fg="#0f172a",
            bg="#ffffff"
        ).pack(side="left")

        tk.Label(
            fila_sup,
            text=f"[{item['categoria']}]",
            font=("Segoe UI", 8, "bold"),
            fg="#2563eb",
            bg="#eff6ff",
            padx=6,
            pady=2
        ).pack(side="right")

        # Descripción
        tk.Label(
            tarjeta,
            text=item["desc"],
            font=("Segoe UI", 9),
            fg="#475569",
            bg="#ffffff"
        ).pack(anchor="w", pady=(4, 8))

        # Fila inferior: Archivo y Botón de Ejecutar
        fila_inf = tk.Frame(tarjeta, bg="#ffffff")
        fila_inf.pack(fill="x")

        tk.Label(
            fila_inf,
            text=f"📄 {item['archivo']}",
            font=("Consolas", 8),
            fg="#64748b",
            bg="#ffffff"
        ).pack(side="left")

        btn_ejecutar = tk.Button(
            fila_inf,
            text="▶ Ejecutar Módulo",
            command=lambda arch=item["archivo"]: self.ejecutar_script(arch),
            bg="#2563eb",
            fg="#ffffff",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            padx=12,
            pady=3,
            cursor="hand2"
        )
        btn_ejecutar.pack(side="right")

    def ejecutar_script(self, nombre_archivo):
        ruta_script = os.path.join(self.directorio_base, nombre_archivo)
        if not os.path.exists(ruta_script):
            messagebox.showerror("Error", f"No se encontró el archivo:\n{nombre_archivo}")
            return

        try:
            # Ejecutar el script en un proceso independiente
            subprocess.Popen([sys.executable, ruta_script])
        except Exception as e:
            messagebox.showerror("Error al ejecutar", f"No se pudo iniciar {nombre_archivo}:\n{e}")


if __name__ == "__main__":
    app_root = tk.Tk()
    app = LanzadorApp(app_root)
    app_root.mainloop()
