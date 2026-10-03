# Full archive at Day8 folder of https://github.com/Sana-Allah-Kheiri/100-Days-of-code

import sys
import time
import random
import csv
retry = 1

def exitF(): # To exit the app
    print("Exiting app after 5 seconds...");
    print("S");
    time.sleep(1)
    print("A");
    time.sleep(1)
    print("S");
    time.sleep(1)
    print("A");
    time.sleep(1)
    print("N");
    time.sleep(1)
    sys.exit("Goodbye!")

def retryF(): # To improve user experience
    retry = input(" Type 0 to exit | Type 1 to restart ");
    retry = int(retry);
    if (retry == 0):
        exitF();
    else:
        retry = 1;

def RetrievKey(target_value, Dic):
    return (next(k for k, v in Dic.items() if v == target_value) , None)

def RankSuffix(i):
    suffix = "th"
    match i:
        case 1:
            suffix = "st"
        case 2:
            suffix = "nd"
        case 3:
            suffix = "rd"
    return(suffix);


def scoreGrader(studentScores):
    student_grades = studentScores;
    for name, gpa in studentScores.items():
        if(gpa>91):
            student_grades[name] = "OutStanding";
        elif(gpa<=91 and gpa>81):
            student_grades[name] = "Excellent";
        elif(gpa<=81 and gpa>71):
            student_grades[name] = "Acceptable";
        elif(gpa<=71):
            student_grades[name] = "Failed";
    return (student_grades);



    student_grades.update({})


def clearDic (dict):
    dict = {"" : ""}
    return dict


# Start of secret bid

while(retry == 1):
    print("""
.-----------------------------------------.
|███████╗ ██████╗ ██████╗ ██████╗ ███████╗|
|██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝|
|███████╗██║     ██║   ██║██████╔╝█████╗  |
|╚════██║██║     ██║   ██║██╔══██╗██╔══╝  |
|███████║╚██████╗╚██████╔╝██║  ██║███████╗|
|╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝|
|                                         |
| ██████╗ ██████╗  █████╗ ██████╗ ███████╗|
|██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔════╝|
|██║  ███╗██████╔╝███████║██║  ██║█████╗  |
|██║   ██║██╔══██╗██╔══██║██║  ██║██╔══╝  |
|╚██████╔╝██║  ██║██║  ██║██████╔╝███████╗|
| ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝|
'-----------------------------------------'
    """)  
    studentScores = {} #Bid Dictionary which is a two-field DataBase
    # with N records
    NumberOfStudents = int(input("How many students?"))
    for i in range(NumberOfStudents):
        suffix = RankSuffix(i+1);
        studentName = input(f"{i+1}{suffix} Student name: ")
        gpa = float(input(f"{studentName}'s GPA:"))
        studentScores.update({studentName : gpa})

    finalResult = scoreGrader(studentScores);

    print("******** FINAL GRADE **********")
    print(finalResult)
    print("**************************")

    PrivacySensitive = True;
    PrivacySensitive = input("Should I save data?(Y/N)")
    if(PrivacySensitive=='N' or PrivacySensitive=='n'):
        clearDic(finalResult)
        clearDic(studentScores)
        print("Data cleared")
        print("Student Scores = " , studentScores)
        print("Student Grades = " , finalResult)
    elif(PrivacySensitive=='Y' or PrivacySensitive=='Y'):
        csvFile4scores = "student_scores.csv"
        csvFile4grades = "student_grades.csv"

        fieldLabels4Grades = ["Name" , "Grade"]
        fieldLabels4Scores = ["Name" , "GPA"]

        #Writting to csv files in order:
        with open(csvFile4grades, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames = fieldLabels4Grades)
            writer.writeheader()
            writer.writerows(finalResult)

        with open(csvFile4scores, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames = fieldLabels4Scores)
            writer.writeheader()
            writer.writerows(studentScores) #sccording to dictionary

        print("Student Data Saved Successfully to csv file")
        print("Student Scores = " , studentScores)
        print("Student Grades = " , finalResult)


    retryF();
