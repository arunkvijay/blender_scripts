import bpy

selected_objects = bpy.context.selected_objects

print(selected_objects)
print(len(selected_objects))

for obj in selected_objects:
    obj.lightgroup = "Indoor Lights"
