class FileManager:
    def write(name, data, end='\n'):
        with open(name, "a") as file:
            file.write(data + end)