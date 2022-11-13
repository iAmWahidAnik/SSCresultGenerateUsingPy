#inputWorld

#Bangla 
bangla1 = int(input("Enter your bangla 1st paper mark here : "))
bangla2 = int(input("Enter your bangla 2nd paper mark here : "))
overBang = (bangla1+bangla2)/2

#English 
english1 = int(input("Enter your english 1st paper mark here : "))
english2 = int(input("Enter your english 2nd paper mark here : "))
overEng = (english1+english2)/2

#Mathematics 
math = int(input("Enter your Mathematics paper mark here : "))

#Islam 
islam = int(input("Enter your Islam paper mark here : "))

#SocialScience 
soscience = int(input("Enter your Social Science paper mark here : "))

#physics
phySub = int(input("Enter your Physics paper mark here : "))
phyPr = int(input("Enter your Physics Practical paper mark here : "))
phyAvg = (phySub+phyPr)

#Chemistry
cheSub = int(input("Enter your Chemistry paper mark here : "))
chePr = int(input("Enter your Chemistry Practical paper mark here : "))
cheAvg = (cheSub+chePr)

#Biology
bioSub = int(input("Enter your Biology paper mark here : "))
bioPr = int(input("Enter your Biology Practical paper mark here : "))
bioAvg = (bioSub+bioPr)

#HigherMath
highmathSub = int(input("Enter your Higher Math paper mark here : "))
highMathPr = int(input("Enter your Higher Math Practical paper mark here : "))
highMathAvg = (highmathSub+highMathPr)



#outputWorld

#Bangla 1st Paper
if bangla1 <=32:
    print("Your Bangla 1st paper Grade is F & GPA 0.00")
elif bangla1 <=39:
    print("Your Bangla 1st paper Grade is D & GPA 1.00")
elif bangla1 <=49:
    print("Your Bangla 1st paper Grade is C & GPA 2.00")
elif bangla1 <=59:
    print("Your Bangla 1st paper Grade is B & GPA 3.00")
elif bangla1 <=69:
    print("Your Bangla 1st paper Grade is A- & GPA 3.50")
elif bangla1 <=79:
    print("Your Bangla 1st paper Grade is A & GPA 4.00")
else:
   print("Your Bangla 1st paper Grade is A+ & GPA 5.00") 

#Bangla 2nd Paper
if bangla2 <=32:
    print("Your Bangla 2nd paper Grade is F & GPA 0.00")
elif bangla2 <=39:
    print("Your Bangla 2nd paper Grade is D & GPA 1.00")
elif bangla2 <=49:
    print("Your Bangla 2nd paper Grade is C & GPA 2.00")
elif bangla2 <=59:
    print("Your Bangla 2nd paper Grade is B & GPA 3.00")
elif bangla2 <=69:
    print("Your Bangla 2nd paper Grade is A- & GPA 3.50")
elif bangla2 <=79:
    print("Your Bangla 2nd paper Grade is A & GPA 4.00")
else:
   print("Your Bangla 2nd paper Grade is A+ & GPA 5.00") 

#Overall Bangla
if overBang <=32 or bangla1 <=32 or bangla2 <=32:
    print("Your Overall Bangla Average paper Grade is F & GPA 0.00")
elif overBang <=39:
    print("Your Overall Bangla Average paper Grade is D & GPA 1.00")
elif overBang <=49:
    print("Your Overall Bangla Average paper Grade is C & GPA 2.00")
elif overBang <=59:
    print("Your Overall Bangla Average paper Grade is B & GPA 3.00")
elif overBang <=69:
    print("Your Overall Bangla Average paper Grade is A- & GPA 3.50")
elif overBang <=79:
    print("Your Overall Bangla Average paper Grade is A & GPA 4.00")
else:
   print("Your Overall Bangla Average paper Grade is A+ & GPA 5.00")

#English 1st Paper
if english1 <=32:
    print("Your English 1st paper Grade is F & GPA 0.00")
elif english1 <=39:
    print("Your English 1st paper Grade is D & GPA 1.00")
elif english1 <=49:
    print("Your English 1st paper Grade is C & GPA 2.00")
elif english1 <=59:
    print("Your English 1st paper Grade is B & GPA 3.00")
elif english1 <=69:
    print("Your English 1st paper Grade is A- & GPA 3.50")
elif english1 <=79:
    print("Your English 1st paper Grade is A & GPA 4.00")
else:
   print("Your English 1st paper Grade is A+ & GPA 5.00")

#English 2nd Paper
if english2 <=32:
    print("Your English 2nd paper Grade is F & GPA 0.00")
elif english2 <=39:
    print("Your English 2nd paper Grade is D & GPA 1.00")
elif english2 <=49:
    print("Your English 2nd paper Grade is C & GPA 2.00")
elif english2 <=59:
    print("Your English 2nd paper Grade is B & GPA 3.00")
elif english2 <=69:
    print("Your English 2nd paper Grade is A- & GPA 3.50")
elif english2 <=79:
    print("Your English 2nd paper Grade is A & GPA 4.00")
else:
   print("Your English 2nd paper Grade is A+ & GPA 5.00") 

#Overall English
if overEng <= 32 or english1 <=32 or english2 <=32:
    print("Your Overall English Average paper Grade is F & GPA 0.00")
elif overEng <= 39:
    print("Your Overall English Average paper Grade is D & GPA 1.00")
elif overEng <= 49:
    print("Your Overall English Average paper Grade is C & GPA 2.00")
elif overEng <= 59:
    print("Your Overall English Average paper Grade is B & GPA 3.00")
elif overEng <= 69:
    print("Your Overall English Average paper Grade is A- & GPA 3.50")
elif overEng <= 79:
    print("Your Overall English Average paper Grade is A & GPA 4.00")
else:
    print("Your Overall English Average paper Grade is A+ & GPA 5.00")

#Mathmetics
if math <=32:
    print("Your Mathematics paper Grade is F & GPA 0.00")
elif math <=39:
    print("Your Mathematics paper Grade is D & GPA 1.00")
elif math <=49:
    print("Your Mathematics paper Grade is C & GPA 2.00")
elif math <=59:
    print("Your Mathematics paper Grade is B & GPA 3.00")
elif math <=69:
    print("Your Mathematics paper Grade is A- & GPA 3.50")
elif math <=79:
    print("Your Mathematics paper Grade is A & GPA 4.00")
else:
   print("Your Mathematics paper Grade is A+ & GPA 5.00") 

#Islam
if islam <=32:
    print("Your Islam paper Grade is F & GPA 0.00")
elif islam <=39:
    print("Your Islam paper Grade is D & GPA 1.00")
elif islam <=49:
    print("Your Islam paper Grade is C & GPA 2.00")
elif islam <=59:
    print("Your Islam paper Grade is B & GPA 3.00")
elif islam <=69:
    print("Your Islam paper Grade is A- & GPA 3.50")
elif islam <=79:
    print("Your Islam paper Grade is A & GPA 4.00")
else:
   print("Your Islam paper Grade is A+ & GPA 5.00") 

#Social Science
if soscience <=32:
    print("Your Social Science paper Grade is F & GPA 0.00")
elif soscience <=39:
    print("Your Social Science paper Grade is D & GPA 1.00")
elif soscience <=49:
    print("Your Social Science paper Grade is C & GPA 2.00")
elif soscience <=59:
    print("Your Social Science paper Grade is B & GPA 3.00")
elif soscience <=69:
    print("Your Social Science paper Grade is A- & GPA 3.50")
elif soscience <=79:
    print("Your Social Science paper Grade is A & GPA 4.00")
else:
   print("Your Social Science paper Grade is A+ & GPA 5.00") 

#Physics
if phyAvg <=32 or phySub <=24 or phyPr <=8:
    print("Your Physics paper Grade is F & GPA 0.00")
elif phyAvg <=39:
    print("Your Physics paper Grade is D & GPA 1.00")
elif phyAvg <=49:
    print("Your Physics paper Grade is C & GPA 2.00")
elif phyAvg <=59:
    print("Your Physics paper Grade is B & GPA 3.00")
elif phyAvg <=69:
    print("Your Physics paper Grade is A- & GPA 3.50")
elif phyAvg <=79:
    print("Your Physics paper Grade is A & GPA 4.00")
else:
   print("Your Physics paper Grade is A+ & GPA 5.00") 

#Chemistry
if cheAvg <=32 or cheSub <=24 or chePr <=8:
    print("Your Chemistry paper Grade is F & GPA 0.00")
elif cheAvg <=39:
    print("Your Chemistry paper Grade is D & GPA 1.00")
elif cheAvg <=49:
    print("Your Chemistry paper Grade is C & GPA 2.00")
elif cheAvg <=59:
    print("Your Chemistry paper Grade is B & GPA 3.00")
elif cheAvg <=69:
    print("Your Chemistry paper Grade is A- & GPA 3.50")
elif cheAvg <=79:
    print("Your Chemistry paper Grade is A & GPA 4.00")
else:
   print("Your Chemistry paper Grade is A+ & GPA 5.00") 

#Biology
if bioAvg <=32 or bioSub <=24 or bioPr <=8:
    print("Your Biology paper Grade is F & GPA 0.00")
elif bioAvg <=39:
    print("Your Biology paper Grade is D & GPA 1.00")
elif bioAvg <=49:
    print("Your Biology paper Grade is C & GPA 2.00")
elif bioAvg <=59:
    print("Your Biology paper Grade is B & GPA 3.00")
elif bioAvg <=69:
    print("Your Biology paper Grade is A- & GPA 3.50")
elif bioAvg <=79:
    print("Your Biology paper Grade is A & GPA 4.00")
else:
   print("Your Biology paper Grade is A+ & GPA 5.00") 

#Higher Math
if highMathAvg <=32 or highmathSub <=24 or highMathPr <=8:
    print("Your Higher Math paper Grade is F & GPA 0.00")
elif highMathAvg <=39:
    print("Your Higher Math paper Grade is D & GPA 1.00")
elif highMathAvg <=49:
    print("Your Higher Math paper Grade is C & GPA 2.00")
elif highMathAvg <=59:
    print("Your Higher Math paper Grade is B & GPA 3.00")
elif highMathAvg <=69:
    print("Your Higher Math paper Grade is A- & GPA 3.50")
elif highMathAvg <=79:
    print("Your Higher Math paper Grade is A & GPA 4.00")
else:
   print("Your Higher Math paper Grade is A+ & GPA 5.00")


#OverAll Point
overPoint = (bangla1+bangla2+english1+english2+math+islam+soscience+highMathAvg+phyAvg+cheAvg+bioAvg)/11
if overPoint <=32 or phyPr <=8 or chePr <=8 or bioPr <=8 or highMathPr <=8 or bangla1 <=32 or bangla2 <=32 or english1 <=32 or english2 <=32 or math <=32 or islam <=32 or soscience <=32 or phySub <=32 or cheSub <=32 or bioSub <=32 or highmathSub <=32:
    print("Your Overall Grade is F & GPA 0.00")
elif overPoint <=39:
    print("Your Overall Grade is D & GPA 1.00")
elif overPoint <=49:
    print("Your Overall Grade is C & GPA 2.00")
elif overPoint <=59:
    print("Your Overall Grade is B & GPA 3.00")
elif overPoint <=69:
    print("Your Overall Grade is A- & GPA 3.50")
elif overPoint <=79:
    print("Your Overall Grade is A & GPA 4.00")
else:
    print("Your Overall Grade is A+ & GPA 5.00")
