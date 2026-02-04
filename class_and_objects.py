class Name:
    college_name ="JECRC UNI"

    def __init__(self,name):
        self.name = "Yash"

    def Welcome(self):
        print("Welcome")

s1 = Name("karan")
print(s1.name)
s1.Welcome()


# create student class that takes name and marks of 3 subjects as arguments as constructor.
# then create a method to print the average 
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for value in self.marks:
            sum += value
        print(f"hi,{self.name},Your avg score is : {sum/3}")

s1 = Student("Yash saini",[75,78,80])
s1.get_avg()