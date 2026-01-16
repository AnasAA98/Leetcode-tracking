class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        map_names = {}  # string name : (time,amount,city,index)
        invalid_indices = set() # set of all invalid indicies 
        for index,transaction in enumerate(transactions):
            name,time,amount,city = transaction.split(',')
            time, amount = int(time), int(amount)
            if amount >1000:
                invalid_indices.add(index)
            if name not in map_names:
                map_names[name] = []
            for t,a,c,i in map_names[name]:
                if c != city and abs(t - time) <= 60:
                    invalid_indices.add(index)
                    invalid_indices.add(i)
            map_names[name].append((time,amount,city,index))
        
        return [transactions[i] for i in invalid_indices]

