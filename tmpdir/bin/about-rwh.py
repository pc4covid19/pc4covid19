from ipywidgets import Output
from IPython.display import display, HTML

class AboutTab(object):

    def __init__(self):
        # self.tab = Output(layout={'height': '900px'})
        # self.tab = Output(layout={height=’85%’,min_height=’350px’})
        self.tab = Output(layout={'height': 'auto'})

        # self.tab.append_display_data(HTML(filename='doc/about-good.html'))
        # self.tab.append_display_data(HTML(filename='doc/about-bad.html'))
        # self.tab.append_display_data(HTML(filename='doc/about_with_img.html'))
        self.tab.append_display_data(HTML(filename='doc/about-yafei2.html'))
        
