 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class MicroenvTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}


        menv_var1 = Button(description='virion (virion/micron^3)', disabled=True, layout=name_button_layout)
        menv_var1.style.button_color = 'tan'

        param_name1 = Button(description='diffusion_coefficient', disabled=True, layout=name_button_layout)

        self.virion_diffusion_coefficient = FloatText(value=2.5,
          step=0.1,style=style, layout=widget_layout)

        param_name2 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.virion_decay_rate = FloatText(value=0,
          step=0.01,style=style, layout=widget_layout)
        param_name3 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.virion_initial_condition = FloatText(value=0,style=style, layout=widget_layout)
        param_name4 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.virion_Dirichlet_boundary_condition = FloatText(value=0,style=style, layout=widget_layout)
        self.virion_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)

        menv_var2 = Button(description='assembled_virion (virion/micron^3)', disabled=True, layout=name_button_layout)
        menv_var2.style.button_color = 'lightgreen'

        param_name5 = Button(description='diffusion_coefficient', disabled=True, layout=name_button_layout)

        self.assembled_virion_diffusion_coefficient = FloatText(value=2.5,
          step=0.1,style=style, layout=widget_layout)

        param_name6 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.assembled_virion_decay_rate = FloatText(value=0,
          step=0.01,style=style, layout=widget_layout)
        param_name7 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.assembled_virion_initial_condition = FloatText(value=0,style=style, layout=widget_layout)
        param_name8 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.assembled_virion_Dirichlet_boundary_condition = FloatText(value=0,style=style, layout=widget_layout)
        self.assembled_virion_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)

        menv_var3 = Button(description='interferon_1 (mol/micron^3)', disabled=True, layout=name_button_layout)
        menv_var3.style.button_color = 'tan'

        param_name9 = Button(description='diffusion_coefficient', disabled=True, layout=name_button_layout)

        self.interferon_1_diffusion_coefficient = FloatText(value=25,
          step=1,style=style, layout=widget_layout)

        param_name10 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.interferon_1_decay_rate = FloatText(value=1.02e-2,
          step=0.001,style=style, layout=widget_layout)
        param_name11 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.interferon_1_initial_condition = FloatText(value=0,style=style, layout=widget_layout)
        param_name12 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.interferon_1_Dirichlet_boundary_condition = FloatText(value=0,style=style, layout=widget_layout)
        self.interferon_1_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)

        menv_var4 = Button(description='pro_inflammatory_cytokine (mol/micron^3)', disabled=True, layout=name_button_layout)
        menv_var4.style.button_color = 'lightgreen'

        param_name13 = Button(description='diffusion_coefficient', disabled=True, layout=name_button_layout)

        self.pro_inflammatory_cytokine_diffusion_coefficient = FloatText(value=555.56,
          step=10,style=style, layout=widget_layout)

        param_name14 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.pro_inflammatory_cytokine_decay_rate = FloatText(value=1.02e-2,
          step=0.001,style=style, layout=widget_layout)
        param_name15 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.pro_inflammatory_cytokine_initial_condition = FloatText(value=0,style=style, layout=widget_layout)
        param_name16 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.pro_inflammatory_cytokine_Dirichlet_boundary_condition = FloatText(value=0,style=style, layout=widget_layout)
        self.pro_inflammatory_cytokine_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)

        menv_var5 = Button(description='chemokine (mol/micron^3)', disabled=True, layout=name_button_layout)
        menv_var5.style.button_color = 'tan'

        param_name17 = Button(description='diffusion_coefficient', disabled=True, layout=name_button_layout)

        self.chemokine_diffusion_coefficient = FloatText(value=555.56,
          step=10,style=style, layout=widget_layout)

        param_name18 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.chemokine_decay_rate = FloatText(value=1.02e-2,
          step=0.001,style=style, layout=widget_layout)
        param_name19 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.chemokine_initial_condition = FloatText(value=0,style=style, layout=widget_layout)
        param_name20 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.chemokine_Dirichlet_boundary_condition = FloatText(value=0,style=style, layout=widget_layout)
        self.chemokine_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)

        menv_var6 = Button(description='debris (mol/micron^3)', disabled=True, layout=name_button_layout)
        menv_var6.style.button_color = 'lightgreen'

        param_name21 = Button(description='diffusion_coefficient', disabled=True, layout=name_button_layout)

        self.debris_diffusion_coefficient = FloatText(value=555.56,
          step=10,style=style, layout=widget_layout)

        param_name22 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.debris_decay_rate = FloatText(value=1.02e-2,
          step=0.001,style=style, layout=widget_layout)
        param_name23 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.debris_initial_condition = FloatText(value=0,style=style, layout=widget_layout)
        param_name24 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.debris_Dirichlet_boundary_condition = FloatText(value=0,style=style, layout=widget_layout)
        self.debris_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)

        menv_var7 = Button(description='pro_pyroptosis_cytokine (mol/micron^3)', disabled=True, layout=name_button_layout)
        menv_var7.style.button_color = 'tan'

        param_name25 = Button(description='diffusion_coefficient', disabled=True, layout=name_button_layout)

        self.pro_pyroptosis_cytokine_diffusion_coefficient = FloatText(value=5.56,
          step=0.1,style=style, layout=widget_layout)

        param_name26 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.pro_pyroptosis_cytokine_decay_rate = FloatText(value=1.02e-2,
          step=0.001,style=style, layout=widget_layout)
        param_name27 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.pro_pyroptosis_cytokine_initial_condition = FloatText(value=0,style=style, layout=widget_layout)
        param_name28 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.pro_pyroptosis_cytokine_Dirichlet_boundary_condition = FloatText(value=0,style=style, layout=widget_layout)
        self.pro_pyroptosis_cytokine_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)

        menv_var8 = Button(description='anti_inflammatory_cytokine (mol/micron^3)', disabled=True, layout=name_button_layout)
        menv_var8.style.button_color = 'lightgreen'

        param_name29 = Button(description='diffusion_coefficient', disabled=True, layout=name_button_layout)

        self.anti_inflammatory_cytokine_diffusion_coefficient = FloatText(value=555.56,
          step=10,style=style, layout=widget_layout)

        param_name30 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.anti_inflammatory_cytokine_decay_rate = FloatText(value=1.04e-2,
          step=0.001,style=style, layout=widget_layout)
        param_name31 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.anti_inflammatory_cytokine_initial_condition = FloatText(value=0,style=style, layout=widget_layout)
        param_name32 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.anti_inflammatory_cytokine_Dirichlet_boundary_condition = FloatText(value=0,style=style, layout=widget_layout)
        self.anti_inflammatory_cytokine_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)

        menv_var9 = Button(description='collagen (mol/micron^3)', disabled=True, layout=name_button_layout)
        menv_var9.style.button_color = 'tan'

        param_name33 = Button(description='diffusion_coefficient', disabled=True, layout=name_button_layout)

        self.collagen_diffusion_coefficient = FloatText(value=0,
          step=0.01,style=style, layout=widget_layout)

        param_name34 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.collagen_decay_rate = FloatText(value=0,
          step=0.01,style=style, layout=widget_layout)
        param_name35 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.collagen_initial_condition = FloatText(value=0,style=style, layout=widget_layout)
        param_name36 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.collagen_Dirichlet_boundary_condition = FloatText(value=0,style=style, layout=widget_layout)
        self.collagen_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)

        menv_var10 = Button(description='Ig (mol/micron^3)', disabled=True, layout=name_button_layout)
        menv_var10.style.button_color = 'lightgreen'

        param_name37 = Button(description='diffusion_coefficient', disabled=True, layout=name_button_layout)

        self.Ig_diffusion_coefficient = FloatText(value=6,
          step=0.1,style=style, layout=widget_layout)

        param_name38 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.Ig_decay_rate = FloatText(value=0.00139,
          step=0.0001,style=style, layout=widget_layout)
        param_name39 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.Ig_initial_condition = FloatText(value=0,style=style, layout=widget_layout)
        param_name40 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.Ig_Dirichlet_boundary_condition = FloatText(value=0,style=style, layout=widget_layout)
        self.Ig_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)

        menv_var11 = Button(description='ROS (mol/micron^3)', disabled=True, layout=name_button_layout)
        menv_var11.style.button_color = 'tan'

        param_name41 = Button(description='diffusion_coefficient', disabled=True, layout=name_button_layout)

        self.ROS_diffusion_coefficient = FloatText(value=1e-6,
          step=1e-07,style=style, layout=widget_layout)

        param_name42 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.ROS_decay_rate = FloatText(value=60,
          step=1,style=style, layout=widget_layout)
        param_name43 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.ROS_initial_condition = FloatText(value=0,style=style, layout=widget_layout)
        param_name44 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.ROS_Dirichlet_boundary_condition = FloatText(value=0,style=style, layout=widget_layout)
        self.ROS_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)
        self.calculate_gradient = Checkbox(description='calculate_gradients', disabled=False, layout=desc_button_layout)
        self.track_internal = Checkbox(description='track_in_agents', disabled=False, layout=desc_button_layout)


         #  ------- micronenv info
        menv_units_button1 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        menv_units_button2 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        menv_units_button3 = Button(description='virion/micron^3', disabled=True, layout=units_button_layout) 
        menv_units_button4 = Button(description='virion/micron^3', disabled=True, layout=units_button_layout) 
        menv_units_button5 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        menv_units_button6 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        menv_units_button7 = Button(description='virion/micron^3', disabled=True, layout=units_button_layout) 
        menv_units_button8 = Button(description='virion/micron^3', disabled=True, layout=units_button_layout) 
        menv_units_button9 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        menv_units_button10 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        menv_units_button11 = Button(description='mol/micron^3', disabled=True, layout=units_button_layout) 
        menv_units_button12 = Button(description='mol/micron^3', disabled=True, layout=units_button_layout) 
        menv_units_button13 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        menv_units_button14 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        menv_units_button15 = Button(description='mol/micron^3', disabled=True, layout=units_button_layout) 
        menv_units_button16 = Button(description='mol/micron^3', disabled=True, layout=units_button_layout) 
        menv_units_button17 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        menv_units_button18 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        menv_units_button19 = Button(description='mol/micron^3', disabled=True, layout=units_button_layout) 
        menv_units_button20 = Button(description='mol/micron^3', disabled=True, layout=units_button_layout) 
        menv_units_button21 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        menv_units_button22 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        menv_units_button23 = Button(description='mol/micron^3', disabled=True, layout=units_button_layout) 
        menv_units_button24 = Button(description='mol/micron^3', disabled=True, layout=units_button_layout) 
        menv_units_button25 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        menv_units_button26 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        menv_units_button27 = Button(description='mol/micron^3', disabled=True, layout=units_button_layout) 
        menv_units_button28 = Button(description='mol/micron^3', disabled=True, layout=units_button_layout) 
        menv_units_button29 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        menv_units_button30 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        menv_units_button31 = Button(description='mol/micron^3', disabled=True, layout=units_button_layout) 
        menv_units_button32 = Button(description='mol/micron^3', disabled=True, layout=units_button_layout) 
        menv_units_button33 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        menv_units_button34 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        menv_units_button35 = Button(description='mol/micron^3', disabled=True, layout=units_button_layout) 
        menv_units_button36 = Button(description='mol/micron^3', disabled=True, layout=units_button_layout) 
        menv_units_button37 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        menv_units_button38 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        menv_units_button39 = Button(description='mol/micron^3', disabled=True, layout=units_button_layout) 
        menv_units_button40 = Button(description='mol/micron^3', disabled=True, layout=units_button_layout) 
        menv_units_button41 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        menv_units_button42 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        menv_units_button43 = Button(description='mol/micron^3', disabled=True, layout=units_button_layout) 
        menv_units_button44 = Button(description='mol/micron^3', disabled=True, layout=units_button_layout) 




        row_virion = [menv_var1,  ] 
        row1 = [param_name1, self.virion_diffusion_coefficient, menv_units_button1]
        row2 = [param_name2, self.virion_decay_rate, menv_units_button2]
        row3 = [param_name3, self.virion_initial_condition, menv_units_button3]
        row4 = [param_name4, self.virion_Dirichlet_boundary_condition, menv_units_button4, self.virion_Dirichlet_boundary_condition_toggle]
        row_assembled_virion = [menv_var2,  ] 
        row5 = [param_name5, self.assembled_virion_diffusion_coefficient, menv_units_button5]
        row6 = [param_name6, self.assembled_virion_decay_rate, menv_units_button6]
        row7 = [param_name7, self.assembled_virion_initial_condition, menv_units_button7]
        row8 = [param_name8, self.assembled_virion_Dirichlet_boundary_condition, menv_units_button8, self.assembled_virion_Dirichlet_boundary_condition_toggle]
        row_interferon_1 = [menv_var3,  ] 
        row9 = [param_name9, self.interferon_1_diffusion_coefficient, menv_units_button9]
        row10 = [param_name10, self.interferon_1_decay_rate, menv_units_button10]
        row11 = [param_name11, self.interferon_1_initial_condition, menv_units_button11]
        row12 = [param_name12, self.interferon_1_Dirichlet_boundary_condition, menv_units_button12, self.interferon_1_Dirichlet_boundary_condition_toggle]
        row_pro_inflammatory_cytokine = [menv_var4,  ] 
        row13 = [param_name13, self.pro_inflammatory_cytokine_diffusion_coefficient, menv_units_button13]
        row14 = [param_name14, self.pro_inflammatory_cytokine_decay_rate, menv_units_button14]
        row15 = [param_name15, self.pro_inflammatory_cytokine_initial_condition, menv_units_button15]
        row16 = [param_name16, self.pro_inflammatory_cytokine_Dirichlet_boundary_condition, menv_units_button16, self.pro_inflammatory_cytokine_Dirichlet_boundary_condition_toggle]
        row_chemokine = [menv_var5,  ] 
        row17 = [param_name17, self.chemokine_diffusion_coefficient, menv_units_button17]
        row18 = [param_name18, self.chemokine_decay_rate, menv_units_button18]
        row19 = [param_name19, self.chemokine_initial_condition, menv_units_button19]
        row20 = [param_name20, self.chemokine_Dirichlet_boundary_condition, menv_units_button20, self.chemokine_Dirichlet_boundary_condition_toggle]
        row_debris = [menv_var6,  ] 
        row21 = [param_name21, self.debris_diffusion_coefficient, menv_units_button21]
        row22 = [param_name22, self.debris_decay_rate, menv_units_button22]
        row23 = [param_name23, self.debris_initial_condition, menv_units_button23]
        row24 = [param_name24, self.debris_Dirichlet_boundary_condition, menv_units_button24, self.debris_Dirichlet_boundary_condition_toggle]
        row_pro_pyroptosis_cytokine = [menv_var7,  ] 
        row25 = [param_name25, self.pro_pyroptosis_cytokine_diffusion_coefficient, menv_units_button25]
        row26 = [param_name26, self.pro_pyroptosis_cytokine_decay_rate, menv_units_button26]
        row27 = [param_name27, self.pro_pyroptosis_cytokine_initial_condition, menv_units_button27]
        row28 = [param_name28, self.pro_pyroptosis_cytokine_Dirichlet_boundary_condition, menv_units_button28, self.pro_pyroptosis_cytokine_Dirichlet_boundary_condition_toggle]
        row_anti_inflammatory_cytokine = [menv_var8,  ] 
        row29 = [param_name29, self.anti_inflammatory_cytokine_diffusion_coefficient, menv_units_button29]
        row30 = [param_name30, self.anti_inflammatory_cytokine_decay_rate, menv_units_button30]
        row31 = [param_name31, self.anti_inflammatory_cytokine_initial_condition, menv_units_button31]
        row32 = [param_name32, self.anti_inflammatory_cytokine_Dirichlet_boundary_condition, menv_units_button32, self.anti_inflammatory_cytokine_Dirichlet_boundary_condition_toggle]
        row_collagen = [menv_var9,  ] 
        row33 = [param_name33, self.collagen_diffusion_coefficient, menv_units_button33]
        row34 = [param_name34, self.collagen_decay_rate, menv_units_button34]
        row35 = [param_name35, self.collagen_initial_condition, menv_units_button35]
        row36 = [param_name36, self.collagen_Dirichlet_boundary_condition, menv_units_button36, self.collagen_Dirichlet_boundary_condition_toggle]
        row_Ig = [menv_var10,  ] 
        row37 = [param_name37, self.Ig_diffusion_coefficient, menv_units_button37]
        row38 = [param_name38, self.Ig_decay_rate, menv_units_button38]
        row39 = [param_name39, self.Ig_initial_condition, menv_units_button39]
        row40 = [param_name40, self.Ig_Dirichlet_boundary_condition, menv_units_button40, self.Ig_Dirichlet_boundary_condition_toggle]
        row_ROS = [menv_var11,  ] 
        row41 = [param_name41, self.ROS_diffusion_coefficient, menv_units_button41]
        row42 = [param_name42, self.ROS_decay_rate, menv_units_button42]
        row43 = [param_name43, self.ROS_initial_condition, menv_units_button43]
        row44 = [param_name44, self.ROS_Dirichlet_boundary_condition, menv_units_button44, self.ROS_Dirichlet_boundary_condition_toggle]
        row45 = [self.calculate_gradient,]
        row46 = [self.track_internal,]


        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box_virion = Box(children=row_virion, layout=box_layout)
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box_assembled_virion = Box(children=row_assembled_virion, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box_interferon_1 = Box(children=row_interferon_1, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box_pro_inflammatory_cytokine = Box(children=row_pro_inflammatory_cytokine, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box_chemokine = Box(children=row_chemokine, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)
        box19 = Box(children=row19, layout=box_layout)
        box20 = Box(children=row20, layout=box_layout)
        box_debris = Box(children=row_debris, layout=box_layout)
        box21 = Box(children=row21, layout=box_layout)
        box22 = Box(children=row22, layout=box_layout)
        box23 = Box(children=row23, layout=box_layout)
        box24 = Box(children=row24, layout=box_layout)
        box_pro_pyroptosis_cytokine = Box(children=row_pro_pyroptosis_cytokine, layout=box_layout)
        box25 = Box(children=row25, layout=box_layout)
        box26 = Box(children=row26, layout=box_layout)
        box27 = Box(children=row27, layout=box_layout)
        box28 = Box(children=row28, layout=box_layout)
        box_anti_inflammatory_cytokine = Box(children=row_anti_inflammatory_cytokine, layout=box_layout)
        box29 = Box(children=row29, layout=box_layout)
        box30 = Box(children=row30, layout=box_layout)
        box31 = Box(children=row31, layout=box_layout)
        box32 = Box(children=row32, layout=box_layout)
        box_collagen = Box(children=row_collagen, layout=box_layout)
        box33 = Box(children=row33, layout=box_layout)
        box34 = Box(children=row34, layout=box_layout)
        box35 = Box(children=row35, layout=box_layout)
        box36 = Box(children=row36, layout=box_layout)
        box_Ig = Box(children=row_Ig, layout=box_layout)
        box37 = Box(children=row37, layout=box_layout)
        box38 = Box(children=row38, layout=box_layout)
        box39 = Box(children=row39, layout=box_layout)
        box40 = Box(children=row40, layout=box_layout)
        box_ROS = Box(children=row_ROS, layout=box_layout)
        box41 = Box(children=row41, layout=box_layout)
        box42 = Box(children=row42, layout=box_layout)
        box43 = Box(children=row43, layout=box_layout)
        box44 = Box(children=row44, layout=box_layout)
        box45 = Box(children=row45, layout=box_layout)
        box46 = Box(children=row46, layout=box_layout)

        self.tab = VBox([
          box_virion,
          box1,
          box2,
          box3,
          box4,
          box_assembled_virion,
          box5,
          box6,
          box7,
          box8,
          box_interferon_1,
          box9,
          box10,
          box11,
          box12,
          box_pro_inflammatory_cytokine,
          box13,
          box14,
          box15,
          box16,
          box_chemokine,
          box17,
          box18,
          box19,
          box20,
          box_debris,
          box21,
          box22,
          box23,
          box24,
          box_pro_pyroptosis_cytokine,
          box25,
          box26,
          box27,
          box28,
          box_anti_inflammatory_cytokine,
          box29,
          box30,
          box31,
          box32,
          box_collagen,
          box33,
          box34,
          box35,
          box36,
          box_Ig,
          box37,
          box38,
          box39,
          box40,
          box_ROS,
          box41,
          box42,
          box43,
          box44,
          box45,
          box46,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point

        self.virion_diffusion_coefficient.value = float(vp[0].find('.//diffusion_coefficient').text)
        self.virion_decay_rate.value = float(vp[0].find('.//decay_rate').text)
        self.virion_initial_condition.value = float(vp[0].find('.//initial_condition').text)
        self.virion_Dirichlet_boundary_condition.value = float(vp[0].find('.//Dirichlet_boundary_condition').text)
        if vp[0].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
          self.virion_Dirichlet_boundary_condition_toggle.value = True
        else:
          self.virion_Dirichlet_boundary_condition_toggle.value = False

        self.assembled_virion_diffusion_coefficient.value = float(vp[1].find('.//diffusion_coefficient').text)
        self.assembled_virion_decay_rate.value = float(vp[1].find('.//decay_rate').text)
        self.assembled_virion_initial_condition.value = float(vp[1].find('.//initial_condition').text)
        self.assembled_virion_Dirichlet_boundary_condition.value = float(vp[1].find('.//Dirichlet_boundary_condition').text)
        if vp[1].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
          self.assembled_virion_Dirichlet_boundary_condition_toggle.value = True
        else:
          self.assembled_virion_Dirichlet_boundary_condition_toggle.value = False

        self.interferon_1_diffusion_coefficient.value = float(vp[2].find('.//diffusion_coefficient').text)
        self.interferon_1_decay_rate.value = float(vp[2].find('.//decay_rate').text)
        self.interferon_1_initial_condition.value = float(vp[2].find('.//initial_condition').text)
        self.interferon_1_Dirichlet_boundary_condition.value = float(vp[2].find('.//Dirichlet_boundary_condition').text)
        if vp[2].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
          self.interferon_1_Dirichlet_boundary_condition_toggle.value = True
        else:
          self.interferon_1_Dirichlet_boundary_condition_toggle.value = False

        self.pro_inflammatory_cytokine_diffusion_coefficient.value = float(vp[3].find('.//diffusion_coefficient').text)
        self.pro_inflammatory_cytokine_decay_rate.value = float(vp[3].find('.//decay_rate').text)
        self.pro_inflammatory_cytokine_initial_condition.value = float(vp[3].find('.//initial_condition').text)
        self.pro_inflammatory_cytokine_Dirichlet_boundary_condition.value = float(vp[3].find('.//Dirichlet_boundary_condition').text)
        if vp[3].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
          self.pro_inflammatory_cytokine_Dirichlet_boundary_condition_toggle.value = True
        else:
          self.pro_inflammatory_cytokine_Dirichlet_boundary_condition_toggle.value = False

        self.chemokine_diffusion_coefficient.value = float(vp[4].find('.//diffusion_coefficient').text)
        self.chemokine_decay_rate.value = float(vp[4].find('.//decay_rate').text)
        self.chemokine_initial_condition.value = float(vp[4].find('.//initial_condition').text)
        self.chemokine_Dirichlet_boundary_condition.value = float(vp[4].find('.//Dirichlet_boundary_condition').text)
        if vp[4].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
          self.chemokine_Dirichlet_boundary_condition_toggle.value = True
        else:
          self.chemokine_Dirichlet_boundary_condition_toggle.value = False

        self.debris_diffusion_coefficient.value = float(vp[5].find('.//diffusion_coefficient').text)
        self.debris_decay_rate.value = float(vp[5].find('.//decay_rate').text)
        self.debris_initial_condition.value = float(vp[5].find('.//initial_condition').text)
        self.debris_Dirichlet_boundary_condition.value = float(vp[5].find('.//Dirichlet_boundary_condition').text)
        if vp[5].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
          self.debris_Dirichlet_boundary_condition_toggle.value = True
        else:
          self.debris_Dirichlet_boundary_condition_toggle.value = False

        self.pro_pyroptosis_cytokine_diffusion_coefficient.value = float(vp[6].find('.//diffusion_coefficient').text)
        self.pro_pyroptosis_cytokine_decay_rate.value = float(vp[6].find('.//decay_rate').text)
        self.pro_pyroptosis_cytokine_initial_condition.value = float(vp[6].find('.//initial_condition').text)
        self.pro_pyroptosis_cytokine_Dirichlet_boundary_condition.value = float(vp[6].find('.//Dirichlet_boundary_condition').text)
        if vp[6].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
          self.pro_pyroptosis_cytokine_Dirichlet_boundary_condition_toggle.value = True
        else:
          self.pro_pyroptosis_cytokine_Dirichlet_boundary_condition_toggle.value = False

        self.anti_inflammatory_cytokine_diffusion_coefficient.value = float(vp[7].find('.//diffusion_coefficient').text)
        self.anti_inflammatory_cytokine_decay_rate.value = float(vp[7].find('.//decay_rate').text)
        self.anti_inflammatory_cytokine_initial_condition.value = float(vp[7].find('.//initial_condition').text)
        self.anti_inflammatory_cytokine_Dirichlet_boundary_condition.value = float(vp[7].find('.//Dirichlet_boundary_condition').text)
        if vp[7].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
          self.anti_inflammatory_cytokine_Dirichlet_boundary_condition_toggle.value = True
        else:
          self.anti_inflammatory_cytokine_Dirichlet_boundary_condition_toggle.value = False

        self.collagen_diffusion_coefficient.value = float(vp[8].find('.//diffusion_coefficient').text)
        self.collagen_decay_rate.value = float(vp[8].find('.//decay_rate').text)
        self.collagen_initial_condition.value = float(vp[8].find('.//initial_condition').text)
        self.collagen_Dirichlet_boundary_condition.value = float(vp[8].find('.//Dirichlet_boundary_condition').text)
        if vp[8].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
          self.collagen_Dirichlet_boundary_condition_toggle.value = True
        else:
          self.collagen_Dirichlet_boundary_condition_toggle.value = False

        self.Ig_diffusion_coefficient.value = float(vp[9].find('.//diffusion_coefficient').text)
        self.Ig_decay_rate.value = float(vp[9].find('.//decay_rate').text)
        self.Ig_initial_condition.value = float(vp[9].find('.//initial_condition').text)
        self.Ig_Dirichlet_boundary_condition.value = float(vp[9].find('.//Dirichlet_boundary_condition').text)
        if vp[9].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
          self.Ig_Dirichlet_boundary_condition_toggle.value = True
        else:
          self.Ig_Dirichlet_boundary_condition_toggle.value = False

        self.ROS_diffusion_coefficient.value = float(vp[10].find('.//diffusion_coefficient').text)
        self.ROS_decay_rate.value = float(vp[10].find('.//decay_rate').text)
        self.ROS_initial_condition.value = float(vp[10].find('.//initial_condition').text)
        self.ROS_Dirichlet_boundary_condition.value = float(vp[10].find('.//Dirichlet_boundary_condition').text)
        if vp[10].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
          self.ROS_Dirichlet_boundary_condition_toggle.value = True
        else:
          self.ROS_Dirichlet_boundary_condition_toggle.value = False

        if uep.find('.//options//calculate_gradients').text.lower() == 'true':
          self.calculate_gradient.value = True
        else:
          self.calculate_gradient.value = False
        if uep.find('.//options//track_internalized_substrates_in_each_agent').text.lower() == 'true':
          self.track_internal.value = True
        else:
          self.track_internal.value = False
        


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp[0].find('.//diffusion_coefficient').text = str(self.virion_diffusion_coefficient.value)
        vp[0].find('.//decay_rate').text = str(self.virion_decay_rate.value)
        vp[0].find('.//initial_condition').text = str(self.virion_initial_condition.value)
        vp[0].find('.//Dirichlet_boundary_condition').text = str(self.virion_Dirichlet_boundary_condition.value)
        vp[0].find('.//Dirichlet_boundary_condition').attrib['enabled'] = str(self.virion_Dirichlet_boundary_condition_toggle.value).lower()

        vp[1].find('.//diffusion_coefficient').text = str(self.assembled_virion_diffusion_coefficient.value)
        vp[1].find('.//decay_rate').text = str(self.assembled_virion_decay_rate.value)
        vp[1].find('.//initial_condition').text = str(self.assembled_virion_initial_condition.value)
        vp[1].find('.//Dirichlet_boundary_condition').text = str(self.assembled_virion_Dirichlet_boundary_condition.value)
        vp[1].find('.//Dirichlet_boundary_condition').attrib['enabled'] = str(self.assembled_virion_Dirichlet_boundary_condition_toggle.value).lower()

        vp[2].find('.//diffusion_coefficient').text = str(self.interferon_1_diffusion_coefficient.value)
        vp[2].find('.//decay_rate').text = str(self.interferon_1_decay_rate.value)
        vp[2].find('.//initial_condition').text = str(self.interferon_1_initial_condition.value)
        vp[2].find('.//Dirichlet_boundary_condition').text = str(self.interferon_1_Dirichlet_boundary_condition.value)
        vp[2].find('.//Dirichlet_boundary_condition').attrib['enabled'] = str(self.interferon_1_Dirichlet_boundary_condition_toggle.value).lower()

        vp[3].find('.//diffusion_coefficient').text = str(self.pro_inflammatory_cytokine_diffusion_coefficient.value)
        vp[3].find('.//decay_rate').text = str(self.pro_inflammatory_cytokine_decay_rate.value)
        vp[3].find('.//initial_condition').text = str(self.pro_inflammatory_cytokine_initial_condition.value)
        vp[3].find('.//Dirichlet_boundary_condition').text = str(self.pro_inflammatory_cytokine_Dirichlet_boundary_condition.value)
        vp[3].find('.//Dirichlet_boundary_condition').attrib['enabled'] = str(self.pro_inflammatory_cytokine_Dirichlet_boundary_condition_toggle.value).lower()

        vp[4].find('.//diffusion_coefficient').text = str(self.chemokine_diffusion_coefficient.value)
        vp[4].find('.//decay_rate').text = str(self.chemokine_decay_rate.value)
        vp[4].find('.//initial_condition').text = str(self.chemokine_initial_condition.value)
        vp[4].find('.//Dirichlet_boundary_condition').text = str(self.chemokine_Dirichlet_boundary_condition.value)
        vp[4].find('.//Dirichlet_boundary_condition').attrib['enabled'] = str(self.chemokine_Dirichlet_boundary_condition_toggle.value).lower()

        vp[5].find('.//diffusion_coefficient').text = str(self.debris_diffusion_coefficient.value)
        vp[5].find('.//decay_rate').text = str(self.debris_decay_rate.value)
        vp[5].find('.//initial_condition').text = str(self.debris_initial_condition.value)
        vp[5].find('.//Dirichlet_boundary_condition').text = str(self.debris_Dirichlet_boundary_condition.value)
        vp[5].find('.//Dirichlet_boundary_condition').attrib['enabled'] = str(self.debris_Dirichlet_boundary_condition_toggle.value).lower()

        vp[6].find('.//diffusion_coefficient').text = str(self.pro_pyroptosis_cytokine_diffusion_coefficient.value)
        vp[6].find('.//decay_rate').text = str(self.pro_pyroptosis_cytokine_decay_rate.value)
        vp[6].find('.//initial_condition').text = str(self.pro_pyroptosis_cytokine_initial_condition.value)
        vp[6].find('.//Dirichlet_boundary_condition').text = str(self.pro_pyroptosis_cytokine_Dirichlet_boundary_condition.value)
        vp[6].find('.//Dirichlet_boundary_condition').attrib['enabled'] = str(self.pro_pyroptosis_cytokine_Dirichlet_boundary_condition_toggle.value).lower()

        vp[7].find('.//diffusion_coefficient').text = str(self.anti_inflammatory_cytokine_diffusion_coefficient.value)
        vp[7].find('.//decay_rate').text = str(self.anti_inflammatory_cytokine_decay_rate.value)
        vp[7].find('.//initial_condition').text = str(self.anti_inflammatory_cytokine_initial_condition.value)
        vp[7].find('.//Dirichlet_boundary_condition').text = str(self.anti_inflammatory_cytokine_Dirichlet_boundary_condition.value)
        vp[7].find('.//Dirichlet_boundary_condition').attrib['enabled'] = str(self.anti_inflammatory_cytokine_Dirichlet_boundary_condition_toggle.value).lower()

        vp[8].find('.//diffusion_coefficient').text = str(self.collagen_diffusion_coefficient.value)
        vp[8].find('.//decay_rate').text = str(self.collagen_decay_rate.value)
        vp[8].find('.//initial_condition').text = str(self.collagen_initial_condition.value)
        vp[8].find('.//Dirichlet_boundary_condition').text = str(self.collagen_Dirichlet_boundary_condition.value)
        vp[8].find('.//Dirichlet_boundary_condition').attrib['enabled'] = str(self.collagen_Dirichlet_boundary_condition_toggle.value).lower()

        vp[9].find('.//diffusion_coefficient').text = str(self.Ig_diffusion_coefficient.value)
        vp[9].find('.//decay_rate').text = str(self.Ig_decay_rate.value)
        vp[9].find('.//initial_condition').text = str(self.Ig_initial_condition.value)
        vp[9].find('.//Dirichlet_boundary_condition').text = str(self.Ig_Dirichlet_boundary_condition.value)
        vp[9].find('.//Dirichlet_boundary_condition').attrib['enabled'] = str(self.Ig_Dirichlet_boundary_condition_toggle.value).lower()

        vp[10].find('.//diffusion_coefficient').text = str(self.ROS_diffusion_coefficient.value)
        vp[10].find('.//decay_rate').text = str(self.ROS_decay_rate.value)
        vp[10].find('.//initial_condition').text = str(self.ROS_initial_condition.value)
        vp[10].find('.//Dirichlet_boundary_condition').text = str(self.ROS_Dirichlet_boundary_condition.value)
        vp[10].find('.//Dirichlet_boundary_condition').attrib['enabled'] = str(self.ROS_Dirichlet_boundary_condition_toggle.value).lower()


        uep.find('.//options//calculate_gradients').text = str(self.calculate_gradient.value)
        uep.find('.//options//track_internalized_substrates_in_each_agent').text = str(self.track_internal.value)
