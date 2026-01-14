import string_match
import dictionary as dict_module

class autcomplete:
    def __init__(self, pattern : str):
        self.dm = dict_module.dictionary(pattern)
        self.sm = string_match.match()

    def suggest(self, pattern : str):
        data_set = self.sm.fast_forward(pattern, self.dm.data)

        data_set = list(filter(lambda t: t[1] != 0, data_set)) #removes all non matching words.

        return data_set

if __name__ == "__main__":
    ac = autcomplete("files/lexikon.txt")
    for i in ac.suggest("alle"):
        print(i)