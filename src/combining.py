import json

def load_fail(path, fail):
    Jdata = []
    try:
        Jdata=json.load(open(path))
        # Jdata = dict(Jdata)
        print(Jdata)
        for word in Jdata:
            fail.append(word)
        
        return fail
    except:
        pass
    

def load_OLED(path, final):
    
    Jdata=json.load(open(path))
    # Jdata = dict(Jdata)
    # print(Jdata)
    for word_dict in Jdata:
        final.append(word_dict)
    

    return final
    
        
fail = []
final = []
for i in range(496):
    oled_path = "/home/lafesta/Desktop/DAforIT/dataset/OLED/OLED/OLED" + str(i) + '.json'
    fail_path = "/home/lafesta/Desktop/DAforIT/dataset/OLED/Fail/OLED_fail" + str(i) + '.json'
    # Jdata=json.load(open(oled_path))
    # Jdata = dict(Jdata)
    # print(Jdata)
    # for word_dict in Jdata:
    #     final.append(word_dict)
    load_fail(fail_path, fail)
    load_OLED(oled_path, final)

# print(final)
# print(fail)
with open('/home/lafesta/Desktop/DAforIT/dataset/OLED/OLED/OLED_Combined.json', 'w') as json_file:
    json.dump(final, json_file, indent=4)

with open('/home/lafesta/Desktop/DAforIT/dataset/OLED/Fail/OLED_fail_Combined.json', 'w') as json_file:
    json.dump(fail, json_file, indent=4)