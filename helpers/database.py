import psycopg


# def db_connect(
#     db_name: str, db_user: str, db_password: str, db_host: str, db_port: str
# ) -> psycopg.Connection:
#     conn = psycopg.connect(
#         host=db_host, dbname=db_name, user=db_user, password=db_password, port=db_port
#     )
#     return conn


def db_connect(
    db_name: str, db_user: str, db_password: str, db_host: str, db_port: str
) -> psycopg.Connection:
    conn = psycopg.connect(
        host=db_host, dbname=db_name, user=db_user, password=db_password, port=db_port
    )
    return conn
