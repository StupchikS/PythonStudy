file1 = "file1.txt"
file2 = "file2.txt"
with open(file1, "r") as f1, open(file2, "r") as f2, open("file3.txt", "w") as f3:
    text_data = f1.readlines() + list(
        "\n") + f2.readlines()  # добавил знак переноса, иначе строки сливаются некрасиво как то
    f3.writelines(text_data)
