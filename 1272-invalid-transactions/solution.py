class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        my_map = defaultdict(list)
        res = set()
        for i in range(len(transactions)):
            name,time,amount,city = transactions[i].split(",")
            time = int(time)
            amount = int(amount)
            if amount > 1000:
                res.add(i)
            my_map[name].append([time,amount,city,i])
            for t, a, c, index in my_map[name]:
                if abs(t - time) <= 60 and c != city:
                    res.add(index)
                    res.add(i)
        return [transactions[i] for i in res]


