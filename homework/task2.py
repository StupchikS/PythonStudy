import os.path

for root, dirs, files in os.walk("work1"):
    for file in files:
        if os.path.getsize(root + "\\" + file) != 0:
            print(root + "\\" + file, end="\t")
            print(" размер файда = ", os.path.getsize(root + "\\" + file))

