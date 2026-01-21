import tkinter as tk


def btn_clicked():
    print('Gumb je kliknut.')


root = tk.Tk()
root.title('TkInter DEMO')
root.geometry('600x400')

lbl_title = tk.Label(root,
                     text='Pozdrav iz TkIntera!',
                     font=('Verdana', 18))
lbl_title.pack(padx=10, pady=10)
lbl_subtitle = tk.Label(root,
                        text='Ovo je moja prva TkInter aplikacija',
                        font=('Verdana', 14))
lbl_subtitle.pack(padx=10, pady=10)


btn_click = tk.Button(root,
                      text='Klikni me!',
                      font=('Verdana', 14),
                      command=btn_clicked)
btn_click.pack(padx=10, pady=10)


root.mainloop()