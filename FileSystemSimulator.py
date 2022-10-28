class Tree:

    def __init__(self, name, root):
        self.name = name
        self.root = root
        self.directories = list()
        self.files = list()

    def add_directory(self, name):
        new_dir = Tree(name, self)
        self.directories.append(new_dir)

    def add_file(self, name):
        self.files.append(name)

    def get_dir_names(self):
        dir_names = []
        for dir in self.directories:
            dir_names.append(str(dir.name))
        return dir_names

    def get_dir_and_file_names(self):
        return self.get_dir_names() + self.files


class FileSystem:

    def __init__(self):
        self.root = Tree("Home", None)
        self.current = self.root
        print("File system initiated")
        print("Home is current and root directory")

    def ls(self):
        curr_dir_and_file_names = self.current.get_dir_and_file_names()
        curr_dir_and_file_names.sort()
        self.print_directories_and_files(curr_dir_and_file_names)

    def mkdir(self, name):
        if not self.is_directory_name_valid(name):
            print("Error: Invalid directory name: {}".format(name))
        elif name in self.current.get_dir_and_file_names():
            print("Error: mkdir: {}: File/directory exists".format(name))
        else:
            self.current.add_directory(name)

    def touch(self, name):
        if not self.is_file_name_valid(name):
            print("Error: Invalid file name: {}".format(name))
        elif name in self.current.get_dir_and_file_names():
            print("Error: touch: {}: File/directory exists".format(name))
        else:
            self.current.add_file(name)

    def cd(self, full_path=None):

        # Use temp_current to hold current position and change directories.
        temp_current = self.current

        if full_path is None:
            self.current = self.root

        elif self.is_path_valid(full_path):

            path = full_path.split("/")

            path_incorrect = False

            # change directory for every item in path
            for item in path:

                if path_incorrect:
                    break
                if item == "." or "":
                    pass
                elif item == "..":
                    if temp_current.root is None:
                        path_incorrect = True
                        print("Error cd: no such directory: {}".format(full_path))
                    else:
                        temp_current = temp_current.root
                else:
                    directories = temp_current.directories
                    child_found = False
                    # check if directory name matches the item in path
                    for dir in directories:
                        if dir.name == item:
                            child_found = True
                            temp_current = dir
                            break
                    if not child_found:
                        path_incorrect = True
                        print("Error cd: no such directory: {}".format(full_path))

            # If all directories found correct and changed, assign temp_current value to current directory
            self.current = temp_current

        else:
            print("Error cd: no such directory: {}".format(full_path))

    def is_directory_name_valid(self, directory_name):

        valid_directory_chars = [
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
            "r", "s", "t", "u", "v", "w", "x", "y", "z",
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "H", "L", "M", "N", "O",
            "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
        ]

        dir_chars = [x for x in directory_name]
        invalid_chars = self.list_diff(dir_chars, valid_directory_chars)
        if invalid_chars:
            return False
        else:
            return True

    def is_file_name_valid(self, file_name):

        valid_directory_chars = [
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
            "r", "s", "t", "u", "v", "w", "x", "y", "z",
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "H", "L", "M", "N", "O",
            "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
            "."
        ]

        dir_chars = [x for x in file_name]
        invalid_chars = self.list_diff(dir_chars, valid_directory_chars)
        if invalid_chars:
            return False
        else:
            return True

    def is_path_valid(self, path):

        valid_path_chars = [
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
            "r", "s", "t", "u", "v", "w", "x", "y", "z",
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "H", "L", "M", "N", "O",
            "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
            "/", "."
        ]

        path_chars = [x for x in path]
        invalid_chars = self.list_diff(path_chars, valid_path_chars)

        if invalid_chars:
            return False
        else:
            return True

    @staticmethod
    def print_directories_and_files(dir_file_names):
        for item in dir_file_names:
            print(item)

    @staticmethod
    def list_diff(first_list, second_list):
        second_set = set(second_list)
        return [item for item in first_list if item not in second_set]


if __name__ == "__main__":

    fileSystem = FileSystem()

    print("Perform one of the following operations")
    print("1. ls, 2. cd, 3. mkdir, 4. touch")
    print("Type q to exit")

    while True:

        user_input = input("{}: ".format(fileSystem.current.name))
        user_input = user_input.strip()

        if user_input == "q":
            print("File system destroyed....!")
            break

        elif user_input == "ls":
            fileSystem.ls()

        elif user_input.startswith("cd"):
            if user_input == "cd":
                fileSystem.cd()
            else:
                if user_input.startswith("cd "):
                    arg = user_input[3:]
                    fileSystem.cd(arg)
                else:print("command not found: {}".format(user_input))

        elif user_input.startswith("touch "):
            arg = user_input[6:]
            fileSystem.touch(arg)

        elif user_input.startswith("mkdir "):
            arg = user_input[6:]
            fileSystem.mkdir(arg)

        else:
            print("command not found: {}".format(user_input))
