class search:
    '''
    handles which words will be suggested
    '''
    def __init__(self, words: list[str]):
        self.words = words 

    def sort(self, input: str) -> dict[str, float]:
        '''
        sorts data word list based on input, sorted by match % to give the highest matching words.
        '''
        words : list[str] = self.words 
        output : dict[str, float] = {}

        for i in words:
            output[i] = self.match(input, i)

        return output


    def match(self, pattern: str, word: str) -> float:
        '''
        calculates % of matching letters. if str in input: % < 0 else: % = 0.
        this could be done easier with with python inbuilt functions.
        '''
        j = 0
        for i in range(len(word)):
            if len(word) < len(pattern):
                return 0
            
            if word[i] == pattern[j]:
                word = word[0:]
                j += 1
                if j == len(pattern):
                    break
            
        return len(pattern) / len(word)


if __name__ == "__main__": 
    s = search([""])
    print(s.match("allo", "hallo"))