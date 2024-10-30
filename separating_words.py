from fugashi import Tagger 
from tqdm import tqdm

tagger = Tagger('-Owakati') 

with open('./wiki_notag.txt', 'r', encoding='utf-8') as file:
    content = file.read()
content = content.split("\n")
contents = [item for item in content if item.strip()]
print(len(contents))

re_contents = []
for content in tqdm(contents):
    re_contents.append( tagger.parse(content) )

re_contents = '\n'.join(re_contents)

with open('./wiki_wakati.txt', 'w', encoding='utf-8') as file:
    file.write(re_contents)