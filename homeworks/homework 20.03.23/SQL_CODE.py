import sqlite3
import psycopg2
from openpyxl import load_workbook

wb = load_workbook('data.xlsx')
sheet = wb.active

print(sheet[1][1].value)

id = ['1','2','3','4','5']
title = ['Title 1','Title 2','Title 3','Title 4','Title 5']
description = ['Description 1','Description 2','Description 3','Description 4','Description 5']
success = ['true', 'false', 'true', 'false', 'true']
deadline = ['27.01.2022','27.06.2022','27.01.2022','27.01.2022','27.12.2022']
data_created = ['26.01.2022','25.06.2022','23.01.2022','25.01.2022','26.12.2022']
def insert_one():
    #for i in range(6): с циклом for не получилось что то сделал колхозким методом
        with psycopg2.connect(
            user="postgres",
            password="Takanashi_13",
            host="127.0.0.1",
            port="5432",
            database="hw"
        ) as connection:

            with connection.cursor() as cursor:
                cursor.execute(
                    f'INSERT INTO public.homework (id, title, description, success, deadline, data_created) VALUES '
                    f"('{id[0]}','{title[0]}','{description[0]}','{success[0]}','{deadline[0]}','{data_created[0]}');")
                cursor.execute(
                    f'INSERT INTO public.homework (id, title, description, success, deadline, data_created) VALUES '
                    f"('{id[1]}','{title[1]}','{description[1]}','{success[1]}','{deadline[1]}','{data_created[1]}');")
                cursor.execute(
                    f'INSERT INTO public.homework (id, title, description, success, deadline, data_created) VALUES '
                    f"('{id[2]}','{title[2]}','{description[2]}','{success[2]}','{deadline[2]}','{data_created[2]}');")
                cursor.execute(
                    f'INSERT INTO public.homework (id, title, description, success, deadline, data_created) VALUES '
                    f"('{id[3]}','{title[3]}','{description[3]}','{success[3]}','{deadline[3]}','{data_created[3]}');")
                cursor.execute(
                    f'INSERT INTO public.homework (id, title, description, success, deadline, data_created) VALUES '
                    f"('{id[4]}','{title[4]}','{description[4]}','{success[4]}','{deadline[4]}','{data_created[4]}');")
                cursor.execute(
                    f'INSERT INTO public.homework (id, title, description, success, deadline, data_created) VALUES '
                    f"('{id[5]}','{title[5]}','{description[5]}','{success[5]}','{deadline[5]}','{data_created[5]}');")
insert_one()