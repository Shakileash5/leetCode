class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for i in tasks:
            freq[ord(i)-ord("A")] += 1
        freq.sort(reverse=True)
        idleBlocks = freq[0]-1
        idle = idleBlocks * n

        for i in range(1,26):
            idle -= min(freq[i], idleBlocks)

        return len(tasks) + max(idle, 0)