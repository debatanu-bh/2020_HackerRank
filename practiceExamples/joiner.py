#
# a=" this  is a string"
#
# b=a.split(" ")
# b=("-").join(b)
# # b=b.pop(b[0])
#
# print(b[1:])


def split_and_join(line):
    # write your code here
    a=line
    b=a.split(" ")
    b=("-").join(b)
# b=b.pop(b[0])

    # b=b[1:]
    return b



if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)