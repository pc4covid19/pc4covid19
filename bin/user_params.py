 
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

        param_name2 = Button(description='ignore_smoothing_flag', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.ignore_smoothing_flag = IntText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        div_row1 = Button(description='--Immune activation parameters--', disabled=True, layout=divider_button_layout)

        param_name3 = Button(description='immune_dt', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.immune_dt = FloatText(
          value=10,
          step=1,
          style=style, layout=widget_layout)

        param_name4 = Button(description='immune_z_offset', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.immune_z_offset = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name5 = Button(description='macrophage_max_recruitment_rate', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.macrophage_max_recruitment_rate = FloatText(
          value=6e-9,
          step=1e-09,
          style=style, layout=widget_layout)

        param_name6 = Button(description='macrophage_recruitment_min_signal', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.macrophage_recruitment_min_signal = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name7 = Button(description='macrophage_recruitment_saturation_signal', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.macrophage_recruitment_saturation_signal = FloatText(
          value=0.3,
          step=0.01,
          style=style, layout=widget_layout)

        param_name8 = Button(description='neutrophil_max_recruitment_rate', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.neutrophil_max_recruitment_rate = FloatText(
          value=6e-9,
          step=1e-09,
          style=style, layout=widget_layout)

        param_name9 = Button(description='neutrophil_recruitment_min_signal', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.neutrophil_recruitment_min_signal = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name10 = Button(description='neutrophil_recruitment_saturation_signal', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.neutrophil_recruitment_saturation_signal = FloatText(
          value=0.3,
          step=0.01,
          style=style, layout=widget_layout)

        param_name11 = Button(description='DC_max_recruitment_rate', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.DC_max_recruitment_rate = FloatText(
          value=1e-9,
          step=1e-10,
          style=style, layout=widget_layout)

        param_name12 = Button(description='DC_recruitment_min_signal', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.DC_recruitment_min_signal = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name13 = Button(description='DC_recruitment_saturation_signal', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.DC_recruitment_saturation_signal = FloatText(
          value=0.3,
          step=0.01,
          style=style, layout=widget_layout)

        param_name14 = Button(description='TC_death_rate', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'tan'

        self.TC_death_rate = FloatText(
          value=0.0000014,
          step=1e-07,
          style=style, layout=widget_layout)

        param_name15 = Button(description='max_activation_TC', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'lightgreen'

        self.max_activation_TC = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        param_name16 = Button(description='half_max_activation_TC', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'tan'

        self.half_max_activation_TC = FloatText(
          value=2000,
          step=100,
          style=style, layout=widget_layout)

        param_name17 = Button(description='max_clearance_TC', disabled=True, layout=name_button_layout)
        param_name17.style.button_color = 'lightgreen'

        self.max_clearance_TC = FloatText(
          value=0.0007,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name18 = Button(description='half_max_clearance_TC', disabled=True, layout=name_button_layout)
        param_name18.style.button_color = 'tan'

        self.half_max_clearance_TC = FloatText(
          value=200,
          step=10,
          style=style, layout=widget_layout)

        param_name19 = Button(description='TC_population_threshold', disabled=True, layout=name_button_layout)
        param_name19.style.button_color = 'lightgreen'

        self.TC_population_threshold = FloatText(
          value=10,
          step=1,
          style=style, layout=widget_layout)

        param_name20 = Button(description='T_Cell_Recruitment', disabled=True, layout=name_button_layout)
        param_name20.style.button_color = 'tan'

        self.T_Cell_Recruitment = FloatText(
          value=0.00011,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name21 = Button(description='DM_decay', disabled=True, layout=name_button_layout)
        param_name21.style.button_color = 'lightgreen'

        self.DM_decay = FloatText(
          value=0.00035,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name22 = Button(description='Th1_max_activation', disabled=True, layout=name_button_layout)
        param_name22.style.button_color = 'tan'

        self.Th1_max_activation = FloatText(
          value=0.001,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name23 = Button(description='Th1_damping', disabled=True, layout=name_button_layout)
        param_name23.style.button_color = 'lightgreen'

        self.Th1_damping = FloatText(
          value=0.00002,
          step=1e-06,
          style=style, layout=widget_layout)

        param_name24 = Button(description='Th1_decay', disabled=True, layout=name_button_layout)
        param_name24.style.button_color = 'tan'

        self.Th1_decay = FloatText(
          value=7e-8,
          step=1e-08,
          style=style, layout=widget_layout)

        param_name25 = Button(description='Th_base_decay', disabled=True, layout=name_button_layout)
        param_name25.style.button_color = 'lightgreen'

        self.Th_base_decay = FloatText(
          value=0.0000156,
          step=1e-06,
          style=style, layout=widget_layout)

        param_name26 = Button(description='Th2_self_feeback', disabled=True, layout=name_button_layout)
        param_name26.style.button_color = 'tan'

        self.Th2_self_feeback = FloatText(
          value=0.00004,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name27 = Button(description='Th2_max_conversion', disabled=True, layout=name_button_layout)
        param_name27.style.button_color = 'lightgreen'

        self.Th2_max_conversion = FloatText(
          value=0.000002,
          step=1e-07,
          style=style, layout=widget_layout)

        param_name28 = Button(description='Th1_Th2_conversion_wieght', disabled=True, layout=name_button_layout)
        param_name28.style.button_color = 'tan'

        self.Th1_Th2_conversion_wieght = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name29 = Button(description='BCell_base_rate', disabled=True, layout=name_button_layout)
        param_name29.style.button_color = 'lightgreen'

        self.BCell_base_rate = FloatText(
          value=1.74e-6,
          step=1e-07,
          style=style, layout=widget_layout)

        param_name30 = Button(description='BCell_base_value', disabled=True, layout=name_button_layout)
        param_name30.style.button_color = 'tan'

        self.BCell_base_value = FloatText(
          value=3000,
          step=100,
          style=style, layout=widget_layout)

        param_name31 = Button(description='BCell_DC_proliferation', disabled=True, layout=name_button_layout)
        param_name31.style.button_color = 'lightgreen'

        self.BCell_DC_proliferation = FloatText(
          value=0.004,
          step=0.001,
          style=style, layout=widget_layout)

        param_name32 = Button(description='BCell_Th2_wieght_function', disabled=True, layout=name_button_layout)
        param_name32.style.button_color = 'tan'

        self.BCell_Th2_wieght_function = FloatText(
          value=6.6,
          step=0.1,
          style=style, layout=widget_layout)

        param_name33 = Button(description='BCell_damping', disabled=True, layout=name_button_layout)
        param_name33.style.button_color = 'lightgreen'

        self.BCell_damping = FloatText(
          value=8800,
          step=100,
          style=style, layout=widget_layout)

        param_name34 = Button(description='PCell_recuitment', disabled=True, layout=name_button_layout)
        param_name34.style.button_color = 'tan'

        self.PCell_recuitment = FloatText(
          value=0.0002,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name35 = Button(description='PCell_degradation', disabled=True, layout=name_button_layout)
        param_name35.style.button_color = 'lightgreen'

        self.PCell_degradation = FloatText(
          value=0.00014,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name36 = Button(description='Ig_recuitment', disabled=True, layout=name_button_layout)
        param_name36.style.button_color = 'tan'

        self.Ig_recuitment = FloatText(
          value=0.05,
          step=0.01,
          style=style, layout=widget_layout)

        param_name37 = Button(description='Ig_degradation', disabled=True, layout=name_button_layout)
        param_name37.style.button_color = 'lightgreen'

        self.Ig_degradation = FloatText(
          value=0.00139,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name38 = Button(description='DC_leave_prob', disabled=True, layout=name_button_layout)
        param_name38.style.button_color = 'tan'

        self.DC_leave_prob = FloatText(
          value=0.0000033,
          step=1e-06,
          style=style, layout=widget_layout)

        param_name39 = Button(description='fibroblast_max_recruitment_rate', disabled=True, layout=name_button_layout)
        param_name39.style.button_color = 'lightgreen'

        self.fibroblast_max_recruitment_rate = FloatText(
          value=4e-9,
          step=1e-09,
          style=style, layout=widget_layout)

        param_name40 = Button(description='fibroblast_recruitment_min_signal', disabled=True, layout=name_button_layout)
        param_name40.style.button_color = 'tan'

        self.fibroblast_recruitment_min_signal = FloatText(
          value=7,
          step=0.1,
          style=style, layout=widget_layout)

        param_name41 = Button(description='fibroblast_recruitment_saturation_signal', disabled=True, layout=name_button_layout)
        param_name41.style.button_color = 'lightgreen'

        self.fibroblast_recruitment_saturation_signal = FloatText(
          value=22,
          step=1,
          style=style, layout=widget_layout)

        div_row2 = Button(description='---Initialization Options--', disabled=True, layout=divider_button_layout)

        param_name42 = Button(description='multiplicity_of_infection', disabled=True, layout=name_button_layout)
        param_name42.style.button_color = 'tan'

        self.multiplicity_of_infection = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name43 = Button(description='use_single_infected_cell', disabled=True, layout=name_button_layout)
        param_name43.style.button_color = 'lightgreen'

        self.use_single_infected_cell = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name44 = Button(description='number_of_CD8_Tcells', disabled=True, layout=name_button_layout)
        param_name44.style.button_color = 'tan'

        self.number_of_CD8_Tcells = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name45 = Button(description='number_of_macrophages', disabled=True, layout=name_button_layout)
        param_name45.style.button_color = 'lightgreen'

        self.number_of_macrophages = IntText(
          value=50,
          step=1,
          style=style, layout=widget_layout)

        param_name46 = Button(description='number_of_neutrophils', disabled=True, layout=name_button_layout)
        param_name46.style.button_color = 'tan'

        self.number_of_neutrophils = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name47 = Button(description='number_of_fibroblast', disabled=True, layout=name_button_layout)
        param_name47.style.button_color = 'lightgreen'

        self.number_of_fibroblast = IntText(
          value=57,
          step=1,
          style=style, layout=widget_layout)

        param_name48 = Button(description='number_of_DCs', disabled=True, layout=name_button_layout)
        param_name48.style.button_color = 'tan'

        self.number_of_DCs = IntText(
          value=28,
          step=1,
          style=style, layout=widget_layout)

        param_name49 = Button(description='number_of_CD4_Tcells', disabled=True, layout=name_button_layout)
        param_name49.style.button_color = 'lightgreen'

        self.number_of_CD4_Tcells = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name50 = Button(description='DC_induced_CD8_proliferation', disabled=True, layout=name_button_layout)
        param_name50.style.button_color = 'tan'

        self.DC_induced_CD8_proliferation = FloatText(
          value=0.00208,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name51 = Button(description='DC_induced_CD8_attachment', disabled=True, layout=name_button_layout)
        param_name51.style.button_color = 'lightgreen'

        self.DC_induced_CD8_attachment = FloatText(
          value=0.6,
          step=0.1,
          style=style, layout=widget_layout)

        param_name52 = Button(description='departure_rate_of_DCs', disabled=True, layout=name_button_layout)
        param_name52.style.button_color = 'tan'

        self.departure_rate_of_DCs = FloatText(
          value=0.001,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name53 = Button(description='virions_needed_for_DC_activation', disabled=True, layout=name_button_layout)
        param_name53.style.button_color = 'lightgreen'

        self.virions_needed_for_DC_activation = IntText(
          value=10,
          step=1,
          style=style, layout=widget_layout)

        param_name54 = Button(description='epsilon_distance', disabled=True, layout=name_button_layout)
        param_name54.style.button_color = 'tan'

        self.epsilon_distance = FloatText(
          value=1.75,
          step=0.1,
          style=style, layout=widget_layout)

        param_name55 = Button(description='perecentage_tissue_vascularized', disabled=True, layout=name_button_layout)
        param_name55.style.button_color = 'lightgreen'

        self.perecentage_tissue_vascularized = FloatText(
          value=8.8,
          step=0.1,
          style=style, layout=widget_layout)

        div_row3 = Button(description='---Cell Color Options--', disabled=True, layout=divider_button_layout)

        param_name56 = Button(description='color_variable', disabled=True, layout=name_button_layout)
        param_name56.style.button_color = 'tan'

        self.color_variable = Text(
          value='assembled_virion',
          style=style, layout=widget_layout)

        param_name57 = Button(description='epithelial_opacity', disabled=True, layout=name_button_layout)
        param_name57.style.button_color = 'lightgreen'

        self.epithelial_opacity = FloatText(
          value=0.65,
          step=0.1,
          style=style, layout=widget_layout)

        param_name58 = Button(description='non_epithelial_opacity', disabled=True, layout=name_button_layout)
        param_name58.style.button_color = 'tan'

        self.non_epithelial_opacity = FloatText(
          value=0.8,
          step=0.1,
          style=style, layout=widget_layout)

        param_name59 = Button(description='apoptotic_epithelium_color', disabled=True, layout=name_button_layout)
        param_name59.style.button_color = 'lightgreen'

        self.apoptotic_epithelium_color = Text(
          value='black',
          style=style, layout=widget_layout)

        param_name60 = Button(description='apoptotic_immune_color', disabled=True, layout=name_button_layout)
        param_name60.style.button_color = 'tan'

        self.apoptotic_immune_color = Text(
          value='rosybrown',
          style=style, layout=widget_layout)

        param_name61 = Button(description='pyroptotic_epithelium_color', disabled=True, layout=name_button_layout)
        param_name61.style.button_color = 'lightgreen'

        self.pyroptotic_epithelium_color = Text(
          value='darkorange',
          style=style, layout=widget_layout)

        param_name62 = Button(description='pyroptotic_bystander_epithelium_color', disabled=True, layout=name_button_layout)
        param_name62.style.button_color = 'tan'

        self.pyroptotic_bystander_epithelium_color = Text(
          value='darkred',
          style=style, layout=widget_layout)

        param_name63 = Button(description='vi_apoptotic_epithelium_color', disabled=True, layout=name_button_layout)
        param_name63.style.button_color = 'lightgreen'

        self.vi_apoptotic_epithelium_color = Text(
          value='forestgreen',
          style=style, layout=widget_layout)

        param_name64 = Button(description='CD8_Tcell_color', disabled=True, layout=name_button_layout)
        param_name64.style.button_color = 'tan'

        self.CD8_Tcell_color = Text(
          value='red',
          style=style, layout=widget_layout)

        param_name65 = Button(description='CD4_Tcell_color', disabled=True, layout=name_button_layout)
        param_name65.style.button_color = 'lightgreen'

        self.CD4_Tcell_color = Text(
          value='orange',
          style=style, layout=widget_layout)

        param_name66 = Button(description='Macrophage_color', disabled=True, layout=name_button_layout)
        param_name66.style.button_color = 'tan'

        self.Macrophage_color = Text(
          value='rgb(35,139,69)',
          style=style, layout=widget_layout)

        param_name67 = Button(description='activated_macrophage_color', disabled=True, layout=name_button_layout)
        param_name67.style.button_color = 'lightgreen'

        self.activated_macrophage_color = Text(
          value='lime',
          style=style, layout=widget_layout)

        param_name68 = Button(description='exhausted_macrophage_color', disabled=True, layout=name_button_layout)
        param_name68.style.button_color = 'tan'

        self.exhausted_macrophage_color = Text(
          value='rgb(116,196,118)',
          style=style, layout=widget_layout)

        param_name69 = Button(description='hyperactivated_macrophage_color', disabled=True, layout=name_button_layout)
        param_name69.style.button_color = 'lightgreen'

        self.hyperactivated_macrophage_color = Text(
          value='rgb(168,221,181)',
          style=style, layout=widget_layout)

        param_name70 = Button(description='Neutrophil_color', disabled=True, layout=name_button_layout)
        param_name70.style.button_color = 'tan'

        self.Neutrophil_color = Text(
          value='cyan',
          style=style, layout=widget_layout)

        param_name71 = Button(description='DC_color', disabled=True, layout=name_button_layout)
        param_name71.style.button_color = 'lightgreen'

        self.DC_color = Text(
          value='rgb(129,15,124)',
          style=style, layout=widget_layout)

        param_name72 = Button(description='activated_DC_color', disabled=True, layout=name_button_layout)
        param_name72.style.button_color = 'tan'

        self.activated_DC_color = Text(
          value='deeppink',
          style=style, layout=widget_layout)

        param_name73 = Button(description='fibroblast_color', disabled=True, layout=name_button_layout)
        param_name73.style.button_color = 'lightgreen'

        self.fibroblast_color = Text(
          value='blueviolet',
          style=style, layout=widget_layout)

        param_name74 = Button(description='phagocytes_virus_uptake_rate', disabled=True, layout=name_button_layout)
        param_name74.style.button_color = 'tan'

        self.phagocytes_virus_uptake_rate = FloatText(
          value=0.0001,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name75 = Button(description='ROS_secretion_rate', disabled=True, layout=name_button_layout)
        param_name75.style.button_color = 'lightgreen'

        self.ROS_secretion_rate = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        param_name76 = Button(description='epsilon_ROS', disabled=True, layout=name_button_layout)
        param_name76.style.button_color = 'tan'

        self.epsilon_ROS = FloatText(
          value=10,
          step=1,
          style=style, layout=widget_layout)

        param_name77 = Button(description='Antibody_binding_rate', disabled=True, layout=name_button_layout)
        param_name77.style.button_color = 'lightgreen'

        self.Antibody_binding_rate = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name78 = Button(description='antibody_half_effect', disabled=True, layout=name_button_layout)
        param_name78.style.button_color = 'tan'

        self.antibody_half_effect = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'tan'
        units_button4 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'lightgreen'
        units_button5 = Button(description='micron', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'tan'
        units_button6 = Button(description='cells/min/micron^3', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'lightgreen'
        units_button7 = Button(description='substrate/micron^3', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'tan'
        units_button8 = Button(description='substrate/micron^3', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'lightgreen'
        units_button9 = Button(description='cells/min/micron^3', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'tan'
        units_button10 = Button(description='substrate/micron^3', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'lightgreen'
        units_button11 = Button(description='substrate/micron^3', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'tan'
        units_button12 = Button(description='cells/min/micron^3', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'lightgreen'
        units_button13 = Button(description='substrate/micron^3', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'tan'
        units_button14 = Button(description='substrate/micron^3', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'lightgreen'
        units_button15 = Button(description='cells/min', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'tan'
        units_button16 = Button(description='cells/min', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'lightgreen'
        units_button17 = Button(description='cells', disabled=True, layout=units_button_layout) 
        units_button17.style.button_color = 'tan'
        units_button18 = Button(description='cells/min', disabled=True, layout=units_button_layout) 
        units_button18.style.button_color = 'lightgreen'
        units_button19 = Button(description='cells', disabled=True, layout=units_button_layout) 
        units_button19.style.button_color = 'tan'
        units_button20 = Button(description='cells', disabled=True, layout=units_button_layout) 
        units_button20.style.button_color = 'lightgreen'
        units_button21 = Button(description='cells/min', disabled=True, layout=units_button_layout) 
        units_button21.style.button_color = 'tan'
        units_button22 = Button(description='cells/min', disabled=True, layout=units_button_layout) 
        units_button22.style.button_color = 'lightgreen'
        units_button23 = Button(description='cells/min', disabled=True, layout=units_button_layout) 
        units_button23.style.button_color = 'tan'
        units_button24 = Button(description='cells/min', disabled=True, layout=units_button_layout) 
        units_button24.style.button_color = 'lightgreen'
        units_button25 = Button(description='cells/min', disabled=True, layout=units_button_layout) 
        units_button25.style.button_color = 'tan'
        units_button26 = Button(description='cells/min', disabled=True, layout=units_button_layout) 
        units_button26.style.button_color = 'lightgreen'
        units_button27 = Button(description='cells/min', disabled=True, layout=units_button_layout) 
        units_button27.style.button_color = 'tan'
        units_button28 = Button(description='cells/min', disabled=True, layout=units_button_layout) 
        units_button28.style.button_color = 'lightgreen'
        units_button29 = Button(description='cells/min', disabled=True, layout=units_button_layout) 
        units_button29.style.button_color = 'tan'
        units_button30 = Button(description='cells/min', disabled=True, layout=units_button_layout) 
        units_button30.style.button_color = 'lightgreen'
        units_button31 = Button(description='cells/min', disabled=True, layout=units_button_layout) 
        units_button31.style.button_color = 'tan'
        units_button32 = Button(description='cells/min', disabled=True, layout=units_button_layout) 
        units_button32.style.button_color = 'lightgreen'
        units_button33 = Button(description='cells/min', disabled=True, layout=units_button_layout) 
        units_button33.style.button_color = 'tan'
        units_button34 = Button(description='cells/min', disabled=True, layout=units_button_layout) 
        units_button34.style.button_color = 'lightgreen'
        units_button35 = Button(description='cells/min', disabled=True, layout=units_button_layout) 
        units_button35.style.button_color = 'tan'
        units_button36 = Button(description='cells/min', disabled=True, layout=units_button_layout) 
        units_button36.style.button_color = 'lightgreen'
        units_button37 = Button(description='cells/min', disabled=True, layout=units_button_layout) 
        units_button37.style.button_color = 'tan'
        units_button38 = Button(description='cells/min', disabled=True, layout=units_button_layout) 
        units_button38.style.button_color = 'lightgreen'
        units_button39 = Button(description='cells/min', disabled=True, layout=units_button_layout) 
        units_button39.style.button_color = 'tan'
        units_button40 = Button(description='cells/min/micron^3', disabled=True, layout=units_button_layout) 
        units_button40.style.button_color = 'lightgreen'
        units_button41 = Button(description='substrate/micron^3', disabled=True, layout=units_button_layout) 
        units_button41.style.button_color = 'tan'
        units_button42 = Button(description='substrate/micron^3', disabled=True, layout=units_button_layout) 
        units_button42.style.button_color = 'lightgreen'
        units_button43 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button43.style.button_color = 'lightgreen'
        units_button44 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button44.style.button_color = 'tan'
        units_button45 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button45.style.button_color = 'lightgreen'
        units_button46 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button46.style.button_color = 'tan'
        units_button47 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button47.style.button_color = 'lightgreen'
        units_button48 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button48.style.button_color = 'tan'
        units_button49 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button49.style.button_color = 'lightgreen'
        units_button50 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button50.style.button_color = 'tan'
        units_button51 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button51.style.button_color = 'lightgreen'
        units_button52 = Button(description='cells/min/micron^3', disabled=True, layout=units_button_layout) 
        units_button52.style.button_color = 'tan'
        units_button53 = Button(description='cells/min/micron^3', disabled=True, layout=units_button_layout) 
        units_button53.style.button_color = 'lightgreen'
        units_button54 = Button(description='cells/min/micron^3', disabled=True, layout=units_button_layout) 
        units_button54.style.button_color = 'tan'
        units_button55 = Button(description='virions', disabled=True, layout=units_button_layout) 
        units_button55.style.button_color = 'lightgreen'
        units_button56 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button56.style.button_color = 'tan'
        units_button57 = Button(description='percentage', disabled=True, layout=units_button_layout) 
        units_button57.style.button_color = 'lightgreen'
        units_button58 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button58.style.button_color = 'lightgreen'
        units_button59 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button59.style.button_color = 'tan'
        units_button60 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button60.style.button_color = 'lightgreen'
        units_button61 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button61.style.button_color = 'tan'
        units_button62 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button62.style.button_color = 'lightgreen'
        units_button63 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button63.style.button_color = 'tan'
        units_button64 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button64.style.button_color = 'lightgreen'
        units_button65 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button65.style.button_color = 'tan'
        units_button66 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button66.style.button_color = 'lightgreen'
        units_button67 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button67.style.button_color = 'tan'
        units_button68 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button68.style.button_color = 'lightgreen'
        units_button69 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button69.style.button_color = 'tan'
        units_button70 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button70.style.button_color = 'lightgreen'
        units_button71 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button71.style.button_color = 'tan'
        units_button72 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button72.style.button_color = 'lightgreen'
        units_button73 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button73.style.button_color = 'tan'
        units_button74 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button74.style.button_color = 'lightgreen'
        units_button75 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button75.style.button_color = 'tan'
        units_button76 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button76.style.button_color = 'lightgreen'
        units_button77 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button77.style.button_color = 'tan'
        units_button78 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button78.style.button_color = 'lightgreen'
        units_button79 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button79.style.button_color = 'tan'
        units_button80 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button80.style.button_color = 'lightgreen'
        units_button81 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button81.style.button_color = 'tan'

        desc_button1 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='how often we check to introduce immune cells' , tooltip='how often we check to introduce immune cells', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='immune cell position over the epithelium' , tooltip='immune cell position over the epithelium', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='max macrophage recruitment rate (for saturated signal)' , tooltip='max macrophage recruitment rate (for saturated signal)', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='min concentration to attract macrophages' , tooltip='min concentration to attract macrophages', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='saturating concentration to attract macrophages' , tooltip='saturating concentration to attract macrophages', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='max neutrophil recruitment rate (for saturated signal)' , tooltip='max neutrophil recruitment rate (for saturated signal)', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='min concentration to attract neutrophils' , tooltip='min concentration to attract neutrophils', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='saturating concentration to attract neutrophils' , tooltip='saturating concentration to attract neutrophils', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='max DC recruitment rate (for saturated signal)' , tooltip='max DC recruitment rate (for saturated signal)', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='min concentration to attract DC' , tooltip='min concentration to attract DC', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='saturating concentration to attract DC' , tooltip='saturating concentration to attract DC', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='TC death rate' , tooltip='TC death rate', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button15 = Button(description='max activation TC' , tooltip='max activation TC', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'
        desc_button16 = Button(description='half max activation TC' , tooltip='half max activation TC', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'
        desc_button17 = Button(description='max clearance TC' , tooltip='max clearance TC', disabled=True, layout=desc_button_layout) 
        desc_button17.style.button_color = 'lightgreen'
        desc_button18 = Button(description='half max clearance TC' , tooltip='half max clearance TC', disabled=True, layout=desc_button_layout) 
        desc_button18.style.button_color = 'tan'
        desc_button19 = Button(description='TC population threshold' , tooltip='TC population threshold', disabled=True, layout=desc_button_layout) 
        desc_button19.style.button_color = 'lightgreen'
        desc_button20 = Button(description='T cell recruitment rate to tissue' , tooltip='T cell recruitment rate to tissue', disabled=True, layout=desc_button_layout) 
        desc_button20.style.button_color = 'tan'
        desc_button21 = Button(description='DM decay rate' , tooltip='DM decay rate', disabled=True, layout=desc_button_layout) 
        desc_button21.style.button_color = 'lightgreen'
        desc_button22 = Button(description='Th1 max activation speed' , tooltip='Th1 max activation speed', disabled=True, layout=desc_button_layout) 
        desc_button22.style.button_color = 'tan'
        desc_button23 = Button(description='Th1 damping factor' , tooltip='Th1 damping factor', disabled=True, layout=desc_button_layout) 
        desc_button23.style.button_color = 'lightgreen'
        desc_button24 = Button(description='Th1 active decay rate' , tooltip='Th1 active decay rate', disabled=True, layout=desc_button_layout) 
        desc_button24.style.button_color = 'tan'
        desc_button25 = Button(description='Th base dacay rates' , tooltip='Th base dacay rates', disabled=True, layout=desc_button_layout) 
        desc_button25.style.button_color = 'lightgreen'
        desc_button26 = Button(description='Th2 max self feeback speed' , tooltip='Th2 max self feeback speed', disabled=True, layout=desc_button_layout) 
        desc_button26.style.button_color = 'tan'
        desc_button27 = Button(description='Th2 max conversion speed' , tooltip='Th2 max conversion speed', disabled=True, layout=desc_button_layout) 
        desc_button27.style.button_color = 'lightgreen'
        desc_button28 = Button(description='Th1 to Th2 conversion wieght' , tooltip='Th1 to Th2 conversion wieght', disabled=True, layout=desc_button_layout) 
        desc_button28.style.button_color = 'tan'
        desc_button29 = Button(description='BCell basal rates' , tooltip='BCell basal rates', disabled=True, layout=desc_button_layout) 
        desc_button29.style.button_color = 'lightgreen'
        desc_button30 = Button(description='BCell basal value' , tooltip='BCell basal value', disabled=True, layout=desc_button_layout) 
        desc_button30.style.button_color = 'tan'
        desc_button31 = Button(description='BCell DC influenced proliferation' , tooltip='BCell DC influenced proliferation', disabled=True, layout=desc_button_layout) 
        desc_button31.style.button_color = 'lightgreen'
        desc_button32 = Button(description='BCell proliferation Th2 wieght function' , tooltip='BCell proliferation Th2 wieght function', disabled=True, layout=desc_button_layout) 
        desc_button32.style.button_color = 'tan'
        desc_button33 = Button(description='BCell damping value' , tooltip='BCell damping value', disabled=True, layout=desc_button_layout) 
        desc_button33.style.button_color = 'lightgreen'
        desc_button34 = Button(description='PCell recuitment rate' , tooltip='PCell recuitment rate', disabled=True, layout=desc_button_layout) 
        desc_button34.style.button_color = 'tan'
        desc_button35 = Button(description='PCell degradation rate' , tooltip='PCell degradation rate', disabled=True, layout=desc_button_layout) 
        desc_button35.style.button_color = 'lightgreen'
        desc_button36 = Button(description='Ig recuitment rate' , tooltip='Ig recuitment rate', disabled=True, layout=desc_button_layout) 
        desc_button36.style.button_color = 'tan'
        desc_button37 = Button(description='Ig degradation rate' , tooltip='Ig degradation rate', disabled=True, layout=desc_button_layout) 
        desc_button37.style.button_color = 'lightgreen'
        desc_button38 = Button(description='probability of DC leaving to lymph node' , tooltip='probability of DC leaving to lymph node', disabled=True, layout=desc_button_layout) 
        desc_button38.style.button_color = 'tan'
        desc_button39 = Button(description='max fibroblast cell recruitment rate (for saturated signal)' , tooltip='max fibroblast cell recruitment rate (for saturated signal)', disabled=True, layout=desc_button_layout) 
        desc_button39.style.button_color = 'lightgreen'
        desc_button40 = Button(description='min concentration to attract fibroblast cells' , tooltip='min concentration to attract fibroblast cells', disabled=True, layout=desc_button_layout) 
        desc_button40.style.button_color = 'tan'
        desc_button41 = Button(description='saturating concentration to attract fibroblast cells' , tooltip='saturating concentration to attract fibroblast cells', disabled=True, layout=desc_button_layout) 
        desc_button41.style.button_color = 'lightgreen'
        desc_button42 = Button(description='multiplicity of infection: virions/cells at t=0' , tooltip='multiplicity of infection: virions/cells at t=0', disabled=True, layout=desc_button_layout) 
        desc_button42.style.button_color = 'tan'
        desc_button43 = Button(description='Infect center cell with one virion (overrides MOI)' , tooltip='Infect center cell with one virion (overrides MOI)', disabled=True, layout=desc_button_layout) 
        desc_button43.style.button_color = 'lightgreen'
        desc_button44 = Button(description='initial number of CD8 T cells in tissue' , tooltip='initial number of CD8 T cells in tissue', disabled=True, layout=desc_button_layout) 
        desc_button44.style.button_color = 'tan'
        desc_button45 = Button(description='initial number of macrophages' , tooltip='initial number of macrophages', disabled=True, layout=desc_button_layout) 
        desc_button45.style.button_color = 'lightgreen'
        desc_button46 = Button(description='initial number of neutrophils' , tooltip='initial number of neutrophils', disabled=True, layout=desc_button_layout) 
        desc_button46.style.button_color = 'tan'
        desc_button47 = Button(description='initial number of fibroblast cells' , tooltip='initial number of fibroblast cells', disabled=True, layout=desc_button_layout) 
        desc_button47.style.button_color = 'lightgreen'
        desc_button48 = Button(description='initial number of Dendritic Cells' , tooltip='initial number of Dendritic Cells', disabled=True, layout=desc_button_layout) 
        desc_button48.style.button_color = 'tan'
        desc_button49 = Button(description='initial number of CD4 Tcells in tissue' , tooltip='initial number of CD4 Tcells in tissue', disabled=True, layout=desc_button_layout) 
        desc_button49.style.button_color = 'lightgreen'
        desc_button50 = Button(description='DC induced CD8 proliferation rate' , tooltip='DC induced CD8 proliferation rate', disabled=True, layout=desc_button_layout) 
        desc_button50.style.button_color = 'tan'
        desc_button51 = Button(description='DC induced CD8 attachement rate' , tooltip='DC induced CD8 attachement rate', disabled=True, layout=desc_button_layout) 
        desc_button51.style.button_color = 'lightgreen'
        desc_button52 = Button(description='Departure rate of activated DCs' , tooltip='Departure rate of activated DCs', disabled=True, layout=desc_button_layout) 
        desc_button52.style.button_color = 'tan'
        desc_button53 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button53.style.button_color = 'lightgreen'
        desc_button54 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button54.style.button_color = 'tan'
        desc_button55 = Button(description='percentage of tissue sitting above blood vessels' , tooltip='percentage of tissue sitting above blood vessels', disabled=True, layout=desc_button_layout) 
        desc_button55.style.button_color = 'lightgreen'
        desc_button56 = Button(description='color cells based on this variable' , tooltip='color cells based on this variable', disabled=True, layout=desc_button_layout) 
        desc_button56.style.button_color = 'tan'
        desc_button57 = Button(description='opacity of epithelial cells' , tooltip='opacity of epithelial cells', disabled=True, layout=desc_button_layout) 
        desc_button57.style.button_color = 'lightgreen'
        desc_button58 = Button(description='opacity of non-epithelial cells' , tooltip='opacity of non-epithelial cells', disabled=True, layout=desc_button_layout) 
        desc_button58.style.button_color = 'tan'
        desc_button59 = Button(description='apoptotic epithelial cell color' , tooltip='apoptotic epithelial cell color', disabled=True, layout=desc_button_layout) 
        desc_button59.style.button_color = 'lightgreen'
        desc_button60 = Button(description='apoptotic immune cell color' , tooltip='apoptotic immune cell color', disabled=True, layout=desc_button_layout) 
        desc_button60.style.button_color = 'tan'
        desc_button61 = Button(description='pyroptotic epithelial cell color' , tooltip='pyroptotic epithelial cell color', disabled=True, layout=desc_button_layout) 
        desc_button61.style.button_color = 'lightgreen'
        desc_button62 = Button(description='pyroptotic epithelial cell color' , tooltip='pyroptotic epithelial cell color', disabled=True, layout=desc_button_layout) 
        desc_button62.style.button_color = 'tan'
        desc_button63 = Button(description='pyroptotic epithelial cell color' , tooltip='pyroptotic epithelial cell color', disabled=True, layout=desc_button_layout) 
        desc_button63.style.button_color = 'lightgreen'
        desc_button64 = Button(description='CD8 T cell color' , tooltip='CD8 T cell color', disabled=True, layout=desc_button_layout) 
        desc_button64.style.button_color = 'tan'
        desc_button65 = Button(description='CD4 T cell color' , tooltip='CD4 T cell color', disabled=True, layout=desc_button_layout) 
        desc_button65.style.button_color = 'lightgreen'
        desc_button66 = Button(description='macrophage color' , tooltip='macrophage color', disabled=True, layout=desc_button_layout) 
        desc_button66.style.button_color = 'tan'
        desc_button67 = Button(description='color of activated macrophage' , tooltip='color of activated macrophage', disabled=True, layout=desc_button_layout) 
        desc_button67.style.button_color = 'lightgreen'
        desc_button68 = Button(description='color of exhausted macrophage' , tooltip='color of exhausted macrophage', disabled=True, layout=desc_button_layout) 
        desc_button68.style.button_color = 'tan'
        desc_button69 = Button(description='color of hyperactivated macrophage' , tooltip='color of hyperactivated macrophage', disabled=True, layout=desc_button_layout) 
        desc_button69.style.button_color = 'lightgreen'
        desc_button70 = Button(description='neutrophil color' , tooltip='neutrophil color', disabled=True, layout=desc_button_layout) 
        desc_button70.style.button_color = 'tan'
        desc_button71 = Button(description='DC color' , tooltip='DC color', disabled=True, layout=desc_button_layout) 
        desc_button71.style.button_color = 'lightgreen'
        desc_button72 = Button(description='DC color' , tooltip='DC color', disabled=True, layout=desc_button_layout) 
        desc_button72.style.button_color = 'tan'
        desc_button73 = Button(description='fibroblast cell color' , tooltip='fibroblast cell color', disabled=True, layout=desc_button_layout) 
        desc_button73.style.button_color = 'lightgreen'
        desc_button74 = Button(description='Rate that phagocytes uptake virus after activation' , tooltip='Rate that phagocytes uptake virus after activation', disabled=True, layout=desc_button_layout) 
        desc_button74.style.button_color = 'tan'
        desc_button75 = Button(description='Rate that neutrophils secrete ROS' , tooltip='Rate that neutrophils secrete ROS', disabled=True, layout=desc_button_layout) 
        desc_button75.style.button_color = 'lightgreen'
        desc_button76 = Button(description='ROS half-effect' , tooltip='ROS half-effect', disabled=True, layout=desc_button_layout) 
        desc_button76.style.button_color = 'tan'
        desc_button77 = Button(description='Binding rate of antibody to infected cells' , tooltip='Binding rate of antibody to infected cells', disabled=True, layout=desc_button_layout) 
        desc_button77.style.button_color = 'lightgreen'
        desc_button78 = Button(description='Half effect of antibody on macrophage phagocytosis' , tooltip='Half effect of antibody on macrophage phagocytosis', disabled=True, layout=desc_button_layout) 
        desc_button78.style.button_color = 'tan'

        row1 = [param_name1, self.random_seed, units_button1, desc_button1] 
        row2 = [param_name2, self.ignore_smoothing_flag, units_button2, desc_button2] 
        row3 = [param_name3, self.immune_dt, units_button4, desc_button3] 
        row4 = [param_name4, self.immune_z_offset, units_button5, desc_button4] 
        row5 = [param_name5, self.macrophage_max_recruitment_rate, units_button6, desc_button5] 
        row6 = [param_name6, self.macrophage_recruitment_min_signal, units_button7, desc_button6] 
        row7 = [param_name7, self.macrophage_recruitment_saturation_signal, units_button8, desc_button7] 
        row8 = [param_name8, self.neutrophil_max_recruitment_rate, units_button9, desc_button8] 
        row9 = [param_name9, self.neutrophil_recruitment_min_signal, units_button10, desc_button9] 
        row10 = [param_name10, self.neutrophil_recruitment_saturation_signal, units_button11, desc_button10] 
        row11 = [param_name11, self.DC_max_recruitment_rate, units_button12, desc_button11] 
        row12 = [param_name12, self.DC_recruitment_min_signal, units_button13, desc_button12] 
        row13 = [param_name13, self.DC_recruitment_saturation_signal, units_button14, desc_button13] 
        row14 = [param_name14, self.TC_death_rate, units_button15, desc_button14] 
        row15 = [param_name15, self.max_activation_TC, units_button16, desc_button15] 
        row16 = [param_name16, self.half_max_activation_TC, units_button17, desc_button16] 
        row17 = [param_name17, self.max_clearance_TC, units_button18, desc_button17] 
        row18 = [param_name18, self.half_max_clearance_TC, units_button19, desc_button18] 
        row19 = [param_name19, self.TC_population_threshold, units_button20, desc_button19] 
        row20 = [param_name20, self.T_Cell_Recruitment, units_button21, desc_button20] 
        row21 = [param_name21, self.DM_decay, units_button22, desc_button21] 
        row22 = [param_name22, self.Th1_max_activation, units_button23, desc_button22] 
        row23 = [param_name23, self.Th1_damping, units_button24, desc_button23] 
        row24 = [param_name24, self.Th1_decay, units_button25, desc_button24] 
        row25 = [param_name25, self.Th_base_decay, units_button26, desc_button25] 
        row26 = [param_name26, self.Th2_self_feeback, units_button27, desc_button26] 
        row27 = [param_name27, self.Th2_max_conversion, units_button28, desc_button27] 
        row28 = [param_name28, self.Th1_Th2_conversion_wieght, units_button29, desc_button28] 
        row29 = [param_name29, self.BCell_base_rate, units_button30, desc_button29] 
        row30 = [param_name30, self.BCell_base_value, units_button31, desc_button30] 
        row31 = [param_name31, self.BCell_DC_proliferation, units_button32, desc_button31] 
        row32 = [param_name32, self.BCell_Th2_wieght_function, units_button33, desc_button32] 
        row33 = [param_name33, self.BCell_damping, units_button34, desc_button33] 
        row34 = [param_name34, self.PCell_recuitment, units_button35, desc_button34] 
        row35 = [param_name35, self.PCell_degradation, units_button36, desc_button35] 
        row36 = [param_name36, self.Ig_recuitment, units_button37, desc_button36] 
        row37 = [param_name37, self.Ig_degradation, units_button38, desc_button37] 
        row38 = [param_name38, self.DC_leave_prob, units_button39, desc_button38] 
        row39 = [param_name39, self.fibroblast_max_recruitment_rate, units_button40, desc_button39] 
        row40 = [param_name40, self.fibroblast_recruitment_min_signal, units_button41, desc_button40] 
        row41 = [param_name41, self.fibroblast_recruitment_saturation_signal, units_button42, desc_button41] 
        row42 = [param_name42, self.multiplicity_of_infection, units_button44, desc_button42] 
        row43 = [param_name43, self.use_single_infected_cell, units_button45, desc_button43] 
        row44 = [param_name44, self.number_of_CD8_Tcells, units_button46, desc_button44] 
        row45 = [param_name45, self.number_of_macrophages, units_button47, desc_button45] 
        row46 = [param_name46, self.number_of_neutrophils, units_button48, desc_button46] 
        row47 = [param_name47, self.number_of_fibroblast, units_button49, desc_button47] 
        row48 = [param_name48, self.number_of_DCs, units_button50, desc_button48] 
        row49 = [param_name49, self.number_of_CD4_Tcells, units_button51, desc_button49] 
        row50 = [param_name50, self.DC_induced_CD8_proliferation, units_button52, desc_button50] 
        row51 = [param_name51, self.DC_induced_CD8_attachment, units_button53, desc_button51] 
        row52 = [param_name52, self.departure_rate_of_DCs, units_button54, desc_button52] 
        row53 = [param_name53, self.virions_needed_for_DC_activation, units_button55, desc_button53] 
        row54 = [param_name54, self.epsilon_distance, units_button56, desc_button54] 
        row55 = [param_name55, self.perecentage_tissue_vascularized, units_button57, desc_button55] 
        row56 = [param_name56, self.color_variable, units_button59, desc_button56] 
        row57 = [param_name57, self.epithelial_opacity, units_button60, desc_button57] 
        row58 = [param_name58, self.non_epithelial_opacity, units_button61, desc_button58] 
        row59 = [param_name59, self.apoptotic_epithelium_color, units_button62, desc_button59] 
        row60 = [param_name60, self.apoptotic_immune_color, units_button63, desc_button60] 
        row61 = [param_name61, self.pyroptotic_epithelium_color, units_button64, desc_button61] 
        row62 = [param_name62, self.pyroptotic_bystander_epithelium_color, units_button65, desc_button62] 
        row63 = [param_name63, self.vi_apoptotic_epithelium_color, units_button66, desc_button63] 
        row64 = [param_name64, self.CD8_Tcell_color, units_button67, desc_button64] 
        row65 = [param_name65, self.CD4_Tcell_color, units_button68, desc_button65] 
        row66 = [param_name66, self.Macrophage_color, units_button69, desc_button66] 
        row67 = [param_name67, self.activated_macrophage_color, units_button70, desc_button67] 
        row68 = [param_name68, self.exhausted_macrophage_color, units_button71, desc_button68] 
        row69 = [param_name69, self.hyperactivated_macrophage_color, units_button72, desc_button69] 
        row70 = [param_name70, self.Neutrophil_color, units_button73, desc_button70] 
        row71 = [param_name71, self.DC_color, units_button74, desc_button71] 
        row72 = [param_name72, self.activated_DC_color, units_button75, desc_button72] 
        row73 = [param_name73, self.fibroblast_color, units_button76, desc_button73] 
        row74 = [param_name74, self.phagocytes_virus_uptake_rate, units_button77, desc_button74] 
        row75 = [param_name75, self.ROS_secretion_rate, units_button78, desc_button75] 
        row76 = [param_name76, self.epsilon_ROS, units_button79, desc_button76] 
        row77 = [param_name77, self.Antibody_binding_rate, units_button80, desc_button77] 
        row78 = [param_name78, self.antibody_half_effect, units_button81, desc_button78] 

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
        box19 = Box(children=row19, layout=box_layout)
        box20 = Box(children=row20, layout=box_layout)
        box21 = Box(children=row21, layout=box_layout)
        box22 = Box(children=row22, layout=box_layout)
        box23 = Box(children=row23, layout=box_layout)
        box24 = Box(children=row24, layout=box_layout)
        box25 = Box(children=row25, layout=box_layout)
        box26 = Box(children=row26, layout=box_layout)
        box27 = Box(children=row27, layout=box_layout)
        box28 = Box(children=row28, layout=box_layout)
        box29 = Box(children=row29, layout=box_layout)
        box30 = Box(children=row30, layout=box_layout)
        box31 = Box(children=row31, layout=box_layout)
        box32 = Box(children=row32, layout=box_layout)
        box33 = Box(children=row33, layout=box_layout)
        box34 = Box(children=row34, layout=box_layout)
        box35 = Box(children=row35, layout=box_layout)
        box36 = Box(children=row36, layout=box_layout)
        box37 = Box(children=row37, layout=box_layout)
        box38 = Box(children=row38, layout=box_layout)
        box39 = Box(children=row39, layout=box_layout)
        box40 = Box(children=row40, layout=box_layout)
        box41 = Box(children=row41, layout=box_layout)
        box42 = Box(children=row42, layout=box_layout)
        box43 = Box(children=row43, layout=box_layout)
        box44 = Box(children=row44, layout=box_layout)
        box45 = Box(children=row45, layout=box_layout)
        box46 = Box(children=row46, layout=box_layout)
        box47 = Box(children=row47, layout=box_layout)
        box48 = Box(children=row48, layout=box_layout)
        box49 = Box(children=row49, layout=box_layout)
        box50 = Box(children=row50, layout=box_layout)
        box51 = Box(children=row51, layout=box_layout)
        box52 = Box(children=row52, layout=box_layout)
        box53 = Box(children=row53, layout=box_layout)
        box54 = Box(children=row54, layout=box_layout)
        box55 = Box(children=row55, layout=box_layout)
        box56 = Box(children=row56, layout=box_layout)
        box57 = Box(children=row57, layout=box_layout)
        box58 = Box(children=row58, layout=box_layout)
        box59 = Box(children=row59, layout=box_layout)
        box60 = Box(children=row60, layout=box_layout)
        box61 = Box(children=row61, layout=box_layout)
        box62 = Box(children=row62, layout=box_layout)
        box63 = Box(children=row63, layout=box_layout)
        box64 = Box(children=row64, layout=box_layout)
        box65 = Box(children=row65, layout=box_layout)
        box66 = Box(children=row66, layout=box_layout)
        box67 = Box(children=row67, layout=box_layout)
        box68 = Box(children=row68, layout=box_layout)
        box69 = Box(children=row69, layout=box_layout)
        box70 = Box(children=row70, layout=box_layout)
        box71 = Box(children=row71, layout=box_layout)
        box72 = Box(children=row72, layout=box_layout)
        box73 = Box(children=row73, layout=box_layout)
        box74 = Box(children=row74, layout=box_layout)
        box75 = Box(children=row75, layout=box_layout)
        box76 = Box(children=row76, layout=box_layout)
        box77 = Box(children=row77, layout=box_layout)
        box78 = Box(children=row78, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          div_row1,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          box11,
          box12,
          box13,
          box14,
          box15,
          box16,
          box17,
          box18,
          box19,
          box20,
          box21,
          box22,
          box23,
          box24,
          box25,
          box26,
          box27,
          box28,
          box29,
          box30,
          box31,
          box32,
          box33,
          box34,
          box35,
          box36,
          box37,
          box38,
          box39,
          box40,
          box41,
          div_row2,
          box42,
          box43,
          box44,
          box45,
          box46,
          box47,
          box48,
          box49,
          box50,
          box51,
          box52,
          box53,
          box54,
          box55,
          div_row3,
          box56,
          box57,
          box58,
          box59,
          box60,
          box61,
          box62,
          box63,
          box64,
          box65,
          box66,
          box67,
          box68,
          box69,
          box70,
          box71,
          box72,
          box73,
          box74,
          box75,
          box76,
          box77,
          box78,
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
        self.ignore_smoothing_flag.value = int(uep.find('.//ignore_smoothing_flag').text)
        self.immune_dt.value = float(uep.find('.//immune_dt').text)
        self.immune_z_offset.value = float(uep.find('.//immune_z_offset').text)
        self.macrophage_max_recruitment_rate.value = float(uep.find('.//macrophage_max_recruitment_rate').text)
        self.macrophage_recruitment_min_signal.value = float(uep.find('.//macrophage_recruitment_min_signal').text)
        self.macrophage_recruitment_saturation_signal.value = float(uep.find('.//macrophage_recruitment_saturation_signal').text)
        self.neutrophil_max_recruitment_rate.value = float(uep.find('.//neutrophil_max_recruitment_rate').text)
        self.neutrophil_recruitment_min_signal.value = float(uep.find('.//neutrophil_recruitment_min_signal').text)
        self.neutrophil_recruitment_saturation_signal.value = float(uep.find('.//neutrophil_recruitment_saturation_signal').text)
        self.DC_max_recruitment_rate.value = float(uep.find('.//DC_max_recruitment_rate').text)
        self.DC_recruitment_min_signal.value = float(uep.find('.//DC_recruitment_min_signal').text)
        self.DC_recruitment_saturation_signal.value = float(uep.find('.//DC_recruitment_saturation_signal').text)
        self.TC_death_rate.value = float(uep.find('.//TC_death_rate').text)
        self.max_activation_TC.value = float(uep.find('.//max_activation_TC').text)
        self.half_max_activation_TC.value = float(uep.find('.//half_max_activation_TC').text)
        self.max_clearance_TC.value = float(uep.find('.//max_clearance_TC').text)
        self.half_max_clearance_TC.value = float(uep.find('.//half_max_clearance_TC').text)
        self.TC_population_threshold.value = float(uep.find('.//TC_population_threshold').text)
        self.T_Cell_Recruitment.value = float(uep.find('.//T_Cell_Recruitment').text)
        self.DM_decay.value = float(uep.find('.//DM_decay').text)
        self.Th1_max_activation.value = float(uep.find('.//Th1_max_activation').text)
        self.Th1_damping.value = float(uep.find('.//Th1_damping').text)
        self.Th1_decay.value = float(uep.find('.//Th1_decay').text)
        self.Th_base_decay.value = float(uep.find('.//Th_base_decay').text)
        self.Th2_self_feeback.value = float(uep.find('.//Th2_self_feeback').text)
        self.Th2_max_conversion.value = float(uep.find('.//Th2_max_conversion').text)
        self.Th1_Th2_conversion_wieght.value = float(uep.find('.//Th1_Th2_conversion_wieght').text)
        self.BCell_base_rate.value = float(uep.find('.//BCell_base_rate').text)
        self.BCell_base_value.value = float(uep.find('.//BCell_base_value').text)
        self.BCell_DC_proliferation.value = float(uep.find('.//BCell_DC_proliferation').text)
        self.BCell_Th2_wieght_function.value = float(uep.find('.//BCell_Th2_wieght_function').text)
        self.BCell_damping.value = float(uep.find('.//BCell_damping').text)
        self.PCell_recuitment.value = float(uep.find('.//PCell_recuitment').text)
        self.PCell_degradation.value = float(uep.find('.//PCell_degradation').text)
        self.Ig_recuitment.value = float(uep.find('.//Ig_recuitment').text)
        self.Ig_degradation.value = float(uep.find('.//Ig_degradation').text)
        self.DC_leave_prob.value = float(uep.find('.//DC_leave_prob').text)
        self.fibroblast_max_recruitment_rate.value = float(uep.find('.//fibroblast_max_recruitment_rate').text)
        self.fibroblast_recruitment_min_signal.value = float(uep.find('.//fibroblast_recruitment_min_signal').text)
        self.fibroblast_recruitment_saturation_signal.value = float(uep.find('.//fibroblast_recruitment_saturation_signal').text)
        self.multiplicity_of_infection.value = float(uep.find('.//multiplicity_of_infection').text)
        self.use_single_infected_cell.value = ('true' == (uep.find('.//use_single_infected_cell').text.lower()) )
        self.number_of_CD8_Tcells.value = int(uep.find('.//number_of_CD8_Tcells').text)
        self.number_of_macrophages.value = int(uep.find('.//number_of_macrophages').text)
        self.number_of_neutrophils.value = int(uep.find('.//number_of_neutrophils').text)
        self.number_of_fibroblast.value = int(uep.find('.//number_of_fibroblast').text)
        self.number_of_DCs.value = int(uep.find('.//number_of_DCs').text)
        self.number_of_CD4_Tcells.value = int(uep.find('.//number_of_CD4_Tcells').text)
        self.DC_induced_CD8_proliferation.value = float(uep.find('.//DC_induced_CD8_proliferation').text)
        self.DC_induced_CD8_attachment.value = float(uep.find('.//DC_induced_CD8_attachment').text)
        self.departure_rate_of_DCs.value = float(uep.find('.//departure_rate_of_DCs').text)
        self.virions_needed_for_DC_activation.value = int(uep.find('.//virions_needed_for_DC_activation').text)
        self.epsilon_distance.value = float(uep.find('.//epsilon_distance').text)
        self.perecentage_tissue_vascularized.value = float(uep.find('.//perecentage_tissue_vascularized').text)
        self.color_variable.value = (uep.find('.//color_variable').text)
        self.epithelial_opacity.value = float(uep.find('.//epithelial_opacity').text)
        self.non_epithelial_opacity.value = float(uep.find('.//non_epithelial_opacity').text)
        self.apoptotic_epithelium_color.value = (uep.find('.//apoptotic_epithelium_color').text)
        self.apoptotic_immune_color.value = (uep.find('.//apoptotic_immune_color').text)
        self.pyroptotic_epithelium_color.value = (uep.find('.//pyroptotic_epithelium_color').text)
        self.pyroptotic_bystander_epithelium_color.value = (uep.find('.//pyroptotic_bystander_epithelium_color').text)
        self.vi_apoptotic_epithelium_color.value = (uep.find('.//vi_apoptotic_epithelium_color').text)
        self.CD8_Tcell_color.value = (uep.find('.//CD8_Tcell_color').text)
        self.CD4_Tcell_color.value = (uep.find('.//CD4_Tcell_color').text)
        self.Macrophage_color.value = (uep.find('.//Macrophage_color').text)
        self.activated_macrophage_color.value = (uep.find('.//activated_macrophage_color').text)
        self.exhausted_macrophage_color.value = (uep.find('.//exhausted_macrophage_color').text)
        self.hyperactivated_macrophage_color.value = (uep.find('.//hyperactivated_macrophage_color').text)
        self.Neutrophil_color.value = (uep.find('.//Neutrophil_color').text)
        self.DC_color.value = (uep.find('.//DC_color').text)
        self.activated_DC_color.value = (uep.find('.//activated_DC_color').text)
        self.fibroblast_color.value = (uep.find('.//fibroblast_color').text)
        self.phagocytes_virus_uptake_rate.value = float(uep.find('.//phagocytes_virus_uptake_rate').text)
        self.ROS_secretion_rate.value = float(uep.find('.//ROS_secretion_rate').text)
        self.epsilon_ROS.value = float(uep.find('.//epsilon_ROS').text)
        self.Antibody_binding_rate.value = float(uep.find('.//Antibody_binding_rate').text)
        self.antibody_half_effect.value = float(uep.find('.//antibody_half_effect').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//random_seed').text = str(self.random_seed.value)
        uep.find('.//ignore_smoothing_flag').text = str(self.ignore_smoothing_flag.value)
        uep.find('.//immune_dt').text = str(self.immune_dt.value)
        uep.find('.//immune_z_offset').text = str(self.immune_z_offset.value)
        uep.find('.//macrophage_max_recruitment_rate').text = str(self.macrophage_max_recruitment_rate.value)
        uep.find('.//macrophage_recruitment_min_signal').text = str(self.macrophage_recruitment_min_signal.value)
        uep.find('.//macrophage_recruitment_saturation_signal').text = str(self.macrophage_recruitment_saturation_signal.value)
        uep.find('.//neutrophil_max_recruitment_rate').text = str(self.neutrophil_max_recruitment_rate.value)
        uep.find('.//neutrophil_recruitment_min_signal').text = str(self.neutrophil_recruitment_min_signal.value)
        uep.find('.//neutrophil_recruitment_saturation_signal').text = str(self.neutrophil_recruitment_saturation_signal.value)
        uep.find('.//DC_max_recruitment_rate').text = str(self.DC_max_recruitment_rate.value)
        uep.find('.//DC_recruitment_min_signal').text = str(self.DC_recruitment_min_signal.value)
        uep.find('.//DC_recruitment_saturation_signal').text = str(self.DC_recruitment_saturation_signal.value)
        uep.find('.//TC_death_rate').text = str(self.TC_death_rate.value)
        uep.find('.//max_activation_TC').text = str(self.max_activation_TC.value)
        uep.find('.//half_max_activation_TC').text = str(self.half_max_activation_TC.value)
        uep.find('.//max_clearance_TC').text = str(self.max_clearance_TC.value)
        uep.find('.//half_max_clearance_TC').text = str(self.half_max_clearance_TC.value)
        uep.find('.//TC_population_threshold').text = str(self.TC_population_threshold.value)
        uep.find('.//T_Cell_Recruitment').text = str(self.T_Cell_Recruitment.value)
        uep.find('.//DM_decay').text = str(self.DM_decay.value)
        uep.find('.//Th1_max_activation').text = str(self.Th1_max_activation.value)
        uep.find('.//Th1_damping').text = str(self.Th1_damping.value)
        uep.find('.//Th1_decay').text = str(self.Th1_decay.value)
        uep.find('.//Th_base_decay').text = str(self.Th_base_decay.value)
        uep.find('.//Th2_self_feeback').text = str(self.Th2_self_feeback.value)
        uep.find('.//Th2_max_conversion').text = str(self.Th2_max_conversion.value)
        uep.find('.//Th1_Th2_conversion_wieght').text = str(self.Th1_Th2_conversion_wieght.value)
        uep.find('.//BCell_base_rate').text = str(self.BCell_base_rate.value)
        uep.find('.//BCell_base_value').text = str(self.BCell_base_value.value)
        uep.find('.//BCell_DC_proliferation').text = str(self.BCell_DC_proliferation.value)
        uep.find('.//BCell_Th2_wieght_function').text = str(self.BCell_Th2_wieght_function.value)
        uep.find('.//BCell_damping').text = str(self.BCell_damping.value)
        uep.find('.//PCell_recuitment').text = str(self.PCell_recuitment.value)
        uep.find('.//PCell_degradation').text = str(self.PCell_degradation.value)
        uep.find('.//Ig_recuitment').text = str(self.Ig_recuitment.value)
        uep.find('.//Ig_degradation').text = str(self.Ig_degradation.value)
        uep.find('.//DC_leave_prob').text = str(self.DC_leave_prob.value)
        uep.find('.//fibroblast_max_recruitment_rate').text = str(self.fibroblast_max_recruitment_rate.value)
        uep.find('.//fibroblast_recruitment_min_signal').text = str(self.fibroblast_recruitment_min_signal.value)
        uep.find('.//fibroblast_recruitment_saturation_signal').text = str(self.fibroblast_recruitment_saturation_signal.value)
        uep.find('.//multiplicity_of_infection').text = str(self.multiplicity_of_infection.value)
        uep.find('.//use_single_infected_cell').text = str(self.use_single_infected_cell.value)
        uep.find('.//number_of_CD8_Tcells').text = str(self.number_of_CD8_Tcells.value)
        uep.find('.//number_of_macrophages').text = str(self.number_of_macrophages.value)
        uep.find('.//number_of_neutrophils').text = str(self.number_of_neutrophils.value)
        uep.find('.//number_of_fibroblast').text = str(self.number_of_fibroblast.value)
        uep.find('.//number_of_DCs').text = str(self.number_of_DCs.value)
        uep.find('.//number_of_CD4_Tcells').text = str(self.number_of_CD4_Tcells.value)
        uep.find('.//DC_induced_CD8_proliferation').text = str(self.DC_induced_CD8_proliferation.value)
        uep.find('.//DC_induced_CD8_attachment').text = str(self.DC_induced_CD8_attachment.value)
        uep.find('.//departure_rate_of_DCs').text = str(self.departure_rate_of_DCs.value)
        uep.find('.//virions_needed_for_DC_activation').text = str(self.virions_needed_for_DC_activation.value)
        uep.find('.//epsilon_distance').text = str(self.epsilon_distance.value)
        uep.find('.//perecentage_tissue_vascularized').text = str(self.perecentage_tissue_vascularized.value)
        uep.find('.//color_variable').text = str(self.color_variable.value)
        uep.find('.//epithelial_opacity').text = str(self.epithelial_opacity.value)
        uep.find('.//non_epithelial_opacity').text = str(self.non_epithelial_opacity.value)
        uep.find('.//apoptotic_epithelium_color').text = str(self.apoptotic_epithelium_color.value)
        uep.find('.//apoptotic_immune_color').text = str(self.apoptotic_immune_color.value)
        uep.find('.//pyroptotic_epithelium_color').text = str(self.pyroptotic_epithelium_color.value)
        uep.find('.//pyroptotic_bystander_epithelium_color').text = str(self.pyroptotic_bystander_epithelium_color.value)
        uep.find('.//vi_apoptotic_epithelium_color').text = str(self.vi_apoptotic_epithelium_color.value)
        uep.find('.//CD8_Tcell_color').text = str(self.CD8_Tcell_color.value)
        uep.find('.//CD4_Tcell_color').text = str(self.CD4_Tcell_color.value)
        uep.find('.//Macrophage_color').text = str(self.Macrophage_color.value)
        uep.find('.//activated_macrophage_color').text = str(self.activated_macrophage_color.value)
        uep.find('.//exhausted_macrophage_color').text = str(self.exhausted_macrophage_color.value)
        uep.find('.//hyperactivated_macrophage_color').text = str(self.hyperactivated_macrophage_color.value)
        uep.find('.//Neutrophil_color').text = str(self.Neutrophil_color.value)
        uep.find('.//DC_color').text = str(self.DC_color.value)
        uep.find('.//activated_DC_color').text = str(self.activated_DC_color.value)
        uep.find('.//fibroblast_color').text = str(self.fibroblast_color.value)
        uep.find('.//phagocytes_virus_uptake_rate').text = str(self.phagocytes_virus_uptake_rate.value)
        uep.find('.//ROS_secretion_rate').text = str(self.ROS_secretion_rate.value)
        uep.find('.//epsilon_ROS').text = str(self.epsilon_ROS.value)
        uep.find('.//Antibody_binding_rate').text = str(self.Antibody_binding_rate.value)
        uep.find('.//antibody_half_effect').text = str(self.antibody_half_effect.value)
