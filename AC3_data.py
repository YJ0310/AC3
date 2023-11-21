x_constant = [1.00E3, 1.50E3, 2.00E3, 2.50E3, 3.00E3, 3.50E3, 4.00E3]


class data_set:
    def __init__(self, y):
        self.x = x_constant
        self.y = y


set1 = data_set(
    [20.0E-3,
     39.0E-3,
     84.0E-3,
     98.0E-3,
     57.0E-3,
     40.0E-3,
     30.0E-3]
)

set2 = data_set(
    [20.0E-3,
     38.0E-3,
     74.0E-3,
     82.0E-3,
     54.0E-3,
     38.0E-3,
     30.0E-3
     ]
)

set3 = data_set(
    [18.0E-3,
     34.0E-3,
     54.0E-3,
     58.0E-3,
     45.0E-3,
     34.0E-3,
     28.0E-3
     ]
)

L = 10e-3
C = 0.47e-6
voltage = 1.4