class FileManager:
    def write(name, data, end='\n'):
        file = open(name, "a")
        file.write(data + end)
        file.close()