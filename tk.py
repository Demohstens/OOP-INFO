import tkinter as tk
from Building import Building
from calc import intersect

def spawn_building(x, y):
    b = Building(canvas, x, y)
    if len(buildings) > 1:
        for b2 in buildings:
            if intersect(b, b2):
                canvas.create_rectangle(x, y, x+50, y+50 ,fill="red")  
        else:
            buildings.append(b)
            refresh_canvas()
    else:
        buildings.append(b)
        refresh_canvas()
    


buildings = []

def on_canvas_click(event):
    x, y = event.x, event.y
    print(f"Mouse clicked at ({x}, {y})")
    spawn_building(x, y)
    
def refresh_canvas():
    print("triggered redraw")
    canvas.delete("all")
    for b in buildings:
        b.redraw(canvas)

# Create a Tkinter window
root = tk.Tk()

# Create a Canvas widget
canvas = tk.Canvas(root, width=1800, height=1000)
canvas.pack()


# Draw a line on the canvas
# The line coordinates are (x1, y1, x2, y2)

# You can customize the line color, width, and other attributes using optional parameters like 'fill' and 'width'.

canvas.bind("<Button-1>", on_canvas_click)  # Bind left mouse button click


# To display the Tkinter window, you need to start the main loop
root.mainloop()


