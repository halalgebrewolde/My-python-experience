for x in range(4):
    for y in range(3):
        print(f"({x},{y})")
Numbers=[5,2,5,2,2]
for x in Numbers:
    print("x"*x)
for x in Numbers:
    output=''
    for count in range(x):
        output+='x'
    print(output)
