#pip install pandas
#pip install deep-translator
import pandas as pd
from deep_translator import PonsTranslator
#Чтение данных из git репозитория
url = 'https://raw.githubusercontent.com/nsamoilov/statistic/main/coronavirus_dataset4.csv'
df = pd.read_csv(url, delimiter=',')
#Группировка по странам, так как однйо стране отведено 114 строк в файле
group_data = df.groupby(['Country.Region'])
#Сумма всех элементов столбца 'cases' с привязкой к группе (одной стране)
cases_data = group_data.agg({'cases': ['sum']})['cases']['sum']
#Формирования списка стран, перебор двумерного массива для получения ключа
countries_data = list()
for key, item in group_data:
    #Перевод ключа с анлийского на русский с помощью словаря Pons (https://ru.pons.com/перевод)
    translated_word = PonsTranslator(source='english', target='russian').translate(key, return_all=False)
    #Добавление в список строки типа: страна - общее количество заболевших
    countries_data.append(translated_word+'('+str(cases_data[key])+')')

#Формирования различных цветов для отображения    
colors = [plt.cm.Spectral(i/float(len(countries_data))) for i in range(len(countries_data))]
#Отрисовка фигуры
plt.figure(figsize=(12,8), dpi= 80)
squarify.plot(sizes=cases_data, label=countries_data, color=colors, alpha=.8)
plt.title('Количество заболевших по странам')
plt.axis('off')
plt.show()
