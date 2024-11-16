from tinydb import TinyDB, Query

db = TinyDB("./db.json")
todos = Query()

#db.insert({"name": "John", "age": 22})
#db.insert({"name": "Jane", "age": 22})
#db.insert({"name": "Jim", "age": 22})
#db.insert({"table": 2, "color": "brown"})

#myData = db.search(user.name == "John")
#delete = db.remove(user.name == "Jane")
#update = db.update({"name": "Joe Jim"}, user.name == "Jim")
#llData = db.all()

#print(update)
#print(delete)
#print(myData)

def create():
    userinput = input("add a ToDo: ")
    create = db.insert({"Todo": userinput})
    print("Added ToDo succesfully")

def read():
    allData = db.all()
    for data in allData:
        print("Todo list: " + str(data))

def update():
    userinput = input("change ToDo: ")
    update = db.update({"Todo": userinput}, todos.Todo == userinput)
    print("Changed Todo successfully")

def delete():
    userinput = input("What do you wish to delete? ")
    delete = db.remove(todos.Todo == userinput)
    

while True:
    print("1. Create a ToDo: ")
    print("2. Read ToDo: ")
    print("3. Update ToDo: ")
    print("4. Delete a Todo: ")
    userinput = input("Enter your command: ")
    if userinput == "1":
        create()
    elif userinput == "2":
        read()
    elif userinput == "3":
        update()
    elif userinput == "4":
        delete()
    else: 
        print("Sorry, could not find a command")
        



        
