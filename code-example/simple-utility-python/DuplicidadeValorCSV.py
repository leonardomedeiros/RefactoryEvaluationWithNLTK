import sys
import csv

def carregaCsv(filepath):
    with open(filepath,"rt",encoding='utf-8') as arquivo:
        leitor = csv.reader(x.replace('\0', '') for x in arquivo)
        dados = retornaDados(leitor)
    return dados

def retornaDados(leitor):

    dados = []
    
    lista_colunas = next(leitor)
    
    for i in lista_colunas:
        print("%d - %s" %(lista_colunas.index(i),i))

    index_coluna_escolhida = int (input("Digite o numero correspondente a coluna para verificar duplicidades: "))  
    if index_coluna_escolhida >= 0 and index_coluna_escolhida < len(lista_colunas):
        for linha in leitor:
            dados.append(linha[index_coluna_escolhida])
        return dados
    else:
        print("ERRO! Coluna inválida!")
        
def retornaDuplicados(dados):

    unico = []
    duplicados = []
    
    for x in dados:
        if x not in unico:
            unico.append(x)
        else:
            if x not in duplicados:
                duplicados.append(x)
                
    return duplicados

while(1):
    
    filepath = input("Informe o caminho do arquivo .csv (ex. C:/QueryResults.csv):")
    
    if filepath == 'sair':
        break
    
    dados = carregaCsv(filepath)
    
    if dados != None:
        duplicidades = retornaDuplicados(dados)
        if duplicidades == []:
            print("\nNão foi encontrado nehuma Duplicidade\n")
        else:
            print("Duplicidades encontradas:\n")
            for i in duplicidades:
                print(i)
            print("\nQuantidades de Valores Duplicados: %d" %(len(duplicidades)))
            
    print("\nDigite sair para encerrar!\n")
