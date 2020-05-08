from bs4 import BeautifulSoup
import requests
import os
import sys


print("자동영어과제 - Developed by YJU")
print("개발자 연락처 : yju0808@naver.com - 버그, 오류 등등 발견시 제보해주세요")
print("버젼 : B0 - 베타테스터 버젼\n\n")

print("자동영어과제를 시작합니다\n")


wordsFile = open(os.getcwd() + "\\input.txt",encoding="utf-8")
words = wordsFile.read().split("\n")
wordsFile.close()

#빈 요소 지우기
while '' in words:
    words.remove('')

if len(words) == 0:
    print("인식된 단어가 없습니다 input.txt 파일을 확인해보세요(저장은 하셨죠?)\n")
    print("종료하시려면 아무거나 입력하세요\n")
    input()
    sys.exit()

print("인식된 단어 : {}개\n".format(len(words)))
print("변환을 시작합니다\n")


def GetMeaning(word):
    url = "http://endic.naver.com/search.nhn?query=" + word
    response = requests.get(url)
    crawler = BeautifulSoup(response.text, "html.parser")

    try:
        mean = crawler.find('span', {'class':'fnt_k05'}).get_text()
    except:
        mean = "뜻을 찾지 못했습니다"

    return mean





def GetSentence(word):
    url = "http://endic.naver.com/search.nhn?query=" + word
    response = requests.get(url)
    crawler = BeautifulSoup(response.text, "html.parser")

    try:
        exSentence = crawler.find('span', {'class':'fnt_e07 _ttsText'}).get_text()
    except:
        exSentence = "예문을 찾지 못했습니다"

    try:   
        exSentenceMean = crawler.find('span', {'class':'fnt_k10 _ttsText'}).get_text()
    except:
        exSentenceMean = "예문의 뜻을 찾지 못했습니다"


    sentence = exSentence + "\n    " + exSentenceMean

    return sentence


result = ""
count = 1

for word in words:

    mean = GetMeaning(word)
    exSentence = GetSentence(word)
    result = result + "{}. {} : {}\n   {}\n\n".format(count,word,mean,exSentence)



outputFile = open(os.getcwd() + "\\output.txt","w",encoding="utf-8")
outputFile.write(result)
outputFile.close()

print("변환을 완료했습니다 작동종료!\n")
print("종료하시려면 아무거나 입력하세요\n")
input()
sys.exit()