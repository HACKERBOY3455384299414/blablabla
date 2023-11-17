# ##============================##
# ##
# ## ფიბონაჩს რიცხვის გამოთვლა
# ##
# ##============================##
# # a, b = 0, 1
# # while b < 100:
# #     print(b)
# #     a, b = b, a + b
# #
# ##=============================##

# ##============================##
# ##
# ## რიცხვის ფაქტორიალის ფამოთვლა
# ##
# ##============================##



# # number = int(input("Input Number : "))

# # i = 1
# # factorial = 1
# # while i <= number:
# #     factorial *= i
# #     i += 1
# # print("რიცხვის", number, "ფაქტორიალი ტოლია", factorial,)


# ##============================####============================####============================##

# # number = int(input("Input : "))
# # factorial = 1
# # for i in range(1, number + 1):
# #     factorial *= i
# #     print("ფაქტორიალი", number, "რიცხვის ტოლია", factorial)
# ##============================####============================####============================##



# # i = 0
# # list = [10, 40, 20, 40]
# # for element in list:
# #     list[i] = element + 2
# #     i += 1
# #     print(list)
# ##============================####============================####============================##

# ######## this is continue operator ###########

# # for i in "Muradi Tsutsashvili":
# #     if i == "M":
# #         continue
# #     print(i, end="")

# ##============================####============================####============================##




# ######### this is break operator #############




# # for i in "hello world":
# #     if i == "o":
# #         break
# #     print(i * 2, end='')
    
    
# # for i in "hello world":
# #     if i == "a":
# #         break
# # else:
# #     print("a ასო არ არის სტრიქონში")



# # განვიხილოთ მაგალითი, ვალუტის გამცვლელი პუნქტი:
# # print(" დასრულებისთვის დააჭირეთ Y ")
# # while True:
# #     data = input("შეიტანე თანხა გაცვლისთვის : ")
# #     if data.lower() == "y":
# #         break # ციკლიდან გასვლა
# #     money = int(data)
# #     cache = round(money // 2.56)
# #     print("დაეცემა", cache, 'დოლარი')
# # print('გაცვლითი პუნქტის მუშაობა დასრულებულია')
    

# # for i in range(1, 11):
# #     for j in range(1, 11):
# #         print(i * j, end="\t")
# #     print("\n")


# # x | y --> ან ოპერაცია
# # x ^ y --> გამომეიცხავი ან ოპერაცია
# # x & y --> და ოპერაცია
# # x << n --> დაძვრა მარცხიდან
# # x >> y --> დაძვრა მარჯვნიდან
# # ~x --> ბიტების ინვერსია

# n = -37
# print(bin(n),"\n","---", n.bit_length())
# # # # # # # # import math

# # # # # # # # # ჰიპოტენუზის მნიშვნელობის გამოთვლა

# # # # # # # # a = eval(input("a = "))
# # # # # # # # b = eval(input("b = "))
# # # # # # # # c = math.sqrt(a ** 2 + b ** 2)
# # # # # # # # print("c = ", c, sep='')
# # # # # # # # print("c = %6.4f"%(c), sep='')



# # # # # # # # a = eval(input("a= "))
# # # # # # # # h = eval(input("h= "))
# # # # # # # # s = a * h / 2
# # # # # # # # print("s = ", s, sep="")
# # # # # # # # print("s = %5.3f"%(s), sep="")



# # # # # # # import random
# # # # # # # number = random.randint(65, 90)
# # # # # # # print("number : ", number, sep="")
# # # # # # # print("symbol : ",chr(number))









# # # # # # # a = 2 / 3
# # # # # # # b = 5 / 7
# # # # # # # c = 11 /31

# # # # # # # print("a = %5.10f"%(a))




# # # # # # import random

# # # # # # # number = random.random()
# # # # # # # print("number = %5.5f"%(number))


# # # # # # # number1 = random.random() * 100
# # # # # # # print("number1 = %5.5f"%(number1))


# # # # # # # number2 = random.randint(10,100)
# # # # # # # print("number2 = %6.6f"%(number2))


# # # # # # # number3 = random.randrange(10)
# # # # # # # print("number3 =",number3)



# # # # # # number4 = random.randrange(1,49,2)
# # # # # # print("number4 : ", number4)




# # # # # a, b = 0, 1

# # # # # while b < 100:
# # # # #     print(b)
# # # # #     a, b = b, a + b



# # # #  #### სამ ცვლადს შორის უდიდესის განსაზღვირ ოპერაცია:
 
 
# # # # # a = int(input("Input A : "))
# # # # # b = int(input("Input B : "))
# # # # # c = int(input("Input C : "))
# # # # # maxi = a
# # # # # if maxi < b:
# # # # #     maxi = b
# # # # # if maxi < c:
# # # # #     maxi = c
# # # # # print("Maxi : ", maxi)



# # # # # a = int(input("Input a: "))
# # # # # if a % 2 == 0: 
# # # # #     print("რიცხვი ლუწია")
# # # # # else:
# # # # #     print("რიცხვი კენტია")



# # # # # age = int(input("შეიტანე ასაკი : "))

# # # # # if age < 3:
# # # # #     print('ბაღამდელი ბავშვია')
# # # # # elif(age >= 3) and (age < 6):
# # # # #     print("ბაღის ასაკია")
# # # # # elif(age >= 6) and (age <= 17):
# # # # #     print("სკოლის ასაკია")
# # # # # elif(age >= 18) and (age <= 21):
# # # # #     print("სტუდენტია")
# # # # # elif(age >= 22) and (age <= 23):
# # # # #     print("მაგისტრი")
# # # # # elif(age >= 24) and (age <= 26):
# # # # #     print("დოქტორანტი")
# # # # # elif(age >= 27) and (age <= 65):
# # # # #     print("სამსახურის პერიოდი")
# # # # # else:
# # # # #     print("პენსიონერი")

# # # # x = int(input("შეიტანე x ცვლადის მნიშვნელობა : "))
# # # # y = int(input("შეიტანე y ცვლადის მნიშვნელობა : "))


# # # # if x == y:
# # # #     print("ცვლადები ერთმანეთის ტოლია")
# # # # else:
# # # #     if x > y:
# # # #         print("x > y")
# # # #     else:
# # # #         print("x < y")




# # # x = int(input("შემოიტანეთ x ცვლადის მნიშვნელობა : "))

# # # s = x // 100 + x // 10 % 10 + x % 10
# # # print("შედეგი : ", s)

# # # if x % s == 0:
# # #     print("რიცხვი უნაშთოდ იყოფა თავის ციფრთა ჯამზე")
# # # else:
# # #     print("რიცხვი უნაშთოდ არ იყოფა თავის ციფრთა ჯამზე")
    


# # a = float(input("შემოიტანეთ a კოეფიციენტის მნიშვნელობა : "))
# # b = float(input("შემოიტანეთ b კოეფიციენტის მნიშვნელობა : "))

# # if a != 0:
# #     x = -b/a
# #     print("შედეგი : ", x)
# # elif b == 0:
# #     print("ამონახსნთა უსასრულო სიმრავლე")
# # else:
# #     print("ამონახსნი არ გვაქვს")




# # ეკვივალენტის ალგორითმის პროგრამა რალიზაცია:

# # a = int(input("შეიტანეთ a ცვლადის მნიშვნელობა : "))
# # b = int(input("შეოტანეთ b ცვლადის მნიშვნელობა : "))

# # # while a != b:
# # #     if a > b:
# # #         a -= b
# # #     else:
# # #         b -= a
# # # print("შედეგი", a)


# # a, b = 0, 1

# # while b < 199:
# #     print(a)
# #     a, b = b, a  + b

# # s = input("ჩაწერე სტრიქონი : ")
# # n = 0
# # for i in s:
# #     if i.isdigit():
# #       n += 1
# # print(n)



# n = 0
# for x in range(100, 1001):
#     s = x // 100 + x // 10 % 10 + x % 10
#     if x % s == 0:
#         if n % 10 == 0:
#             print()
#         n += 1
#         print(x, end = " ")



# # while True:
# #     s = input("Input String : ")
# #     if s == "stop":
# #         break
# #     print("Result",(len(s)))

    
    
# import random
# a = random.randint(10, 100)

# while True :
#         a = random.randint(10, 100) 
#     if a == 50:
#         break    
#     print(a)
