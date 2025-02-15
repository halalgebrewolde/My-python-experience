phone=input("Phone:")
numberdictionary={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
}
super=""
for ch in phone:
    super+=numberdictionary.get(ch, "!")+" "
print(super)