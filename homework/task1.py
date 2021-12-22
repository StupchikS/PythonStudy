import os.path
import os


res = []
folder_list = os.listdir("work1")
for i in folder_list:
    if os.path.isfile(r"work1\\" + i):
        res.insert(0, r"file\"" + i)
    else:
        res.append(r"dir\"" + i)

print(res)


