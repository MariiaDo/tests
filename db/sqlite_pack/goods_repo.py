from db.sqlite_pack._base_db_connector import BaseDbConnection


class GoodsRepo:
    def __init__(self, db_params):
        self._db = BaseDbConnection(db_params)
        self._table_name = 'GOODS'

    def get_all(self):
        res = self._db.cursor.execute(f"SELECT * FROM {self._table_name}")
        return res.fetchall()

    def get_by_filter(self, filter_field, filter_value):
        res = self._db.cursor.execute(f"SELECT * FROM {self._table_name} WHERE {filter_field}='{filter_value}'")
        good = res.fetchone()
        return good

    def insert_one(self, artikul: int, name_of_product: str, brand: str, size: str, quantity: int, purchase_amount: int,
                   sales_amount: int):
        query_insert = f'''
                INSERT INTO {self._table_name} (artikul,name_of_product,brand,size,quantity,purchase_amount,sales_amount)
                VALUES ({artikul}, '{name_of_product}','{brand}', '{size}', {quantity}, {purchase_amount}, {sales_amount});
                '''
        self._db.cursor.execute(query_insert)
        self._db.conn.commit()

    def update_by_filter(self, filter_field, filter_value, condition_field, condition_value):
        query_insert = f'''
                UPDATE {self._table_name} 
                SET {filter_field} = '{filter_value}'
                WHERE {condition_field} = '{condition_value}'; 
                '''
        self._db.cursor.execute(query_insert)
        self._db.conn.commit()

    def delete_by_filter(self, filter_field, filter_value):
        self._db.cursor.execute(f"DELETE FROM {self._table_name} WHERE {filter_field}='{filter_value}'")
        self._db.conn.commit()

    def __del__(self):
        self._db.cursor.close()
        self._db.conn.close()
