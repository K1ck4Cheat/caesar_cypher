import tkinter as tk


def error_window(num):
    error_win = tk.Tk()

    w = 640
    h = 128

    error_win.geometry(f"{w}x{h}")
    error_win.resizable(False, False)

    error_bgcolor = '#ada9a8'
    error_win.configure(bg=error_bgcolor)

    error_icon = tk.PhotoImage(file='error_icon.png', master=error_win)
    error_win.iconphoto(False, error_icon)

    error_win.title('Error Message')

    if num == 1:
        error_label = tk.Label(error_win, text='Key can only be a number between 1 and 25!', font=('Arial', 12, 'bold'),
                               bg=error_bgcolor, fg='red')
        error_label.grid(row=0, column=0, stick='we', columnspan=5, padx=140, pady=30)
    elif num == 2:
        error_label = tk.Label(error_win, text='Message can consists only of letters (a-z and A-Z)',
                               font=('Arial', 12, 'bold'), bg=error_bgcolor, fg='red')
        error_label.grid(row=0, column=0, stick='we', columnspan=5, padx=140, pady=30)

    tk.Button(error_win, text='Ok', command=error_win.destroy, width=10).grid(row=1, column=2)

    colw = 30
    win.grid_columnconfigure(0, minsize=colw)
    win.grid_columnconfigure(1, minsize=colw)
    win.grid_columnconfigure(2, minsize=colw)
    win.grid_columnconfigure(3, minsize=colw)
    win.grid_columnconfigure(4, minsize=colw)

    error_win.mainloop()


def get_entry(num):
    # To Do: Add restictions
    result_entry.delete('1.0', tk.END)
    mess = message_entry.get("1.0", tk.END).upper().replace(" ", "").rstrip()
    key = get_key(0)
    if key < 0 or key > 25:
        error_window(1)
        return
    elif not mess.isalpha():
        error_window(2)
        return
    if num == 1:
        decrypt(mess, key)
    else:
        encrypt(mess, key)


def get_key(nr):
    k = int(key_entry.get())
    if nr == 1:
        k += 1
        key_entry.delete(0, tk.END)
        if k > 25:
            key_entry.insert(tk.END, 1)
        else:
            key_entry.insert(tk.END, k)
    elif nr == 2:
        k -= 1
        key_entry.delete(0, tk.END)
        if k < 0:
            key_entry.insert(tk.END, 25)
        else:
            key_entry.insert(tk.END, k)
    else:
        return k


def decrypt(message, key):
    decrypted = ''
    for letter in message:
        c = chr(ord(letter) - key)
        if ord(c) < ord('A'):
            c = chr(ord('Z') - (ord('A') - ord(c)) + 1)
        decrypted = decrypted + c
    print(decrypted)
    result_entry.insert(tk.END, decrypted)


def encrypt(message, key):
    encrypted = ''
    for letter in message:
        c = chr(ord(letter) + key)
        if ord(c) > ord('Z'):
            c = chr(ord('A') + ord(c) - ord('Z') - 1)
        encrypted = encrypted + c
    print(encrypted)
    result_entry.insert(tk.END, encrypted)


win = tk.Tk()
height = 480
width = 640
bgcolor = '#93db9a'

win.geometry(f"{width}x{height}")
win.resizable(False, False)
win.configure(bg=bgcolor)

photo = tk.PhotoImage(file='icon.png')
win.iconphoto(False, photo)

win.title('Caesar Cypher')

message_label = tk.Label(text='Message:', padx=40, background=bgcolor, anchor='s')
message_label.grid(row=0, column=0, stick='w', pady=10)

message_entry = tk.Text(win, height=5, width=70)
message_entry.grid(row=1, column=0, columnspan=4, stick='we', padx=20, pady=10)

up_photo = tk.PhotoImage(file='up.png')
tk.Button(win, image=up_photo, command=lambda: get_key(1), height=28, width=40).grid(row=2, column=1, columnspan=2)

tk.Button(win, text='Decode', command=lambda: get_entry(1)).grid(row=3, column=0, padx=10)

key_label = tk.Label(text='Key:', width='3', background=bgcolor)
key_label.grid(row=3, column=1, stick='e')

key_entry = tk.Entry(win, font=('Arial', 12, 'bold'), width='2')
key_entry.grid(row=3, column=2, stick='w')
key_entry.insert(tk.END, 0)

tk.Button(win, text='Encode', command=lambda: get_entry(2)).grid(row=3, column=3, padx=10)

down_photo = tk.PhotoImage(file='down.png')
tk.Button(win, image=down_photo, command=lambda: get_key(2), height=28, width=40).grid(row=4, column=1, columnspan=2)

result_label = tk.Label(text='Result:', padx=40, background=bgcolor)
result_label.grid(row=5, column=0, stick='w')

result_entry = tk.Text(win, height=5, width=70)
result_entry.grid(row=6, column=0, columnspan=4, stick='we', padx=20, pady=10)

colwidth = 30
win.grid_columnconfigure(0, minsize=colwidth)
win.grid_columnconfigure(1, minsize=colwidth)
win.grid_columnconfigure(2, minsize=colwidth)
win.grid_columnconfigure(3, minsize=colwidth)

win.mainloop()
