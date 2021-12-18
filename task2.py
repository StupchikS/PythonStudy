with open("text2.txt", 'r+') as f:
    text_data = f.readlines()
    print(text_data)
    text_data = text_data[::-1]
    print(text_data)
    f.seek(0)
    f.writelines(text_data)





