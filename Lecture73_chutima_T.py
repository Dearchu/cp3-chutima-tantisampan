SystemMenu = {'กระเพราหมูสับ': 30, 'ต้มจืดสาหร่าย': 50, 'ข้าวไข่เจียว': 40}
menuList = []


def showBill():
    print("----------เมนู อาหาร----------")
    TotalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1], ' บาท')
        TotalPrice = TotalPrice + int(menuList[number][1])
    print('ราคาทั้งหมด :', TotalPrice, ' บาท')


while True:
    menuName = input("โปรดเลือกเมนู :")
    if menuName.lower() == "exit":
        break
    else:
        menuList.append([menuName, SystemMenu[menuName]])

showBill()