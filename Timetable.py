# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 14:50:03 2019
A script to generate on call timetables
Inputs:
    1 - Doctors.txt (list of doctors to be timetabled)
        Name,Rota type as a fraction (e.g. 1/5)
        
    2 - Inclusions.txt (a optional list of specific days people only work, e.g. Mondays only)
        Name,Day
    
    3 - Exclusions.txt (a optional file with restrictions e.g. never work mondays)
        Name,Day
    4 - Holidays.txt (a list of holidays which have been requested)
        Name,Date
        
@author: JohnG
"""
def read_file_to_dict(filename):
    import csv
    data={}
    with open('Doctors.txt') as file:
        docs = csv.reader(file)
        for row in docs:
            data{row[0]}=row
    return data    
        
            


def read_files():
    #Read in our files and return them to the main function
    #We'll store them in dictionaries for easier referencing
    doctors=read_file_to_dict('Doctors.txt')
    print(doctors)
            
            
    

def main():
    read_files()


if __name__ == "__main__":
   main()