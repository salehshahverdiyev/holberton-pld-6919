import argparse
import cmd


class Task:
    task_id = 0

    def __init__(self, title : str, description : str, completed : bool = False):
        Task.task_id += 1
        self.title = title
        self.description = description
        self.completed = completed
        self.task_idd = Task.task_id

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        return f"{self.task_idd} {self.description} {self.completed}"

class TaskManager:
    def __init__(self, tasks : dict = {}):
        self.tasks = tasks

    def add_task(self, title, description):
        new = Task(title, description)
        self.tasks[new.task_idd] = new

    def remove_task(self, task_idd):
        self.tasks.pop(int(task_idd))

    def mark_task_completed(self, id):
        self.tasks[int(id)].mark_as_completed()

    def list_tasks(self):
        for k, v in self.tasks.items():
            print(v)

    def find_task(self, task_idd):
        for key, value in self.tasks.items():
            if key == int(task_idd):
                return value

class CLI(cmd.Cmd):
    manager = TaskManager()

    def do_add(self, arg):
        parser = argparse.ArgumentParser(description='What the program does')
        parser.add_argument('--title',help='title of task')
        parser.add_argument('--desc',help='desc of task')
        args = parser.parse_args(arg.split())
        CLI.manager.add_task(args.title, args.desc)

    def do_get_all(self, arg):
        CLI.manager.list_tasks()

    def do_find(self, arg):
        parser = argparse.ArgumentParser(description='What the program does')
        parser.add_argument('--id',help='id of task')
        args = parser.parse_args(arg.split())
        print(CLI.manager.find_task(args.id))

    def do_remove(self, arg):
        parser = argparse.ArgumentParser(description='What the program does')
        parser.add_argument('--id',help='id of task')
        args = parser.parse_args(arg.split())
        CLI.manager.remove_task(args.id)

    def do_complete(self, arg):
        parser = argparse.ArgumentParser(description='What the program does')
        parser.add_argument('--id',help='id of task')
        args = parser.parse_args(arg.split())
        CLI.manager.mark_task_completed(args.id)

if __name__ == "__main__":
    CLI().cmdloop()
