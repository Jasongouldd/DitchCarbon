
def binarySearch(array, priority, part, low, high):
    """Searches for where the priority would be indexed in the current queue"""
    result = -1 
    while low <= high:
        mid = (low+high) // 2
        
        if priority == array[mid][part]:
            result = mid
            high = mid - 1 
        elif priority < array[mid][part]:
            high = mid - 1
        else:
            low = mid + 1
            
    return result if result != -1 else low

def binarySearchLastInstance(array, priority, part, low, high):
    """Searches for where the last instance of the priority in the current queue"""
    last_instance_index = None
    
    while low <= high:
        mid = (low + high) // 2

        if priority == array[mid][part]:
            last_instance_index = mid
            if last_instance_index == len(array)-1:
                return last_instance_index
            else:
                low = mid + 1
        
        elif priority < array[mid][part]:
            high = mid - 1
        else:
            low = mid + 1

    return last_instance_index

def binary_search_reverse(arr, deadline,part):
    """Searches for where the deadline would be indexed in the current queue"""
    low, high = 0, len(arr) - 1
    result = 0 if arr[low][part]<deadline else high+2 if arr[-1][part]>deadline else -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid][part] == deadline:
            result = mid
            high = mid - 1 
        elif arr[mid][part] < deadline:
            high = mid - 1
        else:
            low = mid + 1
            
    return (mid if deadline > arr[mid][2] else mid+1) if result==-1 else result

def binary_search_reverse_last_instance(arr, deadline,part):
    """Searches for where the last instance of the deadline in the current queue"""
    low, high = 0, len(arr) - 1
    last_instance_index = None
    while low <= high:
        mid = (low + high) // 2

        if arr[mid][part] == deadline:
            last_instance_index = mid
            if last_instance_index == len(arr)-1:
                return last_instance_index
            else: 
                low = mid + 1  # Change low to continue searching in the right half for the last occurrence
        elif arr[mid][part] < deadline:
            high = mid - 1
        else:
            low = mid + 1

    return last_instance_index

class TaskScheduler:
    def __init__(self,task_queue=None):
        self.task_queue = []

    def add_task(self, name, priority=0, deadline=None):
        """Adds a task to the task_queue, first based on priority then deadline.
        If a task has the same priority and deadline then the task goes behind the 
        last task with the same priority/deadline"""

        if type(name)!=str or deadline == None:
            # checks to make sure the task name is a string and deadline has an input
            return None
        
        else:
            high = len(self.task_queue)
            task = [name, priority, deadline]

            if self.count_tasks() == 0: # handling edge case where the queue is empty
                self.task_queue.insert(high,task)

            elif self.task_queue[-1][1]<priority: # handling edge case where task can be added directly to the end of the queue
                self.task_queue.insert(high,task)

            else:
                inst1 = binarySearch(self.task_queue, priority, 1, 0,high)
                inst2 = binarySearchLastInstance(self.task_queue, priority, 1, 0,high)

                if inst1 == inst2: # checks to see if there is only one instance of task in the task queue with the same priority
                    if self.task_queue[inst1][2]>deadline:
                        self.task_queue.insert(inst1+1,task)
                    else:
                        self.task_queue.insert(inst1,task)

                elif inst2 == None: # checks to see if there are no instances of a task in the task queue with the same priority
                    self.task_queue.insert(inst1,task)

                else: # multiple instances of tasks with the same priority in the queue, so need to look at deadline

                    inst3 = binary_search_reverse(self.task_queue[inst1:inst2], deadline , 2)
                    inst4 = binary_search_reverse_last_instance(self.task_queue[inst1:inst2], deadline, 2)

                    if inst4 == None: # checks to see if there are no instances of a task in the task queue with the same deadline
                        self.task_queue.insert((inst1 + inst3),task)
                    
                    else: # multiple instance of tasks with the same priority in the queue, so the new tasks gets added to the end
                        self.task_queue.insert((inst1 + inst3),task)

    def execute_task(self):
        """Executes the task with the highest priority and nearest deadline
           and removes the executed task from the queue
           Input: List of tasks with priority and deadline
        """
        if self.count_tasks() == 0:
            return self.task_queue
        
        else:
            executed_task = self.task_queue[-1]
        
        #performing task
        
            self.task_queue.remove(executed_task)
            return executed_task[0]

    def get_next_task(self):
        """Returns the name of the next task in the queue
           Input: List of tasks with deadline and priority
        """
        return self.task_queue[-1][0] if self.count_tasks() > 0 else []

    def get_task_queue(self):
        """Returns a list of task names in the order of how they are in the queue
           Input: List of tasks with deadline and priority
        """
        task_names = []
        for tasks in reversed(self.task_queue):
            task_names.append(tasks[0])
        return task_names

    def count_tasks(self):
        """Returns how many tasks are in the queue
           Input: List of tasks with deadline and priority
        """
        return len(self.task_queue)


