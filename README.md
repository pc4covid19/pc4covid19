# pc4covid19 - COVID19 tissue simulator nanoHUB app

**Version:** 2.1 - uses the core model at https://github.com/pc4covid19/COVID19/releases/tag/0.2.1

**Release date:** 26 April 2020 

## Overview
This repository contains code and data for the nanoHUB app https://nanohub.org/tools/pc4covid19.
Here, we primarily report on changes to the app's GUI.

It is based on the model at https://github.com/pc4covid19/COVID19. Refer to that repository
for a summary of changes to the model. 

### Caveats and disclaimers: 
**This model is under active development using rapid prototyping:**
* It has not been peer reviewed. 
* It is intended to drive basic scientific research and public education at this stage. 
* **It cannot be used for public policy decisions.**
* **It cannot be used for individual medical decisions.**

**This model will be continually refined with input from the community, particularly experts in infectious diseases. The validation state will be updated as this progresses.**

## Release summary:
### 2.1:
Sync up with the version number of the published app, https://nanohub.org/tools/pc4covid19, and include a reference to the version of the core model in this README.

### 2.0:
The major change to the GUI in this release is the addition of an 'Animate' tab.
This allows animation of cells (not substrates) in the tab and the generation of a .mp4
video that can be downloaded. The animation uses the cells' SVG files.

### 1.0:
Provides a "standard" PhysiCell-based Jupyter notebook GUI consisting of 5 tabs:
* About: a description of the model and the app
* Config Basics: input parameters common to all models (e.g., domain grid, simulation time, choice/frequency of outputs)
* Microenvironment: microenvironment parameters that are model-specific
* User Params: user parameters that are model-specific
* Out: Plots:  output display of cells and substrates
