"""
=============================================================================
06_menus_y_barras_de_herramientas.py
=============================================================================
Implementación de un mini editor de texto que demuestra:
- Barra de menú principal con menús desplegables (Menu, add_cascade).
- Submenús, separadores, opciones con casillas de verificación (add_checkbutton).
- Menú contextual (clic derecho) posicionado con .post().
- Barra de herramientas superior (Toolbar) para acciones rápidas.
- Barra de estado inferior (Status bar) actualizada dinámicamente.
- Atajos de teclado vinculados globalmente (Ctrl+N, Ctrl+O, Ctrl+S, etc.).
=============================================================================
"""

import tkinter as tk
from tkinter import messagebox, filedialog


class EditorConMenusApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("06 - Menús, Barras de Herramientas y Atajos")
        self.root.geometry("780x560")
        self.root.minsize(600, 400)

        # Variables de configuración de la vista
        self.var_ajuste_linea = tk.BooleanVar(value=True)
        self.var_mostrar_barra_estado = tk.BooleanVar(value=True)

        self.crear_barra_menu()
        self.crear_barra_herramientas()
        self.crear_area_edicion()
        self.crear_menu_contextual()
        self.crear_barra_estado()
        self.configurar_atajos()

    # -----------------------------------------------------------------------
    # 1. Barra de Menú Principal
    # -----------------------------------------------------------------------
    def crear_barra_menu(self):
        barra_menu = tk.Menu(self.root)

        # --- Menú Archivo ---
        menu_archivo = tk.Menu(barra_menu, tearoff=False)
        menu_archivo.add_command(label="Nuevo", accelerator="Ctrl+N", command=self.archivo_nuevo)
        menu_archivo.add_command(label="Abrir...", accelerator="Ctrl+O", command=self.archivo_abrir)
        menu_archivo.add_command(label="Guardar", accelerator="Ctrl+S", command=self.archivo_guardar)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", accelerator="Ctrl+Q", command=self.root.quit)
        barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

        # --- Menú Editar ---
        menu_editar = tk.Menu(barra_menu, tearoff=False)
        menu_editar.add_command(label="Deshacer", accelerator="Ctrl+Z", command=lambda: self.texto.event_generate("<<Undo>>"))
        menu_editar.add_command(label="Rehacer", accelerator="Ctrl+Y", command=lambda: self.texto.event_generate("<<Redo>>"))
        menu_editar.add_separator()
        menu_editar.add_command(label="Cortar", accelerator="Ctrl+X", command=lambda: self.texto.event_generate("<<Cut>>"))
        menu_editar.add_command(label="Copiar", accelerator="Ctrl+C", command=lambda: self.texto.event_generate("<<Copy>>"))
        menu_editar.add_command(label="Pegar", accelerator="Ctrl+V", command=lambda: self.texto.event_generate("<<Paste>>"))
        menu_editar.add_command(label="Seleccionar Todo", accelerator="Ctrl+A", command=self.seleccionar_todo)
        barra_menu.add_cascade(label="Editar", menu=menu_editar)

        # --- Menú Ver ---
        menu_ver = tk.Menu(barra_menu, tearoff=False)
        menu_ver.add_checkbutton(
            label="Ajuste de línea (Word Wrap)",
            variable=self.var_ajuste_linea,
            command=self.alternar_ajuste_linea
        )
        menu_ver.add_checkbutton(
            label="Mostrar barra de estado",
            variable=self.var_mostrar_barra_estado,
            command=self.alternar_barra_estado
        )
        barra_menu.add_cascade(label="Ver", menu=menu_ver)

        # --- Menú Ayuda ---
        menu_ayuda = tk.Menu(barra_menu, tearoff=False)
        menu_ayuda.add_command(label="Acerca de...", command=self.mostrar_acerca_de)
        barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

        # Asignar menú a la ventana
        self.root.config(menu=barra_menu)

    # -----------------------------------------------------------------------
    # 2. Barra de Herramientas Superior (Toolbar)
    # -----------------------------------------------------------------------
    def crear_barra_herramientas(self):
        self.toolbar = tk.Frame(self.root, bg="#f1f5f9", bd=1, relief="raised")
        self.toolbar.pack(side="top", fill="x")

        botones = [
            ("📄 Nuevo", self.archivo_nuevo),
            ("📂 Abrir", self.archivo_abrir),
            ("💾 Guardar", self.archivo_guardar),
            ("|", None),
            ("✂️ Cortar", lambda: self.texto.event_generate("<<Cut>>")),
            ("📋 Copiar", lambda: self.texto.event_generate("<<Copy>>")),
            ("📥 Pegar", lambda: self.texto.event_generate("<<Paste>>")),
            ("|", None),
            ("🧹 Limpiar", self.archivo_nuevo)
        ]

        for texto, comando in botones:
            if texto == "|":
                tk.Label(self.toolbar, text="|", bg="#f1f5f9", fg="#94a3b8").pack(side="left", padx=5)
            else:
                btn = tk.Button(
                    self.toolbar,
                    text=texto,
                    command=comando,
                    bg="#f1f5f9",
                    relief="flat",
                    font=("Segoe UI", 8),
                    padx=6,
                    pady=2,
                    cursor="hand2"
                )
                btn.pack(side="left", padx=2, pady=2)

    # -----------------------------------------------------------------------
    # 3. Área de Edición de Texto
    # -----------------------------------------------------------------------
    def crear_area_edicion(self):
        frame_editor = tk.Frame(self.root)
        frame_editor.pack(fill="both", expand=True)

        scroll_y = tk.Scrollbar(frame_editor)
        scroll_y.pack(side="right", fill="y")

        self.texto = tk.Text(
            frame_editor,
            wrap="word",
            undo=True,
            font=("Consolas", 11),
            yscrollcommand=scroll_y.set,
            padx=10,
            pady=10
        )
        self.texto.pack(side="left", fill="both", expand=True)
        scroll_y.config(command=self.texto.yview)

        # Insertar texto de bienvenida
        mensaje_inicial = (
            "# Demostración de Menús y Atajos en Tkinter\n\n"
            "1. Prueba el menú superior desplegable.\n"
            "2. Haz clic derecho sobre este texto para ver el menú contextual.\n"
            "3. Utiliza los botones de la barra de herramientas superior.\n"
            "4. Prueba los atajos de teclado como Ctrl+N, Ctrl+O o Ctrl+S.\n"
            "5. Observa el contador dinámico de palabras y caracteres en la barra de estado inferior.\n"
        )
        self.texto.insert("1.0", mensaje_inicial)

        # Rastrear cambios para actualizar barra de estado
        self.texto.bind("<<Modified>>", self.al_modificar_texto)
        self.texto.bind("<KeyRelease>", lambda e: self.actualizar_contador())

    # -----------------------------------------------------------------------
    # 4. Menú Contextual (Clic Derecho)
    # -----------------------------------------------------------------------
    def crear_menu_contextual(self):
        self.menu_contextual = tk.Menu(self.root, tearoff=False)
        self.menu_contextual.add_command(label="Cortar", command=lambda: self.texto.event_generate("<<Cut>>"))
        self.menu_contextual.add_command(label="Copiar", command=lambda: self.texto.event_generate("<<Copy>>"))
        self.menu_contextual.add_command(label="Pegar", command=lambda: self.texto.event_generate("<<Paste>>"))
        self.menu_contextual.add_separator()
        self.menu_contextual.add_command(label="Seleccionar Todo", command=self.seleccionar_todo)

        # Enlazar clic derecho (<Button-3> en Windows/Linux, <Button-2> o <Button-3> en macOS)
        self.texto.bind("<Button-3>", self.mostrar_menu_contextual)

    def mostrar_menu_contextual(self, event):
        self.menu_contextual.post(event.x_root, event.y_root)

    # -----------------------------------------------------------------------
    # 5. Barra de Estado Inferior
    # -----------------------------------------------------------------------
    def crear_barra_estado(self):
        self.barra_estado = tk.Label(
            self.root,
            text="Listo | Caracteres: 0 | Palabras: 0",
            bd=1,
            relief="sunken",
            anchor="w",
            font=("Segoe UI", 9),
            bg="#e2e8f0",
            fg="#334155",
            padx=8,
            pady=3
        )
        self.barra_estado.pack(side="bottom", fill="x")
        self.actualizar_contador()

    # -----------------------------------------------------------------------
    # 6. Atajos de Teclado
    # -----------------------------------------------------------------------
    def configurar_atajos(self):
        self.root.bind_all("<Control-n>", lambda event: self.archivo_nuevo())
        self.root.bind_all("<Control-o>", lambda event: self.archivo_abrir())
        self.root.bind_all("<Control-s>", lambda event: self.archivo_guardar())
        self.root.bind_all("<Control-q>", lambda event: self.root.quit())

    # --- Acciones y Callbacks ---
    def archivo_nuevo(self):
        self.texto.delete("1.0", tk.END)
        self.actualizar_contador()

    def archivo_abrir(self):
        ruta = filedialog.askopenfilename(filetypes=[("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*")])
        if ruta:
            with open(ruta, "r", encoding="utf-8") as f:
                contenido = f.read()
            self.texto.delete("1.0", tk.END)
            self.texto.insert("1.0", contenido)
            self.actualizar_contador()

    def archivo_guardar(self):
        ruta = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de Texto", "*.txt")])
        if ruta:
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(self.texto.get("1.0", tk.END))
            messagebox.showinfo("Guardado", "Archivo guardado exitosamente.")

    def seleccionar_todo(self):
        self.texto.tag_add("sel", "1.0", "end")

    def alternar_ajuste_linea(self):
        modo = "word" if self.var_ajuste_linea.get() else "none"
        self.texto.config(wrap=modo)

    def alternar_barra_estado(self):
        if self.var_mostrar_barra_estado.get():
            self.barra_estado.pack(side="bottom", fill="x")
        else:
            self.barra_estado.pack_forget()

    def al_modificar_texto(self, event=None):
        if self.texto.edit_modified():
            self.actualizar_contador()
            self.texto.edit_modified(False)

    def actualizar_contador(self):
        contenido = self.texto.get("1.0", "end-1c")
        num_caracteres = len(contenido)
        num_palabras = len(contenido.split())
        self.barra_estado.config(
            text=f"Listo | Caracteres: {num_caracteres} | Palabras: {num_palabras}"
        )

    def mostrar_acerca_de(self):
        messagebox.showinfo(
            "Acerca de",
            "Demostración de Menús, Barras de Herramientas y Atajos de Teclado en Tkinter.\nConstruido con Python."
        )


if __name__ == "__main__":
    app_root = tk.Tk()
    app = EditorConMenusApp(app_root)
    app_root.mainloop()
