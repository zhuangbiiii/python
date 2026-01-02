import ezdxf
import math

# 创建 DXF 文档
doc = ezdxf.new('R2010')  # 使用 AutoCAD 2010 格式
msp = doc.modelspace()

# 齿轮参数
m = 2  # 模数
alpha = math.radians(20)  # 压力角（弧度）
ha = 1 * m  # 齿顶高
hf = 1.25 * m  # 齿根高
p = math.pi * m  # 齿距

# 齿条齿形关键点计算（以一个齿槽中心为原点）
# 分度线上的齿厚
s = p / 2

# 计算齿根处宽度偏移量
root_offset = hf * math.tan(alpha)

# 单个齿槽的关键点（从左侧齿顶开始，顺时针）
points = [
    # 左侧齿面
    (-s/2, ha),  # P1: 左侧齿顶
    (-s/2 - root_offset, -hf),  # P2: 左侧齿根
    
    # 齿底（平底，如果需要圆角可以修改）
    (-s/2 - root_offset + 0.2, -hf),  # 底部左侧稍微延长
    (s/2 + root_offset - 0.2, -hf),   # 底部右侧稍微延长
    
    # 右侧齿面
    (s/2 + root_offset, -hf),  # P3: 右侧齿根
    (s/2, ha),  # P4: 右侧齿顶
]

# 绘制单个齿槽
msp.add_lwpolyline(points, close=True)

# 阵列生成多个齿（10个齿）
for i in range(1, 10):
    copy_points = [(x + i * p, y) for x, y in points]
    msp.add_lwpolyline(copy_points, close=True)

# 添加标注和参考线（可选）
# 分度线
msp.add_line((-5, 0), (p * 10 + 5, 0), dxfattribs={'color': 1})  # 红色

# 齿顶线
msp.add_line((-5, ha), (p * 10 + 5, ha), dxfattribs={'color': 2})  # 黄色

# 齿根线
msp.add_line((-5, -hf), (p * 10 + 5, -hf), dxfattribs={'color': 3})  # 绿色

# 添加参数文本
msp.add_text(f"模数 m = {m}", dxfattribs={
    'height': 1.0,
    'color': 7
}).set_pos((p * 5, ha + 3))

msp.add_text(f"压力角 α = 20°", dxfattribs={
    'height': 1.0,
    'color': 7
}).set_pos((p * 5, ha + 1.5))

msp.add_text(f"齿距 p = {p:.3f} mm", dxfattribs={
    'height': 1.0,
    'color': 7
}).set_pos((p * 5, ha + 0))

# 保存 DXF 文件
doc.saveas('gear_rack_m2_20deg.dxf')

print("齿条 DXF 文件已生成: gear_rack_m2_20deg.dxf")
print(f"参数: 模数={m}, 压力角=20°, 齿距={p:.3f}mm")
print(f"齿顶高={ha}mm, 齿根高={hf}mm")