import psycopg2
from decouple import config

connection = psycopg2.connect(user=config('DB_USER'),
                                password=config('DB_PASSWORD'),
                                host=config('DB_HOST'),
                                port=config('DB_PORT'),
                                database=config('DB_NAME'))
cursor = connection.cursor()
# connection.commit()
# cursor.execute("DROP TABLE users;")
# cursor.execute("DROP TABLE orders;")
# cursor.execute("DROP TABLE feedbacks;")
# connection.commit()
connection.commit();
cursor.execute("""create table users (
    id             serial not null primary key,
    chat_id        bigint                              null,
    phone          varchar(255)                        null,
    first_name     varchar(255)                        null,
    last_name      varchar(255)                        null,
    username       varchar(255)                        null,
    current_order_id int                               null,
    current_action varchar(255)                        null,
    created_at     timestamp default CURRENT_TIMESTAMP not null
);""")
connection.commit()
cursor.execute("""create table orders (
    id             serial not null primary key,
    chat_id        bigint                              null,
    service        varchar(255)                        null,
    name           varchar(255)                        null,
    sphere         varchar(255)                        null,
    created_at     timestamp default CURRENT_TIMESTAMP not null
);""")
connection.commit()
cursor.execute("""create table feedbacks (
    id             serial not null primary key,
    chat_id        bigint                              null,
    answered       int                                 null,
    created_at     timestamp default CURRENT_TIMESTAMP not null
);""")
connection.commit()

connection.close()