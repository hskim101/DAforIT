# Readme

## Crawling 과정
1. Google OED dataset을 github에서 찾음 (약 5만개 단어)
2. Oxford Learner's Dictionary를 크롤링하기 위해 크롤링할 단어를 1번 데이터셋 목록으로 사용
3. 크롤링 response 횟수 제한 및 중간 끊김 방지를 위해 단어 100개 크롤링할 때마다 부분적으로 로컬 파일로 저장 (100개 크롤링 당 30~40초 소요)
4. 크롤링 과정에서 response가 정상적으로 작동한 단어와 그렇지 않은 단어의 목록을 분리 (Fail datas)
5. Fail 단어들에 대해 다시 크롤링을 재시도해보았지만 데이터가 쌓이지 않음.
6. 부분적으로 크롤링한 데이터 파일을 하나로 통합 (dataset/OLED/OLED/OLED_Combined.json)
7. GoogleOED와 OLED 데이터셋의 단어 통일을 위해 GoogleOED에서 OLED에 없는 단어 제외
8. 통일된 단어 총 15,512개 (dataset/Google/GoogleOED_Final.json, dataset/OLED/OLED/OLED_Final.json)
9. 여러 의미를 가진 단어 수: GoogleOED 4,588개, OLED 7,929개 
