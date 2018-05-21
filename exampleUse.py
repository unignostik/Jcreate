def main():
    c = Jcreate("Customers")
    s = {"Name": 'Chase', "Age": 25, "ID": 239029}
    g = {"Name": 'John', "Age": 18, "ID": 329355}
    k = [s, g]
    for item in k:
        c.addobject(item)
    c.endfile()
