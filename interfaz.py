import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
from analizadorLexico import imprimirLex
from analizadorSintactico import imprimirSintactico 

ventana1 = tk.Tk()
ventana1.title("Analizador de codigo (PHP)")
ventana1.geometry('450x500')
ventana1.iconbitmap('php.ico')
scrolledtext1 = st.ScrolledText(ventana1, width=50, height=20 )
labelCod=tk.Label(ventana1, text="Ingresa tu codigo: ")




def __init__():
    labelCod.grid(column=0, row=0, padx=10, pady=10)
    scrolledtext1.grid(column=0, row=1, padx=15, pady=15)
    frameAnalisis()
    ventana1.mainloop()

def frameAnalisis():
    labelframe1 = ttk.LabelFrame(ventana1, text="Análisis" )
    labelframe1.grid(column=0, row=2, padx=115, pady=10, sticky="w")
    boton1 = ttk.Button(labelframe1, text="lexico", command=lexico)
    boton1.grid(column=1, row=5, padx=10, pady=10)
    boton2 = ttk.Button(labelframe1, text="sintactico", command=sintactico)
    boton2.grid(column=2, row=5 , padx=10, pady=10)


def sintactico():
    contenedor = tk.Toplevel()
    contenedor.geometry('500x600')
    canvas = tk.Canvas(contenedor, bg='white')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH , expand=1)
    frame = tk.Frame(canvas, bg='skyblue')
    frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    tk.Label(frame, text='Operaciones realizadas',bg='skyblue' ,font= ("Times New Roman", 20)).grid(row=0,column=0, padx=120, pady=20)

    scroll = tk.Scrollbar(canvas, orient= 'vertical' , command = canvas.yview)
    canvas.configure(yscrollcommand = scroll.set)
    contenedor.bind('<Configure>' , lambda _: canvas.configure(scrollregion = canvas.bbox('all')))
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.create_window((0,0), window=frame, anchor='ne')

    texto=copiar().replace('\t',' ').replace('\n',' ')


    buf=imprimirSintactico(texto)
    
    cont=1
    for b in buf:
        tk.Label(frame, text=b, bg='skyblue',font= ("Times New Roman", 10)).grid(row=cont,column=0, pady=10, columnspan=10)
        cont+=1
    
    #Padding del boton
    tk.Label(frame, text="", bg='skyblue',font= ("Times New Roman", 10)).grid(row=cont+1,column=0, pady=5)
    cont+=1
    tk.Button(frame, text="Entendido", command=contenedor.destroy ).grid(row=cont+1, column=0)
    cont+=1
    tk.Label(frame, text="", bg='skyblue',font= ("Times New Roman", 10)).grid(row=cont+1,column=0, pady=5)
        

def copiar():
    datos = scrolledtext1.get("0.0", tk.END)
    return datos

def lexico():
    win = tk.Toplevel()
    win.geometry("300x600") 
    canvas = tk.Canvas(win, bg='skyblue')
    frame = tk.Frame(canvas, bd=1)

    vertscroll = tk.Scrollbar(canvas, orient='vertical', command=canvas.yview)
    canvas.configure(yscrollcommand=vertscroll.set)

    win.bind('<Configure>', lambda _: canvas.configure(scrollregion=canvas.bbox("all")))


    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    frame.pack(fill=tk.BOTH, expand=1)
    canvas.create_window((0,0), window=frame, anchor="w")
    vertscroll.pack(side=tk.RIGHT, fill=tk.Y)

    frame.configure(background='skyblue')
    tk.Label(frame, text="TOKENS", bg="skyblue", font= ("Times New Roman", 20)).grid(row=0, column=0, pady=20)#font=("Bahnschrift SemiBold",24)

    texto=copiar()
    salida=imprimirLex(texto.replace("\t",""))
    sep=salida.strip().split("\n")
    cont=0
    for c in sep:
        tk.Label(frame, bg='skyblue' ,text=formatoLexico(c), font=("Times New Roman", 10)).grid(row=20+cont, column=0)#font=("Bahnschrift SemiLight", 10)
        cont=cont+25

    tk.Button(frame, text="Entendido", command=win.destroy).grid(row=10+cont, column=0)

    win.rowconfigure(0, weight=10)
    canvas.rowconfigure(1, weight=1)

def formatoLexico(s):
    if "LexToken" in s:
        s=s[9:-2].split(',')
        if(s[3]==''):s[3]="0"
        return s[0]+": "+s[1]+" -- (%s,%s)"%(s[2],s[3])
    else: return s


if __name__=="__main__":
    __init__()







