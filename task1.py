with open("text1.txt", 'r') as f:
    text_data = f.readlines()
    print(text_data)
    first_str = int(input("первую строку выбираем "))
    second_str = int(input("вторую строку выбираем "))
    if first_str > len(text_data) or second_str > len(text_data) or first_str == second_str:
        print("нет такой строки, или вы выбрали одну и туже строку")
    else:
        with open("text1.txt", "w") as f:
            text_data[first_str - 1], text_data[second_str - 1] = text_data[second_str - 1], text_data[first_str - 1]
            print(text_data)
            f.writelines(text_data)
