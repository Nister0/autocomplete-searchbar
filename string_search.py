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
        words : list[str]= self.words 
        output : dict[str, float] = {}

        for i in words:
            output[i] = self.match(input, i)

        return output


    def match(self, pattern:str, word:str) -> float:
        '''
        calculates % of matching letters. if str in input: % < 0 else: % = 0.
        '''

        if len(word) < len(pattern):
            return 0
        
        for i in word: 



