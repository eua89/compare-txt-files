 
with open('first.txt', 'r') as file1:
    with open('second.txt', 'r') as file2:
        same = set(file1).difference(file2)

same.discard('\n')

with open('out.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)