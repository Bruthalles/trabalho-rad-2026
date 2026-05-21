#Thalles Roberto 202602288249
#Leandro Brene 202408624107
#Monique Meneghini 20230329953
#Nathalia Duarte 202303546981
#Yuri Moura 202502274271
import sqlite3, os, tkinter as tk
from tkinter import ttk

tela = tk.Tk()
tela.geometry("1000x1000")
titulo = tk.Label(tela,text="home")
titulo.pack()
conection = sqlite3.connect('banco.db')
cursor = conection.cursor()

tbl_command = '''CREATE TABLE IF NOT EXISTS Idosos(
                nome TEXT NOT NULL,
                pontuacao INTEGER NOT NULL,
                tarefas TEXT NOT NULL);'''


insert_command = '''INSERT INTO Idosos
                    VALUES('lucas',10,'moveu arquivo');'''

#########################################

cursor.execute('''SELECT * FROM Idosos''')
linhas = cursor.fetchall()

conection.commit()

colunas = ('nome','pontuacao','tarefa')
tabela = ttk.Treeview(tela,columns=colunas,show='headings')
tabela.heading('nome', text='nome')
tabela.heading('pontuacao', text='pontuacao')
tabela.heading('tarefa', text='tarefa')

tabela.column('nome', width=200)
tabela.column('pontuacao', width=200)
tabela.column('tarefa', width=200)

def salvar():
    global nome
    nome =  nomeLogin.get()
    with open('velho.txt','r') as f:
        arquivo = f.readline().strip()
        arquivo2 = f.readline().strip()
    if (nome == arquivo or nome == arquivo2):

        for linha in linhas:
            tabela.insert('', tk.END, values=linha)

        tabela.pack()

    else:
        erro = tk.Label(tela,text="erro")
        erro.pack()

nomeLogin = tk.Entry(tela)
nomeLogin.pack()


botaoLogin = tk.Button(tela, text="entrar",command=salvar)
botaoLogin.pack()

def salvarEmail():
    global nome
    pontuacao = cursor.execute("SELECT pontuacao FROM Idosos WHERE nome = '"+nome+"'").fetchall()
    print(pontuacao[0][0])
    nvpontuacao = pontuacao[0][0] + 20
    cursor.execute('''UPDATE Idosos SET pontuacao = ? WHERE nome = ?
                    ''',(nvpontuacao,nome))
    conection.commit()

    cursor.execute('''SELECT * FROM Idosos''')
    linhas = cursor.fetchall()
    for n,row in enumerate(tabela.get_children()):

        tabela.delete(row)
        tabela.insert('', tk.END, values=linhas[n])
        

botao_email = tk.Button(tela,text="salvar email",command=salvarEmail)
botao_email.pack()
tela.mainloop()

tela2 = tk.Tk()
tela2.geometry("1000x1000")