import sqlite3

#Creating database with connection function
def connect():
    connection=sqlite3.connect('routine.db')
    #Defining the cursor
    curr=connection.cursor()
    #Now creating the table
    curr.execute("create table if not exists routine(ID integer primary key,date text,earning text,exercise text,study text,diet text,python text)")
    connection.commit()
    connection.close()
def insert(date,earning,exercise,study,diet,python):

    connection=sqlite3.connect('routine.db')
    curr=connection.cursor()
    curr.execute('insert into routine values(NULL,?,?,?,?,?,?)',(date,earning,exercise,study,diet,python) )
    connection.commit()
    connection.close()
    

def view():
    connection=sqlite3.connect('routine.db')
    curr=connection.cursor()
    curr.execute('select * from routine')
    rows=curr.fetchall()
    connection.commit()
    connection.close()
    return rows
def search(date='',earning='',exercise='',study='',diet='',python=''):
    connection=sqlite3.connect('routine.db')
    curr=connection.cursor()
    curr.execute("select * from routine where date=? or earning=? or exercise=? or study=? or diet=? or python=?",
    (date,earning,exercise,study,diet,python))
    rows=curr.fetchall()
    connection.commit()
    connection.close()
    return rows
def delete(id):
    connection=sqlite3.connect('routine.db')
    curr=connection.cursor()
    curr.execute('delete from routine where id=?',(id,))
    connection.commit()
    connection.close()


connect()