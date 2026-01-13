import string_match
import dictionary as dict_module

class autcomplete:
    def __init__(self, data_set: str):
        dm = dict_module.dictionary(data_set)
        sm = string_match.match(dm.data)
        word = sm.match()

    def suggestion(self):
        pass


if __name__ == "__main__":
    pass 