import sqlite3
import psycopg2
from psycopg2 import Error

query1 = """
# CREATE TABLE IF NOT EXISTS public.buhgalteria
# (
#     id integer NOT NULL,
#     name character varying(255) NOT NULL UNIQUE,
#     count bigint DEFAULT 0,
#     price double precision DEFAULT 0.0,
#     PRIMARY KEY (id, name)
# );
# 
# TABLESPACE pg_default;
# 
# ALTER TABLE IF EXISTS public."buhgalteria "
#     OWNER to postgres;
"""
query2 = """
#SELECT * FROM public.buhgalteria
#ORDER BY id ASC, name DESC
#"""
# TODO чтение всех строк в таблице
"""
SELECT * FROM public.buhgalteria
"""
# TODO чтение всех строк в таблице с определеннными колонками
# """
# SELECT name, price FROM public.buhgalteria
# """
# TODO запись 1 строки в таблицу
"""
#INSERT INTO public.buhgalteria (name, count, price) VALUES ('бананы', '10', '1000.0')
"""
# TODO запись строк в таблицу
"""
#INSERT INTO public.buhgalteria (name, count, price) VALUES ('бананы 1', '10', '18000.0'), ('бананы 2', '10', '18000.0');
"""
# TODO удаление строк
"""
#DELETE FROM public.buhgalteria WHERE name='бананы' and count='10';
"""
# TODO обновление строк
"""
#UPDATE public.buhgalteria SET count = '99', price = price - 500 WHERE name='бананы' and count='0';    
"""
with psycopg2.connect(
        user="postgres",
        password="Takanashi_13",
        host="127.0.0.1",
        port="5432",
        database="shop_by_river"
) as connection:
    print(connection)
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM public."buhgalteria "')
    records = cursor.fetchall()
    print(records)  # [('бананы 2', 10, 18000.0, 3), ('бананы 1', 99, 17500.0, 2)]
    cursor.close()
    for i in records:
        print(i[0])  # TODO только name
        # бананы 2
        # бананы 1


def insert_one():
    name = "картошка"
    count = 600
    price = 150.5

    list1 = ["картошка", 600, 150.5]

    with psycopg2.connect(
            user="postgres",
            password="Takanashi_13",
            host="127.0.0.1",
            port="5432",
            database="shop_by_river"
    ) as connection:
        with connection.cursor() as cursor:
            # cursor.execute("SELECT version();")
            # record = cursor.fetchone()
            cursor.execute(f'INSERT INTO public."buhgalteria " (name, count, price) VALUES '
                           f"('{name}', '{count}', '{price}');")
            # todo DROP TABLE;
            # cursor.execute("INSERT INTO public.buhgalteria (name) VALUES (:t);", "картошка")  # todo NOT SQL injection


#insert_one()
#TODO Исключение
def exc():
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="postgres",
                                      password="pynative@#29",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres_db")

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        # Executing a SQL query
        cursor.execute("SELECT version();")
        # Fetch result
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")