import matplotlib.pyplot as plt
import os

def generate_bar_chart(name,labels, values):
    os.makedirs('imgs', exist_ok=True)
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.savefig(f'imgs/{name}.png')
    plt.close()

def generate_pie_chart(labels, values):
    os.makedirs('imgs', exist_ok=True)
    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)
    ax.axis('equal')
    plt.savefig('imgs/pie.png')
    plt.close()

if __name__ == '__main__':
    labels = ['a','b','c']
    values = [100,30,80]
    #generate_bar_chart(labels,values)
    generate_pie_chart(labels,values)