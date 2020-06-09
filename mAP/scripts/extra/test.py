import sys
import os
import glob
import xml.etree.ElementTree as ET

# make sure that the cwd() in the beginning is the location of the python script (so that every path makes sense)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# change directory to the one with the files to be changed

parent_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

parent_path = os.path.abspath(os.path.join(parent_path, os.pardir))
GT_PATH = os.path.join(parent_path, 'input','ground-truth')

os.chdir(GT_PATH)
xml_list = glob.glob('*.xml')
print(xml_list)





