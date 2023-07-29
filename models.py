from sqlalchemy import Table, Column, MetaData, Integer, String, ForeignKey, select


metadata = MetaData()

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String, nullable=False),
    Column('name', String(length=100), nullable=False),
    Column('time', String(length=320), unique=True, index=True, nullable=False),

    Column('character_id', ForeignKey('character.id'), nullable=True),
)

dialog = Table(
    'dialog',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('request', String, nullable=False),
    Column('response', String(length=320), nullable=False),

    Column('user_id', ForeignKey('user.id'))
)

character = Table(
    'character',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(length=320), unique=True, nullable=False)
)
