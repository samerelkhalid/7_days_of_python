from getpass import getpass
from fabric import Connection

ip = input("Enter the ip of the server you're logging into: ")
username = input("Enter your username: ")
password = getpass("Enter your password: ")
c = Connection(f"{username}@{ip}", connect_kwargs={'password': password})

c.run("ls -l")