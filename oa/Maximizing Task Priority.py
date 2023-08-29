### TikTok Round 1 
def maxPrioritySum(priority, x, y):
      priority.sort(reverse = True)
      res = 0
      res += y//x * sum(priority[:min(len(priority), x)])
      res += sum(priority[:min(len(priority), y%x)])
      return res