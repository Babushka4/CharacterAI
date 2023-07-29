import psycopg2


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

        self.cursor.execute(f'SELECT user_id FROM bikbeepbot."UsersBD" WHERE user_id = {user_id}')
        print('user extracted')

        return self.cursor.fetchone()

    def create_user(self, user_id):

        self.cursor.execute(f'INSERT INTO "user" (id) VALUES({user_id})')
        print('user created')

    def get_users(self):

        self.cursor.execute('SELECT * FROM "user"')
        print('all users getted success')

        return self.cursor.fetchall()