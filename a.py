fruit = {}

while True:
    if len(fruit) == 0:
        helper = {}
        name = input("Enter fruit name : ")
        kg = int(input("Enter fruit weight : "))
        price = int(input("Enter fruit price : "))
        helper ["kg"] = kg
        helper ['price'] = price
        fruit[name] = helper
    else:
        print("this is your cart", fruit)
        ques = input("Add More? Yes/No : ")
        if ques == "Yes" or ques == "yes":
            name = input("Enter fruit name : ") 
            kg = int(input("Enter fruit weight : "))
            price = int(input("Enter fruit price : "))
            helper ["kg"] = kg 
            helper ["price"] = price 
            fruit[name] = helper
        else:
            break

# გაანგარიშება
result = 0
for key, value in fruit.items():
    kg = int(value["kg"])
    price = int(value["price"])
    result += kg*price
    print(key, "Your amount ", kg*price, "GEL")
print("you have to pay ", result, "GEL")
# print("this is your cart", fruit)