class Squad:
    def __init__(self, squadName, homeTown, formed, status, active, members):
      self.squadName = squadName
      self.homeTown = homeTown
      self.formed = formed
      self.status = status
      self.active = active
      #self.members = members
      
    def __repr__(self):
       return f"Squad(squadName={self.squadName}, homeTown={self.homeTown}, formed={self.formed}, status={self.status}, active={self.active}, members={self.members})"

print(Squad)