from _MySQL.database import Database
import mysql.connector


db = Database('localhost','webadmin','password','projekt04')

db.getAbteilungen()