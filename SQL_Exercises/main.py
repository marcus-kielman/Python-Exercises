import mariadb
import sys

def main():
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
    
    #select column_name from information_schema.columns where table_name='customers'; (use to get column names)
    cur = conn.cursor()
    cur.execute(
        "SELECT customerName, phone FROM customers;"
    )
    for i in cur:
        print(f"{i[0]}---->{i[1]}")

    conn.close()
    exit()

if __name__=="__main__":
    main()

