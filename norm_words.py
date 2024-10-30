import re

# ファイルを読み込む
with open('./wiki.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# 1. HTMLタグを削除
content = re.sub(r'<[^>]*>', '', content)

# 2. 全角カッコ（と）を半角カッコに変換
content = content.replace('（', '(').replace('）', ')')

# 3. カッコ内の文字列を削除
content = re.sub(r'\([^)]*\)', '', content)

# 4. スペースを削除し、空行を削除
content = re.sub(r' ', '', content)         # 全スペースを削除
content = re.sub(r'^\s*$', '', content, flags=re.MULTILINE)  # 空行削除
content = list(filter(None, content))

# 結果を新しいファイルに保存
with open('./wiki_notag.txt', 'w', encoding='utf-8') as file:
    file.write(content)