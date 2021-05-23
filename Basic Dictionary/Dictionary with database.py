import mysql.connector

#Connecting to the database
connector=mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)
#Now defining the cursor for execution
curr=connector.cursor()

word=input('Enter the word: ')
#query=curr.execute("select * from Dictionary')
query=curr.execute("select Definition from Dictionary where Expression='%s'"% word.lstrip().rstrip().lower())
result=curr.fetchall()
if result:
    for item in result:
        print(item[0])
else:
    print('Word doesnot exist')

