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

        return self.cursor.fetchone()

    def create_user(self, data: dict):

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

        self.cursor.execute(sql)

    def get_user_character(self, user_id: int):

        sql = f'''SELECT character.name
        FROM character
        JOIN user ON user.character_id = character.id
        WHERE user.id = {user_id};'''
        print(sql)
        result = self.cursor.execute(sql)

        return result if result else None

    def set_user_character(self, user_id, character_id):

        sql = f'''
        UPDATE user
        SET character_id = {character_id}
        WHERE id = {user_id};'''

        self.cursor.execute(sql)
