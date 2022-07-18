import pandas as pd                                                                                         #pip install pandas
from deep_translator import PonsTranslator                                                                  #pip install deep-translator
import matplotlib.pyplot as plt                                                                             #pip install matplotlib
import squarify                                                                                             #pip install squarify

url = 'https://raw.githubusercontent.com/nsamoilov/statistic/main/coronavirus_dataset3.csv'                 #ссылка git репозитория
df = pd.read_csv(url, delimiter=',')                                                                        #Чтение данных из git репозитория
group_data = df.groupby(['Country.Region'])                                                                 #Группировка по странам, так как однйо стране отведено 114 строк в файле
cases_data = group_data.agg({'cases': ['sum']})['cases']['sum']                                             #Сумма всех элементов столбца 'cases' с привязкой к группе (одной стране)

countries_data = list()                                                                                     #Формирования списка стран, перебор двумерного массива для получения ключа
for key, item in group_data:                                                                                #Перевод ключа с анлийского на русский с помощью словаря Pons (https://ru.pons.com/перевод)
    translated_word = PonsTranslator(source='english', target='russian').translate(key, return_all=False)
    countries_data.append(translated_word+'('+str(cases_data[key])+')')                                     #Добавление в список строки типа: страна - общее количество заболевших
   
colors = [plt.cm.Spectral(i/float(len(countries_data))) for i in range(len(countries_data))]                #Формирования различных цветов для отображения 

plt.figure(figsize=(12,8), dpi= 80)                                                                         #Отрисовка фигуры
squarify.plot(sizes=cases_data, label=countries_data, color=colors, alpha=.8)
plt.title('Количество заболевших по странам')
plt.axis('off')
plt.show()
