listOfTask = []

def addTask(taskName):
    listOfTask.append(taskName);
    getTasksLists()

def getTasksLists(): 
    print(listOfTask)

addTask("weak up")
addTask("Go for the bath")
addTask("Learn python")