groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "sprite"]

while True:
    user_ans = input("what do you want to remove? ")
    if user_ans == "stop":
        break
    groceries.remove(user_ans)
    print(groceries)