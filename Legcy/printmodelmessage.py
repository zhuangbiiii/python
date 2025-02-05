import bpy

# Get all selected object,(if any, otherwise get all obj)
objects = bpy.context.selected_objects
if not objects:
    objects = bpy.context.scene.objects

# Print all objects name.
for object in objects:
    print(object.name)
    print(object.dimensions)
    print(object.location)