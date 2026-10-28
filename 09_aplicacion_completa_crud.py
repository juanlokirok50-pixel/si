"""
=============================================================================
09_aplicacion_completa_crud.py
=============================================================================
Proyecto Integral: Gestor de Tareas y Proyectos (CRUD Completo)
Integra todos los conocimientos adquiridos en los módulos anteriores:
- Arquitectura Orientada a Objetos (POO) limpia y modular.
- Operaciones CRUD: Crear, Leer, Actualizar y Eliminar tareas.
- Persistencia de datos en disco local (formato JSON).
- Interfaz moderna con ttk.Treeview, ttk.Notebook, ttk.Combobox y ttk.Style.
- Filtrado por categorías, búsqueda en tiempo real y métricas estadísticas.
- Validación de datos y cuadros de diálogo de confirmación.
=============================================================================
"""

import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime


ARCHIVO_DATOS = "tareas.json"


class GestorTareasApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("TaskMaster - Gestor de Tareas (Tkinter CRUD)")
        self.root.geometry("940x640")
        self.root.minsize(860, 560)
        self.root.configure(bg="#f8fafc")

        # Lista de tareas en memoria
        self.tareas = []
        self.id_tarea_en_edicion = None

        # Configurar estilos ttk
        self.configurar_estilos()

        # Construir UI
        self.crear_interfaz()

        # Cargar datos persistidos
        self.cargar_datos()
        self.actualizar_vista_tabla()
        self.actualizar_estadisticas()

    def configurar_estilos(self):
        style = ttk.Style()
        if "clam" in style.theme_names():
            style.theme_use("clam")

        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), background="#e2e8f0")
        style.configure("Treeview", font=("Segoe UI", 9), rowheight=26)
        style.map("Treeview", background=[("selected", "#2563eb")], foreground=[("selected", "#ffffff")])

    def crear_interfaz(self):
        # -------------------------------------------------------------------
        # Encabezado Principal
        # -------------------------------------------------------------------
        frame_header = tk.Frame(self.root, bg="#1e293b", padx=20, pady=12)
        frame_header.pack(fill="x")

        tk.Label(
            frame_header,
            text="📋 TaskMaster Desktop",
            font=("Segoe UI", 15, "bold"),
            fg="#ffffff",
            bg="#1e293b"
        ).pack(side="left")

        self.lbl_metricas = tk.Label(
            frame_header,
            text="Total: 0 | Pendientes: 0 | Completadas: 0",
            font=("Segoe UI", 9),
            fg="#94a3b8",
            bg="#1e293b"
        )
        self.lbl_metricas.pack(side="right")

        # -------------------------------------------------------------------
        # Contenedor Principal (2 Columnas: Formulario a la izq, Tabla a la der)
        # -------------------------------------------------------------------
        cuerpo = tk.Frame(self.root, bg="#f8fafc", padx=15, pady=15)
        cuerpo.pack(fill="both", expand=True)

        # Panel Izquierdo: Formulario
        frame_form = tk.LabelFrame(cuerpo, text=" Registro / Edición de Tarea ", bg="#ffffff", font=("Segoe UI", 10, "bold"), padx=15, pady=12)
        frame_form.pack(side="left", fill="y", padx=(0, 15))
        frame_form.config(width=320)

        # Campos del formulario
        tk.Label(frame_form, text="Título de la tarea (*):", bg="#ffffff", font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(5, 2))
        self.entry_titulo = ttk.Entry(frame_form, width=32, font=("Segoe UI", 9))
        self.entry_titulo.pack(fill="x", pady=(0, 10))

        tk.Label(frame_form, text="Categoría:", bg="#ffffff", font=("Segoe UI", 9)).pack(anchor="w", pady=(2, 2))
        self.combo_categoria = ttk.Combobox(
            frame_form,
            values=["Desarrollo", "Diseño", "Estudio", "Personal", "Finanzas", "Otros"],
            state="readonly"
        )
        self.combo_categoria.current(0)
        self.combo_categoria.pack(fill="x", pady=(0, 10))

        tk.Label(frame_form, text="Prioridad:", bg="#ffffff", font=("Segoe UI", 9)).pack(anchor="w", pady=(2, 2))
        self.combo_prioridad = ttk.Combobox(
            frame_form,
            values=["Baja", "Media", "Alta", "Urgente"],
            state="readonly"
        )
        self.combo_prioridad.current(1)
        self.combo_prioridad.pack(fill="x", pady=(0, 10))

        tk.Label(frame_form, text="Fecha Límite (YYYY-MM-DD):", bg="#ffffff", font=("Segoe UI", 9)).pack(anchor="w", pady=(2, 2))
        self.entry_fecha = ttk.Entry(frame_form, font=("Segoe UI", 9))
        self.entry_fecha.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.entry_fecha.pack(fill="x", pady=(0, 10))

        tk.Label(frame_form, text="Descripción o Notas:", bg="#ffffff", font=("Segoe UI", 9)).pack(anchor="w", pady=(2, 2))
        self.txt_descripcion = tk.Text(frame_form, height=4, font=("Segoe UI", 9), bd=1, relief="solid")
        self.txt_descripcion.pack(fill="x", pady=(0, 15))

        # Botones de Acción del Formulario
        self.btn_guardar = tk.Button(
            frame_form,
            text="💾 Guardar Tarea",
            command=self.guardar_tarea,
            bg="#2563eb",
            fg="white",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            pady=6,
            cursor="hand2"
        )
        self.btn_guardar.pack(fill="x", pady=(0, 6))

        self.btn_cancelar_edicion = tk.Button(
            frame_form,
            text="Cancelar Edición",
            command=self.limpiar_formulario,
            bg="#e2e8f0",
            relief="flat",
            pady=4,
            cursor="hand2"
        )
        self.btn_cancelar_edicion.pack(fill="x")
        self.btn_cancelar_edicion.pack_forget()  # Oculto al inicio

        # Panel Derecho: Filtros y Tabla de Tareas
        frame_tabla_contenedor = tk.Frame(cuerpo, bg="#f8fafc")
        frame_tabla_contenedor.pack(side="right", fill="both", expand=True)

        # Barra de Filtros y Búsqueda
        frame_filtros = tk.Frame(frame_tabla_contenedor, bg="#f8fafc")
        frame_filtros.pack(fill="x", pady=(0, 10))

        tk.Label(frame_filtros, text="Buscar:", bg="#f8fafc", font=("Segoe UI", 9, "bold")).pack(side="left", padx=(0, 5))
        self.entry_buscar = ttk.Entry(frame_filtros, width=20)
        self.entry_buscar.pack(side="left", padx=(0, 15))
        self.entry_buscar.bind("<KeyRelease>", lambda e: self.actualizar_vista_tabla())

        tk.Label(frame_filtros, text="Filtrar Estado:", bg="#f8fafc", font=("Segoe UI", 9)).pack(side="left", padx=(0, 5))
        self.combo_filtro_estado = ttk.Combobox(
            frame_filtros,
            values=["Todos", "Pendientes", "Completadas"],
            state="readonly",
            width=14
        )
        self.combo_filtro_estado.current(0)
        self.combo_filtro_estado.pack(side="left", padx=(0, 10))
        self.combo_filtro_estado.bind("<<ComboboxSelected>>", lambda e: self.actualizar_vista_tabla())

        # Tabla (Treeview)
        frame_tv = ttk.Frame(frame_tabla_contenedor)
        frame_tv.pack(fill="both", expand=True)

        scroll_y = ttk.Scrollbar(frame_tv, orient="vertical")
        scroll_y.pack(side="right", fill="y")

        columnas = ("id", "estado", "titulo", "categoria", "prioridad", "fecha")
        self.tree = ttk.Treeview(
            frame_tv,
            columns=columnas,
            show="headings",
            selectmode="browse",
            yscrollcommand=scroll_y.set
        )
        scroll_y.config(command=self.tree.yview)
        self.tree.pack(fill="both", expand=True)

        config_cols = {
            "id": ("ID", 40, "center"),
            "estado": ("Estado", 100, "center"),
            "titulo": ("Título", 220, "w"),
            "categoria": ("Categoría", 100, "center"),
            "prioridad": ("Prioridad", 80, "center"),
            "fecha": ("Vencimiento", 100, "center")
        }
        for col, (nom, ancho, align) in config_cols.items():
            self.tree.heading(col, text=nom)
            self.tree.column(col, width=ancho, anchor=align)

        # Vincular doble clic para editar rápidamente
        self.tree.bind("<Double-1>", lambda e: self.editar_tarea())

        # Barra de Botones Inferiores de la Tabla
        frame_acciones_tabla = tk.Frame(frame_tabla_contenedor, bg="#f8fafc", pady=8)
        frame_acciones_tabla.pack(fill="x")

        tk.Button(frame_acciones_tabla, text="✔️ Alternar Estado (Completar)", command=self.alternar_estado_tarea, bg="#10b981", fg="white", relief="flat", padx=10, pady=4).pack(side="left", padx=3)
        tk.Button(frame_acciones_tabla, text="✏️ Editar Tarea", command=self.editar_tarea, bg="#f59e0b", fg="white", relief="flat", padx=10, pady=4).pack(side="left", padx=3)
        tk.Button(frame_acciones_tabla, text="🗑️ Eliminar", command=self.eliminar_tarea, bg="#ef4444", fg="white", relief="flat", padx=10, pady=4).pack(side="left", padx=3)

    # -----------------------------------------------------------------------
    # Lógica CRUD y Persistencia
    # -----------------------------------------------------------------------
    def cargar_datos(self):
        if os.path.exists(ARCHIVO_DATOS):
            try:
                with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
                    self.tareas = json.load(f)
            except Exception as e:
                messagebox.showerror("Error al cargar", f"No se pudieron leer los datos guardados: {e}")
                self.tareas = []
        else:
            # Tareas demostrativas por defecto
            self.tareas = [
                {
                    "id": 1,
                    "titulo": "Aprender widgets básicos de Tkinter",
                    "categoria": "Desarrollo",
                    "prioridad": "Alta",
                    "fecha": datetime.now().strftime("%Y-%m-%d"),
                    "descripcion": "Estudiar Button, Label, Entry y Frame.",
                    "completada": True
                },
                {
                    "id": 2,
                    "titulo": "Diseñar interfaz responsiva con Grid",
                    "categoria": "Diseño",
                    "prioridad": "Media",
                    "fecha": datetime.now().strftime("%Y-%m-%d"),
                    "descripcion": "Configurar pesos con columnconfigure y rowconfigure.",
                    "completada": False
                },
                {
                    "id": 3,
                    "titulo": "Subir repositorio completo a GitHub",
                    "categoria": "Desarrollo",
                    "prioridad": "Urgente",
                    "fecha": datetime.now().strftime("%Y-%m-%d"),
                    "descripcion": "Incluir README detallado y ejemplos funcionales.",
                    "completada": False
                }
            ]
            self.guardar_datos_en_disco()

    def guardar_datos_en_disco(self):
        try:
            with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
                json.dump(self.tareas, f, indent=4, ensure_ascii=False)
        except Exception as e:
            messagebox.showerror("Error de guardado", f"No se pudo escribir en el disco: {e}")

    def guardar_tarea(self):
        titulo = self.entry_titulo.get().strip()
        if not titulo:
            messagebox.showwarning("Dato requerido", "El título de la tarea no puede estar vacío.")
            self.entry_titulo.focus()
            return

        categoria = self.combo_categoria.get()
        prioridad = self.combo_prioridad.get()
        fecha = self.entry_fecha.get().strip()
        descripcion = self.txt_descripcion.get("1.0", "end-1c").strip()

        if self.id_tarea_en_edicion is None:
            # Crear nueva tarea
            nuevo_id = max([t["id"] for t in self.tareas], default=0) + 1
            nueva_tarea = {
                "id": nuevo_id,
                "titulo": titulo,
                "categoria": categoria,
                "prioridad": prioridad,
                "fecha": fecha,
                "descripcion": descripcion,
                "completada": False
            }
            self.tareas.append(nueva_tarea)
            messagebox.showinfo("Éxito", f"Tarea '{titulo}' creada con éxito.")
        else:
            # Actualizar tarea existente
            for t in self.tareas:
                if t["id"] == self.id_tarea_en_edicion:
                    t["titulo"] = titulo
                    t["categoria"] = categoria
                    t["prioridad"] = prioridad
                    t["fecha"] = fecha
                    t["descripcion"] = descripcion
                    break
            messagebox.showinfo("Éxito", "Tarea actualizada correctamente.")

        self.guardar_datos_en_disco()
        self.limpiar_formulario()
        self.actualizar_vista_tabla()
        self.actualizar_estadisticas()

    def alternar_estado_tarea(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Selección", "Por favor selecciona una tarea de la lista.")
            return

        id_tarea = int(self.tree.item(seleccion[0])["values"][0])
        for t in self.tareas:
            if t["id"] == id_tarea:
                t["completada"] = not t["completada"]
                break

        self.guardar_datos_en_disco()
        self.actualizar_vista_tabla()
        self.actualizar_estadisticas()

    def editar_tarea(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Selección", "Selecciona una tarea para editar.")
            return

        id_tarea = int(self.tree.item(seleccion[0])["values"][0])
        tarea = next((t for t in self.tareas if t["id"] == id_tarea), None)
        if not tarea:
            return

        # Cargar datos en el formulario
        self.id_tarea_en_edicion = tarea["id"]
        self.entry_titulo.delete(0, tk.END)
        self.entry_titulo.insert(0, tarea["titulo"])

        self.combo_categoria.set(tarea["categoria"])
        self.combo_prioridad.set(tarea["prioridad"])

        self.entry_fecha.delete(0, tk.END)
        self.entry_fecha.insert(0, tarea["fecha"])

        self.txt_descripcion.delete("1.0", tk.END)
        self.txt_descripcion.insert("1.0", tarea.get("descripcion", ""))

        self.btn_guardar.config(text="🔄 Actualizar Tarea", bg="#f59e0b")
        self.btn_cancelar_edicion.pack(fill="x")

    def eliminar_tarea(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Selección", "Selecciona la tarea que deseas eliminar.")
            return

        id_tarea = int(self.tree.item(seleccion[0])["values"][0])
        titulo_tarea = self.tree.item(seleccion[0])["values"][2]

        confirmacion = messagebox.askyesno(
            "Confirmar Eliminación",
            f"¿Estás seguro de que deseas eliminar permanentemente la tarea:\n'{titulo_tarea}'?"
        )
        if confirmacion:
            self.tareas = [t for t in self.tareas if t["id"] != id_tarea]
            self.guardar_datos_en_disco()
            self.actualizar_vista_tabla()
            self.actualizar_estadisticas()
            if self.id_tarea_en_edicion == id_tarea:
                self.limpiar_formulario()

    def limpiar_formulario(self):
        self.id_tarea_en_edicion = None
        self.entry_titulo.delete(0, tk.END)
        self.combo_categoria.current(0)
        self.combo_prioridad.current(1)
        self.entry_fecha.delete(0, tk.END)
        self.entry_fecha.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.txt_descripcion.delete("1.0", tk.END)
        self.btn_guardar.config(text="💾 Guardar Tarea", bg="#2563eb")
        self.btn_cancelar_edicion.pack_forget()

    def actualizar_vista_tabla(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        termino = self.entry_buscar.get().strip().lower()
        filtro_estado = self.combo_filtro_estado.get()

        for t in self.tareas:
            # Filtro por estado
            if filtro_estado == "Pendientes" and t["completada"]:
                continue
            if filtro_estado == "Completadas" and not t["completada"]:
                continue

            # Filtro por búsqueda de texto
            if termino and (termino not in t["titulo"].lower() and termino not in t.get("descripcion", "").lower()):
                continue

            estado_str = "✅ Completada" if t["completada"] else "⏳ Pendiente"
            self.tree.insert(
                "",
                "end",
                values=(t["id"], estado_str, t["titulo"], t["categoria"], t["prioridad"], t["fecha"])
            )

    def actualizar_estadisticas(self):
        total = len(self.tareas)
        completadas = sum(1 for t in self.tareas if t["completada"])
        pendientes = total - completadas
        porcentaje = (completadas / total * 100) if total > 0 else 0

        self.lbl_metricas.config(
            text=f"Total: {total} | Pendientes: {pendientes} | Completadas: {completadas} ({porcentaje:.0f}%)"
        )


if __name__ == "__main__":
    app_root = tk.Tk()
    app = GestorTareasApp(app_root)
    app_root.mainloop()
