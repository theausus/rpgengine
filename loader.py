import rpgengine
flag = True
while flag:
    prompt = input(">")
    if prompt != "stop":
        output = rpgengine.parser(prompt)
    else:
        flag = False
        output = "Goodbye!"
    print(output)
