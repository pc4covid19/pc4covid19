 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

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
        divider_button_layout={'width':'40%'}

        param_name1 = Button(description='random_seed', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.random_seed = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        div_row1 = Button(description='---Virus Replication---', disabled=True, layout=divider_button_layout)

        param_name2 = Button(description='virion_uncoating_rate', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.virion_uncoating_rate = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        param_name3 = Button(description='uncoated_to_RNA_rate', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.uncoated_to_RNA_rate = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        param_name4 = Button(description='protein_synthesis_rate', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.protein_synthesis_rate = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        param_name5 = Button(description='virion_assembly_rate', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.virion_assembly_rate = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        div_row2 = Button(description='---Virus Adsorption and Export---', disabled=True, layout=divider_button_layout)

        param_name6 = Button(description='virion_export_rate', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.virion_export_rate = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        div_row3 = Button(description='---ACE2 receptor dynamics with virus binding---', disabled=True, layout=divider_button_layout)

        param_name7 = Button(description='ACE2_receptors_per_cell', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.ACE2_receptors_per_cell = FloatText(
          value=1000,
          step=100,
          style=style, layout=widget_layout)

        param_name8 = Button(description='ACE2_binding_rate', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.ACE2_binding_rate = FloatText(
          value=0.001,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name9 = Button(description='ACE2_endocytosis_rate', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.ACE2_endocytosis_rate = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        param_name10 = Button(description='ACE2_cargo_release_rate', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.ACE2_cargo_release_rate = FloatText(
          value=0.001,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name11 = Button(description='ACE2_recycling_rate', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.ACE2_recycling_rate = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        div_row4 = Button(description='---Apoptotic Response---', disabled=True, layout=divider_button_layout)

        param_name12 = Button(description='max_infected_apoptosis_rate', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.max_infected_apoptosis_rate = FloatText(
          value=0.001,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name13 = Button(description='max_apoptosis_half_max', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.max_apoptosis_half_max = FloatText(
          value=500,
          step=10,
          style=style, layout=widget_layout)

        param_name14 = Button(description='apoptosis_hill_power', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'tan'

        self.apoptosis_hill_power = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name15 = Button(description='virus_fraction_released_at_death', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'lightgreen'

        self.virus_fraction_released_at_death = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        div_row5 = Button(description='---Initialization Options--', disabled=True, layout=divider_button_layout)

        param_name16 = Button(description='multiplicity_of_infection', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'tan'

        self.multiplicity_of_infection = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        param_name17 = Button(description='use_single_infected_cell', disabled=True, layout=name_button_layout)
        param_name17.style.button_color = 'lightgreen'

        self.use_single_infected_cell = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        div_row6 = Button(description='---Visualization Options---', disabled=True, layout=divider_button_layout)

        param_name18 = Button(description='color_variable', disabled=True, layout=name_button_layout)
        param_name18.style.button_color = 'tan'

        self.color_variable = Text(
          value='assembled virion',
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'lightgreen'
        units_button3 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'tan'
        units_button4 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'lightgreen'
        units_button5 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'tan'
        units_button6 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'lightgreen'
        units_button7 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'tan'
        units_button10 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'lightgreen'
        units_button11 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'tan'
        units_button12 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'lightgreen'
        units_button13 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'tan'
        units_button14 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'lightgreen'
        units_button15 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'lightgreen'
        units_button16 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'tan'
        units_button17 = Button(description='virion', disabled=True, layout=units_button_layout) 
        units_button17.style.button_color = 'lightgreen'
        units_button18 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button18.style.button_color = 'tan'
        units_button19 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button19.style.button_color = 'lightgreen'
        units_button20 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button20.style.button_color = 'lightgreen'
        units_button21 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button21.style.button_color = 'tan'
        units_button22 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button22.style.button_color = 'lightgreen'
        units_button23 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button23.style.button_color = 'lightgreen'
        units_button24 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button24.style.button_color = 'tan'

        desc_button1 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='rate at which an internalized virion is uncoated', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='rate at which uncoated virion makes its mRNA available', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='rate at mRNA creates complete set of proteins', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='rate at which viral proteins are assembled into complete virion', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='rate at which a virion is exported from a live cell', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='number of ACE2 receptors per cell', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='ACE2 receptor-virus binding rate', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='ACE2 receptor-virus endocytosis rate', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='ACE2 receptor-virus cargo release rate', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='ACE2 receptor recycling rate', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='maximum rate of cell apoptosis due to viral infection', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='viral load at which cells reach half max apoptosis rate', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='Hill power for viral load apoptosis response', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button15 = Button(description='fraction of internal virus released at cell death', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'
        desc_button16 = Button(description='multiplicity of infection: virions/cells at t=0', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'
        desc_button17 = Button(description='Infect center cell with one virion (overrides MOI)', disabled=True, layout=desc_button_layout) 
        desc_button17.style.button_color = 'lightgreen'
        desc_button18 = Button(description='color cells based on this variable', disabled=True, layout=desc_button_layout) 
        desc_button18.style.button_color = 'tan'

        row1 = [param_name1, self.random_seed, units_button1, desc_button1] 
        row2 = [param_name2, self.virion_uncoating_rate, units_button3, desc_button2] 
        row3 = [param_name3, self.uncoated_to_RNA_rate, units_button4, desc_button3] 
        row4 = [param_name4, self.protein_synthesis_rate, units_button5, desc_button4] 
        row5 = [param_name5, self.virion_assembly_rate, units_button6, desc_button5] 
        row6 = [param_name6, self.virion_export_rate, units_button8, desc_button6] 
        row7 = [param_name7, self.ACE2_receptors_per_cell, units_button10, desc_button7] 
        row8 = [param_name8, self.ACE2_binding_rate, units_button11, desc_button8] 
        row9 = [param_name9, self.ACE2_endocytosis_rate, units_button12, desc_button9] 
        row10 = [param_name10, self.ACE2_cargo_release_rate, units_button13, desc_button10] 
        row11 = [param_name11, self.ACE2_recycling_rate, units_button14, desc_button11] 
        row12 = [param_name12, self.max_infected_apoptosis_rate, units_button16, desc_button12] 
        row13 = [param_name13, self.max_apoptosis_half_max, units_button17, desc_button13] 
        row14 = [param_name14, self.apoptosis_hill_power, units_button18, desc_button14] 
        row15 = [param_name15, self.virus_fraction_released_at_death, units_button19, desc_button15] 
        row16 = [param_name16, self.multiplicity_of_infection, units_button21, desc_button16] 
        row17 = [param_name17, self.use_single_infected_cell, units_button22, desc_button17] 
        row18 = [param_name18, self.color_variable, units_button24, desc_button18] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)

        self.tab = VBox([
          box1,
          div_row1,
          box2,
          box3,
          box4,
          box5,
          div_row2,
          box6,
          div_row3,
          box7,
          box8,
          box9,
          box10,
          box11,
          div_row4,
          box12,
          box13,
          box14,
          box15,
          div_row5,
          box16,
          box17,
          div_row6,
          box18,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.random_seed.value = int(uep.find('.//random_seed').text)
        self.virion_uncoating_rate.value = float(uep.find('.//virion_uncoating_rate').text)
        self.uncoated_to_RNA_rate.value = float(uep.find('.//uncoated_to_RNA_rate').text)
        self.protein_synthesis_rate.value = float(uep.find('.//protein_synthesis_rate').text)
        self.virion_assembly_rate.value = float(uep.find('.//virion_assembly_rate').text)
        self.virion_export_rate.value = float(uep.find('.//virion_export_rate').text)
        self.ACE2_receptors_per_cell.value = float(uep.find('.//ACE2_receptors_per_cell').text)
        self.ACE2_binding_rate.value = float(uep.find('.//ACE2_binding_rate').text)
        self.ACE2_endocytosis_rate.value = float(uep.find('.//ACE2_endocytosis_rate').text)
        self.ACE2_cargo_release_rate.value = float(uep.find('.//ACE2_cargo_release_rate').text)
        self.ACE2_recycling_rate.value = float(uep.find('.//ACE2_recycling_rate').text)
        self.max_infected_apoptosis_rate.value = float(uep.find('.//max_infected_apoptosis_rate').text)
        self.max_apoptosis_half_max.value = float(uep.find('.//max_apoptosis_half_max').text)
        self.apoptosis_hill_power.value = float(uep.find('.//apoptosis_hill_power').text)
        self.virus_fraction_released_at_death.value = float(uep.find('.//virus_fraction_released_at_death').text)
        self.multiplicity_of_infection.value = float(uep.find('.//multiplicity_of_infection').text)
        self.use_single_infected_cell.value = ('true' == (uep.find('.//use_single_infected_cell').text.lower()) )
        self.color_variable.value = (uep.find('.//color_variable').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//random_seed').text = str(self.random_seed.value)
        uep.find('.//virion_uncoating_rate').text = str(self.virion_uncoating_rate.value)
        uep.find('.//uncoated_to_RNA_rate').text = str(self.uncoated_to_RNA_rate.value)
        uep.find('.//protein_synthesis_rate').text = str(self.protein_synthesis_rate.value)
        uep.find('.//virion_assembly_rate').text = str(self.virion_assembly_rate.value)
        uep.find('.//virion_export_rate').text = str(self.virion_export_rate.value)
        uep.find('.//ACE2_receptors_per_cell').text = str(self.ACE2_receptors_per_cell.value)
        uep.find('.//ACE2_binding_rate').text = str(self.ACE2_binding_rate.value)
        uep.find('.//ACE2_endocytosis_rate').text = str(self.ACE2_endocytosis_rate.value)
        uep.find('.//ACE2_cargo_release_rate').text = str(self.ACE2_cargo_release_rate.value)
        uep.find('.//ACE2_recycling_rate').text = str(self.ACE2_recycling_rate.value)
        uep.find('.//max_infected_apoptosis_rate').text = str(self.max_infected_apoptosis_rate.value)
        uep.find('.//max_apoptosis_half_max').text = str(self.max_apoptosis_half_max.value)
        uep.find('.//apoptosis_hill_power').text = str(self.apoptosis_hill_power.value)
        uep.find('.//virus_fraction_released_at_death').text = str(self.virus_fraction_released_at_death.value)
        uep.find('.//multiplicity_of_infection').text = str(self.multiplicity_of_infection.value)
        uep.find('.//use_single_infected_cell').text = str(self.use_single_infected_cell.value)
        uep.find('.//color_variable').text = str(self.color_variable.value)
