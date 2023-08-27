### Akuna Captial Round 2 
import collections
import math
class Solution:
    def __init__(self):
        self.stocks_by_date = collections.defaultdict(list)
        self.all_dates = []
        self.dp = []
    def add_trade(self, future_trade: List):
        # Reformatting the date to 'YYYY/MM/DD' with double digits so that we can sort the dates in
        # increasing order later
        date = list(future_trade[1].split("/"))        
        new_date = date[2] + "/"
        new_date += "0" + date[0]+ "/" if int(date[0]) < 10 else date[0] + "/"
        new_date += "0" + date[1] if int(date[1]) < 10 else date[1]  
        
        # add the date to the list so we can iterate later
        if new_date not in self.stocks_by_date:
            self.all_dates.append(new_date)
            
            # create the dynamic list for dp solution
            self.dp.append(0)
        
        # store all the stocks grouped by day
        self.stocks_by_date[new_date].append((future_trade[0], float(future_trade[2])))
        

    def run(self):
        # sort all the dates
        self.all_dates.sort()
        
        # iterate through the dates
        for index, date in enumerate(self.all_dates):
            
            # get all the stocks of that day
            stocks = self.stocks_by_date[date]
            
            # initialize the dp list to the last day (in case we don't do anything), or 0 (if it is the first day)
            temp = 0 if index == 0 else self.dp[index - 1]
            for stock in stocks:
                # get each day in the range of the current day
                for idx in range(index):                  
                    day = self.all_dates[idx]
                    
                    # get all the stocks of that day
                    for item in self.stocks_by_date[day]:
                        
                        # check if the stock we are looking at is available on that day
                        if stock[0] == item[0]:
                            
                            # update the dp value to if we all-in on that day and sell all today
                            temp =  max(temp, self.dp[idx] + (self.dp[idx] + 1000)/item[1] * (stock[1] -item[1])) if idx != 0 else max(temp, 1000/item[1] * (stock[1] -item[1]))
            
            #update the dp to the maximum strategy up to today               
            self.dp[index] = temp
        
        # return best strategy
        return round(self.dp[-1])
            
        
if __name__ == '__main__':
    solution = Solution()
    for row in fileinput.input():
        future_trade = list(row.strip().replace(" ", "").split(","))
        solution.add_trade(future_trade)
        
    print(solution.run())