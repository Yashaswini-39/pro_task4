class Solution:
    def defangIPaddr(self, address: str) -> str:
        '''
        #Runtime: 36 ms, faster than 63.59% of Python3 online submissions for Defanging an IP Address.
        #Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Defanging an IP Address.
        return re.sub("\.","[.]",address)
        '''
        #Runtime: 28 ms, faster than 97.14% of Python3 online submissions for Defanging an IP Address.
        #Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Defanging an IP Address.
        i=0
        while i < len(address):
            if address[i] is ".":
                address = address[:i] + "[.]" + address[i+1:]
                i+=2
            i+=1
        return address
