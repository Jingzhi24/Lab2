def calculate_bmi(height, weight):
    print("Height="+str(height))
    print("Weight="+str(weight))
    bmi = weight/(height*height)
    return bmi

def main():
    bmi_value= calculate_bmi(1.75,62)
    print("The calculated bmi value ="+str(bmi_value))
    check_bmi(bmi_value)

def check_bmi(bmi_value):
    if(bmi_value<18.5):
     print("you are underweight")
     return -1
    if(bmi_value>=18.5 and bmi_value<=25.0):
     print("you have a normal weight") 
     return 0
    if(bmi_value>25.0):
     print("you are overweight")
     return 1

if __name__ == "__main__":
   main()