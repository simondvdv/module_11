class compl_nubmer:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __str__(self):
        if self.img > 0:
            return f'{self.real} + {self.img}i'
        elif self.img < 0:
            return f'{self.real} - {-self.img}i'
        else:
            return f'{self.real}'


def intersept(obj):
    obj_type = type(obj)
    attr_2 = [i for i in dir(c1) if not callable(getattr(c1, i))]
    methods_2 = [i for i in dir(c1) if callable(getattr(c1, i))]
    module_ = obj.__module__
    return {'type': obj_type, 'attributes': attr_2, 'methods': methods_2, 'module': module_}


c1 = compl_nubmer(1, 3)
print(intersept(c1))






