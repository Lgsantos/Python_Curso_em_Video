from tkinter import *

def analise():

    i = texto_resposta.get()
    
    texto = f'''{i} é de qual tipo? {type(i)}
    {i} é numérico? {i.isnumeric()}
    {i} é alfabético? {i.isalpha()}
    {i} é alfanumérico? {i.isalnum()}
    {i} é ASCII? {i.isascii()}
    {i} é decimal? {i.isdecimal()}
    {i} é dígito? {i.isdigit()}
    {i} é identificador? {i.isidentifier()}
    {i} é escrito em minúsculas? {i.islower()}
    {i} pode ser impresso? {i.isprintable()}
    {i} é um espaço? {i.isspace()}
    {i} é um título? {i.istitle()}
    {i} é escrito em maiúsculas? {i.isupper()}
    {i} é escrito em minúsculas? {i.islower()}'''

    texto_analise['text'] = texto

def opcoes():
    pass

def sair():
    janela.destroy()

    
janela = Tk()
janela.title('Análise de Strings')

moldura = Frame(janela,bg = '#CCFFFF')
moldura.pack()

menu_principal = Menu(moldura)

menu_secundario = Menu(menu_principal, tearoff = 0)
menu_secundario.add_command(label = 'Opção 1', command = opcoes)
menu_secundario.add_command(label = 'Opção 2', command = opcoes)
menu_secundario.add_separator()
menu_secundario.add_command(label = 'Sair', command = sair)
menu_principal.add_cascade(label = 'Opções', menu = menu_secundario)

menu_principal.add_command(label = 'Sair', command = sair)

texto_pergunta = Label(moldura, text='Digite algo para fazer a análise',
                       bg = '#CCFFFF')
texto_pergunta.pack(padx = 10, pady = 5)

texto_resposta = Entry(moldura, width = 20, bg = '#CCFFFF',
                       cursor = 'plus', justify = 'center',
                       relief = 'ridge')
texto_resposta.pack(padx = 10)

botao = Button(moldura, text = "Enviar", command = analise,
               bg = '#99FFFF')
botao.pack(padx = 10, pady = 5)

texto_analise = Label(moldura, text = '', bg = '#CCFFFF')
texto_analise.pack(padx = 10, pady = 5)


janela.config(menu = menu_principal)
janela.mainloop()
