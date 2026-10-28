"""
=============================================================================
07_canvas_y_animaciones.py
=============================================================================
Dominando el widget Canvas de Tkinter:
- Dibujo de primitivas gráficas: líneas, rectángulos, círculos, arcos y texto.
- Bucle de animación suave sin congelar la interfaz utilizando root.after().
- Simulación física de pelota rebotando con colisión de bordes.
- Pizarra interactiva para dibujar a mano alzada con el ratón.
- Arrastrar y soltar (drag & drop) de figuras geométricas en el lienzo.
=============================================================================
"""

import tkinter as tk
from tkinter import ttk
import random


class CanvasYAnimacionApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("07 - Gráficos en Canvas y Animaciones con after()")
        self.root.geometry("800x620")
        self.root.minsize(700, 520)

        # Estado de animación
        self.animando = False
        self.pelotas = []

        # Estado de dibujo a mano alzada
        self.color_pincel = "#2563eb"
        self.grosor_pincel = 3
        self.ultimo_x = None
        self.ultimo_y = None

        # Estado de arrastre de figuras
        self.figura_arrastrada = None
        self.offset_x = 0
        self.offset_y = 0

        self.crear_interfaz()

    def crear_interfaz(self):
        # Panel superior de controles
        panel_superior = tk.Frame(self.root, bg="#1e293b", padx=10, pady=8)
        panel_superior.pack(fill="x")

        tk.Label(
            panel_superior,
            text="Lienzo Gráfico (Canvas)",
            font=("Segoe UI", 12, "bold"),
            fg="white",
            bg="#1e293b"
        ).pack(side="left", padx=5)

        # Botones de modo
        tk.Button(panel_superior, text="✨ Dibujos Estáticos", command=self.dibujar_figuras_estaticas, bg="#334155", fg="white", relief="flat", padx=8).pack(side="left", padx=4)
        tk.Button(panel_superior, text="⚽ Animación de Rebote", command=self.iniciar_animacion, bg="#10b981", fg="white", relief="flat", padx=8).pack(side="left", padx=4)
        tk.Button(panel_superior, text="⏹ Detener", command=self.detener_animacion, bg="#ef4444", fg="white", relief="flat", padx=8).pack(side="left", padx=4)
        tk.Button(panel_superior, text="🧹 Limpiar Lienzo", command=self.limpiar_lienzo, bg="#64748b", fg="white", relief="flat", padx=8).pack(side="left", padx=4)

        # Selector de modo de uso del mouse
        tk.Label(panel_superior, text="|  Modo Mouse:", bg="#1e293b", fg="#94a3b8").pack(side="left", padx=(10, 4))
        self.modo_mouse = tk.StringVar(value="dibujar")
        combo_modo = ttk.Combobox(panel_superior, textvariable=self.modo_mouse, values=["dibujar", "arrastrar"], state="readonly", width=10)
        combo_modo.pack(side="left", padx=2)
        combo_modo.bind("<<ComboboxSelected>>", self.cambiar_modo_mouse)

        # Lienzo (Canvas)
        self.canvas = tk.Canvas(self.root, bg="#ffffff", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Barra de ayuda inferior
        self.barra_ayuda = tk.Label(
            self.root,
            text="Modo dibujo activo: Haz clic izquierdo y arrastra sobre el lienzo para pintar.",
            bg="#f1f5f9",
            fg="#475569",
            font=("Segoe UI", 9),
            pady=4
        )
        self.barra_ayuda.pack(fill="x")

        # Configurar eventos iniciales del lienzo
        self.vincular_eventos_dibujo()

        # Dibujar bienvenida en el lienzo
        self.dibujar_figuras_estaticas()

    # -----------------------------------------------------------------------
    # Dibujo de Figuras Básicas
    # -----------------------------------------------------------------------
    def dibujar_figuras_estaticas(self):
        self.detener_animacion()
        self.canvas.delete("all")

        # Texto explicativo
        self.canvas.create_text(
            400, 35,
            text="Demostración de Primitivas Gráficas de Tkinter",
            font=("Segoe UI", 14, "bold"),
            fill="#1e293b"
        )

        # 1. Líneas y flechas
        self.canvas.create_line(50, 80, 250, 80, fill="#3b82f6", width=4, arrow=tk.LAST, tags="figura")
        self.canvas.create_text(150, 100, text="Línea con flecha", font=("Segoe UI", 9), fill="#64748b")

        # 2. Rectángulo con esquinas redondeadas simuladas o bordes
        self.canvas.create_rectangle(50, 130, 250, 220, fill="#dbeafe", outline="#2563eb", width=3, tags="figura")
        self.canvas.create_text(150, 175, text="Rectángulo\n(Arrastrable)", font=("Segoe UI", 10, "bold"), fill="#1e3a8a", justify="center", tags="figura")

        # 3. Círculo / Óvalo
        self.canvas.create_oval(320, 100, 480, 260, fill="#fef08a", outline="#ca8a04", width=3, tags="figura")
        self.canvas.create_text(400, 180, text="Círculo\n(create_oval)", font=("Segoe UI", 10, "bold"), fill="#713f12", justify="center", tags="figura")

        # 4. Polígono (Triángulo)
        puntos_triangulo = [600, 80, 520, 220, 680, 220]
        self.canvas.create_polygon(puntos_triangulo, fill="#bbf7d0", outline="#16a34a", width=3, tags="figura")
        self.canvas.create_text(600, 180, text="Polígono\n(Triángulo)", font=("Segoe UI", 10, "bold"), fill="#14532d", justify="center", tags="figura")

        # 5. Arco
        self.canvas.create_arc(320, 300, 480, 460, start=30, extent=120, fill="#fbcfe8", outline="#db2777", width=2, tags="figura")
        self.canvas.create_text(400, 370, text="Arco (create_arc)", font=("Segoe UI", 9, "bold"), fill="#831843", tags="figura")

    # -----------------------------------------------------------------------
    # Animación con after()
    # -----------------------------------------------------------------------
    def iniciar_animacion(self):
        if self.animando:
            return

        self.canvas.delete("all")
        self.animando = True
        self.pelotas = []

        # Crear 6 pelotas con velocidades y colores aleatorios
        colores = ["#ef4444", "#3b82f6", "#10b981", "#f59e0b", "#8b5cf6", "#ec4899"]
        for color in colores:
            radio = random.randint(18, 30)
            x = random.randint(50, 600)
            y = random.randint(50, 400)
            dx = random.choice([-5, -4, -3, 3, 4, 5])
            dy = random.choice([-5, -4, -3, 3, 4, 5])
            item = self.canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill=color, outline="")
            self.pelotas.append({"id": item, "dx": dx, "dy": dy, "radio": radio})

        self.barra_ayuda.config(text="Animación activa: Se calculan rebotes contra los bordes a 60 FPS.")
        self.bucle_animacion()

    def bucle_animacion(self):
        """Bucle recurrente usando root.after(16, ...) que equivale aproximadamente a 60 FPS."""
        if not self.animando:
            return

        ancho_lienzo = self.canvas.winfo_width()
        alto_lienzo = self.canvas.winfo_height()

        for p in self.pelotas:
            coords = self.canvas.coords(p["id"])
            if not coords:
                continue
            x1, y1, x2, y2 = coords

            # Colisión con paredes laterales
            if x1 <= 0 or x2 >= ancho_lienzo:
                p["dx"] = -p["dx"]
            # Colisión con techo o piso
            if y1 <= 0 or y2 >= alto_lienzo:
                p["dy"] = -p["dy"]

            self.canvas.move(p["id"], p["dx"], p["dy"])

        # Programar siguiente cuadro en ~16 milisegundos (aprox 60 FPS)
        self.root.after(16, self.bucle_animacion)

    def detener_animacion(self):
        self.animando = False
        self.barra_ayuda.config(text="Animación detenida.")

    def limpiar_lienzo(self):
        self.detener_animacion()
        self.canvas.delete("all")
        self.barra_ayuda.config(text="Lienzo limpio.")

    # -----------------------------------------------------------------------
    # Dibujo Libre con el Mouse
    # -----------------------------------------------------------------------
    def vincular_eventos_dibujo(self):
        self.canvas.bind("<Button-1>", self.iniciar_trazo)
        self.canvas.bind("<B1-Motion>", self.trazar)
        self.canvas.bind("<ButtonRelease-1>", self.finalizar_trazo)

    def iniciar_trazo(self, event):
        self.ultimo_x = event.x
        self.ultimo_y = event.y

    def trazar(self, event):
        if self.ultimo_x and self.ultimo_y:
            self.canvas.create_line(
                self.ultimo_x, self.ultimo_y, event.x, event.y,
                width=self.grosor_pincel,
                fill=self.color_pincel,
                capstyle=tk.ROUND,
                smooth=True
            )
            self.ultimo_x = event.x
            self.ultimo_y = event.y

    def finalizar_trazo(self, event):
        self.ultimo_x = None
        self.ultimo_y = None

    # -----------------------------------------------------------------------
    # Arrastrar y Soltar (Drag and Drop)
    # -----------------------------------------------------------------------
    def vincular_eventos_arrastre(self):
        self.canvas.bind("<Button-1>", self.iniciar_arrastre)
        self.canvas.bind("<B1-Motion>", self.mover_figura)
        self.canvas.bind("<ButtonRelease-1>", self.soltar_figura)

    def iniciar_arrastre(self, event):
        items = self.canvas.find_withtag("current")
        if items:
            self.figura_arrastrada = items[0]
            self.offset_x = event.x
            self.offset_y = event.y

    def mover_figura(self, event):
        if self.figura_arrastrada:
            dx = event.x - self.offset_x
            dy = event.y - self.offset_y
            self.canvas.move(self.figura_arrastrada, dx, dy)
            self.offset_x = event.x
            self.offset_y = event.y

    def soltar_figura(self, event):
        self.figura_arrastrada = None

    def cambiar_modo_mouse(self, event=None):
        modo = self.modo_mouse.get()
        if modo == "dibujar":
            self.vincular_eventos_dibujo()
            self.barra_ayuda.config(text="Modo dibujo activo: Haz clic izquierdo y arrastra para dibujar.")
        else:
            self.vincular_eventos_arrastre()
            self.barra_ayuda.config(text="Modo arrastre activo: Haz clic sobre cualquier figura y muévela libremente.")


if __name__ == "__main__":
    app_root = tk.Tk()
    app = CanvasYAnimacionApp(app_root)
    app_root.mainloop()
