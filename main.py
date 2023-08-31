# importando o tkinter
from cgitb import text
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox

# importando tkcalendar
from tkcalendar import Calendar, DateEntry


################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

################# criando janela ###############

janela = Tk()
janela.title("")
janela.geometry('1043x453')
janela.configure(background=co9)
janela.resizable(width=True, height=True)

################# dividindo janela ###############

#frame_cima
frame_cima = Frame(janela, width=500, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

#frame_baixo
frame_baixo = Frame(janela, width=500, height=648, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

frame_direita = Frame(janela, width=700, height=648, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, sticky=NSEW)

################# Label Cima ###############
app_nome = Label(frame_cima, text='Formulário',
                 anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
app_nome.place(x=10, y=20)

#variavel tree global
global tree





################# Configurando Frame Baixo ###############

# Nome
# Número do Processo
l_numero_processo = Label(frame_baixo, text='Nº Processo*', anchor=NW,
               font=('Ivy 8 bold'), bg=co1, fg=co4, relief='flat')
l_numero_processo.place(x=10, y=10)
e_numero_processo = Entry(frame_baixo, width= 24, justify='left', relief='solid')
e_numero_processo.place(x=10, y=35)

#Tipo de Processo
l_tipo_processo = Label(frame_baixo, text='Tipo Processo*', anchor=NW,
               font=('Ivy 8 bold'), bg=co1, fg=co4, relief='flat')
l_tipo_processo.place(x=180, y=10)
e_tipo_processo = Entry(frame_baixo, width= 50, justify='left', relief='solid')
e_tipo_processo.place(x=180, y=35)

#Ação
l_acao = Label(frame_baixo, text='Tipo de Ação*', anchor=NW,
               font=('Ivy 8 bold'), bg=co1, fg=co4, relief='flat')
l_acao.place(x=10, y=80)
e_acao = Entry(frame_baixo, width= 24, justify='left', relief='solid')
e_acao.place(x=10, y=105)

#Regulado
l_regulado = Label(frame_baixo, text='Regulado*', anchor=NW,
               font=('Ivy 8 bold'), bg=co1, fg=co4, relief='flat')
l_regulado.place(x=180, y=80)
e_regulado = Entry(frame_baixo,width= 24, justify='left', relief='solid')
e_regulado.place(x=180, y=105)

#Data Análise
l_data_analise = Label(frame_baixo, text='Data de Análise*', anchor=NW,
               font=('Ivy 8 bold'), bg=co1, fg=co4, relief='flat')
l_data_analise.place(x=335, y=80)
e_data_analise = DateEntry(frame_baixo, width=21, background='darkblue',
                  foreground='white', borderwidth=2, year=2023, locale = 'pt_BR', date_patern ='dd.mm.yyyy')
e_data_analise.place(x=335, y=105)

#Protocolo da Análise
l_protocolo_da_analise = Label(frame_baixo, text='Protocolo da Análise*', anchor=NW,
               font=('Ivy 8 bold'), bg=co1, fg=co4, relief='flat')
l_protocolo_da_analise.place(x=10, y=150)
e_protocolo_da_analise = Entry(frame_baixo, width= 24, justify='left', relief='solid')
e_protocolo_da_analise.place(x=10, y=175)

#Nome do Analista
l_nome_analista = Label(frame_baixo, text='Nome do Analista*', anchor=NW,
               font=('Ivy 8 bold'), bg=co1, fg=co4, relief='flat')
l_nome_analista.place(x=180, y=150)
e_nome_analista = Entry(frame_baixo, width= 50, justify='left', relief='solid')
e_nome_analista.place(x=180, y=175)

#Numero do Ofício Encaminhado
l_numero_oficio_encaminhado = Label(frame_baixo, text='Nº Ofício Encaminhado*', anchor=NW,
               font=('Ivy 8 bold'), bg=co1, fg=co4, relief='flat')
l_numero_oficio_encaminhado.place(x=10, y=220)
e_numero_oficio_encaminhado = Entry(frame_baixo, width= 24, justify='left', relief='solid')
e_numero_oficio_encaminhado.place(x=10, y=245)

#Processo Encerrado?
l_processo_encerrado = Label(frame_baixo, text='Processo Encerrado?*', anchor=NW,
               font=('Ivy 8 bold'), bg=co1, fg=co4, relief='flat')
l_processo_encerrado.place(x=180, y=220)
e_processo_encerrado = Entry(frame_baixo, width= 24, justify='left', relief='solid')
e_processo_encerrado.place(x=180, y=245)

#Data da Intimação Cumprida
l_data_intimacao_cumprida = Label(frame_baixo, text='Data Intimação Cumprida', anchor=NW,
               font=('Ivy 8 bold'), bg=co1, fg=co4, relief='flat')
l_data_intimacao_cumprida.place(x=335, y=220)
e_data_intimacao_cumprida = DateEntry(frame_baixo, width=21, background='darkblue',
                  foreground='white', borderwidth=2, year=2023, locale = 'pt_BR', date_patern ='dd.mm.yyyy')
e_data_intimacao_cumprida.place(x=335, y=245)

#Data Prazo Para Resposta
l_data_prazo_resposta = Label(frame_baixo, text='Prazo para Resposta', anchor=NW,
               font=('Ivy 8 bold'), bg=co1, fg=co4, relief='flat')
l_data_prazo_resposta.place(x=10, y=290)
e_data_prazo_resposta = DateEntry(frame_baixo, width=21, background='darkblue',
                  foreground='white', borderwidth=2, year=2023, locale = 'pt_BR', date_patern ='dd.mm.yyyy')
e_data_prazo_resposta.place(x=10, y=315)

#Protocolo Medida Administrativa 
l_protocolo_medida_administrativa = Label(frame_baixo, text='Protocolo Medida Admin.', anchor=NW,
               font=('Ivy 8 bold'), bg=co1, fg=co4, relief='flat')
l_protocolo_medida_administrativa.place(x=180, y=290)
e_protocolo_medida_administrativa = Entry(frame_baixo, width= 24, justify='left', relief='solid')
e_protocolo_medida_administrativa.place(x=180, y=315)

#Medidas a Serem Tomadas
l_medidas_serem_tomadas = Label(frame_baixo, text='Medidas a Serem Tomadas', anchor=NW,
               font=('Ivy 8 bold'), bg=co1, fg=co4, relief='flat')
l_medidas_serem_tomadas.place(x=335, y=290)
e_medidas_serem_tomadas = Entry(frame_baixo, width= 24, justify='left', relief='solid')
e_medidas_serem_tomadas.place(x=335, y=315)

#CapitulaçãoProtocolo da Análise
l_capitulacao = Label(frame_baixo, text='Capitulação', anchor=NW,
               font=('Ivy 8 bold'), bg=co1, fg=co4, relief='flat')
l_capitulacao.place(x=10, y=360)
e_capitulacao = Entry(frame_baixo, width= 32, justify='left', relief='solid')
e_capitulacao.place(x=10, y=385)

#Data da Efetiva Resposta do Regulado
l_data_efetiva_resposta = Label(frame_baixo, text='Data da Efetiva Resposta do Regulado', anchor=NW,
               font=('Ivy 8 bold'), bg=co1, fg=co4, relief='flat')
l_data_efetiva_resposta.place(x=225, y=360)
e_data_efetiva_resposta = DateEntry(frame_baixo, width=40, background='darkblue',
                  foreground='white', borderwidth=2, year=2023, locale = 'pt_BR', date_patern ='dd.mm.yyyy')
e_data_efetiva_resposta.place(x=225, y=385)

#Data Limite de Implementação das Medidas
l_data_limite_implementacao = Label(frame_baixo, text='Data da Efetiva Resposta do Regulado', anchor=NW,
               font=('Ivy 8 bold'), bg=co1, fg=co4, relief='flat')
l_data_limite_implementacao.place(x=10, y=430)
e_data_limite_implementacao = DateEntry(frame_baixo, width=30, background='darkblue',
                  foreground='white', borderwidth=2, year=2023, locale = 'pt_BR', date_patern ='dd.mm.yyyy')
e_data_limite_implementacao.place(x=10, y=455)

#Data da Efetiva Implementação
l_data_efetiva_implementacao = Label(frame_baixo, text='Data da Efetiva Implementação das Medidas', anchor=NW,
               font=('Ivy 8 bold'), bg=co1, fg=co4, relief='flat')
l_data_efetiva_implementacao.place(x=225, y=430)
e_data_efetiva_implementacao = DateEntry(frame_baixo, width=40, background='darkblue',
                  foreground='white', borderwidth=2, year=2023, locale = 'pt_BR', date_patern ='dd.mm.yyyy')
e_data_efetiva_implementacao.place(x=225, y=455)

# Botão Inserir
b_inserir = Button(frame_baixo, command=   '', text='Inserir', width=18, font=(
'Ivy 8 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
b_inserir.place(x=30, y=515)

# Botão Atualizar
b_atualizar = Button(frame_baixo, command='',text='Atualizar', width=18, font=(
    'Ivy 8 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
b_atualizar.place(x=170, y=515)

# Botão Deletar
b_deletar = Button(frame_baixo, command='',text='Deletar', width=18, font=(
    'Ivy 8 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
b_deletar.place(x=310, y=515)



#################Frame Direita###############

def mostrar():
    
    global tree

    lista = (
        [1, 'teste1','teste1','teste1','teste1','teste1','teste1','teste1','teste1','teste1','teste1', 'teste1', 'teste1', 'teste1', 'teste1', 'teste1', 'teste1','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [2, 'teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2','teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2', 'teste2','teste1'],
        [3, 'teste3','teste3','teste3','teste3','teste3','teste3','teste3','teste3','teste3','teste3', 'teste3', 'teste3', 'teste3', 'teste3', 'teste3', 'teste3','teste1']
        
             )
    # lista para cabeçalho
    tabela_head = ['ID', 'Nº Processo', 'Tipo Processo', 'Tipo de Ação', 'Regulado', 'Data Análise', 'Protocolo da Análise', 'Nome do Analista', 'Nº Ofício Encaminhado', 'Processo Encerrado?', 'Data Intimação Cumprida', 'Data do Prazo p/ Resposta', 'Protocolo da Medida Admin.', 'Medidas a Serem Tomadas', 'Capitulacao', 'Data Efetiva Resposta do Regulado', 'Data Limite Implementação das Medidas', 'Data Efetiva Implementação']

    # criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended",
                        columns=tabela_head, show="headings")
    
    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)
   
    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)
 
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0,weight=12)
    
    

    # para configurar o cabeçalho
    hd = ["nw", "nw", "nw", "nw", "nw", "center", "center","nw", "nw", "nw", "nw", "nw", "center", "center", "nw", "nw", "nw","nw"]
    h = [30, 170, 140, 100, 120, 50, 100,100, 120, 50, 100,100, 120, 50, 100,100, 120, 50]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    # inserção dos valores na coluna
    for item in lista:
        tree.insert('', 'end', values=item)

#Chamando a função mostrar
mostrar()

janela.mainloop()

