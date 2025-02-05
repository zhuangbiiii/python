import csv

input_file = "F:\Download\BLSBookDetailStyle\mapping2.csv"
output_file = "F:\Download\BLSBookDetailStyle\mapping2_1.csv"

with open(input_file, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

# 插入新列到第1列
for row in rows:
    print(type(row))
    if row[1].startswith('v'):
        row.insert(0, 'video')
    elif row[1].startswith('p'):
        row.insert(0, 'PureImage')

# 保存修改后的文件
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)
