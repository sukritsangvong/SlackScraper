# SlackScraper
PJ Sangvong, 17 April 2020

This program creates a csv file with grades for students' reading posts in CS111.
It reads through specific keyword in the messages of a given channel of Slack.

Requirement:

    Need to have reading-post directory in the directory that this program
                                is located

Exclaimer:

    This program strictly uses #R<number> as an identifier for the grades

    Texts other than #R<number> would be considered unknowSymbol, which will be
    printed in the terminal. The output file will not include unknowSymbol

    The file output has students' names as their lastname + first letter of their
    firstname. The order remains similar to the spreadsheet, but the file does
    not include students that had never posted anything before.
