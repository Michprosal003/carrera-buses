import tkinter as tk
import random
from tkinter import messagebox

# Configuración inicial de la ventana
WIDTH = 600
HEIGHT = 400
FINISH_LINE = WIDTH - 50

# Crear la ventana      
root = tk.Tk()
root.title("Carrera de Buses")

# Cambiar el color de fondo del canvas a negro
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Arte ASCII para el bus
bus_ascii = [
    "        ______________________",
    "       |,----.,----.,----.,--.\\",
    "       ||    ||    ||    ||   \\\\",
    "       |`----'`----'|----||----\\`.",
    "       [            |   -||- __|( |",
    "       [  ,--.      |____||.--.  |",
    "       =-(( `))-----------(( `))=="
]

# Cuadros de texto para ingresar los nombres de los países
country1_label = tk.Label(root, text="País 1:", bg="black", fg="white")
country1_label.pack(pady=(10, 0))  # Espacio vertical arriba
country1_entry = tk.Entry(root)
country1_entry.pack(pady=(0, 10))  # Espacio vertical abajo

country2_label = tk.Label(root, text="País 2:", bg="black", fg="white")
country2_label.pack(pady=(10, 0))  # Espacio vertical arriba
country2_entry = tk.Entry(root)
country2_entry.pack(pady=(0, 10))  # Espacio vertical abajo


def draw_bus(x, y, country_name):
    # Dibujar el nombre del país encima del bus
    canvas.create_text(x + 10, y - 20, text=country_name,
                       anchor="nw", font=("Helvetica", 14), fill="white")
    for i, line in enumerate(bus_ascii):
        canvas.create_text(x, y + i * 15, text=line,
                           anchor="nw", font=("Courier", 10), fill="white")


def draw_track():
    # Dibujar la pista
    lane_y_positions = [50, 200]  # Separar los carriles
    lane_height = 50

    for lane_y in lane_y_positions:
        # Dibujar líneas de los carriles
        canvas.create_line(0, lane_y, WIDTH, lane_y, fill="white", width=2)
        canvas.create_line(0, lane_y + lane_height, WIDTH,
                           lane_y + lane_height, fill="white", width=2)

        # Dibujar líneas de separación en la pista
        for i in range(0, WIDTH, 40):
            canvas.create_line(i, lane_y + lane_height / 2, i +
                               20, lane_y + lane_height / 2, fill="black", width=2)

    # Dibujar la línea de meta
    canvas.create_line(FINISH_LINE, 0, FINISH_LINE,
                       HEIGHT, fill="red", width=4)


# Posiciones iniciales
bus1_x, bus1_y = 0, 50
bus2_x, bus2_y = 0, 200  # Cambiar la posición vertical para más espacio

# Función para mover los buses


def move_buses():
    global bus1_x, bus2_x
    # Mover buses con velocidad aleatoria
    bus1_x += random.randint(1, 10)
    bus2_x += random.randint(1, 10)

    # Limpiar canvas, dibujar la pista y redibujar los buses
    canvas.delete("all")
    draw_track()
    draw_bus(bus1_x, bus1_y, country1_entry.get())
    draw_bus(bus2_x, bus2_y, country2_entry.get())

    if bus1_x >= FINISH_LINE and bus2_x >= FINISH_LINE:
        winner = "¡Empate!"
    elif bus1_x >= FINISH_LINE:
        winner = f"¡{country1_entry.get()} gana!"
    elif bus2_x >= FINISH_LINE:
        winner = f"¡{country2_entry.get()} gana!"
    else:
        root.after(100, move_buses)  # Llamar nuevamente después de 100 ms
        return

    # Mostrar el resultado con separación
    canvas.create_text(WIDTH / 2, HEIGHT - 100, text=winner,
                       # Ajustar la posición vertical
                       font=('Helvetica', 24), fill="white")

# Función para iniciar la carrera


def start_race():
    global bus1_x, bus2_x
    country1 = country1_entry.get().strip()
    country2 = country2_entry.get().strip()

    if not country1 or not country2:
        messagebox.showwarning(
            "Advertencia", "Por favor ingrese nombres para ambos países.")
        return

    bus1_x, bus2_x = 0, 0  # Reiniciar posiciones
    move_buses()

# Función para reiniciar la carrera


def reset_race():
    global bus1_x, bus2_x
    bus1_x, bus2_x = 0, 0  # Reiniciar posiciones
    canvas.delete("all")  # Limpiar el canvas
    draw_track()
    draw_bus(bus1_x, bus1_y, country1_entry.get())
    draw_bus(bus2_x, bus2_y, country2_entry.get())


# Crear un Frame para organizar los botones
button_frame = tk.Frame(root)
button_frame.pack(pady=10)  # Agregar un poco de espacio vertical

# Botón para iniciar la carrera
start_button = tk.Button(
    button_frame, text="Iniciar Carrera", command=start_race)
# Agregar espacio horizontal entre los botones
start_button.pack(side="left", padx=10)

# Botón para reiniciar la carrera
reset_button = tk.Button(
    button_frame, text="Reiniciar Carrera", command=reset_race)
reset_button.pack(side="left", padx=10)

# Dibujar la pista inicial
draw_track()

# Ejecutar la aplicación
root.mainloop()
