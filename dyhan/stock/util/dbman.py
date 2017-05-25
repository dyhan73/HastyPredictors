import sqlite3
import pandas as pd


class DbMan:
    def __init__(self):
        self.conn = sqlite3.connect("data/kospi-2010-201704.sqlite")

    def __del__(self):
        self.conn.close()

    def get_stock_data(self, code, fdate='20100101', edate='20170430', field=['date', 'ends', 'amount']):
        query = "select %s from stocks where date between '%s' and '%s' and code='%s'"\
                % (','.join(field), fdate, edate, code)
        print(query)
        df = pd.read_sql_query(query, self.conn)
        return df

    def get_samsung(self):
        return self.get_stock_data('005930')