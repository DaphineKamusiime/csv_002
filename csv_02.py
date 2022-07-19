import csv
file=open("Books.csv","w")
data="   Book                                     Author                         Year Released\n"
file.write(str(data))
data="0  To Kill A Mockingbird                    Harper Lee                     1960\n"
file.write(str(data))
data="1  A Brief History Of Time                  Stephen Hawking                1988\n"
file.write(str(data))
data="2  The Great Gatsby                         F.Scott Fitzerland             1922\n"
file.write(str(data))
data="3  The Man Who Mistook His Wife For a Hat   Oliver Sacks                   1985\n"
file.write(str(data))
data="4  Pride and Prejudice                      Jane Austen                    1813\n"
file.write(str(data))
file.close()
##asking user to enter a new record
file=open("Books.csv","a")
new_data=input("enter new record\n")
file.write((new_data))
file.close()
file=open("Books.csv","r")
#printing all records
for row in file:
    print(row)
num=int(input("How many records would you like to enter\n"))
numm=0
while numm<num:
    record=input("enter record:")   