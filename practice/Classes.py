class Student:
    Batch = 2021
    Count = 000

    # Max_marks = {'Phy': 100, 'Maths': 100, 'Chem': 100}

    def __init__(self, n, r, p, prmj):
        self.Name = n
        self.Rollno = r
        self.Program = p
        self.Premajor = prmj
        # self.Marks = m

    # this is for marks handling
    # def get_percent(self):
    #    return (self.Marks['Physics'] + self.Marks['Maths'] + self.Marks['Chem']) * 100 / (self.Max_marks['Phy'] +
    #                                                                                       self.Max_marks['Maths'] +
    #                                                                                       self.Max_marks['Chem'])

    def get_info(self):
        print("Name : {}\nRollno : {}\nProgram : {}\nBatch : {}\nPremajor : {}", self.Name, self.Rollno, self.Program,
              self.Batch, self.Premajor)


def enroll():
    return Student(input("Enter Name"), 1000 * (Student.Batch % 100) + Student.Count, input("Enter Program"),
                   input("Enter Premajor"))
