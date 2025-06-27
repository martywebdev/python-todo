waiting_list = [ 'allan', 'ben', 'charles']

def print_list(names):
    for index, item in enumerate(waiting_list):
        row = f'{index + 1}.{item.capitalize()}'

        print(row)
    print('*********************\n')

print_list(waiting_list)

print_list(waiting_list.sort())

print_list(waiting_list.sort(reverse=True))


print_list(sorted(waiting_list,reverse=True))


