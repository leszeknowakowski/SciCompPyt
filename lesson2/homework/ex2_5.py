str = "Co oxides and oxyhydroxides have been studied \n" \
      " extensively in the past as promising electrocatalysts \n" \
      "for the oxygen evolution reaction (OER) in neutral to \n"

text_length = len(str)
black_char_num = len(str) - str.count(" ")

words_num = len(str.split())
str_list=[]
words_length=[]

for i in range(words_num):
    a = str.split()[i]
    str_list.append(a)
    words_length.append( len(str_list[i]))

longest_word_len = max(words_length)
longest_word = str_list[ words_length.index(longest_word_len)]

print("number of black characters:  ", black_char_num)
print("number of words: ", words_num)
print("the longest word is: ", longest_word, " and its length is: " , longest_word_len, " characters")
#str_list.sort(key=str.lower()) ##doesn't work - "str" object is not callable :( python 3.9
str_list.sort(key=len)

print("sorted list of words:  \n",str_list)

## L = str.split()
## sum(1 for char in str if not char.isspace())
## sun(len(word) for word in L)

## max(L, key=len)