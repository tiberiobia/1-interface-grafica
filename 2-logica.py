import tkinter as tk
from pathlib import Path
corfundo="#8E2CC7"
cortexto="#FFFFFF"

def registrar():
    nome=nome_entry.get()
    password=password_entry.get()
    if password =='' or nome=='':
        msg_label.configure(text='Por favor preencha os dados', fg="red")
    else: 
        ficheiro=Path(r'dados.txt')
        with ficheiro.open('w', encoding='utf-8', errors='ignore') as file:
            file.write(f'{nome}\n')
            file.write(f'{password}\n')
            msg_label.configure(text='Dados registrados com sucesso', fg="green")


#1-criar a variavel que representa a janela
root= tk.Tk()
root.configure(bg=corfundo)
root.title("1-Esqueleto da GUI")
root.geometry("600x300")
#root.state("zoomed")

#Para criar os elementos (widgets) há sempre 2 passos:
# 1-Criar a variavel que representa o widget
# tk.Widget (qual janela? qual texto?)
nome_label=tk.Label(root, text="Digite o seu nome: ",bg=corfundo, fg=cortexto,font=("Arial",14, 'bold'))
# 2-posicionar o widget na janela
nome_label.pack(pady=20)


nome_entry= tk.Entry(root, width=30) # % do ecra
nome_entry.pack()


password_label=tk.Label(root, text="Digite a sua password: ",bg=corfundo, fg=cortexto,font=("Arial",14, 'bold'))
password_label.pack(pady=20)

password_entry= tk.Entry(root, width=30, show='*') # % do ecra / o show transforma td em *
password_entry.pack()

#Botaão
registrar_button=tk.Button(root, text="registrar",width=20, command=registrar)
registrar_button.pack(pady=(25,0))

msg_label=tk.Label (root, text=" ",bg=corfundo, fg=cortexto,font=("Arial",14, 'bold'))
msg_label.pack(pady=30)

#por ultimo: Iniciar o ciclo de eventos, ou seja, abrir a janela
root.mainloop()

