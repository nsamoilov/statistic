import matplotlib.patches as patches                                                                                #pip install matplotlib

df_raw = pd.read_csv("https://raw.githubusercontent.com/nsamoilov/statistic/main/coronavirus_dataset3.csv")         #Чтение csv
df = df_raw[['cases', 'Country.Region']].groupby('Country.Region').apply(lambda x: x.mean(numeric_only=False))      #Получение столбцов, группировка
df.sort_values('cases', inplace=True)                                                                               #Сортировка данных
df.reset_index(inplace=True)

fig, ax = plt.subplots(figsize=(11,9), facecolor='white', dpi= 80)                                                  #Формирования рисунка
ax.vlines(x=df.index, ymin=0, ymax=df.cases, color='firebrick', alpha=0.7, linewidth=20)

for i, cases in enumerate(df.cases):                                                                                #Аннотация текста
    ax.text(i, cases+0.5, round(cases, 1), horizontalalignment='center')
max_cases = df['cases'].iloc[-1]                                                                                    #Получение последнего элемента
ax.set_title('Количество заболевших по странам', fontdict={'size':22})                                              #Заголовок графика
ax.set(ylabel='Количество случаев', ylim=(0, max_cases+10))                                                         #Название оси y с вычислением максимального и минимального значения

countries_data = list()                                                                                             #Формирования списка стран, перебор двумерного массива для получения ключа
for item in df['Country.Region']:
    translated_word = PonsTranslator(source='english', target='russian').translate(item, return_all=False)          #Перевод ключа с анлийского на русский с помощью словаря Pons (https://ru.pons.com/перевод)
    countries_data.append(translated_word)  
  
plt.xticks(df.index, countries_data, rotation=60, horizontalalignment='right', fontsize=12)                         #Формирования оси x

p1 = patches.Rectangle((.57, -0.005), width=.33, height=.13, alpha=.1,                                              #Разделение на недопустимые значения, закрасятся в красный
                       facecolor='red', transform=fig.transFigure)    
p2 = patches.Rectangle((.124, -0.005), width=.446, height=.13, alpha=.1,                                            #Разделение на допустимые значения, закрасятся в зеленый
                       facecolor='green', transform=fig.transFigure)
fig.add_artist(p1)                                                                                                  #Размещение допустимых и недопустимых границ
fig.add_artist(p2)
plt.show()       
