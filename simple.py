price=float(input("enter principle amount"))
rate=float(input("enter rate of interest"))
time=float(input("enter number of months"))
omr=price * rate/100
print("the one month rate of interest is",omr)
totint=omr*time
print("the total interest is",totint)
tpa=totint+price
print("the total payable amount is",tpa)