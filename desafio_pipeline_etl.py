#Sistema de Hotelaria
#Desafio Proposto 'Santander Dev Week 2023' 

import pandas as pd
import json
df = pd.read_csv('BD2023.csv')
print(df)

def get_user_id(id):
  linha_filtrada = df[df['ID'] == 3]
  if not linha_filtrada.empty:
    print("ID encontrado:")
    print(linha_filtrada)
  else:
    print("ID não encontrado.")
get_user_id(id)

def update_user(novo_nome, novo_sobrenome):
  id_desejado = 3
  linha_a_atualizar = df[df['ID'] == 3]
# Atualiza os valores de nome e sobrenome na linha
  df.loc[df['ID'] == id_desejado, 'Nome'] = novo_nome
  df.loc[df['ID'] == id_desejado, 'Sobrenome'] = novo_sobrenome

# Salva o DataFrame de volta no arquivo CSV, sem index
  df.to_csv('BD2023.csv', index=False)

  print("Linha atualizada com sucesso.")

# Chama a função para atualizar os valores
update_user("Marlene","Juliete")
# Imprime o DataFrame após a atualização
print(df)

def get_valor_total_aluguel_id(id):
  global df

  linha_filtrada = df[df['ID'] == 3]
  if not linha_filtrada.empty:
    print("ID encontrado:")
    print(linha_filtrada)
  else:
    print("ID não encontrado.")
    
  for index, row in linha_filtrada.iterrows():
      valor_diaria = row['Valor Diaria']  # Obtém o valor da coluna 'valor diaria'
      dias_alugados = row['Dias Alugados'] # Obtém o valor da coluna 'dias alugados'
      valor_total = valor_diaria * dias_alugados
      print(valor_diaria, dias_alugados)
      print("Valor total do aluguel:", valor_total)
      
get_valor_total_aluguel_id(id)

def delete_id(id):
  global df
  df = df[df['ID'] != 7]

df.to_csv('BD2023.csv', index=False)
print("Linha deletada com sucesso.")
delete_id(7)
print(df)

json_data = df.to_json(orient='records', indent=4)
with open('dados.json', 'r', encoding='utf-8',) as json_file:
    data = json.load(json_file)

print("Arquivo JSON gerado com sucesso.")
print(json_data)