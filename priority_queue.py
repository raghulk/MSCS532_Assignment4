from heapsort import heapsort
import heapq

class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline
    
    def __lt__(self, other):
        return self.priority < other.priority

class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def insert(self, task):
        heapq.heappush(self.heap, task)
    
    def extract_min(self):
        if self.is_empty():
            return None
        return heapq.heappop(self.heap)
    
    def decrease_key(self, task_id, new_priority):
        for task in self.heap:
            if task.task_id == task_id:
                task.priority = new_priority
                heapq.heapify(self.heap)
                break
    
    def is_empty(self):
        return len(self.heap) == 0
    
# Example usage
if __name__ == "__main__":
    arr = [4, 10, 3, 5, 1]
    sorted_arr = heapsort(arr)
    print("Sorted array:", sorted_arr)
    
    pq = PriorityQueue()
    pq.insert(Task(1, 3, "10:00", "12:00"))
    pq.insert(Task(2, 1, "11:00", "13:00"))
    pq.insert(Task(3, 2, "09:00", "11:30"))
    print("Extracted task with highest priority:", pq.extract_min().task_id)
    pq.decrease_key(3, 0)
    print("Extracted task with new highest priority:", pq.extract_min().task_id)
