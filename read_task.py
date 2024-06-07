def read_task() :
    with open('F:/Code Platton/Day 3/Team_Project_Phone_Terminal/httpsresponse18/tasks.txt', 'r') as taskFile :
        task_contents = [];
        for line in taskFile:
            task_contents.append(line.strip());
        print(f"Task Info: {task_contents}");

read_task();