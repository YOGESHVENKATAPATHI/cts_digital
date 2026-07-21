import configparser

config = configparser.ConfigParser()
config["DATABASE"] = {
    "host": "localhost",
    "user": "root"
}
print(config["DATABASE"]["host"])
