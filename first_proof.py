from os import path
import poet.main as poet

def create_config():
	print("not implemented yet")


def main():
	if (path.exists("config.cfg") == False) :
		create_config()
	file = open("config.cfg")
	line = file.readline();
	if (line.split("=", 1)[0] == "TOKEN") :
		token = line.split("=", 1)[1]
	poet.poet(token, 1)
main()