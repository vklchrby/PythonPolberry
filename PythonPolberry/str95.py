vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Введите текст")
itog = []
for letter in word:
    if letter in vowels:
        #itog.append(letter)
        #print(letter)
        #print(itog)
        if not  letter in itog:
            itog.append(letter)
print(itog)
#for vowels in  itog:
   # print(vowels)