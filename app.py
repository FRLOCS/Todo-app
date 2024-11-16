from tinydb import TinyDB, Query

db = TinyDB("./db.json")
user = Query()

#db.insert({"name": "John", "age": 22})
#db.insert({"name": "Jane", "age": 22})
#db.insert({"name": "Jim", "age": 22})
#db.insert({"table": 2, "color": "brown"})

#myData = db.search(user.name == "John")
#delete = db.remove(user.name == "Jane")
#pdate = db.update({"name": "Joe Jim"}, user.name == "Jim")
#llData = db.all()

#print(update)
#print(delete)
#print(myData)
db.insert({"Todo": "Read a book"})
db.insert({"Todo": "Learn a new language"})
allData = db.all()

while True:
    print("1. Create a to do: ")
    print("2. Read To do: ")
    userinput = input("Enter your to do: ")
    if userinput == "1":
        userinput = input("add a to do: ")
        create = db.insert({"Todo": userinput})
        print("Added to do: " + str(create))
    elif userinput == "2":
        print(allData)


        
