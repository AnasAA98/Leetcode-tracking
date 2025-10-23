class Solution:
    def defangIPaddr(self, address: str) -> str:
        temp = address.replace(".","[.]")
        return temp
