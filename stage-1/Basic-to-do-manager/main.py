# Simple CLI To-Do Manager using conditionals and list operations
"""
Author: Albino Mareleco
"vetor confirmado"
"""
todo=[]
print("""Ready

Commands available: add, remove, view, stats, quit""")

while True:
    cmd=input("Command: ").strip().lower()
    match cmd:
        case "add":
            item=input("Task: ").strip()
            if item and "," in item:
                todo.extend([i.strip() for i in item.split(",")]); print("Added")
            elif item:
                todo.append(item); print("Added")
            else:
                print("Empty ignored")
        case "remove":
            item=input("Remove: ").strip()
            if item in todo:
                todo.remove(item); print("Removed")
            else:
                if todo:
                    popped=todo.pop(); print("Fallback removed",popped)
                else:
                    print("Empty list")
        case "view":
            if todo:
                print(todo, todo[:3])
            else:
                print("No tasks")
        case "stats":
            if len(todo)==0:
                print("No tasks")
            elif len(todo)<3:
                print("Few:",len(todo))
            else:
                print("Many:",len(todo),todo[:2])
        case "quit":
            print("Bye")
            break
        case _:
            print("Unknown")