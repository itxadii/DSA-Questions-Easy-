class taskmanager():
    def __init__(self):
        self.checklist = set()
        self.Completed = set()
        self.notcompleted = set()

    def addtask(self ,task):
        self.checklist.add(task)
    def mark_task(self, task, completed=True):
        if task in self.checklist:
            if completed:
                self.Completed.add(task)
            else:
                self.notcompleted.add(task)
    def show(self):
        print("\nCompleted Tasks:")
        for tasks in self.Completed:
            print(f"-{tasks}")
        print("\nIncomplete Tasks:")
        for tasks in self.notcompleted:
            print(f"-{tasks}")
tm = taskmanager()

tm.addtask("task")
tm.addtask("none")

tm.mark_task("task", True)
tm.mark_task("none", False)

tm.show()

