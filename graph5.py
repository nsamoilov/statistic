import random
import matplotlib.pyplot as plt                                                                                     #pip install matplotlib
import pandas as pd                                                                                                 #pip install pandas
from deep_translator import PonsTranslator                                                                          #pip install PonsTranslator

url = "https://raw.githubusercontent.com/nsamoilov/statistic/main/coronavirus_dataset3.csv"                         #Ссылка на csv

df = pd.read_csv(url, delimiter=',')                                                                                #Чтение и группировка по странам, так как одной стране отведено 114 строк в файле
group_data = df.groupby(['Country.Region'])                                                 
cases_data = group_data.agg({'cases': ['sum']})['cases']['sum']                                                     #Сумма случаев по одной стране

n = group_data.__len__()+1                                                                                          #Количество стран 
all_colors = list(plt.cm.colors.cnames.keys())                                                                      #Формирование и выбор цвета
random.seed(100)
c = random.choices(all_colors, k=n)

countries_data = list()                                                                                             #Формирования списка стран, перебор двумерного массива для получения ключа
for key, item in group_data:
    translated_word = PonsTranslator(source='english', target='russian').translate(key, return_all=False)           #Перевод ключа с анлийского на русский с помощью словаря Pons (https://ru.pons.com/перевод)
    countries_data.append(translated_word)

plt.figure(figsize=(16,10), dpi= 80)                                                                                #Формирование графика
plt.bar(countries_data, cases_data, color=c, width=.5)
for i, val in enumerate(cases_data.values):                                                                         #Цикл для элементов графика
    plt.text(i, val, val, horizontalalignment='center', 
             verticalalignment='bottom', fontdict={'fontweight':50, 'size':16})

plt.gca().set_xticklabels(countries_data, rotation=60,fontdict={'fontsize': 16}, horizontalalignment= 'right')      #Декорирование графика
plt.title('Количество заболевших по странам', fontsize=22)
plt.ylabel('Количество случаев')
plt.show()                                                                                                          #Показ графика
