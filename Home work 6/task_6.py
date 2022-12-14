# 6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

import random
from random import randint

rand_list = list(map(lambda x: random.randint(1,201), range(200)))
print(rand_list)

cort_list = [(index,element) for index,element in enumerate(rand_list) if index!=element]
print(cort_list)

condit_list = [i for i in enumerate(rand_list) if not (i[0]+i[1])%5]
print(condit_list)


