from ipywidgets import Output, Tab, Layout
from IPython.display import display, HTML

class AboutTab(object):

    def __init__(self):
        # self.tab = Output(layout={'height': '900px'})
        # self.tab = Output(layout={height=’85%’,min_height=’350px’})
        # self.background = Output(layout={'height': 'auto'})
        # self.legend = Output(layout={'height': 'auto'})
        self.tab = Output(layout={'height': 'auto'})

        # self.tab.append_display_data(HTML(filename='doc/about-good.html'))
        # self.tab.append_display_data(HTML(filename='doc/about-bad.html'))
        # self.background.append_display_data(HTML(filename='doc/about_background.html'))
        # self.legend.append_display_data(HTML(filename='doc/about_legend.html'))
        self.tab.append_display_data(HTML(filename='doc/about.html'))
        
        # tab_layout = Layout(width='auto',height='auto', overflow_y='scroll',)   # border='2px solid black',
        # titles = ['Background', 'Legend']
        # self.tab = Tab(children=[self.background, self.legend],
        #            _titles={i: t for i, t in enumerate(titles)},
        #            layout=tab_layout)
