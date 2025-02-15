def emojiconverter(message):
    Sss=message.split(" ")
    emojis={
    ":)":"😊",
    ":(":"☹️"
}
    ok=""
    for word in Sss:
        ok+=emojis.get(word,word) + " "
    return ok
message=input(">")
result = emojiconverter(message)
print(result)