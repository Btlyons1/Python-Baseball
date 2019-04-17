import pandas as pd
import matplotlib.pyplot as plt

from data import  games

plays = games[games['type'] == 'play']

strike_outs = plays[plays['event'].strn.contains('K')]
strike_outs = strike_outs.groupby(['year', 'game_id']).size()
strike_outs = strike_outs.reset_index(name='strike_outs')
strike_outs = strike_outs.loc[:, ['year', 'strike_oouts']].apply(pd.to_numeric)
strike_outs.plot(x='year', y='stike_outs', kind='scatter').legend(["strike Outs"])
plt.show()