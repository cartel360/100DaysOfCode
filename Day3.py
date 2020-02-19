# Summing Elements of Two Lists

import numpy as np
import operator
Python_devs = [100, 304, 345, 121212, 45421]
JavaScript_devs = [22, 3, 5654, 876765, 32]

# long way
all_devs = [
    Python_devs[0] + JavaScript_devs[0],
    Python_devs[1] + JavaScript_devs[1],
    Python_devs[2] + JavaScript_devs[2],
    Python_devs[3] + JavaScript_devs[3],
    Python_devs[4] + JavaScript_devs[4]
]

# Compresion using zip
all_devs = [x + y for x, y in zip(Python_devs, JavaScript_devs)]

# Using maps
all_devs = list(map(operator.add, Python_devs, JavaScript_devs))

# Using Numpy 💪 💪
all_devs = np.add(Python_devs, JavaScript_devs)

print(all_devs)
