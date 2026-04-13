class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        map_tr = defaultdict(list)
        res = set()
        for i,tran in enumerate(transactions):
            name,time,amount,city = tran.split(",")
            time = int(time)
            amount = int(amount)
            map_tr[name].append((time,amount,city,i))
            if amount > 1000:
                res.add(i)
            for k in map_tr[name]:
                t,amt,c,index = k
                if abs(t - time) <= 60 and c != city:
                    res.add(index)
                    res.add(i)
        return [transactions[i] for i in res]
            
