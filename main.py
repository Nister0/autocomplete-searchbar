import os

class search:
    def __init__(self, file):
        '''
        intitialize class, open given file and save it to self.data
        '''
        def open_file():
            if not os.path.exists(file):
                raise Exception(f"path '{file}' does not exist") 
            if not os.path.isfile(file):
                raise Exception(f"there is no such file: '{file}'")

            dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(dir, file)

            with open(file_path, "r+") as f:
                self.data = f.read()
                
            return 0
        
        def divide_data():
            divData = ()
            j = 0
            for i in data:
                if i == " ":
                    j += 1
                else:
                    divData[j] = divData[i] + i 
                    j += 1

            data = divData

