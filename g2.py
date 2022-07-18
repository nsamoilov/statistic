import matplotlib.pyplot as plt                                                                                 #pip install matplotlib
from itertools import groupby                                                                                   #pip install itertools
import pandas as pd                                                                                             #pip install pandas
from deep_translator import PonsTranslator                                                                      #pip install deep_translator

df_raw = pd.read_csv("https://raw.githubusercontent.com/nsamoilov/statistic/main/coronavirus_dataset3.csv")     #Чтение данных из csv
dfGrouped = df_raw[['cases', 'Country.Region']].groupby('Country.Region')                                       #Получение столбцов, группировка
df = dfGrouped.apply(lambda x: x.sum(numeric_only=False))                                                       #Сумма случаев в серии
df.sort_values('cases', inplace=True)                                                                           #Сортировка   

fig, ax = plt.subplots(figsize=(16,10), dpi= 80)                                                                #формирование графика
ax.vlines(x=df.index, ymin=0, ymax=df.cases, color='firebrick', alpha=0.7, linewidth=2)
ax.scatter(x=df.index, y=df.cases, s=75, color='firebrick', alpha=0.7)

countries_data = list()                                                                                         #Формирования списка стран, перебор двумерного массива для получения ключа
for key, item in dfGrouped:
    translated_word = PonsTranslator(source='english', target='russian').translate(key, return_all=False)       #Перевод ключа с анлийского на русский с помощью словаря Pons (https://ru.pons.com/перевод)
    countries_data.append(translated_word)  

max_cases = df['cases'].iloc[-1]                                                                                #Получение последнего элемента в отсортированном массиве (максмального) 

ax.set_title('Количество заболевших по странам', fontdict={'size':22})                                          #Декорирование графика
ax.set_ylabel('Количество случаев')
ax.set_xticks(df.index)
plt.xticks(df.index, countries_data, rotation=60, horizontalalignment='right', fontsize=12)                     #Формирования оси x
ax.set_ylim(0,max_cases+1000)                                                                                   #Ограничение по Y

for row in df.itertuples():                                                                                     #Формирование подписей
    ax.text(row.Index, row.cases+.5, s=round(row.cases, 2), horizontalalignment= 'center', verticalalignment='bottom', fontsize=14)

plt.show()                                                                                                      #Показ графика
