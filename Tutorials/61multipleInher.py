class Employee:
    a=1
    def __init__(this, name, job, age):  
        this.name = name
        this.job = job
        this.age = age

    def infoEmployee(this):
        return f'Name is {this.name}...Job is {this.job}...Age is {this.age}'

    @classmethod
    def shortCut(this, string):
        x = string.split('-')
        return this(x[0], x[1], x[2])   # now became a list
  
    @staticmethod
    def static(x):
        print('Hi', x)
        return 'Lol'


class Player:
    a=2
    noOfGames = 4
    def __init__(this, name, game):
        this.name = name
        this.job = game

    def infoPlayer(this):
        return f'Name is {this.name}...Game is {this.game}...'



# Multiple Inheritance --
class EP(Employee, Player):
    a=3
    lang = 'English'
    def printLang(this):
        print(this.lang)

# IMPORTANT IN CASE OF SAME FUNSTION IN SUPER CLASSES THEN FUNC FROM FIRST CLASS IS INHERITED
# FOR EG --  def __init__: is same in both so Employee classs is given priority over Player 
# So to set GAME ATTRIBUTE U HAVE TO SET IT SEPARAYTELY

pip = EP('Pip', 'Coder', '24')

print(pip.__dict__)

print(pip.infoEmployee())
print(pip.lang)

print(pip.noOfGames)
print(pip.a)