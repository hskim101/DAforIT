import requests
from datetime import datetime
from bs4 import BeautifulSoup
import time
import json
def show_definitions(soup, word):

    word_container = {}
    word_container['word'] = word
    word_container['definition'] = []
    # print()
    senseList = []
    # print(word)
    senses = soup.find_all('li', class_='sense')
    for s in senses:
        definition = s.find('span', class_='def').text
        word_container['definition'].append(definition)
        # print("-", definition)
        # Examples
        # examples = s.find_all('ul', class_='examples')
        # for e in examples:
        #     for ex in e.find_all('li'):
        #         print('\t-', ex.text)
    return word_container


start = time.time()

Jdata=json.load(open('/home/lafesta/Desktop/DAforIT/Oxford-Dictionary/google_oxford_dict.json'))
Jdata_dic = dict(Jdata)

words = [test_word for test_word in Jdata_dic.keys()]
Final_result = []
not_found_word = []
fail_word = []
cnt=0
part=496
test_word=words
last_word = 'abandoned industrial site'
for i in range(len(words)):
    if words[i]==last_word:
        test_word=words[i+1:]
        break
    
fail_Jdata=json.load(open('/home/lafesta/Desktop/DAforIT/dataset/OLED/Fail/OLED_fail_Combined.json'))

for word in fail_Jdata:
    word_to_search = word
    print(word)
    scrape_url = 'https://www.oxfordlearnersdictionaries.com/definition/english/' + word_to_search
    headers = {"User-Agent": ""}
    web_response = requests.get(scrape_url, headers=headers)
    cnt+=1
    if cnt%100==0 or word==test_word[-1]:
        print(cnt)
        end = time.time()
        print(f"{end-start:.5f} sec")
        with open('/home/lafesta/Desktop/DAforIT/dataset/OLED/Fail/OLED_fail'+f'{part}'+'.json', 'w') as json_file:
            json.dump(fail_word, json_file, indent=4)

        with open('/home/lafesta/Desktop/DAforIT/dataset/OLED/Not_found/OLED_not_found'+f'{part}'+'.json', 'w') as json_file:
            json.dump(not_found_word, json_file, indent=4)     

        with open('/home/lafesta/Desktop/DAforIT/dataset/OLED/OLED/OLED'+f'{part}'+'.json', 'w') as json_file:
            json.dump(Final_result, json_file, indent=4)
        Final_result = []
        not_found_word = []
        fail_word = []

        part+=1
    if web_response.status_code == 200:
        soup = BeautifulSoup(web_response.text, 'html.parser')
        try:
            result = show_definitions(soup, word)
            print(result)
            Final_result.append(result)
        except AttributeError:
            not_found_word.append(word)
            # print('Word not found!!')
    else:
        fail_word.append(word)
        # print('Failed to get response...')



end = time.time()
print(f"{end-start:.5f} sec")