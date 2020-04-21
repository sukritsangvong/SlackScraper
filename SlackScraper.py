import json
import os
import csv
from Student import *
"""
    PJ Sangvong, 17 April 2020
    
    This program creates csv file with grades for students' reading posts.
    
    Requirement:
    
    Need to have reading-post directory in the directory that this program
    is located
    
    Excliamer:
    
    This program strictly uses #R<number> as an identifier for the grades
    
    Texts other than #R<number> would be considered unknowSymbol, which would be
    printed in the terminal. The output file will not include unknowSymbol
    
    The file output has students' names as their lasname + first letter of their
    firstname. The order remains similar to the spreadsheet, but the file does
    not include students that had never posted anything before.
    """
def loadJSON(filename, studentList):
    """Reads JSON file from filename and add object Student to studentList"""
    #opens JSON file
    with open(filename) as f:
        data = json.load(f)
    
    #loops through the list of dictionary(data)
    for dict in data:
        #normal post would have name
        try:
            name = dict['user_profile']['name']
            userid = dict['user']
            readingPost = dict['text'][0:3]
            
            if len(studentList) == 0: #checks if first time adding
                thisStudent = Student(name,  readingPost, userid)
                studentList.append(thisStudent)
            else:
                foundMatch = False
                for eachStudent in studentList:
                    if eachStudent.equal(userid): #uses userid to check
                        #adds to existing Student
                        eachStudent.addReadingPost(readingPost)
                        foundMatch = True
                        #renames if the name is unknownName
                        if eachStudent.name == 'unknownName':
                            eachStudent.name = name
            
                #makes new Student object
                if not foundMatch:
                    newStudent = Student(name, readingPost, userid)
                    studentList.append(newStudent)
#enters except if name doesn't exist
#reply post somehow does not have name in it
except KeyError:
    try:
        #reply post has subclass as thread_broadcast
        if dict['subtype'] == 'thread_broadcast':
            userid = dict['user'] #reply post has userid
            readingPost = dict['text'][0:3]
            foundMatch = False
                
                for eachStudent in studentList: #uses userid to check
                    #adds to existing Student
                    if eachStudent.equal(userid):
                        eachStudent.addReadingPost(readingPost)
                        foundMatch = True
                    
                    #makes new Student object
                    if not foundMatch:
                        #since reply doesn't include name,
                        #first name the object as unknownName
                        name = 'unknownName'
                        newStudent = Student(name, readingPost, userid)
                        studentList.append(newStudent)
    
        #enters except it is something unrelated
        #ex: join channel message
        except KeyError:
            print("KeyError in " + filename)

return studentList


def sortStudent(thisStudent):
    return thisStudent.name

def main():
    #initializes variable
    directoryName = './reading-posts' #directory should be inside this script
    ignoreList = ['loesper', 'romans2']
    outputFileName = 'Graded.csv'
    studentList = []
    
    #gets directory names
    dir = os.listdir(directoryName)
    curdir = os.getcwd()
    
    #go through every file in the given directoryName
    for file in dir:
        studentList = loadJSON(directoryName+ '/' + file, studentList)
    
    #sorts students in the list
    studentList = sorted(studentList, key = sortStudent)

#displays on terminal
for i in studentList:
    i.display()
    
    #writes up a file
    with open( outputFileName , 'w') as newfile:
        #writes the header
        writer = csv.writer(newfile, delimiter = ',', lineterminator= '\n')
        fieldnames = ['Name','R1','R2','R3','R4','R5','R6','R7','R8','R9','R10',\
                      'R11','R12','R13','R14','R15','R16','R17','R18','R19',\
                      'R20','R21','R22','R23','R24','R25']
                      writer.writerow(fieldnames)
                      
                      #write the data
                      for student in studentList:
                          if not student.name in ignoreList: #not include people in the list
                              stuffnames = [student.name]
                              for i in range (1,26):
                                  thisR = '#R' + str(i)
                                  if thisR in student.readingPost:
                                      stuffnames.append('1')
                                          else:
                                              stuffnames.append('')
                                                  writer.writerow(stuffnames)



if __name__ == "__main__":
    main()
