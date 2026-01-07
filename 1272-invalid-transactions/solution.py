class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        #step 1 parse the input 
        transactions_by_name = defaultdict(list)
        invalid_indices = set()

        for index,transactions_str in enumerate(transactions):
            name , time_str , amt_str , city = transactions_str.split(",")
            time = int(time_str)
            amount = int(amt_str)
        # step 2 check the validity of the ones with an amount higher than 1000
            if amount > 1000:
                invalid_indices.add(index)
        # step3: check if the person had other transactions under same name under 60 mins
                # invalid if: same name, different city, within 60 minutes
            for prev_t,prev_c,prev_i in transactions_by_name[name]:
                if prev_c != city and abs(prev_t - time) <= 60:
                    invalid_indices.add(prev_i)
                    invalid_indices.add(index)
            
            transactions_by_name[name].append((time, city, index))

        return [transactions[i] for i in invalid_indices ]

