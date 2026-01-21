import tkinter as tk


root = tk.Tk()
root.title('TkInter DEMO')
root.geometry('600x400')

lbl_intro_message = tk.Label(root,
                             text='Pozdrav iz TkIntera!',
                             font=('Verdana', 18))
lbl_intro_message.pack(padx=10, pady=10)


root.mainloop()
