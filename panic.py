#Трансформируем строку "Don't panic!" в строку "on tap"

phrase = "Don't panic!"
plist = list(phrase)

print(phrase)
print(plist)      # ['D', 'o', 'n', "'", 't', ' ', 'p', 'a', 'n', 'i', 'c', '!']

for i in range(4):
    plist.pop()    # ['D', 'o', 'n', "'", 't', ' ', 'p', 'a']

plist.pop(0)       # 'o', 'n', "'", 't', ' ', 'p', 'a'
plist.remove("'")  # 'o', 'n', 't', ' ', 'p', 'a'
plist.extend([plist.pop(), plist.pop()]) #сначала отработает код в скобках:  'o', 'n', 't', ' ' а затем извлеченные объекты добавятся в конец списка 'o', 'n', 't', ' ', 'a', 'p'
plist.insert(2, plist.pop(3))   #убираем пробел, затем его помещаем перед элементом с индексом 2 (on tap)

new_phrase = ''.join(plist)      #превращаем "plist" обратно в строку
print(plist)
print(new_phrase)