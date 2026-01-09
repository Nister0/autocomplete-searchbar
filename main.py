import os

class search:
    def __init__(self, file):
        '''
        intitialize class, open given file and save it to self.data
        '''
        self.data = self.divide_data(self.open_file(file))

        if not self.data:
            raise Exception("File is empty.")

    def open_file(self, file):
        dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(dir, file)

        if not os.path.exists(file_path):
            raise Exception(f"file: '{file}' does not exist") 
        if not os.path.isfile(file_path):
            raise Exception(f"there is no file: '{file}' in the path '{file_path}")

        with open(file_path, "r+") as f:
            data = f.read()
            
        return data
    
    def divide_data(self, data):
        divData = []
        divData.append("")
        #print(data)
        j = 0
        for i in data:
            if i == " ":
                divData.append("")
                j += 1
            else:
                divData[j] = divData[j] + i

        while divData and divData[-1] == "":
            divData.pop(-1)
            
        return divData

    def print_data(self):
        for i in self.data:
            print(i, end=" ")
        print()

if __name__ == "__main__":
    s = search("lexikon.txt")
    s.print_data()