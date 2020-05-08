from pipeline.snowpack.sql_queries import basin_table_create, basin_aggregate_table_create,\
    snowpack_table_create, location_table_create, basins_table_insert,location_table_insert
from pipeline.utils.postgresConnection import get_postgres_connection

date_table_create = ("""CREATE TABLE IF NOT EXISTS date_table (
                            id SERIAL PRIMARY KEY,
                            date DATE NOT NULL
                            );""")

insert_date = ("""INSERT INTO date_table (date) VALUES (%s);""")

conn = get_postgres_connection('snowpackDB' ) #, 'snowpack')
cur = conn.cursor()
create_table_queries = [date_table_create , basin_table_create, snowpack_table_create, basin_aggregate_table_create, location_table_create]

for query in create_table_queries:
    cur.execute(query)
conn.commit()
conn.close()

from pipeline.snowpack.populate_tables import extract_snowpack_data

regions_dict = extract_snowpack_data()
regions_dict.pop('year')
regions_dict.pop('day')
regions_dict.pop('month')

conn = get_postgres_connection('snowpackDB')
cur = conn.cursor()
for region in regions_dict.keys():
    try:
        regions_dict[region].pop('Basin Index')
    except Exception as e:
        print(e)
    locations = regions_dict[region].keys()
    cur.execute(basins_table_insert, (region,))
    basin_id  = cur.fetchone()[0]
    conn.commit()
    for location in locations:
        location_dict = regions_dict[region][location]
        elevation = location_dict['Elev (ft) ']
        cur.execute(location_table_insert, (location,elevation,basin_id))
    conn.commit()
conn.close()

# start_date = date(2008, 1, 1)
# end_date = date(2009, 1, 1)
# scrape_snowpack_data(start_date, end_date)