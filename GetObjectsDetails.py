import bpy
import os
# python -m pip install xlwings
import xlwings as xw

# Excel工作簿的路径，自行修改。!!不能放C盘，没有管理员权限会报错！！
excelAssetPath = 'd:/details.xlsx'

# 如果Excel存在就打开，不然就新建一个。
if os.path.exists(excelAssetPath):
    wb = xw.Book(excelAssetPath)
else:
    wb = xw.Book()

# 获取Excel工作表。
sheet = wb.sheets[0]

# 初始化表列名。
sheet.range('A1').value = ['模型名称', '模型位置', '模型旋转', '模型缩放', '模型尺寸']

# 获取选中的模型（如果有），否则获取所有模型。
objects = bpy.context.selected_objects
if not objects:
    objects = bpy.context.scene.objects

# 打印模型位置、旋转、缩放和尺寸。
def _printDetails_():
    for obj in objects:
        print(
            '模型的名称：' + str(obj.name) + '\n',
            '模型的位置：' + str(obj.location) + '\n',
            '模型的旋转：' + str(obj.rotation_euler) + '\n',
            '模型的尺寸：' + str(obj.scale) + '\n'
            '模型的尺寸：' + str(obj.dimensions) + '\n\n')

# 导出模型位置、旋转、缩放和尺寸到Excel。
def _exportToExcel_(inExcelAssetPath):
    for index in range(len(objects)):
        obj = objects[index]
        sheet.range('A' + str(index + 2)).value = str(obj.name)
        sheet.range('B' + str(index + 2)).value = str(obj.location)
        sheet.range('C' + str(index + 2)).value = str(obj.rotation_euler)
        sheet.range('D' + str(index + 2)).value = str(obj.scale)
        sheet.range('E' + str(index + 2)).value = str(obj.dimensions)

    wb.save(inExcelAssetPath)
    print('Excel文件已保存。')
    wb.close()

_exportToExcel_(excelAssetPath)
