import plotly.plotly as py
from plotly.graph_objs import Figure,Data,Scatter
from random import randint
import time
t=1

my_data = Data([Scatter(x=[],y=[], 
                stream=dict(token='akxp47t0xu'))])
my_fig = Figure(data=my_data)
py.plot(my_fig)
s = py.Stream('akxp47t0xu')
s.open()
while True:
	p = randint(1,9)
	s.write(dict(x=t+1,y=p))
	t= t+1
	time.sleep(1)
s.close()
