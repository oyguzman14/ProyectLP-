import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
from analizadorLexico import imprimirLex

ventana1 = tk.Tk()

scrolledtext1 = st.ScrolledText(ventana1, width=50, height=10)



def __init__():
    scrolledtext1.grid(column=0, row=0, padx=10, pady=10)
    frameAnalisis()
    ventana1.mainloop()

def frameAnalisis():
    labelframe1 = ttk.LabelFrame(ventana1, text="Análisis")
    labelframe1.grid(column=0, row=1, padx=5, pady=5, sticky="w")
    boton1 = ttk.Button(labelframe1, text="Léxico", command=lexico)
    boton1.grid(column=1, row=4, padx=10, pady=10)

def copiar():
    datos = scrolledtext1.get("0.0", tk.END)
    return datos

def lexico():
    win = tk.Toplevel()
    win.geometry("600x500")
    canvas = tk.Canvas(win, bg='white', width=340, height=100)
    frame = tk.Frame(canvas, width=500, height=400, bd=1)

    vertscroll = tk.Scrollbar(canvas, orient='vertical', command=canvas.yview)
    canvas.configure(yscrollcommand=vertscroll.set)

    win.bind('<Configure>', lambda _: canvas.configure(scrollregion=canvas.bbox("all")))


    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    canvas.create_window((0,0), window=frame, anchor="center")
    vertscroll.pack(side=tk.RIGHT, fill=tk.Y)


    #canvas.configure(background='dark turquoise')
    frame.configure(background='skyblue')
    #tk.Label(frame, text="TOKENS").place(x="200",y=0)
    tk.Label(frame, text="TOKENS",fg="black",    # Foreground
             bg="white",   # Background
             font=("Bahnschrift SemiBold",24)).grid(row=0, column=90)
    texto=copiar()
    salida=imprimirLex(texto)
    sep=salida.strip().split("\n")
    cont=0
    for c in sep:
        tk.Label(frame, text=c, font=("Bahnschrift SemiLight", 10)).grid(row=20+cont, column=90)
        #tk.Label(frame, text=c, font=("Bahnschrift SemiLight", 10)).place(x=0+cont,y=0)
        cont=cont+25


    tk.Button(frame, text="Entendido", command=win.destroy).grid(row=10+cont, column=90)
    #tk.Button(frame, text="Entendido", command=win.destroy).place(x=0+cont,y=0)

    win.rowconfigure(0, weight=10)
    canvas.rowconfigure(1, weight=1)
__init__()







