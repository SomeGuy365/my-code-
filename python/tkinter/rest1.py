import tkinter as tk

def back():
    print('back')
    root.destroy()
    import tkintetestr

root = tk.Tk()
root.geometry('300x300')
root.title('restaurant')

label1 = tk.Label(text='Order')
label1.pack(padx=20,pady=15)


goback = tk.Button(text='Go back',command=back)
goback.pack(padx=20,pady=25)

root.mainloop()