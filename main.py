
import pyodbc
import pandas.io.sql as pdsql

def connect_sql(my_query):
    server = 'tcp:aice.database.windows.net'
    database = 'aice'
    username = 'aice_candidate'
    password = '@ic3_a3s0c1at3'

    try:
        # get a connection to database
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor = conn.cursor()
        
        # execute our Query and store records as a Pandas DataFrame
        print("Process query:", my_query)
        df = pdsql.read_sql(my_query, conn)
        
        # return the records in the Pandas DataFrame, back to point of calling
        return df

    except (Exception, pyodbc.Error) as error:
        print("Error:", error)
    
    finally:
    #closing database connection.
        if(conn):
            cursor.close()
            conn.close()
            print("\nSQL connection closed successfully.")


if __name__ == "__main__":
    query = '''
        SELECT 
        date, hr, weather
        temperature,
        feels_like_temperature,
        relative_humidity,
        windspeed, psi,
        guest_scooter,
        registered_scooter
        FROM rental_data 
        WHERE date >= '2011-01-01';
        '''
    #print(query)
    data = connect_sql(query)
    # save the data
    data.to_csv('rental_data.csv', index=False)
    print("\nData saved to file: rental_data.csv")

