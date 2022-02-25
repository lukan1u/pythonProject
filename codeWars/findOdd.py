# find unique number in a list which appear odd number of times
def find_it(seq):
    seq = sorted(seq)
    seto = set(seq)
    seq1 = list(seto)
    counter = 0

    while True:
        if seq1[counter] in seq:
            a = seq.count(seq1[counter])
            if a % 2 == 0:
                counter = counter + 1
            elif a % 2 != 0:
                return seq1[counter]

print(find_it([1,1,1,1,1,1,10,1,1,1,1]))

# pure logic: Remember to simplify 
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i