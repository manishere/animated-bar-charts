import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation

plt.rcParams['animation.ffmpeg_path'] = r'C:\\ffmpeg\\bin\\ffmpeg.exe'

df = pd.read_csv('https://git.io/fjpo3', usecols=['name', 'group', 'year', 'value'])

colors = dict(zip(
    ['India','Europe','Asia','Latin America','Middle East','North America','Africa'],
    ['#d40000', '#030000', '#030000', '#030000', '#d40000', '#030000', '#d40000']
))

group_lk = df.set_index('name')['group'].to_dict()

fig, ax = plt.subplots(figsize=(15, 8))

def racing_barchart(year):
    dff = df[df['year'].eq(year)].sort_values(by='value', ascending=True).tail(10)
    ax.clear()
    ax.barh(dff['name'], dff['value'], color=[colors[group_lk[x]] for x in dff['name']])
    dx = dff['value'].max() / 200

    for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
        #print(value-dx,value+dx,i)
        ax.text(value-dx, i, name, size=14, weight=600, ha='right', va='bottom')
        ax.text(value-dx, i-.25, group_lk[name], size=10, color='#000000', ha='right', va='baseline')
        ax.text(value+dx, i, f'{value:,.0f}', size=14, ha='left',  va='center')
    
    ax.text(1, 0.4, year, transform=ax.transAxes, color='#000000', size=46, ha='right', weight=800)
    ax.text(0, 1.06, 'Population (X thousand)', transform=ax.transAxes, size=12, color='#000000')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#000000', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-', color='black')
    ax.set_axisbelow(True)
    ax.text(0, 1.10, 'The most populous cities in the world from 1500 to 2019',
            transform=ax.transAxes, size=20, weight=600, ha='left')
    ax.text(1, 0, 'with <3 by manish', transform=ax.transAxes, ha='right',
            color='#000000', bbox=dict(facecolor='#ffffff', alpha=0.8, edgecolor='#030000'))
    plt.box(True)

plt.xkcd()
fig, ax = plt.subplots(figsize=(15,8))
animator = animation.FuncAnimation(fig, racing_barchart, frames=range(1500, 1600))
mywriter = animation.FFMpegWriter()
plt.show()
#animator.save("F:\\xkcd.mp4")