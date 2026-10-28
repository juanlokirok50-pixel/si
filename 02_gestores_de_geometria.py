"""
=============================================================================
02_gestores_de_geometria.py
=============================================================================
Comparativa práctica de los 3 administradores de diseño de Tkinter:
1. pack()  - Apilamiento secuencial (arriba, abajo, izquierda, derecha).
2. grid()  - Cuadrícula matricial (filas y columnas responsivas).
3. place() - Posicionamiento absoluto y relativo por coordenadas (x, y).

Se utiliza un ttk.Notebook (pestañas) para alternar visualmente entre cada método.
=============================================================================
"""

import tkinter as tk
from tkinter import ttk


def construir_pestana_pack(parent):
    """Demuestra el comportamiento del gestor de empaquetado `pack`."""
    contenedor = tk.Frame(parent, bg="#f8fafc", padx=15, pady=15)

    info = tk.Label(
        contenedor,
        text="Gestor: pack()\nOrganiza widgets en bloques alrededor de los bordes del contenedor.\n"
             "Parámetros clave: side ('top', 'bottom', 'left', 'right'), fill ('x', 'y', 'both'), expand.",
        font=("Segoe UI", 9),
        bg="#f8fafc",
        fg="#334155",
        justify="left"
    )
    info.pack(fill="x", pady=(0, 10))

    # Marco superior (fill='x')
    tk.Label(
        contenedor, text="Encabezado: pack(side='top', fill='x')",
        bg="#3b82f6", fg="white", font=("Segoe UI", 10, "bold"), pady=8
    ).pack(side="top", fill="x", pady=2)

    # Marco inferior (side='bottom', fill='x')
    tk.Label(
        contenedor, text="Pie de página: pack(side='bottom', fill='x')",
        bg="#1e293b", fg="white", font=("Segoe UI", 10, "bold"), pady=8
    ).pack(side="bottom", fill="x", pady=2)

    # Marco central para dividir horizontalmente
    frame_medio = tk.Frame(contenedor, bg="#e2e8f0", bd=1, relief="solid")
    frame_medio.pack(side="top", fill="both", expand=True, pady=8)

    tk.Label(
        frame_medio, text="Panel Izquierdo\nside='left'\nfill='y'",
        bg="#10b981", fg="white", font=("Segoe UI", 9, "bold"), padx=15
    ).pack(side="left", fill="y", padx=3, pady=3)

    tk.Label(
        frame_medio, text="Contenido Central Expandible\nside='left'\nfill='both'\nexpand=True",
        bg="#f59e0b", fg="white", font=("Segoe UI", 10, "bold")
    ).pack(side="left", fill="both", expand=True, padx=3, pady=3)

    tk.Label(
        frame_medio, text="Panel Derecho\nside='right'\nfill='y'",
        bg="#8b5cf6", fg="white", font=("Segoe UI", 9, "bold"), padx=15
    ).pack(side="right", fill="y", padx=3, pady=3)

    return contenedor


def construir_pestana_grid(parent):
    """Demuestra el comportamiento del gestor de cuadrícula `grid`."""
    contenedor = tk.Frame(parent, bg="#f8fafc", padx=15, pady=15)

    info = tk.Label(
        contenedor,
        text="Gestor: grid()\nOrganiza widgets en una cuadrícula bidimensional de filas y columnas.\n"
             "Parámetros clave: row, column, rowspan, columnspan, sticky ('n', 's', 'e', 'w').\n"
             "Permite configurar pesos de expansión con rowconfigure() y columnconfigure().",
        font=("Segoe UI", 9),
        bg="#f8fafc",
        fg="#334155",
        justify="left"
    )
    info.grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 10))

    # Formulario típico maquetado con grid
    frame_form = tk.LabelFrame(
        contenedor, text=" Formulario Responsivo (Grid) ",
        font=("Segoe UI", 10, "bold"), bg="#ffffff", padx=15, pady=15
    )
    frame_form.grid(row=1, column=0, columnspan=3, sticky="nsew", pady=5)

    # Configuración de pesos para que la columna 1 se expanda
    frame_form.columnconfigure(1, weight=1)

    # Fila 0: Nombre
    tk.Label(frame_form, text="Nombre completo:", bg="#ffffff", font=("Segoe UI", 9)).grid(
        row=0, column=0, sticky="w", pady=6
    )
    tk.Entry(frame_form, font=("Segoe UI", 9)).grid(
        row=0, column=1, sticky="ew", padx=10, pady=6
    )

    # Fila 1: Correo Electrónico
    tk.Label(frame_form, text="Correo electrónico:", bg="#ffffff", font=("Segoe UI", 9)).grid(
        row=1, column=0, sticky="w", pady=6
    )
    tk.Entry(frame_form, font=("Segoe UI", 9)).grid(
        row=1, column=1, sticky="ew", padx=10, pady=6
    )

    # Fila 2: Rol / Perfil
    tk.Label(frame_form, text="Rol del usuario:", bg="#ffffff", font=("Segoe UI", 9)).grid(
        row=2, column=0, sticky="w", pady=6
    )
    cb_rol = ttk.Combobox(frame_form, values=["Desarrollador", "Diseñador", "Administrador", "Estudiante"], state="readonly")
    cb_rol.current(0)
    cb_rol.grid(row=2, column=1, sticky="ew", padx=10, pady=6)

    # Fila 3: Botones (columnspan=2)
    frame_btn = tk.Frame(frame_form, bg="#ffffff")
    frame_btn.grid(row=3, column=0, columnspan=2, pady=(15, 0), sticky="e")

    tk.Button(frame_btn, text="Cancelar", bg="#e2e8f0", padx=12, pady=4, relief="flat").pack(side="right", padx=(5, 0))
    tk.Button(frame_btn, text="Guardar Registro", bg="#10b981", fg="white", font=("Segoe UI", 9, "bold"), padx=12, pady=4, relief="flat").pack(side="right")

    # Hacer que el marco_form se expanda en el contenedor principal
    contenedor.columnconfigure(0, weight=1)
    contenedor.rowconfigure(1, weight=1)

    return contenedor


def construir_pestana_place(parent):
    """Demuestra el comportamiento del gestor de coordenadas absolutas y relativas `place`."""
    contenedor = tk.Frame(parent, bg="#0f172a", padx=15, pady=15)

    info = tk.Label(
        contenedor,
        text="Gestor: place()\nUbica elementos indicando coordenadas exactas o porcentajes relativos.\n"
             "Parámetros: x, y (píxeles absolutos) | relx, rely, relwidth, relheight (0.0 a 1.0).\n"
             "Muy útil para interfaces flotantes, juegos o banners fijos.",
        font=("Segoe UI", 9),
        bg="#0f172a",
        fg="#94a3b8",
        justify="left"
    )
    info.place(x=15, y=10)

    # Cuadro posicionado con valores absolutos (x=30, y=90, width=200, height=100)
    box_absoluto = tk.Label(
        contenedor,
        text="Posición Absoluta\nx=30, y=90\nancho=200, alto=100",
        bg="#ef4444",
        fg="white",
        font=("Segoe UI", 9, "bold"),
        relief="ridge",
        bd=2
    )
    box_absoluto.place(x=30, y=90, width=200, height=100)

    # Cuadro centrado dinámicamente con relx y rely (relx=0.5, rely=0.65, anchor='center')
    box_relativo = tk.Label(
        contenedor,
        text="Posición Relativa (Centrado automático)\nrelx=0.5, rely=0.65\nrelwidth=0.85, relheight=0.30",
        bg="#8b5cf6",
        fg="white",
        font=("Segoe UI", 10, "bold"),
        relief="ridge",
        bd=2
    )
    box_relativo.place(relx=0.5, rely=0.65, anchor="center", relwidth=0.85, relheight=0.30)

    # Insignia en la esquina superior derecha
    badge = tk.Label(
        contenedor,
        text="📍 relx=0.98, rely=0.03\nanchor='ne'",
        bg="#06b6d4",
        fg="#0f172a",
        font=("Segoe UI", 8, "bold"),
        padx=8,
        pady=4
    )
    badge.place(relx=0.98, rely=0.03, anchor="ne")

    return contenedor


def main():
    root = tk.Tk()
    root.title("02 - Gestores de Geometría: pack(), grid() y place()")
    root.geometry("640x500")
    root.minsize(580, 420)

    # Título superior
    tk.Label(
        root,
        text="Comparativa de Gestores de Geometría",
        font=("Segoe UI", 14, "bold"),
        bg="#1e293b",
        fg="#ffffff",
        pady=10
    ).pack(fill="x")

    # Contenedor de Pestañas (Notebook)
    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    pestana_pack = construir_pestana_pack(notebook)
    pestana_grid = construir_pestana_grid(notebook)
    pestana_place = construir_pestana_place(notebook)

    notebook.add(pestana_pack, text=" 📦 pack() ")
    notebook.add(pestana_grid, text=" 📐 grid() ")
    notebook.add(pestana_place, text=" 📍 place() ")

    root.mainloop()


if __name__ == "__main__":
    main()
