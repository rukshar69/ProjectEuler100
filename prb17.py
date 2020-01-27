
singleDigits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight','nine']
teens = ['ten','eleven','twelve','thirteen', 'fourteen', 'fifteen', 'sixteen','seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

singles = [len(a) for a in singleDigits]
singlesLen = sum(singles)
#print(singlesLen)
teens_ = [len(a) for a in teens]
teensLen = sum(teens_)
#print(teensLen)
doubleDig = 0
for i in tens:
    a = len(i)
    a = a*10
    doubleDig += (a+singlesLen)

belowHundred = doubleDig + teensLen + singlesLen
hundred_and = 10
hundred = 7

threeDig = 0
for i in singleDigits:
    hundredth = len(i)
    temp = (hundredth+ hundred_and)*99
    threeDig += hundredth + hundred + temp + belowHundred

one_thousand = 11
total = belowHundred + threeDig + one_thousand
print(total)

