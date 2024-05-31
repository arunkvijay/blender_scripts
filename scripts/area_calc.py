import bpy
import bmesh
from functools import reduce
from math import ceil

def area_calc(mesh):
    bm = bmesh.from_edit_mesh(mesh)
    sel_faces = [f for f in bm.faces if f.select]
    area = reduce(lambda x, y: x+y, [sel_f.calc_area() for sel_f in sel_faces])
    return area
    
sel = bpy.context.object.data
#print('Area in SFt = ',ceil(area_calc(sel)*10.7639))
print('Area in Sqmm = ',area_calc(sel)*1000*1000)


    
