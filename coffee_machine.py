from page_func import page, int_input
machine = {"water": 400,
           "milk": 540,
           "coffee beans": 120,
           "disposable cups": 9,
           "money": 550}


def buyPage():
    inp_buy = False
    type_coffee = [{'c': "espresso", 'sell': True}, {
        'c': "latte", 'sell': True}, {'c': "cappuccino", 'sell': True}]
    coffees = [{"water": 250, "coffee beans": 16, "money": 4},
               {"water": 350, "milk": 75, "coffee beans": 20, "money": 7},
               {"water": 200, "coffee beans": 12, "milk": 100, "money": 6}]
    for i, coffee in enumerate(coffees):
        for use, many in coffee.items():
            if (machine[use] - many < 0):
                type_coffee[i]["sell"] = False
    while inp_buy is False:
        page(["What do you want to buy"] +
             ["%d - %s" % (i+1, coffee["c"]) if (coffee["sell"] is True)
              else "%d - %s [Not Available]" % (i+1, coffee["c"])
              for i, coffee in enumerate(type_coffee)] +
             ["4 - Back to menu"])
        inp_buy = int_input(start=1, stop=4)
    if (inp_buy == 4):
        return False
    cof_select = coffees[inp_buy - 1]
    if (type_coffee[inp_buy - 1]["sell"] is False):
        page(["Sorry, It's not avaliable now."])
        input()
    else:
        for i in range(len(cof_select.keys())):
            name = list(cof_select.keys())[i]
            if (name == "money"):
                machine[name] += cof_select[name]
            else:
                machine[name] -= cof_select[name]
        machine["disposable cups"] -= 1


def fillPage():
    page(["Write how many ml of water do you want to add :"])
    machine["water"] += int_input()
    page(["Write how many ml of milk do you want to add :"])
    machine["milk"] += int_input()
    page(["Write how many grams of coffee beans do you want to add :"])
    machine["coffee beans"] += int_input()
    page(["Write how many disposable cups of coffee do you want to add :"])
    machine["disposable cups"] += int_input()


def takePage():
    page(["I take you $" + str(machine["money"])])
    machine["money"] = 0
    int_input()


while True:
    page(["The coffee machine has", 1,
          str(machine["water"]) + " of " + "water", 1,
          str(machine["milk"]) + " of " + "milk", 1,
          str(machine["coffee beans"]) + " of " + "coffee beans", 1,
          str(machine["disposable cups"]) +
          " of " + "disposable cups", 1,
          str(machine["money"]) + " of " + "money"])
    int_input()
    action = ""
    while (action != "buy" and action != "fill" and action != "take"):
        page(["Write action (buy, fill, take)"])
        action = input().strip()
    if (action == "buy"):
        buyPage()
    elif (action == "fill"):
        fillPage()
    elif (action == "take"):
        takePage()
