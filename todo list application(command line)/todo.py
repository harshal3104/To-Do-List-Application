tasks=[]

def lavender(text):
    return f"\033[95m\033[1m{text}\033[0m"

def green(text):
    return f"\033[92m\033[1m{text}\033[0m"

def blue(text):
    return f"\033[96m\033[1m{text}\033[0m"

def red(text):
    return f"\033[91m{text}\033[0m" 



def add_task(task):
    tasks.append({"task":task, "completed":False})
    print(blue("Task Added")) 
    
def list_tasks():
    print(lavender("\nTo-Do List"))
    for index, task in enumerate(tasks, start=1):
        if task["completed"]:
            status="✓"
        else:
            status=" "
            
        print(f"{index}. [{status}] {task['task']}")
    print()
    

def delete_task():
    if not tasks:
        print(red("No tasks to delete."))
        return

    index = int(input("Enter the task number you want to delete: "))

    if 1 <= index <= len(tasks):
        tasks.pop(index-1)
        print(blue(f"Task {index} has been removed."))
    else:
        print(red(f"Task {index} was not found."))

        
        
def mark_completed(index):
    if 1<=index<=len(tasks):
        tasks[index-1]["completed"]=True
        print(blue(f"Task {index} marked as completed"))
    else:
        print(red("Invalid task index"))
        
while True:
    print(green("\nOptions"))
    print("1. Add a task")
    print("2. List tasks")
    print("3. Delete a task")
    print("4. Mark as completed")
    print("5. Exit")
    
    choice=input("Enter your choice from 1 to 5: ")
    
    if choice=="1":
        task=input("Enter the task: ")
        add_task(task)
        
    elif choice=="2":
        list_tasks()
        
    elif choice=="3":
        list_tasks()
        delete_task()
    
    elif choice=="4":
        list_tasks()
        index=int(input("Enter the task number: "))
        mark_completed(index)
    
    elif choice=="5":
        print(red("Goodbye!!"))
        break
    
    else:
        print(red("Invalid Choice!! Please choose between 1,2,3,4 or 5: "))
    
    