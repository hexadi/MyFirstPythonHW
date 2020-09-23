# ฟังก์ชั่น Print หน้าแสดงค่าน้ำมัน
def oil_page():
    print("#"*120)
    for i in range(3):
        print("#" + (" " * 118) + "#")
    print("#" + (" " * 46) + "1. " + price_oil[0]["name"] +
          " : %.2f BAHT" % (price_oil[0]["price"]) + (" " * 45) + "#")
    for i in range(3):
        print("#" + (" " * 118) + "#")
    print("#" + (" " * 46) + "2. " + price_oil[1]["name"] +
          " : %.2f BAHT" % (price_oil[1]["price"]) + (" " * 45) + "#")
    for i in range(3):
        print("#" + (" " * 118) + "#")
    print("#" + (" " * 46) + "3. " + price_oil[2]["name"] +
          " : %.2f BAHT" % (price_oil[2]["price"]) + (" " * 46) + "#")
    for i in range(3):
        print("#" + (" " * 118) + "#")
    print("#" + (" " * 46) + "4. " + price_oil[3]["name"] +
          " : %.2f BAHT" % (price_oil[3]["price"]) + (" " * 45) + "#")
    for i in range(3):
        print("#" + (" " * 118) + "#")
    print("#" + (" " * 46) + "5. " + price_oil[4]["name"] +
          " : %.2f BAHT" % (price_oil[4]["price"]) + (" " * 46) + "#")
    for i in range(3):
        print("#" + (" " * 118) + "#")
    print("#" + (" " * 48) + "6. " + price_oil[5]["name"] +
          " : %.2f BAHT" % (price_oil[5]["price"]) + (" " * 48) + "#")
    for i in range(3):
        print("#" + (" " * 118) + "#")
    print("#"*120)


# ฟังก์ชั่น Print หน้าคำนวณเงินเป็นลิตร หรือจำนวนลิตรเป็นเงิน
def cal_page():
    print("#"*120)
    for i in range(12):
        print("#" + (" " * 118) + "#")
    print("#" + (" " * 46) + "1. Calculate money to litre" + (" " * 45) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 46) + "2. Calculate litre to money" + (" " * 45) + "#")
    for i in range(12):
        print("#" + (" " * 118) + "#")
    print("#"*120)


def main():
    # แสดงหน้า Welcome
    print("#"*120)
    for i in range(13):
        print("#" + (" " * 118) + "#")
    print("#" + (" " * 56) + "Welcome" + (" " * 55) + "#")
    for i in range(13):
        print("#" + (" " * 118) + "#")
    print("#"*120)
    inp = input("> ")
    # แสดงหน้า โชว์ค่าน้ำมัน
    oil_page()
    select = input("Select Type : ")
    # เช็คว่าค่าที่รับมาเป็นตัวเลขหรือไม่ แล้วอยู่ใน 0 - 5 หรือไม่
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
    # แสดงหน้า ถามการคำนวณ
    cal_page()
    category = input("Calculation Type : ")
    # เช็คว่าค่าที่รับมาเป็นตัวเลขหรือไม่ แล้วเป็น 0 หรือ 1 หรือไม้
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
    cal = [["Calculate money to litre", "Money", "Litre", "Litre"],
           ["Calculate litre to money", "Litre", "Money", " BAHT"]]
    # หน้ารับค่าจำนวนเงิน/จำนวนลิตร
    print("#"*120)
    for i in range(13):
        print("#" + (" " * 118) + "#")
    print("#" + (" " * 47) + cal[category][0] + (" " * 47) + "#")
    for i in range(13):
        print("#" + (" " * 118) + "#")
    print("#"*120)
    inp = input("Input " + cal[category][1] + " : ")
    if (inp.isnumeric()):
        inp = float(inp)
    else:
        print("Error : Input Your Money Incorrect")
        input()
        return False
    # ถ้าคำนวณเงินเป็นลิตรจะใช้วิธีคำนวณแรก
    # ถ้าคำนวณลิตรเป็นเงินจะใช้วิธีคำนวณที่สอง
    if (category == 0):
        total = inp/price_oil[select]["price"]
    elif (category == 1):
        total = inp * price_oil[select]["price"]
    # แสดงหน้าจำนวนลิตร/จำนวนเงินที่ได้
    print("#"*120)
    for i in range(12):
        print("#" + (" " * 118) + "#")
    # คำนวณจำนวนช่องเว้นว่างตามขนาดของตัวเลข
    m = len(str("%.2f" % (total))) - 4
    a1, a2 = 47, 47
    if (m == 1):
        a1, a2 = 46, 46
    elif (m == 2):
        a1, a2 = 46, 46
    elif (m == 3):
        a1, a2 = 45, 45
    elif (m == 4):
        a1, a2 = 45, 44
    elif (m == 5):
        a1, a2 = 44, 44
    elif (m == 6):
        a1, a2 = 44, 43
    elif (m == 7):
        a1, a2 = 43, 43
    print("#" + (" " * a1) + "Total " + cal[category][2] +
          " : %.2f" % (total), cal[category][3], (" " * a2) + "#")
    for i in range(13):
        print("#" + (" " * 118) + "#")
    print("#"*120)
    print("Total " + cal[category][2] +
          " : %.2f" % (total), cal[category][3])
    input("> ")
    # หน้าที่ถามว่าต้องการจะออกจากโปรแกรมไหม ถ้าไม่ต้องการกด Enter
    # แต่ถ้าต้องการ ให้พิมพ์ exit แล้วกด Enter
    print("#"*120)
    for i in range(13):
        print("#" + (" " * 118) + "#")
    print("#" + (" " * 33) +
          "Press Enter to continue or Press exit to exit program" +
          (" " * 32) + "#")
    for i in range(13):
        print("#" + (" " * 118) + "#")
    print("#"*120)
    return input("> ")

# ทำ Loop เมื่อ ฟังก์ชั่น main ให้ค่าออกมาเป็น exit แล้วปิดโปรแกรม
# แต่ถ้าไม่ใช่ให้ทำต่อไป
while True:
    if main() == "exit":
        break
