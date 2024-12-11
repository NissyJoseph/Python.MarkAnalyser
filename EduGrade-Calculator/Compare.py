#EduGrade Calculator
"""
This program is to showcase my profiency in python programing language.
PS: No AI tools were used.
"""
def Compare(Candidate1, Candidate2):

    if Candidate1.cgpa > Candidate2.cgpa:
        print(f"{Candidate1.name} has Higher CGPA ({round(Candidate1.cgpa, 2)}) than {Candidate2.name} ({round(Candidate2.cgpa, 2)}).")
    elif Candidate1.cgpa < Candidate2.cgpa:
        print(f"{Candidate2.name} has Higher CGPA ({round(Candidate2.cgpa, 2)}) than {Candidate1.name} ({round(Candidate1.cgpa, 2)}).")
    else:
        print(f"Both {Candidate1.name} and {Candidate2.name} have the same CGPA ({round(Candidate1.cgpa, 2)}).")
    print()
    
    if Candidate1.Sum > Candidate2.Sum:
        print(f"{Candidate1.name} has Higher total marks ({Candidate1.Sum}) than {Candidate2.name} ({Candidate2.Sum}).")
    elif Candidate1.Sum < Candidate2.Sum:
        print(f"{Candidate2.name} has Higher total marks ({Candidate2.Sum}) than {Candidate1.name} ({Candidate1.Sum}).")
    else:
        print(f"Both {Candidate1.name} and {Candidate2.name} have the same total marks ({Candidate1.Sum}).")
    print()
    
    if Candidate1.Avg > Candidate2.Avg:
        print(f"{Candidate1.name} has Higher Average ({Candidate1.Avg}) than {Candidate2.name} ({Candidate2.Avg}).")
    elif Candidate1.Avg < Candidate2.Avg:
        print(f"{Candidate2.name} has Higher Average ({Candidate2.Avg}) than {Candidate1.name} ({Candidate1.Avg}).")
    else:
        print(f"Both {Candidate1.name} and {Candidate2.name} have the same Average({Candidate1.Avg}).")
    print()
            
    for i in range(5):  
        if Candidate1.Grades[i] < Candidate2.Grades[i]:
            print(f"{Candidate1.name} has a Higher grade in {['English', 'Tamil', 'Science', 'Maths', 'Social'][i]} '{Candidate1.Grades[i]}' than {Candidate2.name} '{Candidate2.Grades[i]}'.")
        elif Candidate1.Grades[i] > Candidate2.Grades[i]:
            print(f"{Candidate2.name} has a Higher grade in {['English', 'Tamil', 'Science', 'Maths', 'Social'][i]} '{Candidate2.Grades[i]}' than {Candidate1.name} '{Candidate1.Grades[i]}'.")
        else:
            print(f"Both {Candidate1.name} and {Candidate2.name} have the same grade in {['English', 'Tamil', 'Science', 'Maths', 'Social'][i]} '{Candidate1.Grades[i]}'.")






