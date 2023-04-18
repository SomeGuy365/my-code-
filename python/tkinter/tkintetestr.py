import tkinter as tk

final = []

def click():
    window.destroy()
    def back():
        print('back')
        import tkintetestr

    root = tk.Tk()
    root.geometry('300x300')
    root.title('restaurant')

    label1 = tk.Label(text='Order')
    label1.pack(padx=20,pady=15)


    goback = tk.Button(text='Go back',command=back)
    goback.pack(padx=20,pady=25)

    root.mainloop()

def out():
    output  = 0
    for i in final:
        output += i
    print(output)


window = tk.Tk()

window.geometry('300x300')
window.title('restaurant')

label1 = tk.Label(text='Order')
label1.pack(padx=20,pady=15)

rest1 = tk.Button(text='rest1',command=click)
rest1.pack(padx=40,pady=0)

rest2 = tk.Button(text='rest2',command=click)
rest2.pack(padx=40,pady=0)

rest3 = tk.Button(text='rest3',command=click)
rest3.pack(padx=40,pady=0)

checkout = tk.Button(text='Checkout',command=out)

window.mainloop()