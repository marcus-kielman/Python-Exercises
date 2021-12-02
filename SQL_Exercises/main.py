import mariadb
import sys

def begin_demonstration(cur):
    print("--------------------Begin-----------------------------------")
    cur.execute(
        "show tables"
    )
    for i in cur:
        print(i[0], end=" | ")
    print()

def get_all_employees(cur):
    print("-------------------Show Fields-----------------------------")
    cur.execute(
        "show fields from employees"
    )
    for i in cur:
        print(i[0], end=" ")
    print()

    cur.execute(
        "select * from employees"
    )
    for i in cur:
        print(i)

def get_job_titles(cur):
    print("----------------------Job Title-------------------------------")
    cur.execute(
        "select firstName, lastName, email from employees where jobTitle = ? order by firstName",
        ("Sales Rep",)
    )

    for i in cur:
        print(i)

def get_similar_last_names(cur):
    print("---------------------------Like---------------------------")
    cur.execute(
        "select UPPER(contactLastName), UPPER(contactFirstName) from customers where contactLastName like ?",
        ("S%",)
    )

    for i in cur:
        print(i)

def create_new_name(cur):
    print("----------------------Drop table-------------------------------")
    cur.execute(
        "drop table IF EXISTS test"
    )
    cur.execute(
        "create table test("
        "id INT PRIMARY KEY,age INT, first VARCHAR(30), last VARCHAR(30))"
    )

    cur.execute(
        "describe test"
    )
    for i in cur:
        print(i)

def insert_new_names(cur):
    print("-----------------------insert into------------------------------")
    cur.execute(
        "insert into test (id, age, first, last) values (100, 25, 'jafer', 'alhaboubi')"
    )
    cur.execute(
        "insert into test (id, age, first, last) values (200, 30, 'x', 'z')"
    )

    cur.execute(
        "select * from test"
    )

    for i in cur:
        print(i)

def end_demonstration(cur):
    print("-----------------------END-----------------------------")
    cur.execute(
        "delete from test where id = ?", (100,)
    )

def generate_user_table(cur, email, name, password):
    #Create table with the following fields:
    #email varchar(100)
    #name varchar(50)
    #password varchar(30)
    
    #insert as parameters for testing
    #ywbaek@perscholas.org, young, 'letsgomets'
    #mcordon@perscholas.org, marcial, 'perscholas'
    #mhaseeb@perscholas.org, haseeb, 'platform'
    pass

def get_all_users(cur):
    #print out email name and password of all users
    pass

def get_user_by_name(cur, name):
    #print email and password of a given name
    pass

def validate_user(cur):
    #validate email and password of a user
    #true if validated and false otherwise
    pass

def update_user(cur):
    #update name and password of user by email
    #return true if successful and false otherwise
    pass
                
def main(menu):
    try:
        conn = mariadb.connect(
            user="root",
            password="halfofperu",
            host="127.0.0.1",
            port=3306,
            database="classicmodels"

        )
        conn.autocommit = True
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    else:
        print("successfully connected")
    
    #select column_name from information_schema.columns where table_name='customers'; (use to get column names)
    cur = conn.cursor()

    try:
        if int(menu) == 1:         
            begin_demonstration(cur)
        elif int(menu) == 2:   
            get_all_employees(cur)
        elif int(menu) == 3:   
            get_job_titles(cur)
        elif int(menu) == 4:   
            get_similar_last_names(cur)
        elif int(menu) == 5:   
            create_new_name(cur)
        elif int(menu) == 6:   
            insert_new_names(cur)
        elif int(menu) == 7:   
            end_demonstration(cur)
            conn.close()
            exit()

    except ValueError:
        print("\nInput not valid\n")


if __name__=="__main__":
    while True:
        print("\nCommands")
        print("show fields ------------>(1)")
        print("get all employees ------>(2)")
        print("get job titles --------->(3)")
        print("get similar last names ->(4)")
        print("create new names  ------>(5)")
        print("end demonstration ------>(7)")
        menu = input("\nWhich command would you like to execute? ")
        quit = main(menu)


