#EduGrade Calculator
"""
This program is to showcase my profiency in python programing language.
PS: No AI tools were used.
"""

class Class_Marks:
    def __init__(self):
        self.name = input("Enter Your Name:- ")
        print()
        print(f"Congrations on your Score {self.name}!! \nKindly enter your Marks only in xx/100")
        self.Grades = []
        self.Credits = [0,0,0,0,0]
        self.TotalNoOfCreditPoints = 18
        self.CredsDict={'O':10,'A+':9,'A':8,'B+':7,'B':6,'C+':5,'C':4,'F':3}
        
    def English(self,mark):
        self.eng = int(mark)
        
    def Tamil(self,mark):
        self.tam = int(mark)
        
    def Science(self,mark):
        self.sci = int(mark)
        
    def Maths(self,mark):
        self.math = int(mark)
        
    def Social(self,mark):
        self.soc = int(mark)
        
    def Total(self):
        self.Sum = self.eng + self.tam + self.sci + self.math + self.soc
        print(f"The Total marks of {self.name} is {self.Sum}")

    def AVG(self):
        self.Avg = self.Sum/5
        print(f"The Average Marks of {self.name} is {self.Avg}")
        
    def Grade(self):
        self.Grades = []
        self.grademarks(self.eng, self.Grades)
        self.grademarks(self.tam, self.Grades)
        self.grademarks(self.sci, self.Grades)
        self.grademarks(self.math, self.Grades)
        self.grademarks(self.soc, self.Grades)
        print(f"English Grade = '{self.Grades[0]}' \nTamil Grade = '{self.Grades[1]}' \nScience Grade = '{self.Grades[2]}' \nMaths Grade = '{self.Grades[3]}' \nSocial Grade = '{self.Grades[4]}'")
    
    def CGPA(self):
        self.EngCred = self.CredsDict[self.Grades[0]]
        self.TamCred = self.CredsDict[self.Grades[1]]
        self.SciCred = self.CredsDict[self.Grades[2]]
        self.MathCred = self.CredsDict[self.Grades[3]]
        self.SocCred = self.CredsDict[self.Grades[4]]
        
        self.TierB = (self.EngCred + self.TamCred)*3
        self.TierA = (self.SciCred + self.MathCred + self.SocCred)*4
        self.cgpa = (self.TierA + self.TierB) / self.TotalNoOfCreditPoints
        
        print(f"The CGPA of {self.name} is {round(self.cgpa,2)}")

    def grademarks(self, mark, Grades):
        if mark==100:
            Grades.append("O")
        elif 90<=mark<=99:
            Grades.append("A+")
        elif 80<=mark<=89:
            Grades.append("A")
        elif 70<=mark<=79:
            Grades.append("B+")
        elif 60<=mark<=69:
            Grades.append("B")
        elif 50<=mark<=59:
            Grades.append("C+")
        elif 40<=mark<=49:
            Grades.append("C")
        else:
            Grades.append("F")

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
        if Candidate1.Grades[i] > Candidate2.Grades[i]:
            print(f"{Candidate1.name} has a Higher grade in {['English', 'Tamil', 'Science', 'Maths', 'Social'][i]} '{Candidate1.Grades[i]}' than {Candidate2.name} '{Candidate2.Grades[i]}'.")
        elif Candidate1.Grades[i] < Candidate2.Grades[i]:
            print(f"{Candidate2.name} has a Higher grade in {['English', 'Tamil', 'Science', 'Maths', 'Social'][i]} '{Candidate2.Grades[i]}' than {Candidate1.name} '{Candidate1.Grades[i]}'.")
        else:
            print(f"Both {Candidate1.name} and {Candidate2.name} have the same grade in {['English', 'Tamil', 'Science', 'Maths', 'Social'][i]} '{Candidate1.Grades[i]}'.")





