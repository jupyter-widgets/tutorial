from bqplot import LinearScale, Axis, Figure, Lines, CATEGORY10
from ipywidgets import Layout

class Chart:
    def __init__(self, figure_title='Line Chart'):
        self._sc_x = LinearScale()
        self._sc_y = LinearScale()
        self._line = Lines(x=[], y=[], labels=['Fake stock price'], display_legend=True,
                         scales={'x': self._sc_x, 'y': self._sc_y})
        self._ax_x = Axis(scale=self._sc_x, label='Index')
        self._ax_y = Axis(scale=self._sc_y, orientation='vertical', label='y-value')
        self._fig = Figure(marks=[self._line], axes=[self._ax_x, self._ax_y], title=figure_title, layout=Layout(flex='1 1 auto', width='100%'))
        
    def get_figure(self):
        return self._fig
    
    def get_line(self):
        return self._line
    
    def set_line(self, x, y, labels, colors):
        self._line.x = x
        self._line.y = y
        self._line.labels = labels
        self._line.colors = colors