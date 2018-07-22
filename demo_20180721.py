"""

1) Python ORM for database operation
2) Unittest framework
3) Goal of Unittest case writing
4) Test structure
5) Test output
6) Assert Statement for Debug

Assignment :
1) Install database (posgresql or mysql)
2) install library (psycopg2-binary or pymysql)
3) Create database schema in db
4) create model file of your project
5) create tables
6) Perform CRUD operation on your database
"""

from models import BASE, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE = {
    'username': 'root',
    'password': 'root',
    'db': 'localhost',
    'db_name': 'twitter'
}


def get_connection():
    """
    get database connection based on setting
    :return:
    """
    db_string = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
        DATABASE['username'], DATABASE['password'],
        DATABASE['db'], DATABASE['db_name']
    )
    try:
        return create_engine(db_string)

    except:
        return False


def get_session():
    """
    generate db session
    :return:
    """
    engine = get_connection()
    if engine:
        return sessionmaker(bind=engine)()


def create_table():
    BASE.metadata.create_all(get_connection())


def insert_data():
    """
    insert data in user table
    :return:
    """

    session = get_session()
    _data = {
        'id': 123243,
        'name': "Parth Patel",
        'email': "whyme@smarthview.com",
        'password': "whyshoulditellyou"
    }
    user = User(**_data)

    session.add(user)
    session.commit()
    session.flush()


def update_data():
    """

    :return:
    """
    session = get_session()
    user = session.query(User).filter(User.id == 123243).first()
    user.phone = "444443335543"
    session.add(user)
    session.commit()

update_data()