"""
Following are the topics we will cover today.

1)  Create SQLight3 database
2)  Database connection
3)  CRUD Operation
4)  Python ORM for database operation

"""

# #############################################################################
# 1)  Create SQLight3 database
# #############################################################################


import sqlite3

USERS = {
    'id': 'INTEGER PRIMARY KEY',
    'name': 'TEXT',
    'phone': 'TEXT',
    'email': 'TEXT unique',
    'password': 'TEXT',
}

# database = sqlite3.connect("demo_20180715.db")
# cursor = database.cursor()
# execute_statement = "CREATE TABLE IF NOT EXISTS users ("
# execute_statement += ", ".join([
#     "{} {}".format(key, value) for key, value in USERS.items()
# ])
# execute_statement += ')'
# print(execute_statement)
# cursor.execute(execute_statement)
# database.close()

DATABASE_NAME = "demo_20180715.db"


def prepare_create_table_statement(table_name, fields):
    """

    :param table_name:
    :param fields:
    :return:
    """

    statement = F"CREATE TABLE IF NOT EXISTS {table_name} ("
    statement += ", ".join([
        "{} {}".format(key, value) for key, value in fields.items()
    ])
    statement += ")"

    return statement


def prepare_insert_statement(table_name, fields, values):
    """

    :param table_name:
    :param fields:
    :param values:
    :return:
    """
    _fields = ", ".join([
        field for field in fields
    ])
    place_holder = ", ".join(['?' for value in values])
    statement = F"INSERT INTO {table_name}({_fields}) " \
                F"VALUES({place_holder})"

    return statement


def prepare_select_statement(table_name, fields):
    """

    :param table_name:
    :param fields:
    :param values:
    :return:
    """
    _fields = ", ".join([
        field for field in fields
    ])
    statement = F"SELECT {_fields} FROM {table_name}"

    return statement


class DataBaseORM(object):
    """

    """

    def __init__(self):
        """

        """
        self.db = None
        self.cursor = None
        self.methods = {
            'create_table': self.create_table,
            'drop_table': self.drop_table,
            'create_record': self.create_record,
            'read_record': self.read_record,
            'update_record': self.update_record
        }
        self.data = None
        self.response = None

    def controller(self, **kwargs):
        """

        :return:
        """
        self.data = kwargs.get('data')
        method = kwargs.get('method')
        if method not in self.methods:
            return {
                'error': 'Not supporting requested method'
            }
        self.methods.get(method)()
        return self.response

    def get_connection(self):
        """

        :return:
        """
        self.db = sqlite3.connect(DATABASE_NAME)
        self.cursor = self.db.cursor()

    def create_table(self):
        """

        :return:
        """
        table_name = self.data.get('table_name')
        fields = self.data.get('fields')

        if not table_name or not fields:
            self.response = {
                'error': 'Table name or fields is missing'
            }
            return

        self.get_connection()
        execute_statement = prepare_create_table_statement(
            table_name=table_name, fields=fields)

        self.cursor.execute(execute_statement)
        self.response = {
            'message': F'Table "{table_name}" is created'
        }

    def drop_table(self):
        """

        :return:
        """

    def create_record(self):
        """

        :return:
        """
        table_name = self.data.get('table_name')
        insert_data = self.data.get('insert_data')
        fields = []
        values = []

        if not table_name or not insert_data:
            self.response = {
                'error': 'Table name or Insert data is missing'
            }
            return

        for field, value in insert_data.items():
            fields.append(field)
            values.append(value)

        self.get_connection()
        execute_statement = prepare_insert_statement(
            table_name=table_name, fields=fields,
            values=values
        )

        self.cursor.execute(execute_statement, tuple(values))
        self.db.commit()
        self.response = {
            'message': F'Data has been inserted in "{table_name}" table'
        }

    def read_record(self):
        """

        :return:
        """

        table_name = self.data.get('table_name')
        fields = self.data.get('fields')

        self.get_connection()
        execute_statement = prepare_select_statement(
            table_name=table_name, fields=fields,
        )

        self.cursor.execute(execute_statement)

        for item in self.cursor.fetchall():
            print(type(item), item)
        self.response = {
            'message': F'Data has been inserted in "{table_name}" table'
        }

    def update_record(self):
        """

        :return:
        """

    def __del__(self):
        """

        :return:
        """
        self.db.close()


create_table_payload = {
    'data': {
        'table_name': 'users',
        'fields': {
            'id': 'INTEGER PRIMARY KEY',
            'name': 'TEXT',
            'phone': 'TEXT',
            'email': 'TEXT unique',
            'password': 'TEXT',
        }
    },
    'method': 'create_table'
}

insert_record_payload = {
    'data': {
        'table_name': 'users',
        'insert_data': {
            'id': '1234335533',
            'name': 'Parth',
            'phone': '09786890864',
            'email': 'parth@gmail.com',
            'password': 'WhyITellyou',
        }
    },
    'method': 'create_record'
}

read_record_payload = {
    'data': {
        'table_name': 'users',
        'fields': [
            'id',
            'name',
            'phone',
            'email',
            'password',
        ]
    },
    'method': 'read_record'
}

print(DataBaseORM().controller(**read_record_payload))
