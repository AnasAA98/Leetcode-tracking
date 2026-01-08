class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions_name = defaultdict(list)
        invalid_indices = set()
        for index, transactions_str in enumerate(transactions):
            name, time_str, amount_str, city = transactions_str.split(",")
            time, amount = int(time_str), int(amount_str)
            if amount > 1000:
                invalid_indices.add(index)
            for prev_t, prev_c, prev_i in transactions_name[name]:
                if prev_c != city and abs(prev_t - time) <= 60:
                    invalid_indices.add(index)
                    invalid_indices.add(prev_i)

            transactions_name[name].append((time, city, index))
        return [transactions[i] for i in invalid_indices]

