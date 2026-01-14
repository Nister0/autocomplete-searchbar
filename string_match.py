class match:
    '''
    handles which words will be suggested
    '''

    def __init__(self, dictionary: list[str]):
        self.dictionary : list[str] = dictionary 
        suggestions : list[str] = self.sort()

    def sort(self, input: str) -> dict[str, float]:
        '''
        sorts data word list based on input, sorted by match % to give the highest matching words.
        '''

        output : list[tuple[str, float]] = ()

        for i in self.dictionary:
            output.append((i, self._match(input, i)))

        return self._mergesort(output)


    def _match(self, pattern: str, word: str) -> float:
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

    def _mergesort(self, matched_words : list[tuple[str, float]]) -> list[tuple[str, float]]:
        '''
        Simple mergesort for this specific case.
        '''

        if len(matched_words) <= 1:
            return matched_words
        xs = ()
        ys = ()
        nmw = len(matched_words) - 1

        xs = matched_words[0 : nmw//2]
        ys = matched_words[nmw//2: nmw]

        l = self._mergesort(xs)
        r = self._mergesort(ys)

        return self._merge(l, r)
    
    def _merge(self, l : list[tuple[str, float]], r : list[tuple[str, float]]): 
        '''
        subfunction for merge sort. merges two lists.
        '''

        xs = []
        while l and r:
            if l[0][1] >= r[0][1]:
                xs.append(l.pop(0))
            else:
                xs.append(r.pop(0))

        if l:
            xs.append(l[0:(len(l))])
        if r:
            xs.append(r[0:(len(r))])

        return xs

if __name__ == "__main__": 
    s = match([""])
    print(s._match("allo", "hallo")) 

