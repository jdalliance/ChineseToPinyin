import json, pinyin, re, os

print("KTapeChinese by Just Dance Alliance. Version: 0.0.1")
filename = input("Enter filename: ")
with open(filename, 'r' , encoding="utf-8") as json_file:
    data = json.load(json_file)
    
for track in data["Clips"]:
 if re.search(u'[\u4e00-\u9fff]', track['Lyrics']):
  track['Lyrics'] = pinyin.get(track['Lyrics'], format="strip", delimiter=" ") + " "

with open('output/' + filename, "w", encoding='utf-8') as f:
      json.dump(data,f,ensure_ascii=False)
