def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

totalPrice = float(input("Input total proce : "))
print(vatCalculate(totalPrice))
