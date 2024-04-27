import tkinter as tk
from tkinter import ttk
import script
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Pixel Bakground Generator")
window.geometry("992x496")  # Increase the window size for better visibility

# GUI background image
bg_image = Image.open("gui_background.png")
bg_photo = None  # Initialize bg_photo variable

def resize_background(event):
    global bg_photo
    window_width = event.width
    window_height = event.height
    resized_bg = bg_image.resize((window_width, window_height), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(resized_bg)
    bg_label.config(image=bg_photo)

bg_label = tk.Label(window)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
window.bind("<Configure>", resize_background)

# Custom font for labels, buttons, and selectors
label_font = ("Overpass Mono", 24)
button_font = ("Overpass Mono", 16)
selector_font = ("Overpass Mono", 12)

# Custom style for the button
button_style = ttk.Style()
button_style.configure("CustomButton.TButton", font=button_font)

# Custom style for the selectors (Combobox and Entry)
selector_style = ttk.Style()
selector_style.configure("CustomSelector.TCombobox", font=selector_font)
selector_style.configure("CustomSelector.TEntry", font=selector_font)

# Amount of Images
amount_label = ttk.Label(window, text="Amount of Images:", font=label_font)
amount_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
amount_entry = ttk.Entry(window, style="CustomSelector.TEntry")
amount_entry.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

# Size Selection
size_label = ttk.Label(window, text="Size:", font=label_font)
size_label.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
size_var = tk.StringVar()
size_dropdown = ttk.Combobox(window, textvariable=size_var, values=["(31, 17)", "(62, 34)", "(93, 51)", "(124, 68)"], style="CustomSelector.TCombobox")
size_dropdown.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Rule Selection
rule_label = ttk.Label(window, text="Rule:", font=label_font)
rule_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
rule_var = tk.StringVar()
rule_dropdown = ttk.Combobox(window, textvariable=rule_var, values=["Rule 1", "Rule 2", "Rule 3", "Rule 4", "Rule 5", "Rule 6", "Rule 7"], style="CustomSelector.TCombobox")
rule_dropdown.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

def generate_images():
    amount = int(amount_entry.get())
    size = eval(size_dropdown.get())
    width, height = size
    rule_index = rule_dropdown.current()

    script.generate_images(amount, width, height, rule_index)

    for i in range(amount):
        canvas = script.create_background_canvas(width, height, 'white')
        script.rules[rule_index](canvas)
        scale_factor = round(1980 / width)
        canvas = canvas.resize((canvas.width * scale_factor, canvas.height * scale_factor), resample=script.Image.NEAREST)
        filename = f"{i+1}_{width}x{height}_{rule_index+1}.png"
        output_path = script.os.path.join(script.output_dir, filename)
        canvas.save(output_path)
        print(f"Image '{filename}' saved successfully.")

generate_button = ttk.Button(window, text="Generate Images", command=generate_images, style="CustomButton.TButton")
generate_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

window.mainloop()