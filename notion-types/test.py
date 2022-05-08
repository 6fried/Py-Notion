class Litteral:
    def __init__(self, *args):
        self.values = []
        for data in args:
            self.values.append(data)
        self.value = self.values[0]

    def __setattr__(self, __name: str, __value: any) -> None:
        if __value in self.values:
           self.value = __value
        else:
            raise (ValueError("{_v} is not in range {v}".format(_v = __value, v = self.values) ))

# Test
j = Litteral(5, 2, 3, 6)
j=7
