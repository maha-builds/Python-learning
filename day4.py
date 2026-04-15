def BMI_Calculator():
    weight=float(input("Enter the weight: "))
    height=float(input("Enter the height: "))
    BMI=weight/(height*height)
    total=round(BMI,2)
    if total<18.5:
        print("Underweighted")
    elif 18.5<=total<=24.9:
        print("Normal weight")
    elif 25<=total<=29.9:
        print("Overweight")
    else:
        print("Obese")
BMI_Calculator()
