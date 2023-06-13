import numpy as np
from datetime import date
import pandas as pd


#Ler o total de colaboradores da Planilha Excel
C_df = pd.read_excel('ProblemaToy.xlsx',sheet_name=1, names=['Colaborador'])
print("======================================")
print("| C_df                                |")
print("======================================")
print(C_df)
print()


# Ler as áreas da planilha Excel.
A_df = pd.read_excel('ProblemaToy.xlsx',sheet_name=0, names=['Area'])
print("======================================")
print("| A_df                                  |")
print("======================================")
print(A_df)
print()

# Ler os turnos da planilha Excel.
T_df = pd.read_excel('ProblemaToy.xlsx',sheet_name=2, names=['Turno'])
print("======================================")
print("| T_df                                  |")
print("======================================")
print(T_df)
print()

C_d_t_df = pd.read_excel('ProblemaToy.xlsx',sheet_name=3, names=['ColaboradoresDiaTurno'])
print("======================================")
print("|C_d_t_df                                   |")
print("======================================")
print(C_d_t_df)
print()

#colaboradoresCargaHoraria_df = pd.read_excel('ProblemaToy.xlsx',sheet_name=4, names=['ColaboradoresCargaHoraria'])

#print("======================================")
#print("| colaboradoresCargaHoraria_df                                  |")
#print("======================================")
#print(colaboradoresCargaHoraria_df)
#print()


#Dicionário com os dias da semana.
D = ("Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom")
print("======================================")
print("| D                                  |")
print("======================================")
print(D)
print()

#Cria um loop for e aloca os colaboradores no dia e turno de trabalho, puxando os dados da planilha.
#OBS : O arquivo está lendo só o primeiro dia da semana, não esta percorrendo todas as linhas.

#dados = pd.read_excel('ProblemaToy.xlsx',sheet_name=3)
#conjunto = set()

#for index, row in dados.iterrows():
 #   print(row)
  #  Dia = row["Dia"]
   # Turno = row["Turno"]
    #Colaboradores = row["Colaboradores Disponiveis"]
    #conjunto.add((Dia, Turno,Colaboradores))

#print(conjunto)
#print()

#PARÂMETROS

# h[c, d, t] = carga horária máxima (em minutos) do colaborador c no dia d no turno t
dadosminutos = pd.read_excel('ProblemaToy.xlsx',sheet_name=4)
# Cria o dicionário
h = {}

# Itera sobre as linhas do DataFrame
for index, row in dadosminutos.iterrows():
    # Extrai as informações de colaborador, dia e turno
    colaborador = row['Colaborador']
    dia = row['Dia']
    turno = row['Turno']
    
    # Extrai a carga horária máxima
    carga_horaria = row['Carga Horaria Maxima']
    
    # Adiciona a carga horária máxima ao dicionário
    h[(colaborador, dia, turno)] = carga_horaria

# Exibe o dicionário
print("======================================")
print("| h                                  |")
print("======================================")
print(h)
print()

# t[a] = tempo (em minutos) que a área a leva para ser limpada
df_tempoLimpeza = pd.read_excel('ProblemaToy.xlsx')

# Cria um dicionário com o tempo que cada área leva para ser limpa
t_a = dict(zip(df_tempoLimpeza["Area"], df_tempoLimpeza["Tempo_limpeza_em_minutos"]))
print("======================================")
print("| t_a                                  |")
print("======================================")
print(t_a)

#ar[a] = INT prédio no qual a área a está localizado


df_predioArea = pd.read_excel('ProblemaToy.xlsx')
# Criando um dicionário que associa cada área ao prédio correspondente
ar = {}
for index, row in df_predioArea.iterrows():
    area = row['Area']
    predio = row['Predio']
    ar[area] = predio
print("======================================")
print("| ar                                  |")
print("======================================")
print(ar)
print()


# ler as abas 'Área' e 'Colaboradores' do arquivo Excel
df_Fixo = pd.read_excel('ProblemaToy.xlsx', sheet_name=['Area', 'Colaboradores'])

f = {}
if isinstance(df_Fixo, pd.DataFrame):
    # Criar um dicionário para armazenar a fixação dos colaboradores às áreas
    

    # Iterar sobre as linhas do DataFrame
    for index, row in df_Fixo.iterrows():
        # Acessar os dados de cada linha
        colaborador = row['colaborador']
        area = row['Area']
        fixado = row['fixado']

        # Atribuir o valor da fixação no dicionário
        f[(colaborador, area)] = fixado

    # Exibir o dicionário com a fixação dos colaboradores às áreas
    
print("======================================")
print("|   f                                |")
print("======================================")
print(f)
print()




















##quantidade_colaborador = 5
##quantidade_area = 15
##dados_area = tabela_areas['Área']


##Colaborador = list()
##for c in range(quantidade_colaborador):
  ##  Colaborador.append("Colaborador_{}".format(c+1))

##Area = list()
##for a in range(quantidade_area):
##    Area.append(dados_area[a])
##print(Area)
   ## Area.append("Area_{}".format(a+1))
   

##Turno = ("M6", "V15", "N18")
##for t in Turno:
   ## print (t)


##Dia = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")

##print(Colaborador)
##print(Area)
##print(Dia)
##print(Turno)

##print(tabela_colaboradores)

##limpeza_area = [[[0 for t in range(len(Turno))] for d in range(len(Dia))] for a in range(len(Area))]