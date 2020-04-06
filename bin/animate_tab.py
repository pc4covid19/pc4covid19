from ipywidgets import Button, VBox, Output
from IPython.display import display, HTML
import os
import glob
import subprocess
import time

class AnimateTab(object):

    def __init__(self):
        # self.tab = Output(layout={'height': '600px'})
        # self.tab = Output(layout={'height': 'auto'})

        gen_button = Button(
            description='Generate',
            button_style='success',  # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Generate a MP4 video of cells',
        )
        gen_button.on_click(self.gen_button_cb)

        animate_out = Output(layout={'height': 'auto'})
        animate_out.append_display_data(HTML(filename='doc/animate.html'))

        self.tab = VBox([gen_button, animate_out])

    def gen_button_cb(self, b):
        print('running...')
        tdir = os.path.abspath('tmpdir')
        os.chdir(tdir)
    # os.system('rm -rf tmpdir*')
    # subprocess.Popen(["../bin/myproj", "config.xml"])
        # cmd = 'magick mogrify -format jpg snapshot*.svg'
        # print(cmd)
        # os.system(cmd)
        # cmd = 'mencoder "mf://snapshot*.jpg" -ovc lavc -lavcopts vcodec=mpeg4:vbitrate=10000:mbd=2:trell -mf fps=5:type=jpg -nosound -o out.avi'
        # print(cmd)
        # os.system(cmd)
        # cmd = 'convert out.avi cells.mp4'
        # print(cmd)
        # os.system(cmd)
        # print('done.')


        num_svg = len(glob.glob('snap*.svg'))
        idx_start = 0
        idx_end = num_svg
        for idx in range(idx_start,idx_end):
            fname = "snapshot%08d" % idx
            # cmd = "convert " + fname + ".svg -resize " + str(resize_pct) + "% " + fname + ".jpg &" 
            svg_file = fname + ".svg"
            jpg_file = fname + ".jpg"
            # print("convert " + svg_file + " " + jpg_file)
            # print(cmd)
            #  os.system(cmd)
            # subprocess.Popen(["../bin/myproj", "config.xml"])
            subprocess.Popen(["convert", svg_file, jpg_file])
        print("Converting all svg to jpg...")

        delay = 15  # secs
        # while True:
        for idx in range(num_svg):
            print ("%s" % ( time.ctime(time.time()) ))
            # print(len(glob.glob(os.path.join(".", 'snap*.svg'))))
            num_jpg = len(glob.glob('snap*.jpg'))
            print("%d of %d" % (num_jpg, num_svg))
            time.sleep(delay)
            if num_jpg == num_svg:
                break

        cmd = 'mencoder "mf://snapshot*.jpg" -ovc lavc -lavcopts vcodec=mpeg4:vbitrate=10000:mbd=2:trell -mf fps=5:type=jpg -nosound -o out.avi'
        print(cmd)
        os.system(cmd)
        cmd = 'convert out.avi cells.mp4'
        print(cmd)
        os.system(cmd)
        print('done.')

        # %%HTML
# <video width=500 height=500 controls>
#   <source src="out.mp4" type="video/mp4">
# </video>

        
