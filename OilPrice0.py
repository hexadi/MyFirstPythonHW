def oil_page():
    print("#"*120)
    for i in range(3):
        print("#"+ (" " * 118) + "#")
    print("#" + (" " * 46) + "1. " + price_oil[0]["name"] + " : %.2f BAHT" %(price_oil[0]["price"]) + (" " * 45) + "#")
    for i in range(3):
        print("#"+ (" " * 118) + "#")
    print("#" + (" " * 46) + "2. " + price_oil[1]["name"] + " : %.2f BAHT" %(price_oil[1]["price"]) + (" " * 45) + "#")
    for i in range(3):
        print("#"+ (" " * 118) + "#")
    print("#" + (" " * 46) + "3. " + price_oil[2]["name"] + " : %.2f BAHT" %(price_oil[2]["price"]) + (" " * 46) + "#")
    for i in range(3):
        print("#"+ (" " * 118) + "#")
    print("#" + (" " * 46) + "4. " + price_oil[3]["name"] + " : %.2f BAHT" %(price_oil[3]["price"]) + (" " * 45) + "#")
    for i in range(3):
        print("#"+ (" " * 118) + "#")
    print("#" + (" " * 46) + "5. " + price_oil[4]["name"] + " : %.2f BAHT" %(price_oil[4]["price"]) + (" " * 46) + "#")
    for i in range(3):
        print("#"+ (" " * 118) + "#")
    print("#" + (" " * 48) + "6. " + price_oil[5]["name"] + " : %.2f BAHT" %(price_oil[5]["price"]) + (" " * 48) + "#")
    for i in range(3):
        print("#"+ (" " * 118) + "#")
    print("#"*120)

def cal_page():
    print("#"*120)
    for i in range(12):
        print("#"+ (" " * 118) + "#")
    print("#" + (" " * 46) + "1. Calculate money to litre" + (" " * 45) + "#")
    print("#"+ (" " * 118) + "#")
    print("#" + (" " * 46) + "2. Calculate litre to money" + (" " * 45) + "#")
    for i in range(12):
        print("#"+ (" " * 118) + "#")
    print("#"*120)

def main():
    print("#"*120)
    for i in range(13):
        print("#"+ (" " * 118) + "#")
    print("#" + (" " * 56) + "Welcome" + (" " * 55) + "#")
    for i in range(13):
        print("#"+ (" " * 118) + "#")
    print("#"*120)
    inp = input("> ")
    oil_page()
    select = input("Select Type : ")
    if (select.isnumeric()): 
        select = int(select) - 1
        if (select < 0 or select > 5):
            print("Error : Input Your Type Incorrect")
            input()
            return False
    else: 
        print("Error : Input Your Type Incorrect")
        input()
        return False
    cal_page()
    category = input("Calculation Type : ")
    if (category.isnumeric()):
        category = int(category) - 1
        if (category != 0 and category != 1):
            print("Error : Input Your Calculation Type Incorrect")
            input()
            return False  
    else: 
        print("Error : Input Your Calculation Type Incorrect")
        input()
        return False
    if (select > -1 and select < 6 and (category == 0 or category == 1)):
        cal = [["Calculate money to litre","Money","Litre","Litre"],["Calculate litre to money","Litre","Money"," BAHT"]]
        print("#"*120)
        for i in range(13):
            print("#"+ (" " * 118) + "#")
        print("#" + (" " * 47) + cal[category][0] + (" " * 47) + "#")
        for i in range(13):
            print("#"+ (" " * 118) + "#")
        print("#"*120)
        inp = input("Input " + cal[category][1] + " : ")
        if (inp.isnumeric()): 
            inp = float(inp)
        else: 
            print("Error : Input Your Money Incorrect")
            input()
            return False
        if (category == 0):
            total = inp/price_oil[select]["price"]
        elif (category == 1):
            total = inp * price_oil[select]["price"]
        print("#"*120)
        for i in range(12):
            print("#"+ (" " * 118) + "#")
        m = len(str("%.2f" %(total))) - 4
        a1,a2 = 47,47
        if (m == 1):
            a1,a2 = 46,46
        elif (m == 2):
            a1,a2 = 46,46
        elif (m == 3):
            a1,a2 = 45,45
        elif (m == 4):
            a1,a2 = 45,44
        elif (m == 5):
            a1,a2 = 44,44
        elif (m == 6):
            a1,a2 = 44,43
        elif (m == 7):
            a1,a2 = 43,43
        print("#" + (" " * a1) + "Total " + cal[category][2] + " : %.2f" %(total),cal[category][3], (" " * a2) + "#")
        for i in range(13):
            print("#"+ (" " * 118) + "#")
        print("#"*120)
        print("Total " + cal[category][2] + " : %.2f" %(total),cal[category][3])
        input("> ")
        print("#"*120)
        for i in range(13):
            print("#"+ (" " * 118) + "#")
        print("#" + (" " * 33) + "Press Enter to continue or Press exit to exit program" + (" " * 32) + "#")
        for i in range(13):
            print("#"+ (" " * 118) + "#")
        print("#"*120)
    return input("> ")

while True:
    if main() == "exit":
        break