class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        read_idx = 0
        write_idx = 0
        while read_idx < n:
            end_idx = read_idx + 1
            while end_idx < n and chars[read_idx] == chars[end_idx]:
                end_idx+=1
            chars[write_idx] = chars[read_idx]
            write_idx +=1
            size = end_idx - read_idx
            if size > 1:
                for c in str(size):
                    chars[write_idx] = c
                    write_idx+=1
            read_idx = end_idx
        return write_idx
                
