host = "ec2-50-17-217-166.compute-1.amazonaws.com" 
user = "orbprnlwyfrrgf"
passwd = "70e8df2c720a4b9e306ad56c217e758a9d70a770b13b18012d2d0fd7606517a6" 
db = "dem3go8risn9ns"

from urllib import parse
import psycopg2
import os
from sqlalchemy import * 

engine = create_engine('postgres://orbprnlwyfrrgf:70e8df2c720a4b9e306ad56c217e758a9d70a770b13b18012d2d0fd7606517a6@ec2-54-163-233-103.compute-1.amazonaws.com:5432/dem3go8risn9ns')
connection = engine.connect()
metadata = MetaData()
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String),
 )

addresses = Table('addresses', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', None, ForeignKey('users.id')),
    Column('email_address', String, nullable=False)
 )
metadata.create_all(engine)

t = text( "CREATE TABLE Artist(ArtistID bigint NOT NULL PRIMARY KEY,Name varchar(50) NOT NULL, ArtistGenreID bigint NOT NULL, Popularity bigint NOT NULL);")

for t in metadata.sorted_tables:
    print(t.name)


    # uri = 'postgres://orbprnlwyfrrgf:70e8df2c720a4b9e306ad56c217e758a9d70a770b13b18012d2d0fd7606517a6@ec2-54-163-233-103.compute-1.amazonaws.com:5432/dem3go8risn9ns'

# parse.uses_netloc.append("postgres")
# url = parse.urlparse(os.environ["DATABASE_URL"])

# conn = psycopg2.connect(
#     database=url.path[1:],
#     user=url.username,
#     password=url.password,
#     host=url.hostname,
#     port=url.port
# )