def delete_task() :
    with open('F:/Code Platton/Day 3/Team_Project_Phone_Terminal/httpsresponse18/tasks.txt', 'w') as taskFile :
        taskFile.write('');

delete_task();
print('Tasks have been deleted!')