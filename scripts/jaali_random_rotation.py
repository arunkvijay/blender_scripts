import bpy
import random
from mathutils import Quaternion
from math import radians

sel_objects = bpy.context.selected_objects
rotation_angles = [random.choice([0,1,3])*90 for s in sel_objects]

for sel, angle in zip(sel_objects, rotation_angles):
    angle_rad = radians(angle)
    sel.rotation_euler.rotate(Quaternion((0.,1.,0.), angle_rad))
