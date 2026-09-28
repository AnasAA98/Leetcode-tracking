class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        map_n = defaultdict(list)
        res = set()
        for index,transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(",")
            time = int(time)
            amount = int(amount)
            if amount > 1000:
                res.add(index)
            map_n[name].append((time,amount,city,index))
            for k in map_n[name]:
                t,a,c,i = k
                if abs(t - time) <= 60 and c != city:
                    res.add(i)
                    res.add(index)
        return [transactions[i] for i in res]


