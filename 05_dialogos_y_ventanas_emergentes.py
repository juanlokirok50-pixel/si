"""
=============================================================================
05_dialogos_y_ventanas_emergentes.py
=============================================================================
Manejo de diálogos estándar del sistema y ventanas secundarias:
- messagebox: Alertas informativas, advertencias, errores y confirmaciones.
- filedialog: Diálogos de apertura y guardado de archivos y carpetas.
- colorchooser: Selector de color interactivo RGB/Hexadecimal.
- Toplevel: Creación de ventanas secundarias modales (grab_set) y no modales.
=============================================================================
"""

import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser


class DialogosApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("05 - Diálogos del Sistema y Ventanas Toplevel")
        self.root.geometry("720x580")
        self.root.minsize(650, 500)
        self.root.configure(bg="#f8fafc")

        self.color_seleccionado = "#3b82f6"

        self.crear_interfaz()

    def crear_interfaz(self):
        # Título
        tk.Label(
            self.root,
            text="Diálogos Nativos y Gestión de Ventanas Secundarias",
            font=("Segoe UI", 13, "bold"),
            bg="#1e293b",
            fg="white",
            pady=12
        ).pack(fill="x")

        contenedor = tk.Frame(self.root, bg="#f8fafc", padx=20, pady=15)
        contenedor.pack(fill="both", expand=True)

        # -------------------------------------------------------------------
        # 1. Sección: Messagebox
        # -------------------------------------------------------------------
        sec_msg = tk.LabelFrame(contenedor, text=" Cuadros de Mensaje (tkinter.messagebox) ", bg="#ffffff", padx=15, pady=10)
        sec_msg.pack(fill="x", pady=(0, 12))

        frame_btn_msg = tk.Frame(sec_msg, bg="#ffffff")
        frame_btn_msg.pack(fill="x")

        tk.Button(frame_btn_msg, text="ℹ️ Info", command=self.mostrar_info, bg="#e2e8f0", relief="flat", padx=10, pady=4).pack(side="left", padx=4)
        tk.Button(frame_btn_msg, text="⚠️ Advertencia", command=self.mostrar_warning, bg="#fef3c7", relief="flat", padx=10, pady=4).pack(side="left", padx=4)
        tk.Button(frame_btn_msg, text="❌ Error", command=self.mostrar_error, bg="#fee2e2", relief="flat", padx=10, pady=4).pack(side="left", padx=4)
        tk.Button(frame_btn_msg, text="❓ Pregunta (Sí/No)", command=self.mostrar_pregunta, bg="#dbeafe", relief="flat", padx=10, pady=4).pack(side="left", padx=4)

        # -------------------------------------------------------------------
        # 2. Sección: FileDialog
        # -------------------------------------------------------------------
        sec_file = tk.LabelFrame(contenedor, text=" Explorador de Archivos (tkinter.filedialog) ", bg="#ffffff", padx=15, pady=10)
        sec_file.pack(fill="x", pady=(0, 12))

        frame_btn_file = tk.Frame(sec_file, bg="#ffffff")
        frame_btn_file.pack(fill="x", pady=(0, 8))

        tk.Button(frame_btn_file, text="📂 Abrir Archivo", command=self.abrir_archivo, bg="#2563eb", fg="white", relief="flat", padx=10, pady=4).pack(side="left", padx=4)
        tk.Button(frame_btn_file, text="💾 Guardar Como...", command=self.guardar_archivo, bg="#10b981", fg="white", relief="flat", padx=10, pady=4).pack(side="left", padx=4)
        tk.Button(frame_btn_file, text="📁 Seleccionar Carpeta", command=self.seleccionar_carpeta, bg="#f59e0b", fg="white", relief="flat", padx=10, pady=4).pack(side="left", padx=4)

        self.lbl_ruta_archivo = tk.Label(sec_file, text="Ruta seleccionada: (ninguna)", font=("Consolas", 9), bg="#f1f5f9", anchor="w", padx=8, pady=5)
        self.lbl_ruta_archivo.pack(fill="x")

        # -------------------------------------------------------------------
        # 3. Sección: ColorChooser
        # -------------------------------------------------------------------
        sec_color = tk.LabelFrame(contenedor, text=" Selector de Color (tkinter.colorchooser) ", bg="#ffffff", padx=15, pady=10)
        sec_color.pack(fill="x", pady=(0, 12))

        frame_color_ctrl = tk.Frame(sec_color, bg="#ffffff")
        frame_color_ctrl.pack(fill="x")

        tk.Button(frame_color_ctrl, text="🎨 Elegir Color", command=self.elegir_color, bg="#6366f1", fg="white", relief="flat", padx=10, pady=4).pack(side="left", padx=(0, 10))

        self.muestra_color = tk.Label(
            frame_color_ctrl,
            text=f"Color actual: {self.color_seleccionado}",
            bg=self.color_seleccionado,
            fg="white",
            font=("Segoe UI", 9, "bold"),
            padx=15,
            pady=5
        )
        self.muestra_color.pack(side="left")

        # -------------------------------------------------------------------
        # 4. Sección: Ventanas Secundarias (Toplevel)
        # -------------------------------------------------------------------
        sec_top = tk.LabelFrame(contenedor, text=" Ventanas Secundarias (Toplevel) ", bg="#ffffff", padx=15, pady=10)
        sec_top.pack(fill="x")

        tk.Label(
            sec_top,
            text="Toplevel permite crear ventanas hijas independientes. Con grab_set() se convierten en modales.",
            bg="#ffffff",
            font=("Segoe UI", 9)
        ).pack(anchor="w", pady=(0, 8))

        frame_btn_top = tk.Frame(sec_top, bg="#ffffff")
        frame_btn_top.pack(fill="x")

        tk.Button(frame_btn_top, text="🪟 Ventana Estándar", command=self.abrir_ventana_estandar, bg="#e2e8f0", relief="flat", padx=10, pady=4).pack(side="left", padx=4)
        tk.Button(frame_btn_top, text="🔒 Ventana Modal (Bloquea la principal)", command=self.abrir_ventana_modal, bg="#334155", fg="white", relief="flat", padx=10, pady=4).pack(side="left", padx=4)

    # --- Métodos de Messagebox ---
    def mostrar_info(self):
        messagebox.showinfo("Información", "Esta es una notificación informativa estándar.")

    def mostrar_warning(self):
        messagebox.showwarning("Advertencia", "¡Cuidado! Este recurso podría tener restricciones de acceso.")

    def mostrar_error(self):
        messagebox.showerror("Error Crítico", "No se pudo conectar a la base de datos simulada.")

    def mostrar_pregunta(self):
        respuesta = messagebox.askyesno("Confirmación", "¿Deseas aplicar los cambios ahora?")
        if respuesta:
            messagebox.showinfo("Resultado", "Seleccionaste: SÍ")
        else:
            messagebox.showinfo("Resultado", "Seleccionaste: NO")

    # --- Métodos de FileDialog ---
    def abrir_archivo(self):
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo",
            filetypes=[("Archivos de Texto", "*.txt;*.md"), ("Archivos Python", "*.py"), ("Todos los archivos", "*.*")]
        )
        if ruta:
            self.lbl_ruta_archivo.config(text=f"Archivo abierto: {ruta}")

    def guardar_archivo(self):
        ruta = filedialog.asksaveasfilename(
            title="Guardar archivo como",
            defaultextension=".txt",
            filetypes=[("Documento de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if ruta:
            self.lbl_ruta_archivo.config(text=f"Guardar en: {ruta}")

    def seleccionar_carpeta(self):
        carpeta = filedialog.askdirectory(title="Seleccionar directorio de trabajo")
        if carpeta:
            self.lbl_ruta_archivo.config(text=f"Carpeta: {carpeta}")

    # --- Métodos de ColorChooser ---
    def elegir_color(self):
        # askcolor() retorna una tupla: ((r, g, b), "#hex")
        color = colorchooser.askcolor(title="Selecciona un color", initialcolor=self.color_seleccionado)
        if color[1]:
            self.color_seleccionado = color[1]
            self.muestra_color.config(
                bg=self.color_seleccionado,
                text=f"Color actual: {self.color_seleccionado}"
            )

    # --- Métodos de Toplevel ---
    def abrir_ventana_estandar(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Ventana Secundaria Estándar")
        ventana.geometry("360x200")
        tk.Label(
            ventana,
            text="Esta es una ventana no-modal.\nPuedes seguir interactuando con la ventana principal.",
            font=("Segoe UI", 10),
            padx=20,
            pady=30
        ).pack()
        tk.Button(ventana, text="Cerrar", command=ventana.destroy, padx=15, pady=4).pack()

    def abrir_ventana_modal(self):
        modal = tk.Toplevel(self.root)
        modal.title("Ventana Modal")
        modal.geometry("380x240")
        modal.transient(self.root)  # Mantener siempre encima de la ventana padre
        modal.grab_set()            # Captura todos los eventos: bloquea la ventana padre

        tk.Label(
            modal,
            text="⚠️ Ventana Modal Activa\n\nNo podrás interactuar con la ventana principal\nhasta que cierres esta ventana.",
            font=("Segoe UI", 10, "bold"),
            fg="#991b1b",
            padx=20,
            pady=20
        ).pack()

        tk.Button(
            modal,
            text="Entendido y Cerrar",
            command=modal.destroy,
            bg="#2563eb",
            fg="white",
            padx=15,
            pady=6,
            relief="flat"
        ).pack()


if __name__ == "__main__":
    app_root = tk.Tk()
    app = DialogosApp(app_root)
    app_root.mainloop()
