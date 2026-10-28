"""
=============================================================================
01_hola_mundo_y_basicos.py
=============================================================================
Demostración básica de Tkinter:
- Creación de la ventana principal (Tk).
- Configuración de propiedades (título, tamaño, fondo, redimensionado).
- Widgets fundamentales: Label (etiqueta), Entry (campo de texto) y Button (botón).
- Agrupación mediante Frames (marcos contenedores).
- Manejo del bucle de eventos principal (mainloop).
=============================================================================
"""

import tkinter as tk
from tkinter import messagebox


def cambiar_saludo():
    """Toma el texto ingresado en el campo de texto y actualiza la etiqueta de saludo."""
    nombre = entry_nombre.get().strip()
    if nombre:
        lbl_resultado.config(
            text=f"¡Hola, {nombre}! Bienvenido a Tkinter.",
            fg="#1b5e20",  # Verde oscuro
        )
    else:
        messagebox.showwarning(
            "Campo vacío", "Por favor, escribe tu nombre antes de saludar."
        )


def limpiar_campos():
    """Borra el contenido del Entry y restaura el mensaje por defecto."""
    entry_nombre.delete(0, tk.END)
    lbl_resultado.config(
        text="Escribe tu nombre y presiona el botón.",
        fg="#555555"
    )
    entry_nombre.focus()  # Vuelve a colocar el cursor en el campo


# ---------------------------------------------------------------------------
# 1. Configuración de la Ventana Principal
# ---------------------------------------------------------------------------
root = tk.Tk()
root.title("01 - Hola Mundo y Widgets Básicos en Tkinter")
root.geometry("520x420")  # Ancho x Alto en píxeles
root.minsize(450, 350)    # Dimensiones mínimas permitidas
root.resizable(True, True)  # Permitir redimensionar tanto ancho como alto
root.configure(bg="#f4f6f9")  # Color de fondo de la ventana

# ---------------------------------------------------------------------------
# 2. Marco Contenedor Superior (Título y Explicación)
# ---------------------------------------------------------------------------
frame_encabezado = tk.Frame(root, bg="#1e293b", padx=20, pady=15)
frame_encabezado.pack(fill="x")

lbl_titulo = tk.Label(
    frame_encabezado,
    text="Mi Primera Aplicación Tkinter",
    font=("Segoe UI", 16, "bold"),
    fg="#ffffff",
    bg="#1e293b"
)
lbl_titulo.pack()

lbl_subtitulo = tk.Label(
    frame_encabezado,
    text="Aprende el uso de Label, Entry, Button y Frame",
    font=("Segoe UI", 9),
    fg="#94a3b8",
    bg="#1e293b"
)
lbl_subtitulo.pack(pady=(4, 0))

# ---------------------------------------------------------------------------
# 3. Marco de Contenido Principal
# ---------------------------------------------------------------------------
frame_cuerpo = tk.Frame(root, bg="#f4f6f9", padx=25, pady=20)
frame_cuerpo.pack(fill="both", expand=True)

# Etiqueta indicativa
lbl_instruccion = tk.Label(
    frame_cuerpo,
    text="¿Cómo te llamas?",
    font=("Segoe UI", 11, "bold"),
    fg="#334155",
    bg="#f4f6f9"
)
lbl_instruccion.pack(anchor="w", pady=(0, 5))

# Campo de entrada de texto (Entry)
entry_nombre = tk.Entry(
    frame_cuerpo,
    font=("Segoe UI", 11),
    relief="solid",
    bd=1,
    bg="#ffffff",
    fg="#0f172a"
)
entry_nombre.pack(fill="x", ipady=5, pady=(0, 15))
entry_nombre.focus()  # Poner foco al iniciar la ventana

# Vincular la tecla 'Enter' al campo de texto para saludar directamente
entry_nombre.bind("<Return>", lambda event: cambiar_saludo())

# ---------------------------------------------------------------------------
# 4. Marco para Botones de Acción
# ---------------------------------------------------------------------------
frame_botones = tk.Frame(frame_cuerpo, bg="#f4f6f9")
frame_botones.pack(pady=10)

btn_saludar = tk.Button(
    frame_botones,
    text="Saludar 👋",
    command=cambiar_saludo,
    font=("Segoe UI", 10, "bold"),
    bg="#2563eb",       # Azul
    fg="#ffffff",
    activebackground="#1d4ed8",
    activeforeground="#ffffff",
    padx=15,
    pady=6,
    relief="flat",
    cursor="hand2"
)
btn_saludar.pack(side="left", padx=5)

btn_limpiar = tk.Button(
    frame_botones,
    text="Limpiar 🧹",
    command=limpiar_campos,
    font=("Segoe UI", 10),
    bg="#e2e8f0",       # Gris claro
    fg="#334155",
    activebackground="#cbd5e1",
    activeforeground="#0f172a",
    padx=15,
    pady=6,
    relief="flat",
    cursor="hand2"
)
btn_limpiar.pack(side="left", padx=5)

# ---------------------------------------------------------------------------
# 5. Área de Resultado
# ---------------------------------------------------------------------------
lbl_resultado = tk.Label(
    frame_cuerpo,
    text="Escribe tu nombre y presiona el botón.",
    font=("Segoe UI", 11, "italic"),
    fg="#64748b",
    bg="#ffffff",
    relief="groove",
    bd=1,
    pady=15,
    padx=10
)
lbl_resultado.pack(fill="x", pady=(20, 0))

# ---------------------------------------------------------------------------
# 6. Iniciar el ciclo de ejecución
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # mainloop() mantiene abierta la ventana a la espera de eventos del usuario
    root.mainloop()
