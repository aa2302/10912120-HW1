from mymath import myArithmetic,myCalcArea,myStatistics
a = 0
for i in range(5):
    b = float(input("請輸入五個有理數"))
    sum = myArithmetic.myAdd(a,b)
    a = sum
print("五次平均為",myArithmetic.myDiv(a,5))
