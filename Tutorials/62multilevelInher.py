class Grandpa:
    basketball = 1

class Dad(Grandpa):
    dance = 1
    def d(this):
        return f"Yes I Dance {this.dance} no of times"

class Grandson(Dad):
    dance = 6
    def d(this):
        return f"Yes I Dance AWESOMELY {this.dance} no of times"
    
jo = Grandpa()
bo = Dad()
po = Grandson()

#  Everything DAD[OR GANDPA] HAS GOES TO SON TOO --
print(po.basketball)
print(po.d())