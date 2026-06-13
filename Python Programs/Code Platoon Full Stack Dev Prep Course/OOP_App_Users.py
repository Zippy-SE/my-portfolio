class User:
    def __init__(self, name, email, drivers_license=None):
        self.name = name
        self.email = email
        self.drivers_license = drivers_license

    def __repr__(self):
        return f"User(name={self.name!r}, email={self.email!r})"


alice = User("Alice Smith", "alice@example.com", "D1234567")
bob   = User("Bob Jones",  "bob@example.com",   "B9876543")
carol = User("Carol White", "carol@example.com")  # no license on file

print(alice)
print(bob)
print(carol)