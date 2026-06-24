# 注意：单词表xlsx文件要和本程序处于同一文件夹下，且此xlsx表A列要求为单元（如：Unit 1 XXX），B列为英文（如：apple），C列为中文（如：n. 苹果）。生成后的csv文件与本程序处于同一文件夹下。

# 如果提示缺少库，请按下win+R，输入cmd打开命令提示符，输入pip install pandas，再重新运行本程序即可。

import pandas as pd
import csv

# 读取Excel文件
df = pd.read_excel('Vocabulary.xlsx', sheet_name='工作表1', header=None)

# 打开CSV文件用于写入
with open('vocabulary.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # 写入CSV表头
    writer.writerow(['unit', 'en', 'cn'])
    
    current_unit = None
    # 遍历Excel的每一行
    for index, row in df.iterrows():
        # 如果A列有值（非空），说明是一个新单元
        if pd.notna(row[0]):
            current_unit = row[0]
        # 如果B列有值，说明是一个单词条目
        elif pd.notna(row[1]):
            en = row[1]
            cn = row[2] if pd.notna(row[2]) else ''
            writer.writerow([current_unit, en, cn])

print("✅ 转换完成！已生成 vocabulary.csv")