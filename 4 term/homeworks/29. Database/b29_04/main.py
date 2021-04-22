import os
import sqlite3


db_filename = "receipts.db"


def create_db_from_zero():
    if os.path.exists(db_filename):
        os.remove(db_filename)

    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE foods (
            food_id INTEGER NOT NULL, 
            name TEXT,
            PRIMARY KEY (food_id AUTOINCREMENT)
        );
        """
    )

    cursor.execute(
        """
        CREATE TABLE receipts (
            receipt_id INTEGER NOT NULL,
            food_id INTEGER,
            description TEXT,
            PRIMARY KEY (receipt_id AUTOINCREMENT),
            FOREIGN KEY (food_id)
                REFERENCES foods (food_id)
        );
        """
    )

    cursor.execute(
        """
        CREATE TABLE ingredients (
            ingredient_id INTEGER NOT NULL,
            name TEXT, 
            PRIMARY KEY (ingredient_id AUTOINCREMENT)
        );
        """
    )

    cursor.execute(
        """ 
        CREATE TABLE receipt_items(
            receipt_id INTEGER NOT NULL,
            ingredient_id INTEGER,
            quantity INTEGER NOT NULL,
            units TEXT,
            FOREIGN KEY (receipt_id)
                REFERENCES receipts (receipt_id),
            FOREIGN KEY (ingredient_id)
                REFERENCES ingredients (ingredient_id)
        );
        """
    )

    conn.commit()
    conn.close()


def add_food(food_name):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO foods (
            name
        ) 
        VALUES (?);
        """,
        (food_name, )
    )
    inserted_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return inserted_id


def add_receipt(food_id, description, ingredients: dict):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO receipts (
            description,
            food_id
        ) 
        VALUES (?, ?);
        """,
        (description, food_id)
    )
    receipt_id = cursor.lastrowid

    for ingr_id, data in ingredients.items():
        cursor.execute(
            """
            INSERT INTO receipt_items (
                ingredient_id,
                receipt_id,
                quantity,
                units 
            )
            VALUES (?, ?, ?, ?);
            """,
            (ingr_id, receipt_id, *data)
        )

    inserted_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return inserted_id


def add_ingredient(name):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO ingredients (
            name        
        )
        VALUES (?);
        """,
        (name, )
    )

    inserted_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return inserted_id


def search_receipt(food_name):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT receipts.receipt_id, receipts.description 
            FROM receipts, foods 
            WHERE foods.name = (?) 
        """,
        (food_name, )
    )
    receipts_ids = cursor.fetchall()

    for row in receipts_ids:
        receipt_id = row[0]
        desc = row[1]

        cursor.execute(
            """
            SELECT * FROM receipt_items
            WHERE receipt_id = (?)
            """,
            (receipt_id, )
        )
        ingrs = cursor.fetchall()

        print("Receipt", receipt_id)
        print("Ingredients:")
        for ingr in ingrs:
            cursor.execute("SELECT name FROM ingredients "
                           "WHERE ingredient_id = (?)", (ingr[1], ))
            ingr_name = cursor.fetchall()[0][0]
            print(ingr_name, '-', *ingr[2:])
        print("Description:", desc)

    conn.close()


if __name__ == '__main__':
    create_db_from_zero()
    flour_id = add_ingredient("Мука")
    water_id = add_ingredient("Вода")
    sugar_id = add_ingredient("Сахар")
    salt_id = add_ingredient("Соль")
    cherry_id = add_ingredient("Вишня")
    vareniki_id = add_food("Вареники с вишней")

    description = """Отмеряйте необходимое количество муки 
        и пересыпьте в большую миску, добавьте щепотку соли. 
        Добавьте горячую воду и немного перемешайте. 
        Замесите тесто в миске, а затем переложите на рабочую поверхность, 
        посыпанную мукой, и вымесите. Тесто должно стать упругим и не липнуть к рукам.
        Раскатайте тесто толщиной около 2-3 миллиметров на доске или рабочей поверхности. 
        При помощи кружки или стакана вырежьте в тесте кружочки.
        Выложите немного начинки на один край кружочка и аккуратно прижмите другой стороной. 
        Хорошо защипите края теста, чтоб начинка в процессе варки не могла вытечь из вареника.
        Сформируйте вареники из всех кружочков теста. Варите вареники в кипящей воде примерно 3-4 минуты.
        Выложите горячие вареники в мисочку и присыпьте сахаром. Это придаст сладость и не позволит 
        вареникам слипнуться между собой. Именно поэтому мы не добавляли сахар в саму начинку."""
    ingredients = {
        flour_id: (320, 'г'),
        water_id: (180, 'мл'),
        sugar_id: (1, 'ст. л.'),
        salt_id: (1, 'щепотка'),
        cherry_id: (400, 'г')
    }
    add_receipt(vareniki_id, description, ingredients)

    search_receipt("Вареники с вишней")
