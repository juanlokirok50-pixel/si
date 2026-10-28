"""
=============================================================================
08_eventos_y_atajos.py
=============================================================================
Profundización en el sistema de eventos y enlaces (Event Binding) de Tkinter:
- Sintaxis del descriptor de eventos: <modificador-tipo-detalle>
- Eventos de ratón: <Button-1>, <Double-Button-1>, <Enter>, <Leave>, <Motion>, <MouseWheel>
- Eventos de teclado: <Key>, <Return>, <Escape>, combinaciones con Control y Alt.
- Eventos de ventana: <FocusIn>, <FocusOut>, <Configure> (redimensionado).
- Inspector visual de propiedades del objeto `Event`:
  x, y, x_root, y_root, keysym, char, keycode, widget, state.
=============================================================================
"""

import tkinter as tk
from tkinter import ttk


class InspectorEventosApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("08 - Sistema de Eventos y Enlace de Teclado/Ratón")
        self.root.geometry("820x620")
        self.root.minsize(720, 520)
        self.root.configure(bg="#0f172a")

        self.contador_eventos = 0
        self.crear_interfaz()
        self.vincular_eventos()

    def crear_interfaz(self):
        # Título
        tk.Label(
            self.root,
            text="Inspector Interactivo de Eventos de Tkinter",
            font=("Segoe UI", 13, "bold"),
            bg="#1e293b",
            fg="#f8fafc",
            pady=12
        ).pack(fill="x")

        contenedor = tk.Frame(self.root, bg="#0f172a", padx=15, pady=10)
        contenedor.pack(fill="both", expand=True)

        # -------------------------------------------------------------------
        # Zona Interactiva de Pruebas (Zona Activa)
        # -------------------------------------------------------------------
        frame_prueba = tk.LabelFrame(
            contenedor,
            text=" 🎯 Zona de Prueba (Haz clic, escribe, arrastra o pasa el ratón aquí) ",
            font=("Segoe UI", 10, "bold"),
            bg="#1e293b",
            fg="#38bdf8",
            padx=15,
            pady=15
        )
        frame_prueba.pack(fill="x", pady=(0, 10))

        # Cuadro sensible a eventos de ratón
        self.caja_interactiva = tk.Label(
            frame_prueba,
            text="PASAR EL RATÓN AQUÍ | CLIC IZQUIERDO / DERECHO | DOBLE CLIC",
            bg="#334155",
            fg="#e2e8f0",
            font=("Segoe UI", 10, "bold"),
            relief="groove",
            bd=2,
            pady=20,
            cursor="crosshair"
        )
        self.caja_interactiva.pack(fill="x", pady=(0, 10))

        # Campo para probar teclas
        frame_inputs = tk.Frame(frame_prueba, bg="#1e293b")
        frame_inputs.pack(fill="x")

        tk.Label(
            frame_inputs,
            text="Prueba de Teclas:",
            bg="#1e293b",
            fg="#94a3b8",
            font=("Segoe UI", 9)
        ).pack(side="left", padx=(0, 8))

        self.entry_tecla = tk.Entry(
            frame_inputs,
            font=("Consolas", 10),
            bg="#0f172a",
            fg="#38bdf8",
            insertbackground="#38bdf8",
            relief="solid",
            bd=1
        )
        self.entry_tecla.pack(side="left", fill="x", expand=True, padx=(0, 10), ipady=3)
        self.entry_tecla.insert(0, "Escribe letras, Enter, Escape, Flechas...")

        btn_limpiar = tk.Button(
            frame_inputs,
            text="Limpiar Registro",
            command=self.limpiar_registro,
            bg="#ef4444",
            fg="white",
            relief="flat",
            padx=10,
            cursor="hand2"
        )
        btn_limpiar.pack(side="right")

        # -------------------------------------------------------------------
        # Registro en Vivo de Eventos (Treeview)
        # -------------------------------------------------------------------
        frame_registro = tk.LabelFrame(
            contenedor,
            text=" 📋 Registro de Propiedades del Objeto `event` ",
            font=("Segoe UI", 10, "bold"),
            bg="#1e293b",
            fg="#38bdf8",
            padx=10,
            pady=10
        )
        frame_registro.pack(fill="both", expand=True)

        scroll_y = ttk.Scrollbar(frame_registro, orient="vertical")
        scroll_y.pack(side="right", fill="y")

        columnas = ("num", "tipo", "widget", "x_y", "keysym", "char", "keycode")
        self.tabla_eventos = ttk.Treeview(
            frame_registro,
            columns=columnas,
            show="headings",
            yscrollcommand=scroll_y.set
        )
        scroll_y.config(command=self.tabla_eventos.yview)

        cabeceras = {
            "num": ("#", 45, "center"),
            "tipo": ("Tipo de Evento", 140, "w"),
            "widget": ("Widget Emisor", 120, "w"),
            "x_y": ("(X, Y) Rel / Abs", 140, "center"),
            "keysym": ("KeySym", 110, "center"),
            "char": ("Char", 70, "center"),
            "keycode": ("KeyCode", 80, "center")
        }

        for col, (titulo, ancho, alineacion) in cabeceras.items():
            self.tabla_eventos.heading(col, text=titulo, anchor=alineacion)
            self.tabla_eventos.column(col, width=ancho, anchor=alineacion)

        self.tabla_eventos.pack(fill="both", expand=True)

    def vincular_eventos(self):
        # Eventos de ratón sobre la caja interactiva
        self.caja_interactiva.bind("<Enter>", lambda e: self.registrar_evento("Mouse Enter (Hover)", e, color="#10b981"))
        self.caja_interactiva.bind("<Leave>", lambda e: self.registrar_evento("Mouse Leave", e, color="#64748b"))
        self.caja_interactiva.bind("<Button-1>", lambda e: self.registrar_evento("Clic Izquierdo (<Button-1>)", e))
        self.caja_interactiva.bind("<Button-2>", lambda e: self.registrar_evento("Clic Central (<Button-2>)", e))
        self.caja_interactiva.bind("<Button-3>", lambda e: self.registrar_evento("Clic Derecho (<Button-3>)", e))
        self.caja_interactiva.bind("<Double-Button-1>", lambda e: self.registrar_evento("Doble Clic (<Double-Button-1>)", e))
        self.caja_interactiva.bind("<MouseWheel>", lambda e: self.registrar_evento("Rueda Mouse (<MouseWheel>)", e))

        # Eventos de teclado sobre el Entry
        self.entry_tecla.bind("<KeyPress>", lambda e: self.registrar_evento("Tecla Presionada (<KeyPress>)", e))
        self.entry_tecla.bind("<KeyRelease>", lambda e: self.registrar_evento("Tecla Soltada (<KeyRelease>)", e))
        self.entry_tecla.bind("<FocusIn>", lambda e: self.registrar_evento("Foco Recibido (<FocusIn>)", e))
        self.entry_tecla.bind("<FocusOut>", lambda e: self.registrar_evento("Foco Perdido (<FocusOut>)", e))

        # Evento global de redimensionado de ventana
        self.root.bind("<Configure>", self.al_redimensionar)

    def registrar_evento(self, nombre_evento, event, color=None):
        self.contador_eventos += 1

        # Obtener datos del objeto evento
        coords = f"({getattr(event, 'x', '-')}, {getattr(event, 'y', '-')})"
        keysym = getattr(event, "keysym", "-")
        char = repr(getattr(event, "char", "-")) if getattr(event, "char", "") else "''"
        keycode = getattr(event, "keycode", "-")
        nombre_widget = str(event.widget).split(".")[-1] or "root"

        # Insertar fila en la tabla
        item_id = self.tabla_eventos.insert(
            "",
            0,  # Insertar al inicio para ver los más recientes arriba
            values=(self.contador_eventos, nombre_evento, nombre_widget, coords, keysym, char, keycode)
        )

        # Efecto visual de color temporal en la caja si aplica
        if color:
            self.caja_interactiva.config(bg=color)
            if color == "#10b981":
                self.caja_interactiva.config(fg="white")
            elif color == "#64748b":
                self.caja_interactiva.config(fg="#e2e8f0", bg="#334155")

        # Limitar número máximo de filas para mantener rendimiento
        hijos = self.tabla_eventos.get_children()
        if len(hijos) > 40:
            self.tabla_eventos.delete(hijos[-1])

    def al_redimensionar(self, event):
        # Filtrar solo eventos de la ventana raíz para evitar cascada de hijos
        if event.widget == self.root:
            pass  # El evento se puede monitorear si se desea

    def limpiar_registro(self):
        for item in self.tabla_eventos.get_children():
            self.tabla_eventos.delete(item)
        self.contador_eventos = 0


if __name__ == "__main__":
    app_root = tk.Tk()
    app = InspectorEventosApp(app_root)
    app_root.mainloop()
