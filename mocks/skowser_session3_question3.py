import heapq
import sys

def cpu_tasks(tasks, n):

    task_counts = get_counts(tasks)
    heap = []

    for task in task_counts:
        # multiply by -1 since pop() gives us min val
        heapq.heappush(heap, (-1 * task_counts[task], task))

    cool_down = {}
    time = 0
    tasks_completed = 0

    while True:
        if len(heap) > 0:
            neg_count, task = heapq.heappop(heap)
            task_counts[task] -= 1
            tasks_completed += 1

            if task_counts[task] > 0:
                cool_down[task] = time

        else:
            if tasks_completed == len(tasks):
                return time

        for task in cool_down:
            time_in = cool_down[task]
            if time - time_in == n:
                heapq.heappush(heap, (-1 * task_counts[task], task))
        time += 1

def get_counts(tasks):
    counts = {}
    for task in tasks:
        if task not in counts:
            counts[task] = 0
        counts[task] += 1
    return counts

print(cpu_tasks(["A", "A", "A","A", "A", "A", "B", "C", "D", "E", "F", "G"], 3))