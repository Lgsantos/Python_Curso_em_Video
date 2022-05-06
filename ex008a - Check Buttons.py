from tkinter import *

def escolhas():
    if int(var1.get()) and int(var2.get()):
        conversor()
    elif int(var1.get()) and not int(var2.get()):
        conversor_cent()
    elif not int(var1.get()) and int(var2.get()):
        conversor_mil()
    else:
        medida_convertida['text'] = ''

def conversor_cent():
    c = int(medida.get()) * 100
##    m = medida * 1000
    texto = f'{medida.get()} metros equivale a {c} centímetros.'
    medida_convertida['text'] = texto

def conversor_mil():
##    c = medida * 100
    m = int(medida.get()) * 1000
    texto = f'{medida.get()} metros equivale a {m} milímetros.'
    medida_convertida['text'] = texto

def conversor():
    c = int(medida.get()) * 100
    m = int(medida.get()) * 1000
    texto = f'{medida.get()} metros equivale a {c} centímetros e a {m} milímetros.'
    medida_convertida['text'] = texto
    
def sair():
    janela.destroy()


janela = Tk()
janela.title('Conversor de unidades')

moldura = Frame(janela, bg = '#CCFFFF')
moldura.pack()

menu = Menu(moldura)
menu.add_command(label = 'Sair', command = sair)

pergunta = Label(moldura, text = 'Qual é a medida em metros?',
                 bg = '#CCFFFF')
pergunta.pack(padx = 10, pady = 5)
medida = Entry(moldura, width = 10, bg = '#CCFFFF',
                 cursor = 'dotbox', justify = 'center')
medida.pack(padx = 10, pady = 5)
pergunta1 = Label(moldura, text = 'Converter para:', bg = '#CCFFFF')
pergunta1.pack()

var1 = IntVar()
var2 = IntVar()

chkbutton1 = Checkbutton(moldura, text = 'Centímetros', variable = var1,
                         command = escolhas, bg = '#CCFFFF')
chkbutton1.pack(padx = 10, pady = 5)

chkbutton2 = Checkbutton(moldura, text = 'Milímetros', variable = var2,
                         command = escolhas, bg = '#CCFFFF')
chkbutton2.pack(padx = 10, pady = 5)

medida_convertida = Label(moldura, text = '', bg = '#CCFFFF')
medida_convertida.pack()

janela.config(menu = menu)
janela.mainloop()
