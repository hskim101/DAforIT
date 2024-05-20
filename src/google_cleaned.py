import json


# fail_Jdata=json.load(open('/home/lafesta/Desktop/DAforIT/dataset/OLED/Fail/OLED_fail_Combined.json'))

Jdata=json.load(open('/home/lafesta/Desktop/DAforIT/Oxford-Dictionary/google_oxford_dict.json'))

Jdata_dict = dict(Jdata)

# final=[]

# for word, definition in Jdata.items():
#     if word in fail_Jdata:
#         pass
#     else:
#         temp = {}
#         temp['word'] = word
#         temp['definition'] = definition
#         final.append(temp)

# print(len(final))

# with open('/home/lafesta/Desktop/DAforIT/dataset/Google/GoogleOED_except_fail.json', 'w') as json_file:
#             json.dump(final, json_file, indent=4, ensure_ascii=False)

oled_Jdata=json.load(open('/home/lafesta/Desktop/DAforIT/dataset/OLED/OLED/OLED_Combined.json'))
#print(oled_Jdata)

temp = []
temp2 = []
garbage = []
for i in oled_Jdata:
    temp.append(i['word'])
# print(temp)
for word in Jdata.keys():
    if word in temp:
        temp2.append(word)
    else:
        garbage.append(word)

final = []
final_word = []
for word in temp2:
     if word in Jdata.keys():
          temp_dict = {}
          temp_dict['word'] = word
          temp_dict['definition'] = Jdata[word]
          final.append(temp_dict)
          final_word.append(word)

print(len(final_word))
final2_word = [] 
redun=[]
final2 = []
for item in oled_Jdata:
     if item['word'] in final_word:
          if item['word'] in final2_word:
             continue
          temp_dict = {}
          temp_dict['word'] = item['word']
          temp_dict['definition'] = item['definition']
          final2.append(temp_dict)
          final2_word.append(item['word'])

# print(temp2)
print(len(final))
print(len(final2))
print(len(final2_word))
print(len(final2_word+final_word))
print(len(set(final2_word+final_word)))

with open('/home/lafesta/Desktop/DAforIT/dataset/Google/Google_OLED_co.json', 'w') as json_file:
        json.dump(final, json_file, indent=4, ensure_ascii=False)

with open('/home/lafesta/Desktop/DAforIT/dataset/OLED/OLED_Google_co.json', 'w') as json_file:
        json.dump(final2, json_file, indent=4, ensure_ascii=False)