

def read_names(filename: str) -> list[str]:
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            lines = [i.rstrip("\n") for i in lines if i not in ("", "\n")]
            print(lines)
    except Exception as err:
        print(err)
    else:
        return lines
    finally:
        f.close()


def count_symbols(string_list: list[str]) -> int:
    count = 0
    try:
        for i in string_list:
            string_length = len(i)
            if string_length < 5:
                raise Exception(f"Length of {i}:{string_length} is less than 5!")
            count += string_length
    except Exception as err:
        print(err.args[0])
    else:
        print("Total symbols in names: ", count)
        return count


file_name = "names.txt"
count_symbols(read_names(file_name))
