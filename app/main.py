import sys
import os


def main():
    while True:
        sys.stdout.write("$ ")

        command = input()
        if command == "exit":
            break

        if command.startswith("echo"):
            print(command[5:])

        elif command.startswith("type"):
            arg = command[5:]
            if arg in ["echo", "type", "exit"]:
                print(f"{arg} is a shell builtin")

            
            else:
                path_dirs = os.environ.get("PATH", "").split(os.pathsep)

                for directory in path_dirs:
                    full_path = os.path.join(directory, arg)

                    if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                        print(f"{arg} is {full_path}")
                        break
                else:
                    print(f"{arg}: not found")

        else: 
            print(f"{command}: command not found")

    


if __name__ == "__main__":
    main()
