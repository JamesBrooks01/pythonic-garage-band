import abc
from abc import ABC


class Band(ABC):
  instances = []


  def __init__(self, name, members):
    self.name = name
    self.members = members
    Band.instances.append(self)

  def play_solos(self):
    solos = []
    for member in self.members:
      solos.append(member.play_solo())
    return solos

  def to_list():
    return Band.instances


class Musician(Band):
  def __init__(self, name):
    self.name = name


class Guitarist(Musician):
  def __str__(self):
    return f"My name is {self.name} and I play guitar"

  def __repr__(self):
    return f"Guitarist instance. Name = {self.name}"

  @staticmethod
  def get_instrument():
    return "guitar"

  @staticmethod
  def play_solo():
    return "face melting guitar solo"

class Bassist(Musician):
  def __str__(self):
    return f"My name is {self.name} and I play bass"

  def __repr__(self):
    return f"Bassist instance. Name = {self.name}"

  @staticmethod
  def get_instrument():
    return "bass"

  @staticmethod
  def play_solo():
    return "bom bom buh bom"

class Drummer(Musician):
  def __str__(self):
    return f"My name is {self.name} and I play drums"

  def __repr__(self):
    return f"Drummer instance. Name = {self.name}"

  @staticmethod
  def get_instrument():
    return "drums"

  @staticmethod
  def play_solo():
    return "rattle boom crash"