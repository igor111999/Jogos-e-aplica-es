#!/usr/bin/env python
# coding: utf-8

# ### Criação da Janela

# In[6]:


from tkinter import *

######## funcionalidades do sistema #############
import pyodbc

dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=tabuada.db")

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()


#     print(caixa_texto.get('1.0', END))
#     print(numero1.get())
#     print(sinal.get())
#     print(numero2.get())
#     print(sinaligual.get())

def adicionar_insumo():
    cursor.execute(f'''
    INSERT INTO Tabuada (numero1, sinal, numero2, sinaligual)
    VALUES
    ("{numero1.get()}", {sinal.get()}, "{numero2.get()}", {sinaligual.get()})
    ''')
    cursor.commit()

    # deletar tudo da caixa de texto
    caixa_texto.delete("1.0", END)

    # escrever na caixa de texto
    caixa_texto.insert("1.0", f"{numero1.get()} adicionado com sucesso!")


def somar():
    if numero1 != " ":
        caixa_texto.delete("1.0", END)
        caixa_texto.insert("1.0", f"numero1 inválido!")
        if numero1.isnumeric() == True or numero1.isdigit() == False:
            pass
        elif numero1.isalpha() == False:
            while numero1.isalpha() == False:
                numero = input('digite um numero')
                return
        else:
            while numero1 == " ":
                numero = input('digite um numero')
                return

    # deletar o insumo
    cursor.execute(f'''
    DELETE FROM tabuada 
    WHERE Produto="{numero1.get()}"
    ''')
    cursor.commit()

    # deletar tudo da caixa de texto
    caixa_texto.delete("1.0", END)

    # escrever na caixa de texto
    caixa_texto.insert("1.0", f"{numero1.get()} deletado com sucesso!")


def sinal1():
    if sinal != " ":
        if sinal1.isnumeric() == True or numero.isdigit() == False:
            caixa_texto.insert("1.0", f"sinal inválido!")
            return
        elif sinal.isalpha() == False:
            while sinal.isalpha() == False:
                caixa_texto.insert("1.0", f"sinal inválido!")
                return
        else:
            while sinal == "+" or "-" or "*":
                pass

    # deletar tudo da caixa de texto
    caixa_texto.delete("1.0", END)

    # escrever na caixa de texto
    #caixa_texto.insert("1.0", f"{nome_insumo.get()} foi consumido em {qtde_insumo.get()} unidades!")

def numerod():
    if numero2 != " ":
        caixa_texto.delete("1.0", END)
        if numero2.isnumeric() == True or numero.isdigit() == False:
            pass
        elif numero2.isalpha() == True:
            while numero2.isalpha() == True:
                caixa_texto.insert("1.0", f"numero inválido!")
                return
        else:
            while numero2 == " ":
                return


def igual():
    if sinal != " ":
        if sinal.isnumeric() == True or sinal.isdigit() == False:
            caixa_texto.insert("1.0", f"sinal inválido!")
            return
        elif sinal.isalpha() == False:
            while sinal.isalpha() == False:
                caixa_texto.insert("1.0", f"sinal inválido!")
                return
        else:
            while sinal == "=":
                pass

    # pesquisar pelo insumo
    #cursor.execute(f'SELECT * FROM Estoque WHERE Produto="{sinaligual.get()}"')
    #valores = cursor.fetchall()

    texto = ""
    for numero, operação, numer2o, resltado in valores:
        texto = texto + f'''
        -----
        numero: {numero1}
        operação: {sinal}
        numer2o: {numero2}
        resultado: {sinaligual}
        '''

    # deletar tudo da caixa de texto
    caixa_texto.delete("1.0", END)
    # escrever na caixa de texto
    caixa_texto.insert("1.0", texto)


######### criação da Janela ##################

window = Tk()

window.geometry("711x646")
window.configure(bg="#ffffff")
canvas = Canvas(
    window,
    bg="#ffffff",
    height=646,
    width=711,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"janela/background2.png")
background = canvas.create_image(
    355.5, 323.0,
    image=background_img)

img0 = PhotoImage(file=f"janela/img20.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=igual,
    relief="flat")

b0.place(
    x=479, y=195,
    width=178,
    height=38)

img1 = PhotoImage(file=f"janela/img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=sinal1,
    relief="flat")

b1.place(
    x=247, y=197,
    width=178,
    height=36)

img2 = PhotoImage(file=f"janela/img2.png")
b2 = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=numerod,
    relief="flat")

b2.place(
    x=479, y=123,
    width=178,
    height=35)

img3 = PhotoImage(file=f"janela/img3.png")
b3 = Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command=somar,
    relief="flat")

b3.place(
    x=247, y=125,
    width=178,
    height=34)

entry0_img = PhotoImage(file=f"janela/img_textBox0.png")
entry0_bg = canvas.create_image(
    455.0, 560.0,
    image=entry0_img)

caixa_texto = Text(
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

caixa_texto.place(
    x=250, y=502,
    width=410,
    height=114)

entry1_img = PhotoImage(file=f"janela/img_textBox1.png")
entry1_bg = canvas.create_image(
    517.0, 294.5,
    image=entry1_img)

numero1 = Entry(
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

numero1.place(
    x=377, y=278,
    width=280,
    height=31)

entry2_img = PhotoImage(file=f"janela/img_textBox2.png")
entry2_bg = canvas.create_image(
    517.0, 340.5,
    image=entry2_img)

sinal = Entry(
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

sinal.place(
    x=377, y=324,
    width=280,
    height=31)

entry3_img = PhotoImage(file=f"janela/img_textBox3.png")
entry3_bg = canvas.create_image(
    517.0, 388.5,
    image=entry3_img)

numero2 = Entry(
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

numero2.place(
    x=377, y=372,
    width=280,
    height=31)

entry4_img = PhotoImage(file=f"janela/img_textBox4.png")
entry4_bg = canvas.create_image(
    517.0, 436.5,
    image=entry4_img)

sinaligual = Entry(
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

sinaligual.place(
    x=377, y=420,
    width=280,
    height=31)

window.resizable(False, False)
window.mainloop()

cursor.close()
conexao.close()

# In[ ]:


# In[ ]:




