import pandas as pd

# criando o banco de dados no excel com o uso do python
banco_de_dados = pd.read_excel('banco_de_dados.xlsx', engine='openpyxl')

lista = []
new_info_bd = pd.DataFrame(lista, columns=['cinco'])
banco_de_dados = banco_de_dados.append(new_info_bd, ignore_index=True)
banco_de_dados.to_excel('banco_de_dados.xlsx', index=False)

print(banco_de_dados.shape[0] + 1)