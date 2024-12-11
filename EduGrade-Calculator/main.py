#EduGrade Calculator
"""
This program is to showcase my profiency in python programing language.
PS: No AI tools were used.
"""

from IndexCode import Class_Marks
from Compare import Compare

print("Your are Candidate 1")
Candidate1  = Class_Marks()

Candidate1.English(input("English Marks: "))
Candidate1.Tamil(input("Tamil Marks: "))
Candidate1.Science(input("Science Marks: "))
Candidate1.Maths(input("Maths Marks: "))
Candidate1.Social(input("Social Marks: "))
print()

Candidate1.Total()
Candidate1.AVG()
Candidate1.Grade()
Candidate1.CGPA()
print()

print("Candidate 2")
Candidate2 = Class_Marks()
print()

Candidate2.English(input("Enter Your English Marks: "))
Candidate2.Tamil(input("Enter Your Tamil Marks: "))
Candidate2.Science(input("Enter Your Science Marks: "))
Candidate2.Maths(input("Enter Your Maths Marks: "))
Candidate2.Social(input("Enter Your Social Marks: "))
print()

Candidate2.Total()
Candidate2.AVG()
Candidate2.Grade()
Candidate2.CGPA()
print()

Compare(Candidate1, Candidate2)
