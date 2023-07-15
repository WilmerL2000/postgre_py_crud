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
            sentence = 'UPDATE person SET name = %s, last_name = %s, email = %s WHERE person_id = %s'
            values = ('Nayelli', 'Lopez', 'wenlopez@gmail.com', 5)

            # cursor.execute(sentence, values)
            cursor.execute(sentence, values)

            updated_records = cursor.rowcount

            print(f'Updated Amount: {updated_records}')
except Exception as e:
    print(e)
finally:
    connection.close()