import bpy

def changeInstance(obj):
    obj.instance_collection = bpy.data.collections["Recessed Downlighter."]

def nameUpdate(obj, index, n):
    obj.name = 'Recessed Downlighter.' + str(index + n + 1)

sel = bpy.context.view_layer.objects.selected.values() #select lights that are not recessed
objIndex = int([k for k in bpy.data.objects.keys() if 'Recessed Downlighter' in k][-1][-3:])

for i in range(len(sel)):
    obj = sel[i]
    changeInstance(obj)
    nameUpdate(obj, objIndex, i)
