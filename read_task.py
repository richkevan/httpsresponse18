def read_task() :
    with open('tasks.txt', 'r') as taskFile :
        task_contents = [];
        for line in taskFile:
            task_contents.append(line.strip());
        print(f"Task Info: {task_contents}");

read_task();