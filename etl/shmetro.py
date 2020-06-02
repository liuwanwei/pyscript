#coding='utf-8'

from etlalchemy import ETLAlchemySource, ETLAlchemyTarget

mssql_db_source = ETLAlchemySource(conn_string="mysql://root:1801@localhost/shmetro")

mysql_db_target = ETLAlchemyTarget("mysql://root:1801@localhost/shmetro-etl", drop_database=True)
mysql_db_target.addSource(mssql_db_source)
mysql_db_target.migrate()
