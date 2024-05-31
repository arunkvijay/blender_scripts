import bpy

cursor_loc = bpy.context.scene.cursor.location
sel_objects = bpy.context.selected_objects
sel_objects.sort(key=lambda obj: obj.name)

cursor_coord = []

for i in range(0,10):
    for j in range(0,12):
        new_cursor_loc = cursor_loc.copy()
        new_cursor_loc[0] -= i*0.200
        new_cursor_loc[2] += j*0.200
        cursor_coord.append(new_cursor_loc)

for s in sel_objects:
    s.select_set(False)

for i in range(len(sel_objects)):
    bpy.context.scene.cursor.location = cursor_coord[i]
    sel_objects[i].select_set(True)
    bpy.context.view_layer.objects.active = sel_objects[i]
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    sel_objects[i].select_set(False)

