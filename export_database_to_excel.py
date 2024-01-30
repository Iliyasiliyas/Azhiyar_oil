from unwrap import db
import pandas as pd

def export_database_to_excel():
    with pd.ExcelWriter('database_export.xlsx', engine='xlsxwriter') as writer:
        meta = db.metadata
        for table in reversed(meta.sorted_tables):  # Reverse the order of tables
            query = db.session.query(table).statement
            df = pd.read_sql(query, db.session.bind)
            df.to_excel(writer, sheet_name=table.name, index=False)
