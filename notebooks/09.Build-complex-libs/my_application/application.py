from IPython.display import display
from ipywidgets import HBox, VBox, HTML
from ipydatagrid import DataGrid
from bqplot import CATEGORY10
from .chart import Chart
import numpy as np

class MyApplication:
    def __init__(self, data, application_title='My complex application'):
        self.dataframe = data
        self.datagrid = self.process_data(data)
        self.chart = Chart()
        self.app_title = HTML(value=f"<h1 style='color: salmon'>{application_title}</h1><h2>Select a column to plot it</h2>")
        self.run_application()
        
    def process_data(self, dataframe):
        return DataGrid(dataframe, selection_mode='column')
        
    def generate_layout(self):
        return VBox([self.app_title, HBox([self.datagrid, self.chart.get_figure()])])
    
    def setup_event_handlers(self):
        self.datagrid.observe(self.plot_stock, names='selections')
    
    def run_application(self):
        self.setup_event_handlers()
        display(self.generate_layout())
        
    # Callbacks section
    def plot_stock(self, *args):
        column_index = self.datagrid.selections[0]['c1']
        line = self.chart.get_line()
        selected_values = self.datagrid.selected_cell_values
        self.chart.set_line(
            range(len(selected_values)), 
            selected_values, 
            [self.dataframe.columns[column_index]], 
            [CATEGORY10[np.random.randint(0, len(CATEGORY10)) % len(CATEGORY10)]]
        )