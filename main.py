import requests
from bs4 import BeautifulSoup as BS
import random

page = requests.get("https://kupidonia.ru/spisok/spisok-suschestvitelnyh-russkogo-jazyka/bukov/5?ysclid=ld1uvpqhwl717400972")

AllWords = []
Words = []
List = []
soup = BS(page.text, "html.parser")

AllWords = soup.findAll('li', class_='position_li link_ok')

for data in AllWords:
    if data.find('div', class_='position_title') is not None:
        Words.append(data.text)

for data in Words:
    data = [x for x in data.split() if x]
    List += data

new_list = [x.upper() for x in List]
random_index = random.randint(0, len(new_list) - 1)
word = new_list[random_index]
word_c = "\033[32m{}\033[0m".format(word)
word_l = list(word)
#print(new_list)
#print(word)

while True:
    user_word = input("\n Введите слово из 5 букв: \n")
    user_word = user_word.upper()
    user_word_l = list(user_word)
    if user_word in new_list:
        if len(user_word_l) == len(word_l):
            if user_word_l == word_l:
                print(f'Слово отгадано! Было загадано "{word_c}"' )
                break

            if user_word_l[0] == word_l[0]:
                user_word_l[0] = "\033[32m{}\033[0m".format(user_word_l[0])
            elif user_word_l[0] in word_l:
                user_word_l[0] = "\033[33m{}\033[0m".format(user_word_l[0])

            if user_word_l[1] == word_l[1]:
                user_word_l[1] = "\033[32m{}\033[0m".format(user_word_l[1])
            elif user_word_l[1] in word_l:
                user_word_l[1] = "\033[33m{}\033[0m".format(user_word_l[1])

            if user_word_l[2] == word_l[2]:
                user_word_l[2] = "\033[32m{}\033[0m".format(user_word_l[2])
            elif user_word_l[2] in word_l:
                user_word_l[2] = "\033[33m{}\033[0m".format(user_word_l[2])

            if user_word_l[3] == word_l[3]:
                user_word_l[3] = "\033[32m{}\033[0m".format(user_word_l[3])
            elif user_word_l[3] in word_l:
                user_word_l[3] = "\033[33m{}\033[0m".format(user_word_l[3])

            if user_word_l[4] == word_l[4]:
                user_word_l[4] = "\033[32m{}\033[0m".format(user_word_l[4])
            elif user_word_l[4] in word_l:
                user_word_l[4] = "\033[33m{}\033[0m".format(user_word_l[4])

            full_word = ''.join(user_word_l)
            print(full_word)

        elif len(user_word_l) > len(word_l):
            print("Вы ввели слово длиннее, чем нужно")
        elif len(user_word_l) < len(word_l):
            print("Вы ввели слово короче, чем нужно")
            continue
    else:
        print('Этого слова нет в списке загадываемых слов(')
