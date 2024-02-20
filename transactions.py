import psycopg2 as db

connection = db.connect(
    user='postgres',
    password='W1lm3r2000',
    host='localhost',
    port='5432',
    database='test_db'
)

# Create connection and cursor (= executer to fetch data o make queries)
try:
    with connection:
        with connection.cursor() as cursor:

            sentence = 'INSERT INTO person (name, last_name, email) VALUES(%s, %s, %s)'
            values = ("Carlos", 'Munoz', 'carlos@gmail.com')
            cursor.execute(sentence, values)

            sentence = 'UPDATE person SET name = %s, last_name = %s, email = %s WHERE person_id = %s'
            values = ('Karla', 'Solorzano', 'karla@gmail.com', 2)
            cursor.execute(sentence, values)
except Exception as e:
    connection.rollback()
    print(e)
finally:
    connection.close()

print("Transaction finished")
