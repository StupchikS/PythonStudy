a = -5
b = 7
print(a, b)
a = a + b
b = a - b
a = a - b
print(a, b)
# второй способ, подсказка с урока
a, b = b, a
print(a, b)