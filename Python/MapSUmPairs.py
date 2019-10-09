class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def insert(self, key: str, val: int) -> None:
        if key in self.dic.keys():
            self.dic.update({key: val})
        else:
            self.dic.update({key: val})

    def sum(self, prefix: str) -> int:
        result = 0
        n = len(prefix)
        for key, value in self.dic.items():
            if key[0: n] == prefix:
                result += value
        return result

    # Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)