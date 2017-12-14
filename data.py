host = "ec2-50-17-217-166.compute-1.amazonaws.com" 
user = "wrhvnfvfjkhwto"
passwd = "dab621c8498910b8bb5d48d79905f6f81c22c850ce0c5818b75a50138494d68d" 
db = "dei0rdv9pousvv"

from urllib import parse
import psycopg2
import os
uri = 'postgres://wrhvnfvfjkhwto:dab621c8498910b8bb5d48d79905f6f81c22c850ce0c5818b75a50138494d68d@ec2-50-17-217-166.compute-1.amazonaws.com:5432/dei0rdv9pousvv'

parse.uses_netloc.append("postgres")
url = parse.urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)