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

def sair():
    janela.destroy()

    
janela = Tk()
janela.title('Análise de Strings')
#janela.geometry('300x350')
moldura = Frame(janela,bg = '#CCFFFF')
moldura.pack()

#texto_pergunta = Label(janela, text='Digite algo para fazer a análise')
texto_pergunta = Label(moldura, text='Digite algo para fazer a análise',
                       bg = '#CCFFFF')
#texto_pergunta.grid(column = 0, row = 0, padx = 10, pady = 5)
texto_pergunta.pack(padx = 10, pady = 5)

#texto_resposta = Entry(janela, width = 20)
texto_resposta = Entry(moldura, width = 20, bg = '#CCFFFF',
                       cursor = 'plus', justify = 'center',
                       relief = 'ridge')
#texto_resposta.grid(column = 0, row = 1, padx = 10)
texto_resposta.pack(padx = 10)

#botao = Button(janela, text = "Enviar", command = analise)
botao = Button(moldura, text = "Enviar", command = analise,
               bg = '#99FFFF')
#botao.grid(column = 0, row = 2, padx = 10, pady = 5)
botao.pack(padx = 10, pady = 5)

#texto_analise = Label(janela, text = '')
texto_analise = Label(moldura, text = '', bg = '#CCFFFF')
#texto_analise.grid(column = 0, row = 3, padx = 10, pady = 5)
texto_analise.pack(padx = 10, pady = 5)

#botao_sair = Button(janela, text = 'Sair', command = sair)
botao_sair = Button(moldura, text = 'Sair', command = sair,
                    bg = '#99FFFF')
#botao_sair.grid(column = 0, row = 4, padx = 10, pady = 5)
botao_sair.pack(padx = 10, pady = 5)

janela.mainloop()
