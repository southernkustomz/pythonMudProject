import logging
import re
from core import MUDObject
from core import MUDInterface

class Player(MUDObject):
    name = None
    location = None
    classes = []
    inventory = []
    ''' Future attribures. uncomment when ready for use.
    level = 1
    hit_points = 0
    mana_points = 0
    move_points = 0
    max_hit_points = 100
    max_mana_points = 100
    max_move_points = 100
    
    hit_regen_rate = 5
    mana_regen_rate = 5
    move_regen_rate = 5
    
    attack_power = 1
 
    states = {}
    
    client = None
    prompt = None
    prompt_enabled = True
    
    connected = True
    
    can_attack = True
    can_be_attacked = True
    '''
def __init__(self,*args,**kwargs)
    super().__init__()
    for k,v in kwargs.items():
        setattr(self,k,v)
    self.interface = MUDInterface.get_interface("player")()
    self.level = kwargs.get("level",self.level)