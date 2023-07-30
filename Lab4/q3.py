"""using the os module to print all the environment variables"""
import os

print("Printing all the environment variables:")
for k,v in os.environ.items():
    print("{} = {}".format(k,v))
