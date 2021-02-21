from collections import defaultdict
from typing import final


class GPAPredictor:
    # Default dictionalry to store result
    subjectDetails = defaultdict(list)
    subjectNames = []

    #Add marks out of 100
    def getSubjectDetails(self, numberOfSubjects):
        for subject in range(numberOfSubjects):
            subjectName = input("Enter subject name:")
            self.subjectNames.append(subjectName)
            print(f'Marks for {subjectName}')
            theoryMarks = float(
                input(f"Enter your theory marks for {subjectName}: "))
            labMarks = float(
                input(f"Enter your lab marks for {subjectName}: "))
            projectMarks = float(
                input(f"Enter your project marks for {subjectName}: "))
            numberOfCredits = float(
                input(f"Enter number of credits for {subjectName}: "))
            # Storing the result as {"Subject name":[Theory Marks, Lab Marks,Project Marks,Number of credits,Grade(float)]}
            self.subjectDetails[subjectName].extend(
                [theoryMarks, labMarks, projectMarks, numberOfCredits])

    # Calculates subject grade for individual subject and gives them as an int (S=10,A=9,B=8,C=7,D=6)
    def getSubjectGrade(self, subjectName):
        numberOfCredits = self.subjectDetails[subjectName][3]
        theoryMarks = self.subjectDetails[subjectName][0]
        labMarks = self.subjectDetails[subjectName][1]
        projectMarks = self.subjectDetails[subjectName][2]
        if(theoryMarks != 0 and labMarks == 0 and projectMarks == 0):
            self.subjectDetails[subjectName][0] = numberOfCredits*theoryMarks

        elif(labMarks != 0 and theoryMarks != 0 and projectMarks == 0):
            self.subjectDetails[subjectName][0] = theoryMarks*3
            self.subjectDetails[subjectName][1] = labMarks*1

        elif(labMarks != 0 and theoryMarks != 0 and projectMarks != 0):
            self.subjectDetails[subjectName][0] = theoryMarks*2

        numberOfCredits = self.subjectDetails[subjectName][3]
        theoryMarks = self.subjectDetails[subjectName][0]
        labMarks = self.subjectDetails[subjectName][1]
        projectMarks = self.subjectDetails[subjectName][2]
        finalGrade = (theoryMarks+labMarks+projectMarks)//(10*numberOfCredits)
        self.subjectDetails[subjectName].append(finalGrade+1)

        # To get the grade in all subjects

    def makeGrades(self):
        for subjectName in self.subjectNames:
            self.getSubjectGrade(subjectName)
        print(self.subjectDetails)

    def makeGPA(self):
        creditSum = 0
        GPA = 0
        for subjectName in self.subjectNames:
            subjectCredit = self.subjectDetails[subjectName][-2]
            subjectGrade = self.subjectDetails[subjectName][-1]
            creditSum += subjectCredit
            GPA += subjectGrade*subjectCredit
        GPA = GPA/creditSum
        print(GPA)


g = GPAPredictor()
numberOfSubjects = int(input("Enter number of subjects: "))
g.getSubjectDetails(numberOfSubjects)
g.makeGrades()
g.makeGPA()
