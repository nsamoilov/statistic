import plotly                                                                                             #pip install plotly
import plotly.graph_objs as go                                                                            
import pandas as pd                                                                                       #pip install pandas
from deep_translator import PonsTranslator                                                                #pip install deep_translator

url = 'https://raw.githubusercontent.com/nsamoilov/statistic/main/coronavirus_dataset3.csv' 
df = pd.read_csv(url, delimiter=',')                                                                      #Чтение и группировка по странам, так как однйо стране отведено 114 строк в файле
group_data = df.groupby(['Country.Region'])                                                 
cases_data = group_data.agg({'cases': ['sum']})['cases']['sum']                                           #Сумма всех элементов столбца 'cases' с привязкой к группе (одной стране)
countries_data = list()                                                                                   #Формирования списка стран, перебор двумерного массива для получения ключа
for key, item in group_data:
    translated_word = PonsTranslator(source='english', target='russian').translate(key, return_all=False) #Перевод ключа с анлийского на русский с помощью словаря Pons (https://ru.pons.com/перевод)
    countries_data.append(translated_word+'('+str(cases_data[key])+')')                                   #Добавление в список строки типа: страна - общее количество заболевших

fig = go.Figure()                                                                                         #Отрисовка графика
fig.add_trace(go.Pie(values=cases_data, labels=countries_data))
fig.show()
