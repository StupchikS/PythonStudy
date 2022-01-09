# import os.path
# import os
#
# for root, dirs, files in os.walk("work1"):
#     for file in files:
#         if os.path.getsize(root + "\\" + file) != 0:
#             print(root + "\\" + file, end="\t")
#             print(" размер файда = ", os.path.getsize(root + "\\" + file))
#         else:
#             os.rename(root + "\\" + file, "work1\\emptyfiles" "\\" + file)




n = [1, 2, 3, 4, 5]
for c, i in enumerate(n):
    if c % 2 == 0:
        print(i)

# print(c)

