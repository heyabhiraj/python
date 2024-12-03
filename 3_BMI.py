#WAP to take weight and height from the user and determine BMI Score and find whether a person is Underweight, Overweight, Normal or Obesity

weight=float(input("Enter your weight in Kilograms: "))
height=float(input("Enter your height in Meters: "))

#calculate BMI Score
bmi=weight/(height**2)

#determine BMI Category based on BMI value
if bmi<18.5:
    print(f"Your BMI Score is {bmi}\nSo based on the BMI value you are Under Weight")
elif 18.5<=bmi<25:
    print(f"Your BMI Score is {bmi}\nSo based on the BMI value you are Normal Weight")
elif 25<=bmi<30:
    print(f"Your BMI Score is {bmi}\nSo based on the BMI value you are Over Weight")
else:
    print(f"Your BMI Score is {bmi}\nSo based on the BMI value you have Obesity")
