from tabulate import tabulate
import random
import time

placement = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0

while i <10 :
    names = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
    ]
    names[random.randint(-1, 9)][random.randint(-1, 9)] = 'c'
    names[random.randint(-1, 9)][random.randint(-1, 9)] = 'r'
    print(tabulate(names, tablefmt='grid'))
    print('NEXT TABLE')
    time.sleep(2)
    i = i + 1
