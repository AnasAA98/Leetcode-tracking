class Solution:
    def equalFrequency(self, word: str) -> bool:
        # Map of each character to how many times it appears
        # Ex: "aabbc" -> {'a': 2, 'b': 2, 'c': 1}
        char_counts = Counter(word)

        # A "meta-count": How many characters share the same frequency?
        # Ex: values are [2, 2, 1] -> {2: 2, 1: 1}
        # Meaning: 2 characters appear twice, 1 character appears once.
        frequency_distribution = Counter(char_counts.values())

        # --- SCENARIO 1: All characters already have the same frequency ---
        if len(frequency_distribution) == 1:
            common_frequency = next(iter(frequency_distribution))
            
            # Valid if:
            # 1. Every character appears exactly once (e.g., "abc"). Remove any to get empty/valid state.
            # 2. There is only one unique character type (e.g., "zzzz"). Remove one 'z', still valid.
            return common_frequency == 1 or len(char_counts) == 1

        # --- SCENARIO 2: We have complex frequencies ---
        # If we have more than 2 different frequency counts, we can't fix it by removing just 1 char.
        if len(frequency_distribution) != 2:
            return False

        # Unpack the two frequency states
        # items() gives us pairs of (frequency_value, how_many_chars_have_it)
        (freq_val_1, char_count_1), (freq_val_2, char_count_2) = frequency_distribution.items()

        # Case A: One character appears exactly once (freq 1). 
        # If we remove it entirely, the remaining characters (which all share the other frequency) are valid.
        # Ex: "aabbc" -> remove 'c' -> "aabb" (valid)
        if (freq_val_1 == 1 and char_count_1 == 1):
            return True
        if (freq_val_2 == 1 and char_count_2 == 1):
            return True

        # Case B: One group of characters appears 1 time more than the other group.
        # And there is ONLY ONE character in that "higher" group.
        # If we remove one instance of that character, it drops down to match the others.
        # Ex: "aabbccc" -> 'c' appears 3 times, others appear 2 times. Remove one 'c'.
        if abs(freq_val_1 - freq_val_2) == 1:
            if (freq_val_1 > freq_val_2 and char_count_1 == 1):
                return True
            if (freq_val_2 > freq_val_1 and char_count_2 == 1):
                return True

        return False
