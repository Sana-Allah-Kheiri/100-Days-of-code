#By Sasan at https://github.com/Sana-Allah-Kheiri/100-Days-of-code/
# User enters a bill price, tip percentage & the app prints the name alphabet by alphabet
# Tutorial Goal is to understand that string = array = list = pointers(In C++ actually)
import sys
import time
retry = 1;

def exitF(): # To exit the app
    print("Exiting app after 5 seconds...");
    time.sleep(1)
    print("*");
    time.sleep(1)
    print("*");
    time.sleep(1)
    print("*");
    time.sleep(1)
    print("*");
    time.sleep(1)
    sys.exit("Goodbye!")


def retryF(): # To improve user experience
    retry = input(" Type 0 to exit | Type 1 to restart");
    retry = int(retry);
    if (retry == 0):
        exitF();
    else:
        retry = 1;
        
while(retry==1):
    metric_system = input(" Press 1 for SI Metric(KG & Meters) \n Press 2 for US(Pound & inch) ");
    metric_system = int(metric_system);
    
    if(metric_system == 1):
        weight = input(" Enter your weight in KG : ");
        weight = float (weight);
        height = input(" How tall you are in meters? " );
        height = float(height);
        BMI = weight / (height*height)
    
    if(metric_system == 2):
        weight = input(" Enter your weight in Pound(Lbs) : ");
        weight = float (weight);
        height = input(" How tall you are in Inch(in)? " );
        height = float(height);
        BMI = (weight / (height*height))*(703.00)
    #BMI = round(BMI, 3);    
    print (f"Your BMI with 3 decimal precision is {round(BMI, 3)}");    
    match BMI:
        case BMI if (BMI<16.0):
            print(" Severe Thinness ")
        case BMI if (BMI>=16.0 and BMI<17.0):
            print(" Moderate Thinness ")
        case BMI if (BMI>=17.0 and BMI<18.5):
            print(" Mild Thinness ")
        case BMI if (BMI>=18.5 and BMI<25.0):
            print(" Normal ")
        case BMI if (BMI>=25.0 and BMI<30.0):
            print(" Overweight ")
        case BMI if (BMI>=30.0 and BMI<35.0):
            print(" Obese Class 1 ")
        case BMI if (BMI>=35.0 and BMI<40.0):
            print(" Obese Class 2 ");
        case _:
            print(" Obese Class 3 ")
    retryF();
