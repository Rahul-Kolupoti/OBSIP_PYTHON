def bmicalculate(h,w):
    bmi=w/((h/100)**2)
    return bmi

height=int(input("Enter the height(in cm): "))
weight=int(input("Enter the weight(in kg): "))

bmi=bmicalculate(height,weight)

if bmi < 18.5:
    category="Underweight"
elif 18.5 <= bmi < 25:
    category="Normal Weight"
elif 25 <= bmi < 30:
    category="Overweight"
else:
    category="Obese"
    
print("Your BMI is %.2f . You are %s" % (bmi, category))
