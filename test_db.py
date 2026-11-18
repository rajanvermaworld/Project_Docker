from db import get_connection

connection = get_connection()
cursor = connection.cursor()
cursor.execute(" insert into users (username, email, password_hash) values('dockeruser2', 'docker2@docker.com', 'password')")
#result = cursor.fetchone()          # we use fetchone to get the first row of the result set, which is a tuple containing the values of the selected columns.
#print(f" database and user are: {result}")
connection.commit()                  # we use commit to save the changes made to the database, such as inserting a new row into a table. If we don't call commit, the changes will not be saved and will be lost when the connection is closed.
cursor.close()
connection.close()