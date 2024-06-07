def delete_task() :
    with open('tasks.txt', 'w') as taskFile :
        taskFile.write('');

delete_task();
print('Tasks have been deleted!')