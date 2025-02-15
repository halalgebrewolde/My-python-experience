message=input(">")
Sss=message.split(" ")
emojis={
    ":)":"😊",
    ":(":"☹️"
}
ok=""
for word in Sss:
    ok+=emojis.get(word,word) + " "
print(ok)