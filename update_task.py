def update_task() :
    with open('F:/Code Platton/Day 3/Team_Project_Phone_Terminal/httpsresponse18/tasks.txt', 'w') as taskFile :
        newTaskName = input("Write the new name of your task : ");
        newTaskInfo = input("Write your updated task details: ");
        newTaskDate = input("Write new date and time for your task: ");
        newTaskLocation = input("Write the new location for your task: ");
        taskFile.write(newTaskName + '\n');
        taskFile.write(newTaskInfo + '\n');
        taskFile.write(newTaskDate + '\n');
        taskFile.write(newTaskLocation + '\n');

update_task();