import csv

def read_csv(path, country):

    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        header_clean = [h.strip() for h in header]
        country_dict={}
        for row in reader:
            row_clean = [c.strip() for c in row]
            iterable = zip(header_clean,row_clean)
            if(country in row_clean):
                country_dict = {key.replace("Population", ""): int(value) for key,value in iterable if 'Population' in key and 'World' not in key}
    return country_dict.keys(),country_dict.values()

def per_country(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        header_clean = [h.strip() for h in header]
        country_dict={}
        for row in reader:
            row_clean = [c.strip() for c in row]
            iterable = zip(header_clean,row_clean)
            
            pais = next(valor for clave, valor in iterable if clave == "Country/Territory")
            porcentaje = next(valor for clave, valor in iterable if clave == "World Population Percentage")

            country_dict[pais] = float(porcentaje)

    return country_dict.keys(),country_dict.values()

if __name__ == '__main__':
    #keys, values = read_csv('./app/data.csv','Angola')
    keys, values = per_country('./app/data.csv')
    print(keys,values)