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

            # %s = placeholder (indicate that there will be a variable or it'll be a parameter)
            sentence = 'SELECT * FROM person WHERE person_id IN %s'
            primary_keys = ((1,2,3),)

            cursor.execute(sentence, primary_keys)

            records = cursor.fetchall()

            for record in records:
                print(record)

except Exception as e:
    print(e)
finally:
    connection.close()