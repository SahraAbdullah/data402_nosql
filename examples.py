#def generateRange(start, stop, step):
#    return list(range(start, stop, step))

#start = 1
#stop = 10
#step = 1
#results = generateRange(start, stop, step)
#print(results)

def remove_exclamation_marks(s):
    return s.replace("!", "")

names = ['Charles', 'Susan', 'Patrick', 'George', 'Carol']

new_list = []
for n in names:
    if n.endswith('n'):
        new_list.append(n)
print(new_list)