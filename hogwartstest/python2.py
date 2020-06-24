##
import yaml


class Animal:
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def call(self):
        print(f"{self.name} this animal can call")

    def run(self):
        print(f"{self.name} this animal can run")


class cat(Animal):
    def __init__(self, name, color, age, gender):
        super().__init__(name, color, age, gender)
        self.maofa = 'duanfa'

    def catch(self):
        print(f"{self.name} this animal can catch")

    def call(self):
        print(f"{self.name} maomao  can miaomiaocall")


class dog(Animal):
    def __init__(self, name, color, age, gender):
        super().__init__(name, color, age, gender)
        self.maofa = 'changfa'

    def watchhome(self):
        print(f"{self.name} this animal can watchhome")

    def call(self):
        print(f"{self.name} gougou can wangwangcall")


"""
未使用yaml文件的代码

if __name__ == '__main__':
    maomao = cat ('mimi','white',2,'male')
    maomao.catch()
    print(f"{maomao.name} is {maomao.color} and its age is {maomao.age} ,its gender is {maomao.gender} ,its hair is {maomao.maofa},and it can catch mouse")

    gougou = dog ('wangwang','yellow',5,'fmale')
    gougou.watchhome()
    print(f"{gougou.name} is {gougou.color} and its age is {gougou.age} ,its gender is {gougou.gender} ,its hair is {gougou.maofa}")
"""

"""
下述为使用yaml的代码
"""
if __name__ == '__main__':
    with open('animal_data.yml') as f:
        data = yaml.safe_load(f)

    # print(data)
    maomao1 = data['cat']
    # mao_mao =maomao1['name']
    mymaomao = cat(maomao1['name'], maomao1['color'], maomao1['age'], maomao1['gender'])
    mymaomao.catch()
    print(maomao1['name'], maomao1['color'], maomao1['age'], maomao1['gender'], maomao1['maofa'], 'catched a mouse!')

    gougou1 = data['dog']
    mygougou = dog(gougou1['name'], gougou1['color'], gougou1['age'], gougou1['gender'])
    mygougou.watchhome()
    print(gougou1['name'], gougou1['color'], gougou1['age'], gougou1['gender'], gougou1['maofa'])
