import psycopg2
from datetime import datetime


class SQLRequests:

    def __init__(self):

        db_uri = 'postgresql://postgres:r58n16k51@localhost:5433/CharacterAiDB'

        # установим соединение с БД c безопасным соединением SSL
        self.connection = psycopg2.connect(db_uri)

        # инициализируем объект обработки строк
        self.cursor = self.connection.cursor()

        # включение автоматической фиксации изменений
        self.connection.autocommit = True

    def user_exists(self, user_id):

        self.cursor.execute(f'SELECT * FROM "user" WHERE id = {user_id}')
        print('user extracted')

        return self.cursor.fetchone()

    def create_user(self, data: dict):
        print(data)
        sql = 'INSERT INTO "user" ('
        column_list = ', '.join(data.keys())
        sql += column_list + ') VALUES('

        for value in data.values():
            if isinstance(value, datetime):
                sql += 'Null, '
            elif type(value) == int:
                sql += f'{value}, '
            elif type(value) == str:
                sql += f"'{value}', "
            else:
                sql += 'Null, '

        sql = sql[:-2] + ');'
        print(sql)

        self.cursor.execute(sql)
        print('user created')

    def get_users(self):

        self.cursor.execute('SELECT * FROM "user"')
        print('all users getted success')

        return self.cursor.fetchall()