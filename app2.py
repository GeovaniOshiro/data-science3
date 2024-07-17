import pandas as pd
import tkinter as tk

def mostrar():
    ler = pd.read_excel('dados.xlsx')
    text.delete(1.0, tk.END)
    text.insert(tk.END, ler) 

janela = tk.Tk()
janela.title('Exibição de Dados Excel')

btn = tk.Button(janela, text='Carregar Dados', command=mostrar)
btn.grid(pady=10)

text = tk.Text(janela, width=100, height=20)
text.grid(pady=10, padx=10)

janela.mainloop()
