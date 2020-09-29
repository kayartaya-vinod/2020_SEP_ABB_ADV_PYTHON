from sqlite3 import connect

# cfg = dict(host='localhost', username='root', password='TopSecret', database='sample_db')
cfg = 'example_db.sqlite3'


def create_table():
    sql = ''' create table products(
    id integer primary key autoincrement,
    name varchar(50) not null,
    price double,
    category varchar(50) default 'uncategorized'
    )
    '''

    with connect(cfg) as conn:
        cur = conn.cursor()
        cur.execute(sql)
        print('Table "products" created in the db example_db')


def add_products():
    with connect(cfg) as conn:
        cur = conn.cursor()
        while True:
            name = input('Enter product name: ')
            price = float(input('Enter product price: '))
            sql = 'insert into products(name, price) values (?, ?)'
            cur.execute(sql, (name, price))
            choice = input('Want to add another (yes/no): [yes] ')
            if choice.lower() == 'no':
                break


def display_products():
    with connect(cfg) as conn:
        cur = conn.cursor()
        sql = 'select * from products'
        cur.execute(sql)

        for p in cur.fetchall():
            print(f'ID={p[0]}, Name={p[1]}, Category={p[3]}, Price=₹{p[2]}')

        # while True:
        #     p = cur.fetchone()
        #     if p is None:
        #         break
        #     print(f'ID={p[0]}, Name={p[1]}, Category={p[3]}, Price=₹{p[2]}')


if __name__ == '__main__':
    # create_table()
    # add_products()
    display_products()
