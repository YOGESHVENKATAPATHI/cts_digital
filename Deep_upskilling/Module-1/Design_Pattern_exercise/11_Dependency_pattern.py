class ClientDatabase:
    def get_client_by_id(self, c_id):
        print("Customer Found:", c_id)


class ClientManager:
    def __init__(self, database):
        self.database = database

    def fetch_client(self, c_id):
        self.database.get_client_by_id(c_id)


if __name__ == "__main__":
    db = ClientDatabase()
    manager = ClientManager(db)
    manager.fetch_client(101)