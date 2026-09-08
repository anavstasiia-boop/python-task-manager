def save_tasks(tasks):

    with open("tasks.txt", "w") as file:
        for task in tasks:
            name, priority, completed = task
            file.write(f"{name},{priority},{completed}\n")


def load_tasks():
    tasks = []
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                parts = [p.strip() for p in line.strip().split(",")]
                if len(parts) == 1:
                    tasks.append((parts[0], 2, False))
                else:
                    name, priority, completed = parts

                    mapping = {"high": 1, "medium": 2, "low": 3}
                    p = priority.strip()

                    if p.isdigit():
                        priority_num = int(p)
                    else:
                        priority_num = mapping.get(p.lower(), 2)

                    tasks.append((name, priority_num, completed == "True"))
    except FileNotFoundError:
        pass

    return tasks