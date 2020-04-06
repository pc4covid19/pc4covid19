 
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


        menv_var1 = Button(description='virion (virion/um^3)', disabled=True, layout=name_button_layout)
        menv_var1.style.button_color = 'tan'

        param_name1 = Button(description='diffusion_coefficient', disabled=True, layout=name_button_layout)

        self.virion_diffusion_coefficient = FloatText(value=900.0,
          step=10,style=style, layout=widget_layout)

        param_name2 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.virion_decay_rate = FloatText(value=0,
          step=0.01,style=style, layout=widget_layout)
        param_name3 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.virion_initial_condition = FloatText(value=0,style=style, layout=widget_layout)
        param_name4 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.virion_Dirichlet_boundary_condition = FloatText(value=0,style=style, layout=widget_layout)
        self.virion_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)

        menv_var2 = Button(description='uncoated_virion (virion/um^3)', disabled=True, layout=name_button_layout)
        menv_var2.style.button_color = 'lightgreen'

        param_name5 = Button(description='diffusion_coefficient', disabled=True, layout=name_button_layout)

        self.uncoated_virion_diffusion_coefficient = FloatText(value=900.0,
          step=10,style=style, layout=widget_layout)

        param_name6 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.uncoated_virion_decay_rate = FloatText(value=3.5e-4,
          step=0.0001,style=style, layout=widget_layout)
        param_name7 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.uncoated_virion_initial_condition = FloatText(value=0,style=style, layout=widget_layout)
        param_name8 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.uncoated_virion_Dirichlet_boundary_condition = FloatText(value=0,style=style, layout=widget_layout)
        self.uncoated_virion_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)

        menv_var3 = Button(description='viral_RNA (mRNA/um^3)', disabled=True, layout=name_button_layout)
        menv_var3.style.button_color = 'tan'

        param_name9 = Button(description='diffusion_coefficient', disabled=True, layout=name_button_layout)

        self.viral_RNA_diffusion_coefficient = FloatText(value=9000.0,
          step=100,style=style, layout=widget_layout)

        param_name10 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.viral_RNA_decay_rate = FloatText(value=3.5e-4,
          step=0.0001,style=style, layout=widget_layout)
        param_name11 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.viral_RNA_initial_condition = FloatText(value=0,style=style, layout=widget_layout)
        param_name12 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.viral_RNA_Dirichlet_boundary_condition = FloatText(value=0,style=style, layout=widget_layout)
        self.viral_RNA_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)

        menv_var4 = Button(description='viral_protein (protein/um^3)', disabled=True, layout=name_button_layout)
        menv_var4.style.button_color = 'lightgreen'

        param_name13 = Button(description='diffusion_coefficient', disabled=True, layout=name_button_layout)

        self.viral_protein_diffusion_coefficient = FloatText(value=9000.0,
          step=100,style=style, layout=widget_layout)

        param_name14 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.viral_protein_decay_rate = FloatText(value=3.5e-4,
          step=0.0001,style=style, layout=widget_layout)
        param_name15 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.viral_protein_initial_condition = FloatText(value=0,style=style, layout=widget_layout)
        param_name16 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.viral_protein_Dirichlet_boundary_condition = FloatText(value=0,style=style, layout=widget_layout)
        self.viral_protein_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)

        menv_var5 = Button(description='assembled_virion (virion/um^3)', disabled=True, layout=name_button_layout)
        menv_var5.style.button_color = 'tan'

        param_name17 = Button(description='diffusion_coefficient', disabled=True, layout=name_button_layout)

        self.assembled_virion_diffusion_coefficient = FloatText(value=900.0,
          step=10,style=style, layout=widget_layout)

        param_name18 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.assembled_virion_decay_rate = FloatText(value=0,
          step=0.01,style=style, layout=widget_layout)
        param_name19 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.assembled_virion_initial_condition = FloatText(value=0,style=style, layout=widget_layout)
        param_name20 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.assembled_virion_Dirichlet_boundary_condition = FloatText(value=0,style=style, layout=widget_layout)
        self.assembled_virion_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)
        self.calculate_gradient = Checkbox(description='calculate_gradients', disabled=False, layout=desc_button_layout)
        self.track_internal = Checkbox(description='track_in_agents', disabled=False, layout=desc_button_layout)


         #  ------- micronenv info
        menv_units_button1 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        menv_units_button2 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        menv_units_button3 = Button(description='virion/um^3', disabled=True, layout=units_button_layout) 
        menv_units_button4 = Button(description='virion/um^3', disabled=True, layout=units_button_layout) 
        menv_units_button5 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        menv_units_button6 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        menv_units_button7 = Button(description='virion/um^3', disabled=True, layout=units_button_layout) 
        menv_units_button8 = Button(description='virion/um^3', disabled=True, layout=units_button_layout) 
        menv_units_button9 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        menv_units_button10 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        menv_units_button11 = Button(description='mRNA/um^3', disabled=True, layout=units_button_layout) 
        menv_units_button12 = Button(description='mRNA/um^3', disabled=True, layout=units_button_layout) 
        menv_units_button13 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        menv_units_button14 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        menv_units_button15 = Button(description='protein/um^3', disabled=True, layout=units_button_layout) 
        menv_units_button16 = Button(description='protein/um^3', disabled=True, layout=units_button_layout) 
        menv_units_button17 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        menv_units_button18 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        menv_units_button19 = Button(description='virion/um^3', disabled=True, layout=units_button_layout) 
        menv_units_button20 = Button(description='virion/um^3', disabled=True, layout=units_button_layout) 




        row_virion = [menv_var1,  ] 
        row1 = [param_name1, self.virion_diffusion_coefficient, menv_units_button1]
        row2 = [param_name2, self.virion_decay_rate, menv_units_button2]
        row3 = [param_name3, self.virion_initial_condition, menv_units_button3]
        row4 = [param_name4, self.virion_Dirichlet_boundary_condition, menv_units_button4, self.virion_Dirichlet_boundary_condition_toggle]
        row_uncoated_virion = [menv_var2,  ] 
        row5 = [param_name5, self.uncoated_virion_diffusion_coefficient, menv_units_button5]
        row6 = [param_name6, self.uncoated_virion_decay_rate, menv_units_button6]
        row7 = [param_name7, self.uncoated_virion_initial_condition, menv_units_button7]
        row8 = [param_name8, self.uncoated_virion_Dirichlet_boundary_condition, menv_units_button8, self.uncoated_virion_Dirichlet_boundary_condition_toggle]
        row_viral_RNA = [menv_var3,  ] 
        row9 = [param_name9, self.viral_RNA_diffusion_coefficient, menv_units_button9]
        row10 = [param_name10, self.viral_RNA_decay_rate, menv_units_button10]
        row11 = [param_name11, self.viral_RNA_initial_condition, menv_units_button11]
        row12 = [param_name12, self.viral_RNA_Dirichlet_boundary_condition, menv_units_button12, self.viral_RNA_Dirichlet_boundary_condition_toggle]
        row_viral_protein = [menv_var4,  ] 
        row13 = [param_name13, self.viral_protein_diffusion_coefficient, menv_units_button13]
        row14 = [param_name14, self.viral_protein_decay_rate, menv_units_button14]
        row15 = [param_name15, self.viral_protein_initial_condition, menv_units_button15]
        row16 = [param_name16, self.viral_protein_Dirichlet_boundary_condition, menv_units_button16, self.viral_protein_Dirichlet_boundary_condition_toggle]
        row_assembled_virion = [menv_var5,  ] 
        row17 = [param_name17, self.assembled_virion_diffusion_coefficient, menv_units_button17]
        row18 = [param_name18, self.assembled_virion_decay_rate, menv_units_button18]
        row19 = [param_name19, self.assembled_virion_initial_condition, menv_units_button19]
        row20 = [param_name20, self.assembled_virion_Dirichlet_boundary_condition, menv_units_button20, self.assembled_virion_Dirichlet_boundary_condition_toggle]
        row21 = [self.calculate_gradient,]
        row22 = [self.track_internal,]


        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box_virion = Box(children=row_virion, layout=box_layout)
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box_uncoated_virion = Box(children=row_uncoated_virion, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box_viral_RNA = Box(children=row_viral_RNA, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box_viral_protein = Box(children=row_viral_protein, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box_assembled_virion = Box(children=row_assembled_virion, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)
        box19 = Box(children=row19, layout=box_layout)
        box20 = Box(children=row20, layout=box_layout)
        box21 = Box(children=row21, layout=box_layout)
        box22 = Box(children=row22, layout=box_layout)

        self.tab = VBox([
          box_virion,
          box1,
          box2,
          box3,
          box4,
          box_uncoated_virion,
          box5,
          box6,
          box7,
          box8,
          box_viral_RNA,
          box9,
          box10,
          box11,
          box12,
          box_viral_protein,
          box13,
          box14,
          box15,
          box16,
          box_assembled_virion,
          box17,
          box18,
          box19,
          box20,
          box21,
          box22,
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

        self.uncoated_virion_diffusion_coefficient.value = float(vp[1].find('.//diffusion_coefficient').text)
        self.uncoated_virion_decay_rate.value = float(vp[1].find('.//decay_rate').text)
        self.uncoated_virion_initial_condition.value = float(vp[1].find('.//initial_condition').text)
        self.uncoated_virion_Dirichlet_boundary_condition.value = float(vp[1].find('.//Dirichlet_boundary_condition').text)
        if vp[1].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
          self.uncoated_virion_Dirichlet_boundary_condition_toggle.value = True
        else:
          self.uncoated_virion_Dirichlet_boundary_condition_toggle.value = False

        self.viral_RNA_diffusion_coefficient.value = float(vp[2].find('.//diffusion_coefficient').text)
        self.viral_RNA_decay_rate.value = float(vp[2].find('.//decay_rate').text)
        self.viral_RNA_initial_condition.value = float(vp[2].find('.//initial_condition').text)
        self.viral_RNA_Dirichlet_boundary_condition.value = float(vp[2].find('.//Dirichlet_boundary_condition').text)
        if vp[2].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
          self.viral_RNA_Dirichlet_boundary_condition_toggle.value = True
        else:
          self.viral_RNA_Dirichlet_boundary_condition_toggle.value = False

        self.viral_protein_diffusion_coefficient.value = float(vp[3].find('.//diffusion_coefficient').text)
        self.viral_protein_decay_rate.value = float(vp[3].find('.//decay_rate').text)
        self.viral_protein_initial_condition.value = float(vp[3].find('.//initial_condition').text)
        self.viral_protein_Dirichlet_boundary_condition.value = float(vp[3].find('.//Dirichlet_boundary_condition').text)
        if vp[3].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
          self.viral_protein_Dirichlet_boundary_condition_toggle.value = True
        else:
          self.viral_protein_Dirichlet_boundary_condition_toggle.value = False

        self.assembled_virion_diffusion_coefficient.value = float(vp[4].find('.//diffusion_coefficient').text)
        self.assembled_virion_decay_rate.value = float(vp[4].find('.//decay_rate').text)
        self.assembled_virion_initial_condition.value = float(vp[4].find('.//initial_condition').text)
        self.assembled_virion_Dirichlet_boundary_condition.value = float(vp[4].find('.//Dirichlet_boundary_condition').text)
        if vp[4].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
          self.assembled_virion_Dirichlet_boundary_condition_toggle.value = True
        else:
          self.assembled_virion_Dirichlet_boundary_condition_toggle.value = False

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

        vp[1].find('.//diffusion_coefficient').text = str(self.uncoated_virion_diffusion_coefficient.value)
        vp[1].find('.//decay_rate').text = str(self.uncoated_virion_decay_rate.value)
        vp[1].find('.//initial_condition').text = str(self.uncoated_virion_initial_condition.value)
        vp[1].find('.//Dirichlet_boundary_condition').text = str(self.uncoated_virion_Dirichlet_boundary_condition.value)
        vp[1].find('.//Dirichlet_boundary_condition').attrib['enabled'] = str(self.uncoated_virion_Dirichlet_boundary_condition_toggle.value).lower()

        vp[2].find('.//diffusion_coefficient').text = str(self.viral_RNA_diffusion_coefficient.value)
        vp[2].find('.//decay_rate').text = str(self.viral_RNA_decay_rate.value)
        vp[2].find('.//initial_condition').text = str(self.viral_RNA_initial_condition.value)
        vp[2].find('.//Dirichlet_boundary_condition').text = str(self.viral_RNA_Dirichlet_boundary_condition.value)
        vp[2].find('.//Dirichlet_boundary_condition').attrib['enabled'] = str(self.viral_RNA_Dirichlet_boundary_condition_toggle.value).lower()

        vp[3].find('.//diffusion_coefficient').text = str(self.viral_protein_diffusion_coefficient.value)
        vp[3].find('.//decay_rate').text = str(self.viral_protein_decay_rate.value)
        vp[3].find('.//initial_condition').text = str(self.viral_protein_initial_condition.value)
        vp[3].find('.//Dirichlet_boundary_condition').text = str(self.viral_protein_Dirichlet_boundary_condition.value)
        vp[3].find('.//Dirichlet_boundary_condition').attrib['enabled'] = str(self.viral_protein_Dirichlet_boundary_condition_toggle.value).lower()

        vp[4].find('.//diffusion_coefficient').text = str(self.assembled_virion_diffusion_coefficient.value)
        vp[4].find('.//decay_rate').text = str(self.assembled_virion_decay_rate.value)
        vp[4].find('.//initial_condition').text = str(self.assembled_virion_initial_condition.value)
        vp[4].find('.//Dirichlet_boundary_condition').text = str(self.assembled_virion_Dirichlet_boundary_condition.value)
        vp[4].find('.//Dirichlet_boundary_condition').attrib['enabled'] = str(self.assembled_virion_Dirichlet_boundary_condition_toggle.value).lower()


        uep.find('.//options//calculate_gradients').text = str(self.calculate_gradient.value)
        uep.find('.//options//track_internalized_substrates_in_each_agent').text = str(self.track_internal.value)
