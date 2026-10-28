"""
=============================================================================
03_widgets_interactivos.py
=============================================================================
Exploración de controles interactivos y Variables de Control de Tkinter:
- Checkbutton (casillas de verificación con BooleanVar)
- Radiobutton (opciones mutuamente excluyentes con StringVar)
- Scale / Slider (deslizador numérico continuo con DoubleVar)
- Spinbox (selector numérico con incrementos)
- Listbox con Scrollbar (lista de elementos con barra de desplazamiento)
- Variables de control y seguimiento reactivo de cambios con .trace_add()
=============================================================================
"""

import tkinter as tk
from tkinter import messagebox


class CatalogoWidgetsApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("03 - Widgets Interactivos y Variables de Control")
        self.root.geometry("760x600")
        self.root.minsize(700, 550)
        self.root.configure(bg="#f1f5f9")

        # -------------------------------------------------------------------
        # 1. Variables de Control de Tkinter
        # Permiten sincronizar automáticamente la vista (GUI) con el modelo de datos.
        # -------------------------------------------------------------------
        self.var_notificaciones = tk.BooleanVar(value=True)
        self.var_modo_oscuro = tk.BooleanVar(value=False)
        self.var_plan = tk.StringVar(value="Pro")
        self.var_volumen = tk.DoubleVar(value=65.0)
        self.var_cantidad = tk.IntVar(value=1)

        # Vincular trazador de cambios (trace_add) para actualizar el resumen en vivo
        for var in [self.var_notificaciones, self.var_modo_oscuro, self.var_plan, self.var_volumen, self.var_cantidad]:
            var.trace_add("write", lambda *args: self.actualizar_resumen())

        self.crear_interfaz()
        self.actualizar_resumen()

    def crear_interfaz(self):
        # Título superior
        tk.Label(
            self.root,
            text="Widgets Interactivos y Enlace de Datos Reactivo",
            font=("Segoe UI", 14, "bold"),
            bg="#0f172a",
            fg="#f8fafc",
            pady=12
        ).pack(fill="x")

        # Contenedor dividido en dos columnas: izquierda (controles), derecha (listbox y resumen)
        cuerpo = tk.Frame(self.root, bg="#f1f5f9", padx=15, pady=15)
        cuerpo.pack(fill="both", expand=True)

        col_izquierda = tk.Frame(cuerpo, bg="#f1f5f9")
        col_izquierda.pack(side="left", fill="both", expand=True, padx=(0, 10))

        col_derecha = tk.Frame(cuerpo, bg="#f1f5f9")
        col_derecha.pack(side="right", fill="both", expand=True, padx=(10, 0))

        # --- SECCIÓN: Checkbuttons ---
        sec_check = tk.LabelFrame(col_izquierda, text=" Checkbuttons (Casillas) ", bg="#ffffff", padx=10, pady=8)
        sec_check.pack(fill="x", pady=(0, 10))

        tk.Checkbutton(
            sec_check,
            text="Recibir notificaciones por correo",
            variable=self.var_notificaciones,
            bg="#ffffff",
            activebackground="#ffffff",
            font=("Segoe UI", 9)
        ).pack(anchor="w")

        tk.Checkbutton(
            sec_check,
            text="Modo oscuro (Vista previa)",
            variable=self.var_modo_oscuro,
            bg="#ffffff",
            activebackground="#ffffff",
            font=("Segoe UI", 9)
        ).pack(anchor="w")

        # --- SECCIÓN: Radiobuttons ---
        sec_radio = tk.LabelFrame(col_izquierda, text=" Radiobuttons (Planes de Suscripción) ", bg="#ffffff", padx=10, pady=8)
        sec_radio.pack(fill="x", pady=(0, 10))

        for plan in ["Gratuito", "Pro", "Empresarial"]:
            tk.Radiobutton(
                sec_radio,
                text=f"Plan {plan}",
                variable=self.var_plan,
                value=plan,
                bg="#ffffff",
                activebackground="#ffffff",
                font=("Segoe UI", 9)
            ).pack(anchor="w")

        # --- SECCIÓN: Scale & Spinbox ---
        sec_numericos = tk.LabelFrame(col_izquierda, text=" Scale (Deslizador) y Spinbox ", bg="#ffffff", padx=10, pady=8)
        sec_numericos.pack(fill="x")

        tk.Label(sec_numericos, text="Volumen del sistema:", bg="#ffffff", font=("Segoe UI", 9)).pack(anchor="w")
        self.scale_vol = tk.Scale(
            sec_numericos,
            from_=0,
            to=100,
            orient="horizontal",
            variable=self.var_volumen,
            bg="#ffffff",
            troughcolor="#e2e8f0",
            highlightthickness=0
        )
        self.scale_vol.pack(fill="x", pady=(0, 10))

        tk.Label(sec_numericos, text="Cantidad de licencias (Spinbox):", bg="#ffffff", font=("Segoe UI", 9)).pack(anchor="w")
        self.spin_cant = tk.Spinbox(
            sec_numericos,
            from_=1,
            to=50,
            textvariable=self.var_cantidad,
            font=("Segoe UI", 9),
            width=10
        )
        self.spin_cant.pack(anchor="w", pady=(2, 5))

        # --- SECCIÓN COLUMNA DERECHA: Listbox con Scrollbar ---
        sec_listbox = tk.LabelFrame(col_derecha, text=" Listbox con Scrollbar (Habilidades) ", bg="#ffffff", padx=10, pady=8)
        sec_listbox.pack(fill="both", expand=True, pady=(0, 10))

        # Marco para el Listbox y la barra de desplazamiento
        frame_lista = tk.Frame(sec_listbox, bg="#ffffff")
        frame_lista.pack(fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame_lista, orient="vertical")
        self.listbox = tk.Listbox(
            frame_lista,
            yscrollcommand=scrollbar.set,
            selectmode=tk.SINGLE,
            font=("Segoe UI", 9),
            bd=1,
            relief="solid"
        )
        scrollbar.config(command=self.listbox.yview)

        scrollbar.pack(side="right", fill="y")
        self.listbox.pack(side="left", fill="both", expand=True)

        # Poblar elementos iniciales
        habilidades = ["Python", "Tkinter", "SQLite", "Git & GitHub", "APIs REST", "Pandas", "Django", "FastAPI"]
        for item in habilidades:
            self.listbox.insert(tk.END, item)

        # Marco para agregar o remover elementos
        frame_acciones_lista = tk.Frame(sec_listbox, bg="#ffffff")
        frame_acciones_lista.pack(fill="x", pady=(6, 0))

        self.entry_nueva_hab = tk.Entry(frame_acciones_lista, font=("Segoe UI", 9))
        self.entry_nueva_hab.pack(side="left", fill="x", expand=True, padx=(0, 5))
        self.entry_nueva_hab.bind("<Return>", lambda e: self.agregar_habilidad())

        btn_agregar = tk.Button(frame_acciones_lista, text="+ Agregar", command=self.agregar_habilidad, bg="#2563eb", fg="white", relief="flat")
        btn_agregar.pack(side="left", padx=2)

        btn_eliminar = tk.Button(frame_acciones_lista, text="Eliminar", command=self.eliminar_habilidad, bg="#ef4444", fg="white", relief="flat")
        btn_eliminar.pack(side="left", padx=2)

        # --- SECCIÓN: Resumen en Tiempo Real ---
        sec_resumen = tk.LabelFrame(col_derecha, text=" Estado Reactivo en Tiempo Real ", bg="#ffffff", padx=10, pady=8)
        sec_resumen.pack(fill="x")

        self.lbl_resumen = tk.Label(
            sec_resumen,
            text="",
            bg="#ffffff",
            fg="#1e293b",
            font=("Consolas", 9),
            justify="left",
            anchor="w"
        )
        self.lbl_resumen.pack(fill="x")

    def agregar_habilidad(self):
        item = self.entry_nueva_hab.get().strip()
        if item:
            self.listbox.insert(tk.END, item)
            self.entry_nueva_hab.delete(0, tk.END)
        else:
            messagebox.showinfo("Atención", "Escribe el nombre de la habilidad.")

    def eliminar_habilidad(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            self.listbox.delete(seleccion[0])
        else:
            messagebox.showwarning("Selección vacía", "Selecciona una habilidad para eliminar.")

    def actualizar_resumen(self):
        """Se ejecuta automáticamente cada vez que una variable de control cambia."""
        texto = (
            f"Notificaciones : {'Activadas' if self.var_notificaciones.get() else 'Desactivadas'}\n"
            f"Modo Oscuro    : {'Sí' if self.var_modo_oscuro.get() else 'No'}\n"
            f"Plan           : {self.var_plan.get()}\n"
            f"Volumen        : {self.var_volumen.get():.1f}%\n"
            f"Licencias      : {self.var_cantidad.get()} unidad(es)"
        )
        self.lbl_resumen.config(text=texto)


if __name__ == "__main__":
    app_root = tk.Tk()
    app = CatalogoWidgetsApp(app_root)
    app_root.mainloop()
