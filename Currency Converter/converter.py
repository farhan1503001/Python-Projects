import json
from urllib.request import urlopen

class converter:
    def __init__(self,urlname='https://api.exchangerate-api.com/v4/latest/USD') -> None:
        self.url=urlname
        self.temp=urlopen(url=self.url).read()
        self.data=json.loads(self.temp)
        self.keys=[item for item in self.data['rates'].keys()]
    
    def convert(self,from_,to_,amount=1):
        if from_!='USD':
            return round((self.data['rates']['USD']/self.data['rates'][from_])*self.data['rates'][to_]*amount,3)
        else:
            return round(self.data['rates'][to_]*amount,3)



ob=converter()
print(ob.keys)
print(ob.convert('BDT','USD'))
