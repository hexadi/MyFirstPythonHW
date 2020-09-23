import subprocess as sp
from suds.client import Client
import xml.etree.ElementTree as ET
network = True

sp.call("", shell=True)

price_oil = [{"name": "Gasoline 95", "price": 29.16},
             {"name": "Gasoline 91", "price": 25.30},
             {"name": "Gasohol 91", "price": 21.68},
             {"name": "Gasohol E20", "price": 20.2},
             {"name": "Gasohol 95", "price": 21.2},
             {"name": "Diesel", "price": 21.1}]

# Retrieve data from pttor website and update oil price
try:
    client = Client('https://www.pttor.com/OilPrice.asmx?WSDL')
    OilPrice = client.service.CurrentOilPrice(Language='thai')
    tree = ET.fromstring(OilPrice)
    for child in tree:
        oil = ""
        for i in child:
            oil += i.text + "//"
        oil = oil.split("//", 2)
        oil[2] = oil[2].rstrip("//")
        if (len(oil) == 3):
            li = [name for name in price_oil if name["name"] == oil[1]]
            if (len(li) == 1 and oil[2] != ''):
                li[0]["price"] = float(oil[2])
except Exception:
    network = False


# receive input and check that is int function
def int_input(start=None, stop=None, type_=None):
    inp = input().strip()
    print("")
    if inp.isnumeric():
        if (type_ == "float"):
            inp = float(inp)
        else:
            inp = int(inp)
        if (start is not None):
            if inp < start:
                return False
        if (stop is not None):
            if inp > stop:
                return False
        return inp
    else:
        return False


# make an output as block page in terminal
def page(Lists, symbol="#"):
    space = 78
    sp.call("clear", shell=True)
    print(symbol*(space + 2))
    for e in Lists:
        if isinstance(e, int):
            for i in range(e):
                print(symbol + " " * space + symbol)
        elif isinstance(e, str):
            s = len(e)/2
            if (int(s) != s):
                s1, s2 = s-1, s
            else:
                s1, s2 = s, s
            print(symbol + (" " * int(space/2 - s1)) + e +
                  (" " * int(space/2 - s2)) + symbol)
        elif isinstance(e, tuple):
            print(symbol + (" " * e[1]) + e[0] +
                  (" " * int(space - len(e[0]) - e[1])) +
                  symbol)
    print(symbol + " " * int(space/2-4) + "Enter : \0337", end="")
    print(" " * int(space/2-4) + symbol + "\n" + symbol + " " * (space) +
          symbol + "\n" + symbol*(space + 2) + "\0338", end="")


while True:
    # Welcome Page
    if (network is False):
        page([1, ("* Can't Connect To Oil Server", 2),
              10, "Welcome", 10])
    else:
        page([11, "Welcome", 10])
    int_input()

    # Oil Select Page
    select = False
    while select is False:
        page([5, "Oil Price", 1,
              "1. %s : %.2f BAHT" % (
                  price_oil[0]["name"], price_oil[0]["price"]), 1,
              "2. %s : %.2f BAHT" % (
                  price_oil[1]["name"], price_oil[1]["price"]), 1,
              "3. %s : %.2f BAHT" % (
                  price_oil[2]["name"], price_oil[2]["price"]), 1,
              "4. %s : %.2f BAHT" % (
                  price_oil[3]["name"], price_oil[3]["price"]), 1,
              "5. %s : %.2f BAHT" % (
                  price_oil[4]["name"], price_oil[4]["price"]), 1,
              "6. %s : %.2f BAHT" %
              (price_oil[5]["name"], price_oil[5]["price"]), 4])
        select = int_input(start=1, stop=6)

    # Select Calculate Type Page
    cal_type = False
    while cal_type is False:
        page([9, "Calculation Type", 1,
              "1.Calculate Money to Litre", 1,
              "2.Calculate Litre to Money", 8])
        cal_type = int_input(start=1, stop=2)

    # Total Page
    amount = False
    if (cal_type == 1):
        while amount is False:
            page([11, "Calculate Money to Litre", 10])
            amount = int_input(type_="float")
        total = amount / price_oil[select - 1]["price"]
        page([11, "Total Litre : %.2f Litre" % (total), 10])
        int_input()
    elif (cal_type == 2):
        while amount is False:
            page([11, "Calculate Litre to Money", 10])
            amount = int_input(type_="float")
        total = amount * price_oil[select - 1]["price"]
        page([11, "Total Money : %.2f Baht" % (total), 10])
        int_input()

    # Enter to continue or exit page
    page([10, "Press Enter to Continue",
          "Or Press exit to Exit Program", 10])
    if input() == "exit":
        sp.call("clear", shell=True)
        break
