

import json


# helper functions 
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError     :

        return []

def save_tasks(tasks):
        with open('tasks.txt', "w") as file:
            json.dump(tasks, file)

# handler functions
def getAllTasks(tasks):
    if(len(tasks) == 0):
        print([])
    for index, value in enumerate(tasks, start  = 1):
        print(f"{index}. {value["name"]}  {value["time"]}")        

def updateTask(tasks):
    getAllTasks(tasks)
    try:
        index = int(input("Type the task index to update"))
    except ValueError:
        print("Enter a number")
        return


    if  (index <1 or index> len(tasks)):
        print("invalid index")
        return

    name = input("Enter NEW task name")
    time = input("Enter NEW task time")
    tasks[index -1] = {'name': name, 'time' : time}
    save_tasks(tasks)
    
    

def addNewTask(tasks):
    name = input("Enter task name")
    time = input("Enter task time")
    tasks.append({'name' : name, 'time' : time})
    save_tasks(tasks)

def deleteTask(tasks):
    getAllTasks(tasks)
    index = print("Type the task index to update")

    if type(index) != int or (index <=1 or index> len(tasks)):
        print("invalid index")
        return

    del tasks[index -1]
    save_tasks(tasks)
    

# main loop
def main():
    
 while True:
        tasks = load_tasks()
        print("Enter your choices")
        print("1. Get all tasks")
        print("2. Update task")
        print("3. Add new task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Enter your choice")
        match choice:
            case "1": getAllTasks(tasks)
            case "2" : updateTask(tasks)
            case "3" : addNewTask(tasks)
            case "4" : deleteTask(tasks)
            case "5" : break
            case _: print("Invalid choice")

if __name__ == "__main__":
    main()

