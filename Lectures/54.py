class Some:
    def __init__(self, lengt: float, hight: float, depth: float):
        self.lengt = lengt
        self.hight = hight
        self.depth = depth

    def __lt__(self, other):
        v_self = self.lengt * self.hight * self.depth
        v_other = other.lengt * other.hight * other.depth
        return v_self < v_other

    def __le__(self, other):
        v_self = self.lengt * self.hight * self.depth
        v_other = other.lengt * other.hight * other.depth
        return v_self <= v_other

    def __ge__(self, other):
        v_self = self.lengt * self.hight * self.depth
        v_other = other.lengt * other.hight * other.depth
        return v_self >= v_other

    def __gt__(self, other):
        v_self = self.lengt * self.hight * self.depth
        v_other = other.lengt * other.hight * other.depth
        return v_self > v_other

    def __ne__(self, other):
        v_self = self.lengt * self.hight * self.depth
        v_other = other.lengt * other.hight * other.depth
        return v_self != v_other

    def __eq__(self, other):
        v_self = self.lengt * self.hight * self.depth
        v_other = other.lengt * other.hight * other.depth
        return v_self == v_other


some1 = Some(12, 20, 22)
some2 = Some(12, 20, 22)
print(some1 < some2)
print(some1 <= some2)
print(some1 >= some2)
print(some1 == some2)
print(some1 != some2)