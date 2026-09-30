list_1 = [1, 2, 3]
list_2 = list([1, 2, 3])
list_3 = [i for i in range(4)]
list_4 = [i for i in range(4) if i % 2 == 0]
list_5 = [6]*3

print('1. Truy xuất phần tử của List theo chỉ mục')
my_list = [1, 2, 3, 4]
print(my_list[2])
print('2. Duyệt list theo tập hợp')
for i in my_list:
    print(i, end=' ')
print('\n3. Duyệt list theo chỉ mục')
for i in range(len(my_list)):
    print(my_list[i], end=' ')
print("\n-------------------------------")

my_list = ['Python', 'Perl', 'Ruby', 'Golang', 'C#', 'Java', 'Swift']
print(my_list[:2])
print(my_list[None:1])
print(my_list[3:6])
print(my_list[5:])
print(my_list[4:None])
print(my_list[-2:])
print("\n-------------------------------")
list_1 = [1, 2, 3, 4]
list_2 = ["Python", "Angular", "Ruby"]
print(list_1)
print(list_2)
list_1[0] = 9
list_2[1] = "Golang"
print(list_1)
print(list_2)
print("\n-------------------------------")
list_1 = [1, 2, 3, 4]
list_2 = list_1
print(list_1)
print(list_2)
list_1[0] = 9
list_1[1] = 8
print(list_1)
print(list_2)
print("\n-------------------------------")
list_1 = [1, 2, 3, 4]
list_2 = list(list_1)
print(list_1)
print(list_2)
list_1[0] = 9
list_1[1] = 8
print(list_1)
print(list_2)
print("\n-------------------------------")
list_1 = [1, 2, 3, 4]
list_2 = list_1.copy()
print(list_1)
print(list_2)
list_1[0] = 9
list_1[1] = 8
print(list_1)
print(list_2)
print("\n-------------------------------")
my_list = ["Python", "Angular", "Ruby"]
my_list.insert(1, "Perl")
print(my_list)
print("\n-------------------------------")
my_list = ["Python", "Ruby"]
my_list.append(["Perl", "Golang"])
print(my_list)
print("\n-------------------------------")
my_list = ["Python", "Ruby"]
my_list.extend(["Perl", "Golang"])
print(my_list)
print("\n-------------------------------")
my_list = ["Python", "Angular", "Ruby"]
print(my_list.__add__(["Perl"]))
print("\n-------------------------------")
my_list = ["Python", "Angular", "Ruby", "Golang"]
my_list.pop()
print(my_list)
my_list.pop(1)
print(my_list)
print("\n-------------------------------")
my_list = ["Python", "Angular", "Ruby", "Angular", "Golang"]
my_list.remove('Angular') # del my_list[1]
print(my_list)
print("\n-------------------------------")
my_list = [3, 9, 7, 9, 5, 9, 8]
print(my_list.count(9))
print("\n-------------------------------")
my_list = [3, 9, 7, 9, 5, 9, 8]
print(my_list.__contains__(2))
print(my_list.__contains__(7))
my_list = [3, 9, 7]
print(3 in my_list)
print(8 in my_list)
print("\n-------------------------------")
my_list = [3, 2, 7, 5, 9, 8]
my_list.sort()
print(my_list)
my_list_2 = [4, 2, 5, 7, 3, 6]
sorted_list = sorted(my_list_2)
print(sorted_list)
print("\n-------------------------------")
my_list = [3, 2, 7, 5, 9, 8]
my_list.sort()
my_list.reverse()
print(my_list)
my_list_2 = [4, 2, 5, 7, 3, 6]
my_list_2.sort(reverse=True)
print(my_list_2)
print("\n-------------------------------")
my_list = ['Python', 'Perl', 'Ruby', 'Golang', 'C#', 'Java', 'Swift']
print(my_list[::-1])
print("\n-------------------------------")
s1 = 'madam'
print(f"s1: {s1}")
s_list = list(s1)
print(s_list)
s2 = ''.join(s_list)
print("s2: {0}".format(s2))
