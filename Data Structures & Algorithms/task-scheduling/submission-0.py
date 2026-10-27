class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for task in tasks:
            counts[task] = counts.get(task, 0) + 1
        
        maxf = max(counts.values())
        num_max = sum(1 for c in counts.values() if c == maxf)

        return max(len(tasks), (maxf - 1) * (n + 1) + num_max)