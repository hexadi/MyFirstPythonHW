from page_func import *
from suds.client import Client
import xml.etree.ElementTree as ET

# initialize Oil Type
price_oil = {"Gasoline 95": 29.16,
             "Gasoline 91": 25.30,
             "Gasohol 91": 21.68,
             "Gasohol E20": 20.2,
             "Gasohol 95": 21.2,
             "Diesel": 21.1}


# Select Oil Type Function
def oilSelectPage():
    value = False
    while value is False:
        page(["Oil Price", 1] +
             ["{}. {}: {:.2f} BAHT".format(i+1, name, price)
              for i, (name, price) in enumerate(price_oil.items())])
        value = int_input(start=1, stop=6)
    return value


# Select Calculation Type Function
def calSelectPage():
    value = False
    while value is False:
        page(["Calculation Type", 1,
              "1.Calculate Money to Litre", 1,
              "2.Calculate Litre to Money"])
        value = int_input(start=1, stop=2)
    return value


# Total Page Function
def totalPage(select, cal_type):
    amount = False
    select_price = price_oil[list(price_oil.keys())[select - 1]]
    if (cal_type == 1):
        while amount is False:
            page(["Calculate Money to Litre"])
            amount = int_input(type_="float")
        total = amount / select_price
        page(["Total Litre : %.2f Litre" % (total)])
    elif (cal_type == 2):
        while amount is False:
            page(["Calculate Litre to Money"])
            amount = int_input(type_="float")
        total = amount * select_price
        page(["Total Money : %.2f Baht" % (total)])
    int_input()


while True:
    # Welcome Page
    page(["Welcome"])
    int_input()

    # Oil Select Page
    oil = oilSelectPage()

    # Select Calculate Type Page
    cal_type = calSelectPage()

    # Total Page
    totalPage(oil, cal_type)

    # Enter to continue or exit page
    page(["Press Enter to Continue",
          "Or Press exit to Exit Program"])
    if input() == "exit":
        clearScreen()
        break
