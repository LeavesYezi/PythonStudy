# Phones = ["Iphone", "huawEi", "Samsung"]
# for i in range(len(Phones)):
#     if Phones[i].lower() == "iphone":
#         Phones[i] = "iPhone"
#     else:
#         Phones[i] = Phones[i].lower()
# if Phones[-1] == "samsung":
#     print("Last phone is samsung")
# print(Phones)
# print("iPhone" in Phones and "xiaomi" not in Phones)

# users = ('admin', 'Leaves', 'Stone', 'Dandan')
# if users:
#     for user in users:
#         if user == 'admin':
#             print(f'Hi administrator, {user} can check a status report')
#         else:
#             print(f'hi {user}')
# else:
#     print('一个人也没有')

numbers = list(range(1, 10))
for num in numbers:
    if num == 1:
        print('1st')
    elif num == 2:
        print('2nd')
    elif num == 3:
        print('3rd')
    else:
        print(f'{num}th')