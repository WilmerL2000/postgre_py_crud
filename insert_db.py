import psycopg2

connection = psycopg2.connect(
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
            sentence = 'INSERT INTO person(name, last_name, email) VALUES(%s, %s, %s)'
            values = (
                ("Sara", 'Marquez', 'Sara@gmail.com'),
                ('Lara', 'Pitty', 'Lara@gmail.com')
            )

            # cursor.execute(sentence, values)
            cursor.executemany(sentence, values)

            # connection.commit() -> when use WITH the data is saved automatically

            inserted_records = cursor.rowcount

            print(f'Inserted Amount: {inserted_records}')
except Exception as e:
    print(e)
finally:
    connection.close()