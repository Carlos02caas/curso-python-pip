import utils
from reto_read_csv import read_csv,per_country
import charts

def run():
    country = input('Type Country: ')
    keys,values = read_csv('./data.csv',country.title())
    print(country.title())
    
    if(keys):
        charts.generate_bar_chart(country,keys,values)
    else:
        print("País no encontrado")

    country,percentage = per_country('./data.csv') 
    if(country):
        charts.generate_pie_chart(country,percentage)
    else:
        print("No data")  
    #result = utils.population_by_country(data,country.capitalize())
    #print(result)

if __name__ == '__main__':
    run()