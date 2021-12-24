import csv

#função pra importar os dados e exportar para o 'banco'

def main():
    with open("DataScience\Kapitalo\Dados.csv", 'r') as file:
        dados = file.read().split('\n')

    
    rows = []
    for line in dados:
        row = []
        for x in line.split(','):
            row.append(x)
        rows.append(row)

    
    with open("DataScience\Kapitalo\Base.csv", 'w', newline = '') as base:
        writer = csv.writer(base)
        writer.writerows(rows)

if __name__ == '__main__':
    main()