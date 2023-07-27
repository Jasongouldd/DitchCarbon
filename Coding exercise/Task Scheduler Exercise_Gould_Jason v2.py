import heapq

class TaskScheduler:
    def __init__(self,task_queue=None):
        self.task_queue = []
        self.id = 0

    def add_task(self, name, priority=0, deadline=None):
        """Adds a task to the task_queue, first based on priority then deadline.
        If a task has the same priority and deadline then the task goes behind the 
        last task with the same priority/deadline
        Approach: Through using heap (tree-based data structure) a priority queue is created, the priority input is negative
        bc the default is min heap and deadline is positive bc we want to order based on the nearest deadline to current time
        this data structure allows for tasks to be retrieved and inputed easily with a time complexity of O(logn)  
        """

        if type(name)!=str or deadline == None:
            # checks to make sure the task name is a string and deadline has an input
            return None
        else:
            heapq.heappush(self.task_queue, [-priority, deadline, self.id, name])
            self.id +=1 # added an id to decide tiebreaker if priority and deadline are the same 

    def execute_task(self):
        """Executes the task with the highest priority and nearest deadline
           and removes the executed task from the queue
           Approach: calls the count_tasks method and if the queue is empty returns None
           otherwise using heappop function the first task in the queue is removed and the name is returned
        """
        if self.count_tasks() == 0:
            return None
        
        else:
            executed_task = heapq.heappop(self.task_queue)
        
        #performing task

            return executed_task[3]

    def get_next_task(self):
        """Returns the name of the next task in the queue
           Approach: calls the count_tasks method and if the queue has tasks 
           returns the name of the first task in the queue otherwise returns None
        """
        return self.task_queue[0][3] if self.count_tasks() > 0 else None

    def get_task_queue(self):
        """Returns a list of task names in order of how they are in the queue
           Approach: Creates a copy of the queue and then iterates over the copy 
           removing the first task in the queue and appending the task name to the task_names list 
        """
        task_names = []
        copy = self.task_queue[:]
        for x in range(len(self.task_queue)):
            task_names.append(heapq.heappop(copy)[3])
        return task_names

    def count_tasks(self):
        """Returns how many tasks are in the queue 
           Approach: Calls the length function on the queue 
        """
        return len(self.task_queue)
    

scheduler = TaskScheduler()
scheduler.add_task("Task A", 3, 10)
scheduler.add_task("Task B", 5, 25)
scheduler.add_task("Task C", 5, 15)
scheduler.add_task("Task D", 5, 15)
scheduler.add_task("Task F", 5, 10)
scheduler.add_task("Task G", 11, 15)
scheduler.add_task("Task z", 11, 20)
scheduler.add_task("Task I", 11, 23)

print(scheduler.count_tasks())
print(scheduler.get_next_task())
print(scheduler.get_task_queue())
print(scheduler.execute_task())
print(scheduler.count_tasks())
print(scheduler.get_next_task())
print(scheduler.get_task_queue())