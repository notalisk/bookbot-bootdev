def count_words(text):
    count = 0
    lines = text.splitlines()
    for line in lines:
        x = line.split()
        for word in x:
            count += 1
    print(f"Found {count} total words")
    return count

def count_chars(text):
    count_dict = {}

    chars = list(text)

    for char in chars:
        x = char.lower()
        if x in count_dict:
            count_dict[x] += 1
        else:
            count_dict[x] = 1

    return count_dict

def sort_chars(chars):
    list = []
    for c in chars:
        if c.isalpha():
            list.append({"char": c, "num": chars[c]})
    return sorted(list, reverse=True, key=lambda x: x["num"])

def print_chars(list):
    for i in list:
        print(f"{i["char"]}: {i["num"]}")
    return