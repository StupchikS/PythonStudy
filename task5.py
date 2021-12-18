#  def shell_sort(s):
#     gap = len(s)
#
#     while gap > 0:
#         for val in range(gap, len(s)):
#             cur_val = s[val]
#             pos = val
#
#             while pos >= gap and s[pos - gap] > cur_val:
#                 s[pos] = s[pos-gap]
#                 pos -= gap
#                 s[pos] = cur_val
#
#         gap //= 2
#         # print("После увеличения размера", gap, "Список:", s)
#     return s
#
#
# a = [randint(1, 99) for i in range(10000)]
# print(a)
# start = t.monotonic()
# shell_sort(a)
# print(a)
# res = t.monotonic() - start
# print(round(res, 4), "sec")
