class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        name_transaction = {}
        invalid_indices = set()
        for index,transaction in enumerate(transactions):
            name,time,amount,city = transaction.split(",")
            time,amount = int(time),int(amount)
            if amount > 1000:
                invalid_indices.add(index)
                
            if name not in name_transaction:
                name_transaction[name] = []
            for t,a,c,i in name_transaction[name]:
                if c != city and abs(t-time) <= 60:
                    invalid_indices.add(index)
                    invalid_indices.add(i)
            name_transaction[name].append((time,amount,city,index))
        return [transactions[i] for i in invalid_indices]

            
