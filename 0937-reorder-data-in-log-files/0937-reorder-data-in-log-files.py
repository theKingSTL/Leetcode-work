class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
                # if not logs:
        #     return []
        
        digits = []
        letters = []

        for log in logs:
            identifier, rest = log.split(" ", 1)
            if rest[0].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        letters.sort(key=lambda log: (log.split(" ", 1)[1], log.split(" ", 1)[0]))

        return letters + digits