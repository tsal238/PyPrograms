import mysql.connector
from csv import reader
import os


#creating a database in mySQL
def create_database(host, user, passwd, database):
    mydb = mysql.connector.connect(
        host=host,
        user = user,
        passwd= passwd   
    )
    mycursor=mydb.cursor()
    mycursor.execute("CREATE DATABASE " + database)
    mycursor.execute("SET GLOBAL max_allowed_packet=10000000")
    print("Database has been created")
    mydb.close()

#populate the database
def database_pop(host, user,passwd,database,lines):
    cols=[]
    l_= []
    place_holder =[]
    list_of_rows= []
    cols=lines[0].rstrip().split(",")

    for i in cols:
            place_holder +=["%s"]
            element= i+ " VARCHAR(255)"
            l_+= [element]

    #converting a list to a string       
    listTostr = ','.join([str(elem) for elem in l_])
    colsTostr = ','.join([str(elem) for elem in cols])
    place_holderTostr = ','.join([str(elem) for elem in place_holder])
    
    #access database that was created in create_database
    mydb = mysql.connector.connect(
        host=host,
        user = user,
        passwd= passwd,
        database=database   
    )
    mycursor=mydb.cursor()

    # creating a table in the database
    mycursor.execute("CREATE TABLE "+database+" ("+listTostr+")")
    print("Table creation completed")
    
    #sql formula for populating the table 
    sqlformula = "INSERT INTO "+database +" ("+colsTostr+ ") VALUES(" +place_holderTostr+ ")"
    print("sql formula creation completed")

    for k in reader(lines[1:]):
        list_of_rows+=[tuple(k)]
        

    #populating the table with all the information from the csv file
    mycursor.executemany(sqlformula, list_of_rows)
    print("Table population completed")
    mydb.commit()
    print()
    print("**** Congratulations ur database has been populated you are now able to access all information in csv file in mysql ****")
    mydb.close()

# Function handles the opening, reading and closing of the data file
def file_handle(host,user,passwd,database,file1):

        f=os.path.dirname(os.path.abspath(__file__))
        path_file = f +"\\"+file1
        file_1=open(path_file,"r")
        lines = file_1.readlines()

        #calling function to populate the table
        database_pop(host,user,passwd,database,lines)
        file_1.close()

print("***** Hi this is a csv file convertion to database system for mysql *****")
print()


def main():
    csv_f = input("csv file: ")
    host = input("Host: ")
    user = input("User: ")
    passwd = input("Passwd: ")
    k=csv_f.find(".")
    ext_ = csv_f[k+1:]
    try:
        if ext_== "csv":
            database =csv_f[0:k]
            create_database(host, user, passwd, database)
            file_handle(host, user, passwd, database,csv_f)
        else:
            print("error this is not a csv file try again")
            main()
    except Exception as ex:
        print(ex)
        print("\n**** please try again or exit ****")
        boolean_1=True
        while (boolean_1):
            k= input("To try again?Y/N: ")
            if k=="Y" or k=="y":
                main()
            if k=="N" or k=="n":
                boolean_1=False
            else:
                print("wrong input")
            
main()
