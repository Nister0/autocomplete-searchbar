import string_match
import dictionary as dict_module

class autcomplete:
    def __init__(self, data_set : str):
        self.dm = dict_module.dictionary(data_set)
        self.sm = string_match.match()

    def suggest(self, pattern : str):
       return self.sm.fastforward(pattern, self.dm.data)

if __name__ == "__main__":
    ac = autcomplete("files/lexikon.txt")
    for i in ac.suggest("ralle"):
        print(i)