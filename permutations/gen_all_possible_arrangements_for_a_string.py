def permutations(string):

    if string == "":
        return [""]

    for char in string:
        subpermutations = permutations(string.replace(char, "", 1))
        print(subpermutations)


permutations('Shashank')