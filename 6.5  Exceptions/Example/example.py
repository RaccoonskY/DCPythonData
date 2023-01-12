# import traceback to get stack on exception handling

user_input = input("Enter text to write to the new file: ")
new_filename = input("Enter the name of new file: ")


def error_handling_input(user_input: str, new_filename: str):
    try:
        with open(new_filename, "x") as f:
            f.write(user_input)
    except FileExistsError as err:
        print(err)
        print(f"File '{new_filename}' is already exists, please, try again")
    except OSError as err:
        print(err)
    except Exception as err:
        print("Unknown error occurred!")
        print(err)


error_handling_input(user_input, new_filename)
