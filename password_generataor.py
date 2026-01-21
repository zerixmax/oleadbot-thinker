import tkinter as tk
from tkinter import messagebox
import random
import string


# Globalne varijable
current_password = ''


def generate_password():
    """Generiše nasumičnu lozinku sa odabranim karakterima"""
    global current_password
    
    try:
        length = int(entry_length.get())
        
        if length < 4:
            messagebox.showwarning('Upozorenje', 'Lozinka mora biti najmanje 4 karaktera!')
            return
        if length > 128:
            messagebox.showwarning('Upozorenje', 'Lozinka može biti maksimalno 128 karaktera!')
            return
        
        # Odaberi karaktere
        characters = ''
        
        if var_uppercase.get():
            characters += string.ascii_uppercase
        if var_lowercase.get():
            characters += string.ascii_lowercase
        if var_digits.get():
            characters += string.digits
        if var_special.get():
            characters += string.punctuation
        
        if not characters:
            messagebox.showwarning('Upozorenje', 'Odaberi najmanje jedan tip karaktera!')
            return
        
        # Generiši lozinku
        current_password = ''.join(random.choice(characters) for _ in range(length))
        
        # Prikaži lozinku
        lbl_password_display.config(text=current_password)
        lbl_status.config(text='✓ Lozinka generisana!', fg='#27ae60')
        
    except ValueError:
        messagebox.showerror('Greška', 'Unesite broj za dužinu lozinke!')


def copy_to_clipboard():
    """Kopira lozinku u clipboard"""
    if current_password:
        root.clipboard_clear()
        root.clipboard_append(current_password)
        root.update()
        lbl_status.config(text='✓ Kopljeno u clipboard!', fg='#3498db')
    else:
        messagebox.showwarning('Upozorenje', 'Nema lozinke za kopiranje!')


def reset():
    """Resetuj sve"""
    global current_password
    current_password = ''
    entry_length.delete(0, tk.END)
    entry_length.insert(0, '12')
    lbl_password_display.config(text='Nema lozinke')
    lbl_status.config(text='✓ Resetovano!', fg='#e74c3c')
    var_uppercase.set(True)
    var_lowercase.set(True)
    var_digits.set(True)
    var_special.set(False)


# Glavna prozor
root = tk.Tk()
root.title('Generisač Lozinki - Tkinter DEMO')
root.geometry('600x700')
root.resizable(False, False)

# Boje
bg_color = '#ecf0f1'
header_color = '#2c3e50'

root.config(bg=bg_color)

# ===== HEADER FRAME =====
header_frame = tk.Frame(root, bg=header_color, height=100)
header_frame.pack(fill=tk.X, padx=0, pady=0)
header_frame.pack_propagate(False)

lbl_title = tk.Label(header_frame,
                     text='🔐 GENERISAČ LOZINKI',
                     font=('Arial', 26, 'bold'),
                     bg=header_color,
                     fg='white')
lbl_title.pack(pady=20)

lbl_subtitle = tk.Label(header_frame,
                        text='Kreiraj sigurne lozinke',
                        font=('Arial', 11),
                        bg=header_color,
                        fg='#bdc3c7')
lbl_subtitle.pack(pady=5)

# ===== GLAVNI SADRŽAJ FRAME =====
content_frame = tk.Frame(root, bg=bg_color)
content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# --- Dužina lozinke ---
length_frame = tk.Frame(content_frame, bg=bg_color)
length_frame.pack(fill=tk.X, pady=10)

lbl_length = tk.Label(length_frame,
                      text='Dužina lozinke:',
                      font=('Arial', 11, 'bold'),
                      bg=bg_color,
                      fg='#2c3e50')
lbl_length.pack(side=tk.LEFT)

entry_length = tk.Entry(length_frame,
                        font=('Arial', 12),
                        width=5,
                        justify=tk.CENTER)
entry_length.insert(0, '12')
entry_length.pack(side=tk.LEFT, padx=10)

lbl_length_info = tk.Label(length_frame,
                           text='(4-128 karaktera)',
                           font=('Arial', 9),
                           bg=bg_color,
                           fg='#7f8c8d')
lbl_length_info.pack(side=tk.LEFT)

# --- Checkboxes za vrste karaktera ---
checkbox_frame = tk.Frame(content_frame, bg=bg_color)
checkbox_frame.pack(fill=tk.X, pady=15)

lbl_options = tk.Label(checkbox_frame,
                       text='Tipovi karaktera:',
                       font=('Arial', 11, 'bold'),
                       bg=bg_color,
                       fg='#2c3e50')
lbl_options.pack(anchor=tk.W)

var_uppercase = tk.BooleanVar(value=True)
var_lowercase = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_special = tk.BooleanVar(value=False)

check_uppercase = tk.Checkbutton(checkbox_frame,
                                 text='Velika slova (A-Z)',
                                 variable=var_uppercase,
                                 font=('Arial', 10),
                                 bg=bg_color,
                                 activebackground=bg_color)
check_uppercase.pack(anchor=tk.W, padx=10, pady=2)

check_lowercase = tk.Checkbutton(checkbox_frame,
                                 text='Mala slova (a-z)',
                                 variable=var_lowercase,
                                 font=('Arial', 10),
                                 bg=bg_color,
                                 activebackground=bg_color)
check_lowercase.pack(anchor=tk.W, padx=10, pady=2)

check_digits = tk.Checkbutton(checkbox_frame,
                              text='Brojevi (0-9)',
                              variable=var_digits,
                              font=('Arial', 10),
                              bg=bg_color,
                              activebackground=bg_color)
check_digits.pack(anchor=tk.W, padx=10, pady=2)

check_special = tk.Checkbutton(checkbox_frame,
                               text='Specijalni znakovi (!@#$%)',
                               variable=var_special,
                               font=('Arial', 10),
                               bg=bg_color,
                               activebackground=bg_color)
check_special.pack(anchor=tk.W, padx=10, pady=2)

# --- Prikaz generirane lozinke ---
display_frame = tk.Frame(content_frame, bg='white', relief=tk.SUNKEN, bd=2)
display_frame.pack(fill=tk.X, pady=20)

lbl_password_label = tk.Label(display_frame,
                              text='Vaša lozinka:',
                              font=('Arial', 10, 'bold'),
                              bg='white',
                              fg='#2c3e50')
lbl_password_label.pack(anchor=tk.W, padx=10, pady=(10, 5))

lbl_password_display = tk.Label(display_frame,
                                text='Nema lozinke',
                                font=('Courier New', 14, 'bold'),
                                bg='white',
                                fg='#27ae60',
                                wraplength=520)
lbl_password_display.pack(padx=10, pady=10)

# --- Status poruka ---
lbl_status = tk.Label(content_frame,
                      text='Spreman!',
                      font=('Arial', 11),
                      bg=bg_color,
                      fg='#7f8c8d')
lbl_status.pack(pady=10)

# --- Gumbi ---
button_frame = tk.Frame(content_frame, bg=bg_color)
button_frame.pack(pady=15, fill=tk.X)

btn_generate = tk.Button(button_frame,
                         text='⚡ GENERIŠI',
                         font=('Arial', 12, 'bold'),
                         bg='#27ae60',
                         fg='white',
                         activebackground='#229954',
                         padx=20,
                         pady=12,
                         border=0,
                         cursor='hand2',
                         command=generate_password)
btn_generate.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)

btn_copy = tk.Button(button_frame,
                     text='📋 KOPIRAJ',
                     font=('Arial', 12, 'bold'),
                     bg='#3498db',
                     fg='white',
                     activebackground='#2980b9',
                     padx=20,
                     pady=12,
                     border=0,
                     cursor='hand2',
                     command=copy_to_clipboard)
btn_copy.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)

btn_reset = tk.Button(button_frame,
                      text='🔄 RESET',
                      font=('Arial', 12, 'bold'),
                      bg='#e74c3c',
                      fg='white',
                      activebackground='#c0392b',
                      padx=20,
                      pady=12,
                      border=0,
                      cursor='hand2',
                      command=reset)
btn_reset.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)

# ===== FOOTER FRAME =====
footer_frame = tk.Frame(root, bg=header_color, height=60)
footer_frame.pack(fill=tk.X, side=tk.BOTTOM, padx=0, pady=0)
footer_frame.pack_propagate(False)

lbl_footer = tk.Label(footer_frame,
                      text='Tkinter Password Generator za Raspberry Pi 5 | Python GUI',
                      font=('Arial', 9),
                      bg=header_color,
                      fg='#95a5a6')
lbl_footer.pack(pady=15)

root.mainloop()