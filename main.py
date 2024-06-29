import tkinter as tk
import hashlib

def try_exit(*event):
    label.config(text='Не выйдешь)')

def close(*event):
    root.destroy()

def try_password(*event):
    password = password_input.get()
    
    # if password == 'Good password!': 
    if hashlib.sha256(password.encode()).hexdigest() == '361dbd93b6f700ca8be1740caa2e0d3df6c4fa6b67362cc4a3027ce0345ffebd': 
        label.config(text='С вами приятно иметь дело!)')
        
        root.attributes('-fullscreen', False)
        root.bind('<Alt-F4>', close)
        root.bind('<Escape>', close)
        root.protocol("WM_DELETE_WINDOW", close)
        
        enter_button['text'] = 'Выйти'
        enter_button.bind('<Button-1>', close)
    
    else: label.config(text='Неверный пароль')
    
    clean_input()
        
def clean_input(*event):
    password_input.delete(0, tk.END)

root = tk.Tk()
root.attributes('-fullscreen', True)
root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
root.title("А я надеялся, что ты не сможешь(")

height = root.winfo_screenheight()

label = tk.Label(root, text='Введите пароль', font=(f'Consolas {height//15}'))
label.pack(anchor=tk.CENTER)

password_input = tk.Entry(font=(f'Consolas {height//20}'))
password_input.pack(anchor=tk.CENTER, pady=100)

enter_button = tk.Button(text='Enter', command=try_password, font=(f'Consolas {height//25}'))
enter_button.pack(anchor=tk.S)

root.bind('<Alt-F4>', try_exit)
root.bind('<Escape>', try_exit)
root.bind('<Alt-q>', close)
root.bind('<Control-BackSpace>', clean_input)
root.bind('<Return>', try_password)
root.protocol("WM_DELETE_WINDOW", try_exit)

root.mainloop()