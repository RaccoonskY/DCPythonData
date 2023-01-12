text = """Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 

Aenean commodo ligula eget dolor. Aenean massa. 

Cum sociis natoque penatibus et"""


def get_str_list(text):
    str_lit = text.split()
    list = []
    for word in str_lit:
        clean_word = word.strip(",.").lower()
        if clean_word not in str_lit:
            list.append(clean_word)
    return list


goal_list = get_str_list(text)
print(goal_list)
