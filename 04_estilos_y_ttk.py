"""
=============================================================================
04_estilos_y_ttk.py
=============================================================================
Exploración de la biblioteca `tkinter.ttk` (Themed Tkinter):
- Uso de ttk.Style para personalizar la apariencia de los widgets.
- Cambio dinámico de temas del sistema ('clam', 'alt', 'default', 'classic', etc.).
- ttk.Treeview: Tablas avanzadas de datos con columnas y encabezados.
- ttk.Progressbar: Barras de progreso determinadas e indeterminadas.
- ttk.Combobox: Listas desplegables estilizadas.
- ttk.Separator: Divisores visuales.
=============================================================================
"""

import tkinter as tk
from tkinter import ttk


class EstilosYTTKApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("04 - Estilos Modernos y Widgets ttk")
        self.root.geometry("820x640")
        self.root.minsize(750, 580)

        # Gestor de estilos ttk
        self.style = ttk.Style()

        # Estilo personalizado para botones destacados
        self.style.configure(
            "Accent.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=6
        )

        self.crear_interfaz()

    def crear_interfaz(self):
        # -------------------------------------------------------------------
        # 1. Barra Superior con Selector de Temas
        # -------------------------------------------------------------------
        frame_tema = ttk.Frame(self.root, padding=10)
        frame_tema.pack(fill="x")

        ttk.Label(frame_tema, text="Tema ttk actual:", font=("Segoe UI", 10, "bold")).pack(side="left", padx=(0, 8))

        temas_disponibles = self.style.theme_names()
        self.combo_temas = ttk.Combobox(
            frame_tema,
            values=list(temas_disponibles),
            state="readonly",
            width=15
        )
        self.combo_temas.set(self.style.theme_use())
        self.combo_temas.pack(side="left", padx=5)
        self.combo_temas.bind("<<ComboboxSelected>>", self.cambiar_tema)

        ttk.Label(
            frame_tema,
            text="(Cambia el tema para ver cómo se transforma la apariencia de toda la app)",
            font=("Segoe UI", 9, "italic")
        ).pack(side="left", padx=10)

        ttk.Separator(self.root, orient="horizontal").pack(fill="x", padx=10)

        # -------------------------------------------------------------------
        # 2. Contenedor de Pestañas (Notebook)
        # -------------------------------------------------------------------
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        tab_tabla = ttk.Frame(notebook, padding=12)
        tab_progreso = ttk.Frame(notebook, padding=12)

        notebook.add(tab_tabla, text=" 📊 Treeview (Tabla de Datos) ")
        notebook.add(tab_progreso, text=" ⏳ Barras de Progreso e Indicadores ")

        self.construir_tab_tabla(tab_tabla)
        self.construir_tab_progreso(tab_progreso)

    def construir_tab_tabla(self, parent):
        """Construye una vista de tabla con ttk.Treeview y desplazamiento."""
        lbl_info = ttk.Label(
            parent,
            text="ttk.Treeview permite mostrar jerarquías (árboles) o tablas multicolumna con ordenación y selección.",
            font=("Segoe UI", 9)
        )
        lbl_info.pack(anchor="w", pady=(0, 8))

        # Contenedor para Treeview + Scrollbars
        frame_tv = ttk.Frame(parent)
        frame_tv.pack(fill="both", expand=True)

        scroll_y = ttk.Scrollbar(frame_tv, orient="vertical")
        scroll_x = ttk.Scrollbar(frame_tv, orient="horizontal")

        columnas = ("id", "nombre", "lenguaje", "experiencia", "estado")
        self.tree = ttk.Treeview(
            frame_tv,
            columns=columnas,
            show="headings",  # Ocultar la columna raíz '#'
            selectmode="browse",
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set
        )

        scroll_y.config(command=self.tree.yview)
        scroll_x.config(command=self.tree.xview)

        scroll_y.pack(side="right", fill="y")
        scroll_x.pack(side="bottom", fill="x")
        self.tree.pack(side="left", fill="both", expand=True)

        # Configurar encabezados y anchos de columna
        titulos = {
            "id": ("ID", 50, "center"),
            "nombre": ("Nombre del Programador", 200, "w"),
            "lenguaje": ("Lenguaje Principal", 140, "center"),
            "experiencia": ("Nivel", 100, "center"),
            "estado": ("Disponibilidad", 120, "center")
        }

        for col_id, (titulo, ancho, alineacion) in titulos.items():
            self.tree.heading(col_id, text=titulo, anchor=alineacion)
            self.tree.column(col_id, width=ancho, anchor=alineacion)

        # Datos de ejemplo
        desarrolladores = [
            (1, "Ana Martínez", "Python / Tkinter", "Senior", "Disponible"),
            (2, "Carlos Gómez", "JavaScript / React", "Semi-Senior", "En Proyecto"),
            (3, "Laura Díaz", "C++ / Qt", "Senior", "Disponible"),
            (4, "Marcos López", "Rust / Actix", "Junior", "En Capacitación"),
            (5, "Elena Torres", "Python / FastAPI", "Senior", "Disponible"),
            (6, "Javier Ruiz", "Go / Kubernetes", "Semi-Senior", "En Proyecto"),
        ]

        for dev in desarrolladores:
            self.tree.insert("", "end", values=dev)

        # Acciones sobre la tabla
        frame_acciones = ttk.Frame(parent, padding=(0, 10, 0, 0))
        frame_acciones.pack(fill="x")

        ttk.Button(frame_acciones, text="Ver Registro Seleccionado", command=self.mostrar_seleccion).pack(side="left", padx=5)
        ttk.Button(frame_acciones, text="Eliminar Seleccionado", command=self.eliminar_seleccion).pack(side="left", padx=5)

    def construir_tab_progreso(self, parent):
        """Demuestra el uso de ttk.Progressbar determinada e indeterminada."""
        ttk.Label(
            parent,
            text="ttk.Progressbar ofrece dos modos de uso fundamentales:",
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w", pady=(0, 10))

        # 1. Barra Determinada
        frame_det = ttk.LabelFrame(parent, text=" Modo Determinado (Valor Conocido: 0 - 100%) ", padding=15)
        frame_det.pack(fill="x", pady=10)

        self.pb_determinada = ttk.Progressbar(frame_det, orient="horizontal", length=400, mode="determinate")
        self.pb_determinada.pack(fill="x", pady=10)
        self.pb_determinada["value"] = 30

        frame_btn_det = ttk.Frame(frame_det)
        frame_btn_det.pack(anchor="w")

        ttk.Button(frame_btn_det, text="+10%", command=lambda: self.ajustar_progreso(10)).pack(side="left", padx=5)
        ttk.Button(frame_btn_det, text="-10%", command=lambda: self.ajustar_progreso(-10)).pack(side="left", padx=5)
        ttk.Button(frame_btn_det, text="Reiniciar (0%)", command=lambda: self.ajustar_progreso(-100)).pack(side="left", padx=5)

        # 2. Barra Indeterminada
        frame_indet = ttk.LabelFrame(parent, text=" Modo Indeterminado (Cargas Asíncronas o Esperas) ", padding=15)
        frame_indet.pack(fill="x", pady=10)

        self.pb_indeterminada = ttk.Progressbar(frame_indet, orient="horizontal", length=400, mode="indeterminate")
        self.pb_indeterminada.pack(fill="x", pady=10)

        frame_btn_indet = ttk.Frame(frame_indet)
        frame_btn_indet.pack(anchor="w")

        ttk.Button(frame_btn_indet, text="▶ Iniciar Animación", command=self.pb_indeterminada.start).pack(side="left", padx=5)
        ttk.Button(frame_btn_indet, text="⏹ Detener Animación", command=self.pb_indeterminada.stop).pack(side="left", padx=5)

    def cambiar_tema(self, event=None):
        nuevo_tema = self.combo_temas.get()
        self.style.theme_use(nuevo_tema)

    def ajustar_progreso(self, delta):
        actual = self.pb_determinada["value"]
        nuevo = max(0, min(100, actual + delta))
        self.pb_determinada["value"] = nuevo

    def mostrar_seleccion(self):
        seleccion = self.tree.selection()
        if seleccion:
            item = self.tree.item(seleccion[0])
            valores = item["values"]
            tk.messagebox.showinfo("Detalle de Seleccionado", f"Programador: {valores[1]}\nLenguaje: {valores[2]}\nNivel: {valores[3]}")
        else:
            tk.messagebox.showwarning("Sin selección", "Por favor selecciona una fila de la tabla.")

    def eliminar_seleccion(self):
        seleccion = self.tree.selection()
        if seleccion:
            self.tree.delete(seleccion[0])
        else:
            tk.messagebox.showwarning("Sin selección", "Selecciona una fila para eliminar.")


if __name__ == "__main__":
    app_root = tk.Tk()
    app = EstilosYTTKApp(app_root)
    app_root.mainloop()
