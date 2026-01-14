class match:
    '''
    handles which words will be suggested
    '''

    def __init__(self):
        self.dictionary = []

    def fastforward(self, pattern : str, dictionary: list[str]) -> list[tuple[str, float]]:
        self.dictionary = dictionary
        return self.sort(pattern)

    def sort(self, pattern: str) -> dict[str, float]:
        '''
        sorts data word list based on input, sorted by match % to give the highest matching words.
        '''

        output : list[tuple[str, float]] = []

        for i in self.dictionary:
            output.append((i, self._match(pattern, i)))

        return self._mergesort(output)


    def _match(self, pattern: str, dictionary: str) -> float:
        '''
        calculates % of matching letters. if str in input: % < 0 else: % = 0.
        this could be done easier with with python inbuilt functions.
        '''

        j = 0
        for i in range(len(dictionary)):
            if len(dictionary) < len(pattern):
                return 0
            
            if dictionary[i] != pattern[j]:
                j == 0
            else:
                j += 1
            dictionary[0:]
            '''
            fix later not working correctly when pattern len == dict len.
            '''
            
        return len(pattern) / len(dictionary)

    def _mergesort(self, matched_words : list[tuple[str, float]]) -> list[tuple[str, float]]:
        '''
        Simple mergesort for this specific case.
        '''

        if len(matched_words) <= 1:
            return matched_words
        
        # split in half (use proper midpoint so no element is dropped)
        mid = len(matched_words) // 2
        xs = matched_words[:mid]
        ys = matched_words[mid:]

        l = self._mergesort(xs)
        r = self._mergesort(ys)

        return self._merge(l, r)
    
    def _merge(self, l : list[tuple[str, float]], r : list[tuple[str, float]]) -> list[tuple[str, float]]: 
        '''
        subfunction for merge sort. merges two lists.
        '''

        xs = []
        while l and r:
            if l[0][1] >= r[0][1]:
                xs.append(l.pop(0))
            else:
                xs.append(r.pop(0))

        # append remaining elements (extend, not append, to avoid nested lists)
        if l:
            xs.extend(l)
        elif r:
            xs.extend(r)

        return xs

if __name__ == "__main__": 
    s = match()
    print(s.fastforward("hallo",["halloooo"])) 

