class Trio(int):
    __DEVIATION = 0.2
    accept = True
    decline = False
    maybe = "Maybe"

    def calc_cur_deviation(value_1, value_2):
        average = (value_1+value_2) / 2
        cur_deviation = float(((value_1-value_2)/2) / average)
        return cur_deviation

    def __eq__(self, other):
        if int(self) == int(other):
            return self.accept
        cur_deviation = Trio.calc_cur_deviation(self, other)
        if abs(cur_deviation) < Trio.__DEVIATION:
            return self.maybe
        else:
            return self.decline

    def __ne__(self, other):
        return not self == other if ((self==other)==self.accept) or ((self==other)==self.decline) else self == other

    def __gt__(self, other):
        if (self == other) == self.accept:
            return self.decline
        cur_deviation = Trio.calc_cur_deviation(self, other)
        if cur_deviation >= Trio.__DEVIATION:
            return self.accept
        elif cur_deviation > 0 and cur_deviation < Trio.__DEVIATION:
            return self.maybe
        elif cur_deviation <= 0:
            return self.decline

    def __lt__(self, other):
        if (self == other) == self.accept:
            return self.decline
        cur_deviation = Trio.calc_cur_deviation(self, other)
        if cur_deviation <= -Trio.__DEVIATION:
            return self.accept
        elif cur_deviation < 0 and cur_deviation > -Trio.__DEVIATION:
            return self.maybe
        elif cur_deviation >= 0:
            return self.decline
        
    def __ge__(self, other):
        if (self == other) == self.accept:
            return self.accept
        else:
            return self > other

    def __le__(self, other):
        if (self == other) == self.accept:
            return self.accept
        else:
            return self < other       

class Person(Trio):
    accept = 'ДА'
    decline = 'НЕТ'
    maybe = 'МОЖЕТ БЫТЬ'

    def check(self, result):
        if result == True:
            return self.accept
        elif result == False:
            return self.decline
        elif result == "Maybe":
            return self.maybe
        else:
            raise ValueError(f'{result} does not exist')

class Soldier(Person):
    accept = 'ДА'
    decline = 'НЕТ'
    maybe = 'Это не солдат'

class Diplomat(Person):
    accept = 'МОЖЕТ БЫТЬ'
    decline = 'Это не дипломат'
    maybe = 'НЕТ'

class Woman(Person):
    accept = 'Это не женщина, это солдат!'
    decline = 'МОЖЕТ БЫТЬ'
    maybe = 'ДА'


a = Trio(10)
b = Trio(9)
c = Trio(10)
d = Trio(3)
z = Trio(0)

operations = {
    "eq": [a==b, a==c, a==d],
    "ne": [a!=b, a!=c, a!=d],
    "gt": [b>a, a>b, a>c, a>d],
    "lt": [b<a, a<b, a<c, a<d],
    "ge": [b>=a, a>=b, a>=c, a>=d],
    "le": [b<=a, a<=b, a<=c, a<=d]
}

P = Person()
S = Soldier()
D = Diplomat()
W = Woman()

for expressions in operations.items():
    print(expressions, end='\n\n')
    for expression in expressions[1]:
        print('\tЕсли солдат говорит ', P.check(expression), ', то это значит ', S.check(expression), sep='')
        print('\tЕсли дипломат говорит ', P.check(expression), ', то это значит ', D.check(expression), sep='')
        print('\tЕсли женщина говорит ', P.check(expression), ', то это значит ', W.check(expression), end='\n\n', sep='')
    

print(f'a({a}) == b({b})', a == b)
print(f'a({a}) == c({c})', a == c)
print(f'a({a}) == d({d})', a == d)
print()
print(f'a({a}) != b({b})', a != b)
print(f'a({a}) != c({c})', a != c)
print(f'a({a}) != d({d})', a != d)
print()
print(f'b({b}) > a({a})', b > a)
print(f'a({a}) > b({b})', a > b)
print(f'a({a}) > c({c})', a > c)
print(f'a({a}) > d({d})', a > d)
print()
print(f'a({a}) < b({b})', a < b)
print(f'b({b}) < a({a})', b < a)
print(f'c({c}) < a({a})', c < a)
print(f'd({d}) < a({a})', d < a)
print()
print(f'b({b}) >= a({a})', b >= a)
print(f'a({a}) >= b({b})', a >= b)
print(f'a({a}) >= c({c})', a >= c)
print(f'a({a}) >= d({d})', a >= d)
print()
print(f'a({a}) <= b({b})', a <= b)
print(f'b({b}) <= a({a})', b <= a)
print(f'c({c}) <= a({a})', c <= a)
print(f'd({d}) <= a({a})', d <= a)