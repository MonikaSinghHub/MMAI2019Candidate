import mysql.connector

def create_table():
    con = mysql.connector.connect(user='*********', password='************', host='localhost', port='3306', database='user_db')
    cursor = con.cursor()
    cursor.execute(
        "CREATE TABLE user_info(customer_id INTEGER, first_name VARCHAR, last_name VARCHAR, age INTEGER, sex VARCHAR, race VARCHAR, observation VARCHAR)")
    con.commit()
    con.close()

def enter_data(custId,firstName,lastName,age,sex,race,observation):
    con = mysql.connector.connect(user='*********', password='************', host='localhost', port='3306', database='user_db')
    cursor = con.cursor()

    try:
        select_sql = "select * from user_info where customer_id = %s and first_name = %s and last_name = %s"
        cursor.execute(select_sql, (custId, firstName, lastName))
        data = cursor.fetchall()
        if not data:
            cursor.execute("insert into user_info (customer_id, first_name, last_name, age, sex, race, observation) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (custId, firstName, lastName, age, sex, race, observation))
            print('User got added to the database::' + firstName + ' ' + lastName)
        else:
            print('Customer already exists')
    except Exception as e:
        con.rollback()
        print(e)
    con.commit()
    con.close()

def read_from_db(userId):
    con = mysql.connector.connect(user='*********', password='************', host='localhost', port='3306', database='user_db')
    cursor = con.cursor()
    cursor.execute("select * from user_info where customer_id= %s", (userId,))
    data = cursor.fetchall()
    if not data:
        print("No data")
    else:
        for row in data:
            print(row)
    con.close()
