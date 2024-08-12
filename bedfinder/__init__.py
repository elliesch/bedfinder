'''
bedfinder.

This is initialized with the following modules:
    - .bedfinder      : Classify TPI products into glacially derived bedforms
    - .filtering   : Filter input TPI data to improve model accuracy
    - .utilities   : Helper functions for the script

'''

__version__ = '0.0.1'
__all__ = ['bedfinder', 'filtering', 'utilities']
__author__ = 'elliesch <ellianna@berkeley.edu>', 'marionmckenzie <marion.mckenzie@mines.edu>'
__minimum_python_version__ = '3.9'

from .bedfinder import *
from .filtering import *
from .utilities import *
