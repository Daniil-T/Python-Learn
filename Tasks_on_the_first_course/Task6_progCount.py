progCount = input()
result = ""
secondDigitIsOne = True if len(progCount) > 1 and progCount[-2] == '1' else False

if progCount[-1] == '1' and secondDigitIsOne == False:
    result = "программист"
elif (progCount[-1] >= '2' and progCount[-1] <= '4') and secondDigitIsOne == False:
    result = 'программиста'
else:
    result = 'программистов'

print(progCount, result)