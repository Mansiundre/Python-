def Delete(double):

    last_list = []

    for n in double:

        if n not in last_list:

            last_list.append(n)

    return last_list

# Driver Code

double = [2, 4, 10, 20, 5, 2, 20, 4]

print(Delete(double))
