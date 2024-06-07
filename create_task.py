def create_task() :
    with open('tasks.txt', 'a') as taskFile :
        newTaskName = input("Write the name of your task : ");
        newTaskInfo = input("Write details of your task: ");
        newTaskDate = input("Write the date and time for the task: ");
        newTaskLocation = input("Write the location for your task: ");
        taskFile.write(newTaskName + '\n');
        taskFile.write(newTaskInfo + '\n');
        taskFile.write(newTaskDate + '\n');
        taskFile.write(newTaskLocation + '\n');

create_task();
