"""
PJ Sangvong, 17 April 2020

This is a class object that is used with SlackScraper

Parameters:

name: name of the student
readingPost: the first 3 indices of string text
userid: the user ID of the student
"""
class Student:
    def __init__(self, name, readingPost, userid):
        self.name = name
        self.userID = userid

        #checks whether it has unknowSymbol or not
        if readingPost[0:2] == '#R':
            self.readingPost = [readingPost]
            self.unknowSymbol = False
            self.unknowSymbolList = []
        else:
            self.readingPost = []
            self.unknowSymbol = True
            self.unknowSymbolList = [readingPost]

    #displays everthing in the terminal
    def display(self):
        print("name: " + self.name + " readingPost: " +  ' '.join(self.readingPost))
        if self.unknowSymbol:
            size = len(self.unknowSymbolList)
            unknowSymbolString = ' '.join(self.unknowSymbolList)
            print('**** '+ str(size) + ' unknowSymbol: ' + unknowSymbolString)

    #adds readingPost to the readingPost List
    def addReadingPost(self, readingPost):
        if readingPost[0:2] == '#R':
            self.readingPost.append(readingPost)
            self.readingPost.sort()
        else:
            self.unknowSymbol = True
            self.unknowSymbolList.append(readingPost)

    #uses userIDs to compare whether two Students are equal
    def  equal(self, anotherID):
        if self.userID == anotherID:
            return True
        else:
            return False
