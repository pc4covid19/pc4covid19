 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box,Dropdown
    
class CellTypesTab(object):

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
        widget_layout_long = {'width': '20%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}
        divider_button_layout={'width':'60%'}
        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')

        self.cell_type_dropdown = Dropdown(description='Cell type:',)
        self.cell_type_dropdown.style = {'description_width': '%sch' % str(len(self.cell_type_dropdown.description) + 1)}

        cell_type_names_layout={'width':'30%'}
        cell_type_names_style={'description_width':'initial'}
        self.parent_name = Text(value='None',description='inherits properties from parent type:',disabled=True, style=cell_type_names_style, layout=cell_type_names_layout)

        explain_inheritance = Label(value='    This cell line inherits its properties from its parent type. Any settings below override those inherited properties.')  # , style=cell_type_names_style, layout=cell_type_names_layout)

        self.cell_type_parent_row = HBox([self.cell_type_dropdown, self.parent_name])
        self.cell_type_parent_dict = {}

        self.cell_type_dict = {}
        self.cell_type_dict['default'] = 'default'
        self.cell_type_dict['lung epithelium'] = 'lung epithelium'
        self.cell_type_dict['immune'] = 'immune'
        self.cell_type_dict['CD8 Tcell'] = 'CD8 Tcell'
        self.cell_type_dict['macrophage'] = 'macrophage'
        self.cell_type_dict['neutrophil'] = 'neutrophil'
        self.cell_type_dropdown.options = self.cell_type_dict

        self.cell_type_dropdown.observe(self.cell_type_cb)

        self.cell_type_parent_dict['default'] = 'None'
        self.cell_type_parent_dict['lung epithelium'] = 'default'
        self.cell_type_parent_dict['immune'] = 'default'
        self.cell_type_parent_dict['CD8 Tcell'] = 'immune'
        self.cell_type_parent_dict['macrophage'] = 'immune'
        self.cell_type_parent_dict['neutrophil'] = 'immune'


        self.cell_def_vboxes = []
        #  >>>>>>>>>>>>>>>>> <cell_definition> = default
        #  ------------------------- 
        div_row1 = Button(description='phenotype:cycle (model: flow_cytometry_separated_cycle_model; code=6)', disabled=True, layout=divider_button_layout)
        div_row1.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 1 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float0 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float0, units_btn, ]
        box0 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 1 -> Phase 2 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float1 = FloatText(value='0.00208333', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float1, units_btn, ]
        box1 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 2 -> Phase 3 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float2 = FloatText(value='0.00416667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float2, units_btn, ]
        box2 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 3 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float3 = FloatText(value='0.0166667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float3, units_btn, ]
        box3 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row2 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row2.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float4 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float4, units_btn, ]
        box4 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float5 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float5, units_btn, ]
        box5 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float6 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float6, units_btn, ]
        box6 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float7 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float7, units_btn, ]
        box7 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float8 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float8, units_btn, ]
        box8 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float9 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float9, units_btn, ]
        box9 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float10 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float10, units_btn, ]
        box10 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float11 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float11, units_btn, ]
        box11 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float12 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float12, units_btn, ]
        box12 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float13 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float13, units_btn, ]
        box13 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float14 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float14, units_btn, ]
        box14 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float15 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float15, units_btn, ]
        box15 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float16 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float16, units_btn, ]
        box16 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float17 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float17, units_btn, ]
        box17 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row3 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row3.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float18 = FloatText(value='2494', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float18, units_btn, ]
        box18 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float19 = FloatText(value='0.75', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float19, units_btn, ]
        box19 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float20 = FloatText(value='540', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float20, units_btn, ]
        box20 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float21 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float21, units_btn, ]
        box21 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float22 = FloatText(value='0.0045', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float22, units_btn, ]
        box22 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float23 = FloatText(value='0.0055', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float23, units_btn, ]
        box23 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcified_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float24 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float24, units_btn, ]
        box24 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float25 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float25, units_btn, ]
        box25 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float26 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float26, units_btn, ]
        box26 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row4 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row4.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float27 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float27, units_btn, ]
        box27 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float28 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float28, units_btn, ]
        box28 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float29 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float29, units_btn, ]
        box29 = Box(children=row, layout=box_layout)

        self.bool0 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float30 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool0, name_btn, self.float30, units_btn, ]
        box30 = Box(children=row, layout=box_layout)

        self.bool1 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float31 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool1, name_btn, self.float31, units_btn, ]
        box31 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row5 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row5.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float32 = FloatText(value='4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float32, units_btn]
        box32 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float33 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float33, units_btn]
        box33 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float34 = FloatText(value='0.7', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float34, units_btn]
        box34 = Box(children=row, layout=box_layout)
        self.bool2 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        self.bool3 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool4 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate1 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate1]
        box35 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction1 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction1]
        box36 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row6 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row6.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text0 = Text(value='interferon 1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text0]
        box37 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float35 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='substrate density', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float35, units_btn]
        box38 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text1 = Text(value='pro-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text1]
        box39 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float36 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='substrate density', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float36, units_btn]
        box40 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text2 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text2]
        box41 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float37 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='substrate density', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float37, units_btn]
        box42 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text3 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text3]
        box43 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float38 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='substrate density', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float38, units_btn]
        box44 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row7 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row7.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        div_row8 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row8.style.button_color = 'cyan'
        name_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float39 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float39, units_btn, description_btn] 

        box45 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float40 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='uncoated endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float40, units_btn, description_btn] 

        box46 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_RNA', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float41 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='RNA', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total (functional) viral RNA copies', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float41, units_btn, description_btn] 

        box47 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_protein', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float42 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='protein', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='total assembled sets of viral protein', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float42, units_btn, description_btn] 

        box48 = Box(children=row, layout=box_layout)
        name_btn = Button(description='assembled_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float43 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total assembled virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float43, units_btn, description_btn] 

        box49 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_uncoating_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float44 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which an internalized virion is uncoated', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float44, units_btn, description_btn] 

        box50 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_to_RNA_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float45 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which uncoated virion makes its mRNA available', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float45, units_btn, description_btn] 

        box51 = Box(children=row, layout=box_layout)
        name_btn = Button(description='protein_synthesis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float46 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at mRNA creates complete set of proteins', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float46, units_btn, description_btn] 

        box52 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_assembly_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float47 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which viral proteins are assembled into complete virion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float47, units_btn, description_btn] 

        box53 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_export_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float48 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which a virion is exported from a live cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float48, units_btn, description_btn] 

        box54 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float49 = FloatText(value='1000', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of unbound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float49, units_btn, description_btn] 

        box55 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float50 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of bound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float50, units_btn, description_btn] 

        box56 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float51 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of internalized unbound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float51, units_btn, description_btn] 

        box57 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float52 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of internalized bound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float52, units_btn, description_btn] 

        box58 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float53 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float53, units_btn, description_btn] 

        box59 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_endocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float54 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor-virus endocytosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float54, units_btn, description_btn] 

        box60 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_cargo_release_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float55 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus cargo release rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float55, units_btn, description_btn] 

        box61 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_recycling_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float56 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor recycling rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float56, units_btn, description_btn] 

        box62 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_infected_apoptosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float57 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='maximum rate of cell apoptosis due to viral infection', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float57, units_btn, description_btn] 

        box63 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_apoptosis_half_max', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float58 = FloatText(value='250', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='viral load at which cells reach half max apoptosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float58, units_btn, description_btn] 

        box64 = Box(children=row, layout=box_layout)
        name_btn = Button(description='apoptosis_hill_power', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float59 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Hill power for viral load apoptosis response', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float59, units_btn, description_btn] 

        box65 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virus_fraction_released_at_death', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float60 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='fraction of internal virus released at cell death', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float60, units_btn, description_btn] 

        box66 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float61 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='max rate that infected cells secrete chemokine', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float61, units_btn, description_btn] 

        box67 = Box(children=row, layout=box_layout)
        name_btn = Button(description='debris_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float62 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate that dead cells release debris', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float62, units_btn, description_btn] 

        box68 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_activated', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float63 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='used internally to track activation of chemokine secretion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float63, units_btn, description_btn] 

        box69 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float64 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='tracks total contact time with CD8 T cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float64, units_btn, description_btn] 

        box70 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float65 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the rate at which the cell attaches to cells in contact', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float65, units_btn, description_btn] 

        box71 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_lifetime', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float66 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='the mean duration of a cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float66, units_btn, description_btn] 

        box72 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_death_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float67 = FloatText(value='50', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='threshold CD8 T cell contact time to trigger apoptosis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float67, units_btn, description_btn] 

        box73 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_attachment_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float68 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float68, units_btn, description_btn] 

        box74 = Box(children=row, layout=box_layout)
        name_btn = Button(description='elastic_attachment_coefficient', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float69 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='elastic coefficient for cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float69, units_btn, description_btn] 

        box75 = Box(children=row, layout=box_layout)
        name_btn = Button(description='relative_maximum_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float70 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='max tolerated volume (relative to normal volume) before triggering apoptosis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float70, units_btn, description_btn] 

        box76 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float71 = FloatText(value='0.167', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float71, units_btn, description_btn] 

        box77 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float72 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float72, units_btn, description_btn] 

        box78 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_chemokine_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float73 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to chemokine in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float73, units_btn, description_btn] 

        box79 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float74 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float74, units_btn, description_btn] 

        box80 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float75 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float75, units_btn, description_btn] 

        box81 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_immune_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float76 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='used internally to track activation state', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float76, units_btn, description_btn] 

        box82 = Box(children=row, layout=box_layout)

        self.cell_def_vbox0 = VBox([
          div_row1, box0, box1, box2, box3, div_row2, death_model1,box4, box5, box6, box7, box8, box9, box10, death_model2,box11, box12, box13, box14, box15, box16, box17, div_row3, box18, box19, box20, box21, box22, box23, box24, box25, box26, div_row4, box27, box28, box29, box30, box31, div_row5, box32,box33,box34,self.bool2,self.bool3,chemotaxis_btn,self.bool4,box35,box36,div_row6, box37,box38,box39,box40,box41,box42,box43,box44,div_row7, div_row8,          box45,
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
          box79,
          box80,
          box81,
          box82,
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox0)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = lung epithelium
        #  ------------------------- 
        div_row9 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row9.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float77 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float77, units_btn, ]
        box83 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row10 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row10.style.button_color = 'orange'
        self.bool5 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        #  ------------------------- 
        div_row11 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row11.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        self.cell_def_vbox1 = VBox([
          div_row9, death_model1,box83, div_row10, self.bool5,div_row11,         ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox1)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = immune
        #  ------------------------- 
        div_row12 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row12.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float78 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float78, units_btn, ]
        box84 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float79 = FloatText(value='10', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float79, units_btn, ]
        box85 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row13 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row13.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float80 = FloatText(value='5e-4', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float80, units_btn, ]
        box86 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row14 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row14.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float81 = FloatText(value='4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float81, units_btn]
        box87 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float82 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float82, units_btn]
        box88 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float83 = FloatText(value='0.70', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float83, units_btn]
        box89 = Box(children=row, layout=box_layout)
        self.bool6 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        self.bool7 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool8 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_substrate3 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate3]
        box90 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_direction3 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction3]
        box91 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row15 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row15.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text4 = Text(value='pro-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text4]
        box92 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float84 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float84, units_btn]
        box93 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text5 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text5]
        box94 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float85 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float85, units_btn]
        box95 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text6 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text6]
        box96 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float86 = FloatText(value='0.1', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float86, units_btn]
        box97 = Box(children=row, layout=box_layout)

#      ================== <custom_data>, if present ==================

        self.cell_def_vbox2 = VBox([
          div_row12, box84, box85, div_row13, death_model1,box86, div_row14, box87,box88,box89,self.bool6,self.bool7,chemotaxis_btn,self.bool8,box90,box91,div_row15, box92,box93,box94,box95,box96,box97,        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox2)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = CD8 Tcell
        #  ------------------------- 
        div_row16 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row16.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float87 = FloatText(value='2.8e-4', step='1e-05', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float87, units_btn, ]
        box98 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row17 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row17.style.button_color = 'orange'

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float88 = FloatText(value='0.70', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float88, units_btn]
        box99 = Box(children=row, layout=box_layout)
        self.bool9 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        self.bool10 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool11 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_substrate4 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate4]
        box100 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_direction4 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction4]
        box101 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row18 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row18.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float89 = FloatText(value='478', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float89, units_btn, ]
        box102 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float90 = FloatText(value='47.8', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float90, units_btn, ]
        box103 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row19 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row19.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text7 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text7]
        box104 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float91 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float91, units_btn]
        box105 = Box(children=row, layout=box_layout)

#      ================== <custom_data>, if present ==================

        div_row20 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row20.style.button_color = 'cyan'
        name_btn = Button(description='cell_attachment_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float92 = FloatText(value='0.2', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float92, units_btn, description_btn] 

        box106 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_lifetime', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float93 = FloatText(value='8.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float93, units_btn, description_btn] 

        box107 = Box(children=row, layout=box_layout)

        self.cell_def_vbox3 = VBox([
          div_row16, death_model1,box98, div_row17, box99,self.bool9,self.bool10,chemotaxis_btn,self.bool11,box100,box101,div_row18, box102, box103, div_row19, box104,box105,div_row20,          box106,
          box107,
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox3)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = macrophage
        #  ------------------------- 
        div_row21 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row21.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float94 = FloatText(value='2.1e-4', step='1e-05', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float94, units_btn, ]
        box108 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row22 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row22.style.button_color = 'orange'

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float95 = FloatText(value='0.7', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float95, units_btn]
        box109 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float96 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float96, units_btn]
        box110 = Box(children=row, layout=box_layout)
        self.bool12 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        self.bool13 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool14 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate5 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate5]
        box111 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction5 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction5]
        box112 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row23 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row23.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float97 = FloatText(value='4849', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float97, units_btn, ]
        box113 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float98 = FloatText(value='485', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float98, units_btn, ]
        box114 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float99 = FloatText(value='0.045', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float99, units_btn, ]
        box115 = Box(children=row, layout=box_layout)


#      ================== <custom_data>, if present ==================

        div_row24 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row24.style.button_color = 'cyan'
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float100 = FloatText(value='0.167', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float100, units_btn, description_btn] 

        box116 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float101 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float101, units_btn, description_btn] 

        box117 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_chemokine_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float102 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to chemokine in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float102, units_btn, description_btn] 

        box118 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float103 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float103, units_btn, description_btn] 

        box119 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float104 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float104, units_btn, description_btn] 

        box120 = Box(children=row, layout=box_layout)

        self.cell_def_vbox4 = VBox([
          div_row21, death_model1,box108, div_row22, box109,box110,self.bool12,self.bool13,chemotaxis_btn,self.bool14,box111,box112,div_row23, box113, box114, box115, div_row24,          box116,
          box117,
          box118,
          box119,
          box120,
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox4)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = neutrophil
        #  ------------------------- 
        div_row25 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row25.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float105 = FloatText(value='8.9e-4', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float105, units_btn, ]
        box121 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row26 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row26.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float106 = FloatText(value='19', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float106, units_btn]
        box122 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float107 = FloatText(value='0.91', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float107, units_btn]
        box123 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float108 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float108, units_btn]
        box124 = Box(children=row, layout=box_layout)
        self.bool15 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        self.bool16 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool17 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate6 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate6]
        box125 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction6 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction6]
        box126 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row27 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row27.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text8 = Text(value='virion', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text8]
        box127 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float109 = FloatText(value='0.1', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float109, units_btn]
        box128 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row28 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row28.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float110 = FloatText(value='1437', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float110, units_btn, ]
        box129 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float111 = FloatText(value='143.7', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float111, units_btn, ]
        box130 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float112 = FloatText(value='0.045', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float112, units_btn, ]
        box131 = Box(children=row, layout=box_layout)


#      ================== <custom_data>, if present ==================

        div_row29 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row29.style.button_color = 'cyan'
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float113 = FloatText(value='0.117', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float113, units_btn, description_btn] 

        box132 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float114 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float114, units_btn, description_btn] 

        box133 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_chemokine_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float115 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to chemokine in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float115, units_btn, description_btn] 

        box134 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float116 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float116, units_btn, description_btn] 

        box135 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float117 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float117, units_btn, description_btn] 

        box136 = Box(children=row, layout=box_layout)

        self.cell_def_vbox5 = VBox([
          div_row25, death_model1,box121, div_row26, box122,box123,box124,self.bool15,self.bool16,chemotaxis_btn,self.bool17,box125,box126,div_row27, box127,box128,div_row28, box129, box130, box131, div_row29,          box132,
          box133,
          box134,
          box135,
          box136,
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox5)



        row = [name_btn, self.float117, units_btn, description_btn] 
        box131 = Box(children=row, layout=box_layout)


        self.tab = VBox([
          self.cell_type_parent_row, explain_inheritance, 
self.cell_def_vbox0, self.cell_def_vbox1, self.cell_def_vbox2, self.cell_def_vbox3, self.cell_def_vbox4, self.cell_def_vbox5,         ])
    #------------------------------
    def cell_type_cb(self, change):
        if change['type'] == 'change' and change['name'] == 'value':
            # print("changed to %s" % change['new'])
            self.parent_name.value = self.cell_type_parent_dict[change['new']]
            idx_selected = list(self.cell_type_parent_dict.keys()).index(change['new'])
            # print('index=',idx_selected)
            # self.vbox1.layout.visibility = 'hidden'  # vs. visible
            # self.vbox1.layout.visibility = None 

            # There's probably a better way to do this, but for now,
            # we hide all vboxes containing the widgets for the different cell defs
            # and only display the contents of the selected one.
            for vb in self.cell_def_vboxes:
                vb.layout.display = 'none'   # vs. 'contents'
            self.cell_def_vboxes[idx_selected].layout.display = 'contents'   # vs. 'contents'


    #------------------------------
    def display_cell_type_default(self):
        # print("display_cell_type_default():")
        #print("    self.cell_type_parent_dict = ",self.cell_type_parent_dict)

        # There's probably a better way to do this, but for now,
        # we hide all vboxes containing the widgets for the different cell defs
        # and only display the contents of 'default'
        for vb in self.cell_def_vboxes:
            vb.layout.display = 'none'   # vs. 'contents'
        self.cell_def_vboxes[0].layout.display = 'contents'


    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//cell_definitions')  # find unique entry point

        # ------------------ cell_definition: default
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        self.float0.value = float(uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        self.float1.value = float(uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[2]').text)
        self.float2.value = float(uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[3]').text)
        self.float3.value = float(uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[4]').text)
        # ---------  death 
        self.float4.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//death_rate').text)
        self.float5.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text)
        self.float6.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text)
        self.float7.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float8.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text)
        self.float9.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//calcification_rate').text)
        self.float10.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//relative_rupture_volume').text)
        self.float11.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//death_rate').text)
        self.float12.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        self.float13.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        self.float14.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float15.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        self.float16.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//calcification_rate').text)
        self.float17.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)
        # ---------  volume 
        self.float18.value = float(uep.find('.//cell_definition[1]//phenotype//volume//total').text)
        self.float19.value = float(uep.find('.//cell_definition[1]//phenotype//volume//fluid_fraction').text)
        self.float20.value = float(uep.find('.//cell_definition[1]//phenotype//volume//nuclear').text)
        self.float21.value = float(uep.find('.//cell_definition[1]//phenotype//volume//fluid_change_rate').text)
        self.float22.value = float(uep.find('.//cell_definition[1]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        self.float23.value = float(uep.find('.//cell_definition[1]//phenotype//volume//nuclear_biomass_change_rate').text)
        self.float24.value = float(uep.find('.//cell_definition[1]//phenotype//volume//calcified_fraction').text)
        self.float25.value = float(uep.find('.//cell_definition[1]//phenotype//volume//calcification_rate').text)
        self.float26.value = float(uep.find('.//cell_definition[1]//phenotype//volume//relative_rupture_volume').text)
        # ---------  mechanics 
        self.float27.value = float(uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float28.value = float(uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float29.value = float(uep.find('.//cell_definition[1]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool0.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool1.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float32.value = float(uep.find('.//cell_definition[1]//phenotype//motility//speed').text)
        self.float33.value = float(uep.find('.//cell_definition[1]//phenotype//motility//persistence_time').text)
        self.float34.value = float(uep.find('.//cell_definition[1]//phenotype//motility//migration_bias').text)
        self.bool2.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//motility//options//enabled').text.lower()))
        self.bool3.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//motility//options//use_2D').text.lower()))
        self.bool4.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate1.value = uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction1.value = uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text0.value = uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]').attrib['name']
        self.float35.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]//secretion_target').text)
        self.text1.value = uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]').attrib['name']
        self.float36.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]//secretion_target').text)
        self.text2.value = uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]').attrib['name']
        self.float37.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]//secretion_target').text)
        self.text3.value = uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]').attrib['name']
        self.float38.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]//secretion_target').text)
        # ---------  molecular
        # ------------------ cell_definition: lung epithelium
        # ---------  death 
        self.float77.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[1]//death_rate').text)
        # ---------  motility 
        self.bool5.value = ('true' == (uep.find('.//cell_definition[2]//phenotype//motility//options//enabled').text.lower()))
        # ---------  secretion 
        # ------------------ cell_definition: immune
        # ---------  mechanics 
        self.float78.value = float(uep.find('.//cell_definition[3]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float79.value = float(uep.find('.//cell_definition[3]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        # ---------  death 
        self.float80.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[1]//death_rate').text)
        # ---------  motility 
        self.float81.value = float(uep.find('.//cell_definition[3]//phenotype//motility//speed').text)
        self.float82.value = float(uep.find('.//cell_definition[3]//phenotype//motility//persistence_time').text)
        self.float83.value = float(uep.find('.//cell_definition[3]//phenotype//motility//migration_bias').text)
        self.bool6.value = ('true' == (uep.find('.//cell_definition[3]//phenotype//motility//options//enabled').text.lower()))
        self.bool7.value = ('true' == (uep.find('.//cell_definition[3]//phenotype//motility//options//use_2D').text.lower()))
        self.bool8.value = ('true' == (uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate3.value = uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction3.value = uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text4.value = uep.find('.//cell_definition[3]//phenotype//secretion//substrate[1]').attrib['name']
        self.float84.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[1]//uptake_rate').text)
        self.text5.value = uep.find('.//cell_definition[3]//phenotype//secretion//substrate[2]').attrib['name']
        self.float85.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[2]//uptake_rate').text)
        self.text6.value = uep.find('.//cell_definition[3]//phenotype//secretion//substrate[3]').attrib['name']
        self.float86.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[3]//uptake_rate').text)
        # ------------------ cell_definition: CD8 Tcell
        # ---------  death 
        self.float87.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[1]//death_rate').text)
        # ---------  motility 
        self.float88.value = float(uep.find('.//cell_definition[4]//phenotype//motility//migration_bias').text)
        self.bool9.value = ('true' == (uep.find('.//cell_definition[4]//phenotype//motility//options//enabled').text.lower()))
        self.bool10.value = ('true' == (uep.find('.//cell_definition[4]//phenotype//motility//options//use_2D').text.lower()))
        self.bool11.value = ('true' == (uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate4.value = uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction4.value = uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  volume 
        self.float89.value = float(uep.find('.//cell_definition[4]//phenotype//volume//total').text)
        self.float90.value = float(uep.find('.//cell_definition[4]//phenotype//volume//nuclear').text)
        # ---------  secretion 
        self.text7.value = uep.find('.//cell_definition[4]//phenotype//secretion//substrate[1]').attrib['name']
        self.float91.value = float(uep.find('.//cell_definition[4]//phenotype//secretion//substrate[1]//uptake_rate').text)
        # ------------------ cell_definition: macrophage
        # ---------  death 
        self.float94.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[1]//death_rate').text)
        # ---------  motility 
        self.float95.value = float(uep.find('.//cell_definition[5]//phenotype//motility//migration_bias').text)
        self.float96.value = float(uep.find('.//cell_definition[5]//phenotype//motility//persistence_time').text)
        self.bool12.value = ('true' == (uep.find('.//cell_definition[5]//phenotype//motility//options//enabled').text.lower()))
        self.bool13.value = ('true' == (uep.find('.//cell_definition[5]//phenotype//motility//options//use_2D').text.lower()))
        self.bool14.value = ('true' == (uep.find('.//cell_definition[5]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate5.value = uep.find('.//cell_definition[5]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction5.value = uep.find('.//cell_definition[5]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  volume 
        self.float97.value = float(uep.find('.//cell_definition[5]//phenotype//volume//total').text)
        self.float98.value = float(uep.find('.//cell_definition[5]//phenotype//volume//nuclear').text)
        self.float99.value = float(uep.find('.//cell_definition[5]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        # ------------------ cell_definition: neutrophil
        # ---------  death 
        self.float105.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[1]//death_rate').text)
        # ---------  motility 
        self.float106.value = float(uep.find('.//cell_definition[6]//phenotype//motility//speed').text)
        self.float107.value = float(uep.find('.//cell_definition[6]//phenotype//motility//migration_bias').text)
        self.float108.value = float(uep.find('.//cell_definition[6]//phenotype//motility//persistence_time').text)
        self.bool15.value = ('true' == (uep.find('.//cell_definition[6]//phenotype//motility//options//enabled').text.lower()))
        self.bool16.value = ('true' == (uep.find('.//cell_definition[6]//phenotype//motility//options//use_2D').text.lower()))
        self.bool17.value = ('true' == (uep.find('.//cell_definition[6]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate6.value = uep.find('.//cell_definition[6]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction6.value = uep.find('.//cell_definition[6]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text8.value = uep.find('.//cell_definition[6]//phenotype//secretion//substrate[1]').attrib['name']
        self.float109.value = float(uep.find('.//cell_definition[6]//phenotype//secretion//substrate[1]//uptake_rate').text)
        # ---------  volume 
        self.float110.value = float(uep.find('.//cell_definition[6]//phenotype//volume//total').text)
        self.float111.value = float(uep.find('.//cell_definition[6]//phenotype//volume//nuclear').text)
        self.float112.value = float(uep.find('.//cell_definition[6]//phenotype//volume//cytoplasmic_biomass_change_rate').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//cell_definitions')  # find unique entry point

        # ------------------ cell_definition: default
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float0.value)
        uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[2]').text = str(self.float1.value)
        uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[3]').text = str(self.float2.value)
        uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[4]').text = str(self.float3.value)
        # ---------  death 
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//death_rate').text = str(self.float4.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text = str(self.float5.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text = str(self.float6.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float7.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text = str(self.float8.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//calcification_rate').text = str(self.float9.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//relative_rupture_volume').text = str(self.float10.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//death_rate').text = str(self.float11.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text = str(self.float12.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text = str(self.float13.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float14.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text = str(self.float15.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//calcification_rate').text = str(self.float16.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//relative_rupture_volume').text = str(self.float17.value)
        # ---------  volume 
        uep.find('.//cell_definition[1]//phenotype//volume//total').text = str(self.float18.value)
        uep.find('.//cell_definition[1]//phenotype//volume//fluid_fraction').text = str(self.float19.value)
        uep.find('.//cell_definition[1]//phenotype//volume//nuclear').text = str(self.float20.value)
        uep.find('.//cell_definition[1]//phenotype//volume//fluid_change_rate').text = str(self.float21.value)
        uep.find('.//cell_definition[1]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float22.value)
        uep.find('.//cell_definition[1]//phenotype//volume//nuclear_biomass_change_rate').text = str(self.float23.value)
        uep.find('.//cell_definition[1]//phenotype//volume//calcified_fraction').text = str(self.float24.value)
        uep.find('.//cell_definition[1]//phenotype//volume//calcification_rate').text = str(self.float25.value)
        uep.find('.//cell_definition[1]//phenotype//volume//relative_rupture_volume').text = str(self.float26.value)
        # ---------  mechanics 
        uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float27.value)
        uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float28.value)
        uep.find('.//cell_definition[1]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float29.value)
        uep.find('.//cell_definition[1]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool0.value)
        uep.find('.//cell_definition[1]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool1.value)
        # ---------  motility 
        uep.find('.//cell_definition[1]//phenotype//motility//speed').text = str(self.float32.value)
        uep.find('.//cell_definition[1]//phenotype//motility//persistence_time').text = str(self.float33.value)
        uep.find('.//cell_definition[1]//phenotype//motility//migration_bias').text = str(self.float34.value)
        uep.find('.//cell_definition[1]//phenotype//motility//options//enabled').text = str(self.bool2.value)
        uep.find('.//cell_definition[1]//phenotype//motility//options//use_2D').text = str(self.bool3.value)
        uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool4.value)
        uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate1.value)
        uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction1.value)
        # ---------  secretion 
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text0.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]//secretion_target').text = str(self.float35.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text1.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]//secretion_target').text = str(self.float36.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text2.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]//secretion_target').text = str(self.float37.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]').attrib['name'] = str(self.text3.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]//secretion_target').text = str(self.float38.value)
        # ---------  molecular
        # ------------------ cell_definition: lung epithelium
        # ---------  death 
        uep.find('.//cell_definition[2]//phenotype//death//model[1]//death_rate').text = str(self.float77.value)
        # ---------  motility 
        uep.find('.//cell_definition[2]//phenotype//motility//options//enabled').text = str(self.bool5.value)
        # ---------  secretion 
        # ------------------ cell_definition: immune
        # ---------  mechanics 
        uep.find('.//cell_definition[3]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float78.value)
        uep.find('.//cell_definition[3]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float79.value)
        # ---------  death 
        uep.find('.//cell_definition[3]//phenotype//death//model[1]//death_rate').text = str(self.float80.value)
        # ---------  motility 
        uep.find('.//cell_definition[3]//phenotype//motility//speed').text = str(self.float81.value)
        uep.find('.//cell_definition[3]//phenotype//motility//persistence_time').text = str(self.float82.value)
        uep.find('.//cell_definition[3]//phenotype//motility//migration_bias').text = str(self.float83.value)
        uep.find('.//cell_definition[3]//phenotype//motility//options//enabled').text = str(self.bool6.value)
        uep.find('.//cell_definition[3]//phenotype//motility//options//use_2D').text = str(self.bool7.value)
        uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool8.value)
        uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate3.value)
        uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction3.value)
        # ---------  secretion 
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text4.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[1]//uptake_rate').text = str(self.float84.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text5.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[2]//uptake_rate').text = str(self.float85.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text6.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[3]//uptake_rate').text = str(self.float86.value)
        # ------------------ cell_definition: CD8 Tcell
        # ---------  death 
        uep.find('.//cell_definition[4]//phenotype//death//model[1]//death_rate').text = str(self.float87.value)
        # ---------  motility 
        uep.find('.//cell_definition[4]//phenotype//motility//migration_bias').text = str(self.float88.value)
        uep.find('.//cell_definition[4]//phenotype//motility//options//enabled').text = str(self.bool9.value)
        uep.find('.//cell_definition[4]//phenotype//motility//options//use_2D').text = str(self.bool10.value)
        uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool11.value)
        uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate4.value)
        uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction4.value)
        # ---------  volume 
        uep.find('.//cell_definition[4]//phenotype//volume//total').text = str(self.float89.value)
        uep.find('.//cell_definition[4]//phenotype//volume//nuclear').text = str(self.float90.value)
        # ---------  secretion 
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text7.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[1]//uptake_rate').text = str(self.float91.value)
        # ------------------ cell_definition: macrophage
        # ---------  death 
        uep.find('.//cell_definition[5]//phenotype//death//model[1]//death_rate').text = str(self.float94.value)
        # ---------  motility 
        uep.find('.//cell_definition[5]//phenotype//motility//migration_bias').text = str(self.float95.value)
        uep.find('.//cell_definition[5]//phenotype//motility//persistence_time').text = str(self.float96.value)
        uep.find('.//cell_definition[5]//phenotype//motility//options//enabled').text = str(self.bool12.value)
        uep.find('.//cell_definition[5]//phenotype//motility//options//use_2D').text = str(self.bool13.value)
        uep.find('.//cell_definition[5]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool14.value)
        uep.find('.//cell_definition[5]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate5.value)
        uep.find('.//cell_definition[5]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction5.value)
        # ---------  volume 
        uep.find('.//cell_definition[5]//phenotype//volume//total').text = str(self.float97.value)
        uep.find('.//cell_definition[5]//phenotype//volume//nuclear').text = str(self.float98.value)
        uep.find('.//cell_definition[5]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float99.value)
        # ------------------ cell_definition: neutrophil
        # ---------  death 
        uep.find('.//cell_definition[6]//phenotype//death//model[1]//death_rate').text = str(self.float105.value)
        # ---------  motility 
        uep.find('.//cell_definition[6]//phenotype//motility//speed').text = str(self.float106.value)
        uep.find('.//cell_definition[6]//phenotype//motility//migration_bias').text = str(self.float107.value)
        uep.find('.//cell_definition[6]//phenotype//motility//persistence_time').text = str(self.float108.value)
        uep.find('.//cell_definition[6]//phenotype//motility//options//enabled').text = str(self.bool15.value)
        uep.find('.//cell_definition[6]//phenotype//motility//options//use_2D').text = str(self.bool16.value)
        uep.find('.//cell_definition[6]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool17.value)
        uep.find('.//cell_definition[6]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate6.value)
        uep.find('.//cell_definition[6]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction6.value)
        # ---------  secretion 
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text8.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[1]//uptake_rate').text = str(self.float109.value)
        # ---------  volume 
        uep.find('.//cell_definition[6]//phenotype//volume//total').text = str(self.float110.value)
        uep.find('.//cell_definition[6]//phenotype//volume//nuclear').text = str(self.float111.value)
        uep.find('.//cell_definition[6]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float112.value)
