import os

# define the example data
root_dir, _ = os.path.split(__file__)
exampleatlas = os.path.join(root_dir, 'data', 'cc400_roi_atlas.nii')
examplezmap = os.path.join(root_dir, 'data', 'cognitive control_pFgA_z_FDR_0.01.nii.gz')
examplet1 = os.path.join(root_dir, 'data', 'T1.nii.gz')

#import main class
from .niwidget import NiWidget



