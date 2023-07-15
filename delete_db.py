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
            sentence = 'DELETE FROM person WHERE person_id = %s'
            values = (3,)

            # cursor.execute(sentence, values)
            cursor.execute(sentence, values)

            deleted_record = cursor.rowcount

            print(f'Deleted Amount: {deleted_record}')
except Exception as e:
    print(e)
finally:
    connection.close()
