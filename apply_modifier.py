sel_objs = bpy.context.selected_objects
for s in sel_objs:
    bpy.context.view_layer.objects.active = s #make the object active
    bpy.ops.object.modifier_apply(modifier="Solidify", report=True)
