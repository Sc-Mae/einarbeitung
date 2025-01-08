class Members: 
    def __init__(self,name, age, secretIdentity, powers):
        self.name = name
        self.age = age
        self.secretIdentity = secretIdentity
        self.powers = powers
    

    def __str__(self):
        return f"Members(name={self.name}, age={self.age}, secretIdentity={self.secretIdentity}, powers={self.powers})"



