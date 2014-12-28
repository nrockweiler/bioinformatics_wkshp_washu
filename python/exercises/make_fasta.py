import random

nucs = ['a','c','g','t']

adapter = 'attaactctgacta'

for n in range(1,12):
    print ">sequence_" + str(n)

    seq = adapter

    length = random.randint(100,300)
    for x in range(1,length):
        seq = seq + nucs[random.randint(0,3)]

    print seq

