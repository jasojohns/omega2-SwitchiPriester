'''
Created on Aug 29, 2016

@author: mp
https://docs.python.org/2/library/xml.etree.elementtree.html
'''

import xml.etree.ElementTree as ET

class Scene:
    name = ''

    def __init__(self, name):
        self.name = name

    def display(self):
        print "Scene Name: ", self.name
        
scenesFile = ET.parse('../scenes.xml')
scenesRoot = scenesFile.getroot()
scenes = []

for scene in scenesRoot:
    scenes.append(Scene(scene.get('name')))
    
for scene in scenes:
    scene.display()
    