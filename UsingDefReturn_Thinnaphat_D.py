def VatCalculate():
    TotalPrice = int(input("Enter the price "))
    result = TotalPrice+(TotalPrice*0.07)
    return result

print((VatCalculate()))