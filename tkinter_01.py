import tkinter as tk
from tkinter import ttk


# Globalna varijabla za brojač
counter = 0


def increment():
    global counter
    counter += 1
    lbl_counter.config(text=str(counter))
    lbl_status.config(text='✓ Inkrementovano!', fg='#27ae60')


def decrement():
    global counter
    counter -= 1
    lbl_counter.config(text=str(counter))
    lbl_status.config(text='✓ Dekrementovano!', fg='#e74c3c')


def reset():
    global counter
    counter = 0
    lbl_counter.config(text=str(counter))
    lbl_status.config(text='✓ Resetovano!', fg='#3498db')


# Glavna prozor
root = tk.Tk()
root.title('Brojač - Tkinter DEMO')
root.geometry('500x550')
root.resizable(False, False)

# Boje
bg_color = '#ecf0f1'
header_color = '#2c3e50'
button_color = '#3498db'
button_hover = '#2980b9'

root.config(bg=bg_color)

# Header Frame
header_frame = tk.Frame(root, bg=header_color, height=100)
header_frame.pack(fill=tk.X, padx=0, pady=0)
header_frame.pack_propagate(False)

# Naslov
lbl_title = tk.Label(header_frame,
                     text='BROJAČ',
                     font=('Arial', 28, 'bold'),
                     bg=header_color,
                     fg='white')
lbl_title.pack(pady=20)

# Podnaslov
lbl_subtitle = tk.Label(header_frame,
                        text='Klikni gumbe za brojanje',
                        font=('Arial', 11),
                        bg=header_color,
                        fg='#bdc3c7')
lbl_subtitle.pack(pady=5)

# Glavni sadržaj Frame
content_frame = tk.Frame(root, bg=bg_color)
content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=30)

# Prikaz brojača
lbl_counter = tk.Label(content_frame,
                       text='0',
                       font=('Arial', 72, 'bold'),
                       bg=bg_color,
                       fg=header_color)
lbl_counter.pack(pady=30)

# Status poruka
lbl_status = tk.Label(content_frame,
                      text='Spreman!',
                      font=('Arial', 12),
                      bg=bg_color,
                      fg='#7f8c8d')
lbl_status.pack(pady=10)

# Frame za gumbe
button_frame = tk.Frame(content_frame, bg=bg_color)
button_frame.pack(pady=20, fill=tk.X)

# Gumb za increment
btn_increment = tk.Button(button_frame,
                          text='➕ INCREMENT',
                          font=('Arial', 12, 'bold'),
                          bg='#27ae60',
                          fg='white',
                          activebackground='#229954',
                          activeforeground='white',
                          padx=20,
                          pady=12,
                          border=0,
                          cursor='hand2',
                          command=increment)
btn_increment.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)

# Gumb za decrement
btn_decrement = tk.Button(button_frame,
                          text='➖ DECREMENT',
                          font=('Arial', 12, 'bold'),
                          bg='#e74c3c',
                          fg='white',
                          activebackground='#c0392b',
                          activeforeground='white',
                          padx=20,
                          pady=12,
                          border=0,
                          cursor='hand2',
                          command=decrement)
btn_decrement.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)

# Gumb za reset
btn_reset = tk.Button(button_frame,
                      text='🔄 RESET',
                      font=('Arial', 12, 'bold'),
                      bg='#3498db',
                      fg='white',
                      activebackground='#2980b9',
                      activeforeground='white',
                      padx=20,
                      pady=12,
                      border=0,
                      cursor='hand2',
                      command=reset)
btn_reset.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)

# Footer Frame
footer_frame = tk.Frame(root, bg=header_color, height=60)
footer_frame.pack(fill=tk.X, side=tk.BOTTOM, padx=0, pady=0)
footer_frame.pack_propagate(False)

lbl_footer = tk.Label(footer_frame,
                      text='Tkinter Demo za Raspberry Pi 5 | Python GUI',
                      font=('Arial', 9),
                      bg=header_color,
                      fg='#95a5a6')
lbl_footer.pack(pady=15)

root.mainloop()
