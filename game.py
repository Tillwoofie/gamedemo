#!/usr/bin/env python

# Generic example for a very basic game battle system.
# written by Jeff Hickson ( rvbcaboose@gmail.com )

import random

class EndOfBattleException(Exception):
	pass

class Creature(object): #base creature class
	def __init__(self):
		self.name = ""
		self.hp = 0
		self.mp = 0
		self.attack = 0
		self.defence = 0
		self.mag_attack = 0
		self.mag_defence = 0
		self.defending = False

		#chances for actions.
		self.attack_chance = 0
		self.defence_chance = 0
		self.run_chance = 0

	def RandomAction(self, target):
		self.defending = False
		roll = random.randint(1,1000)
		if roll <= self.run_chance:
			self.run()
		elif roll <= self.defence_chance:
			self.defend()
		elif roll <= self.attack_chance:
			self.attack_target(target)
		else:
			self.do_nothing()
	
	def attack_target(self, target):
		damage = self.get_damage()
		target.take_damage(damage)
		print "attacks and hits %s for %i damage" % (target.name, damage)
		return damage
	
	def get_damage(self):
		return self.attack
	
	def defend(self):
		self.defending = True
		print "takes a defensive stance."
	
	def take_damage(self, damage):
		if self.defending:
			self.hp -= (damage/2) - self.defence
		else:
			self.hp -= damage - self.defence
	
	def is_alive(self):
		if self.hp > 0:
			return True
		return False
	
	def do_nothing(self):
		print "i did nothing."
	
	def run(self):
		print "%s ran from battle" % (self.name,)
		raise EndOfBattleException
	
class Player(Creature):
	def __init__(self):
		Creature.__init__(self)

		#set our own information
		self.name = "Till"
		self.hp = 10
		self.mp = 10
		self.attack = 3
		self.defend = 1
		self.mag_attack = 3
		self.mag_defence = 1
		
		self.run_chance = 5
		self.defend_chance = 100
		self.attack_chance = 900

class BasicRat(Creature):
	def __init__(self):
		Creature.__init__(self)

		self.name = "Rat"
		self.hp = 5
		self.mp = 5
		self.attack = 2
		self.defence = 1
		self.mag_attack = 0
		self.mag_defence = 0
		
		self.run_chance = 30
		self.defend_chance = 300
		self.attack_chance = 900

def main():
	plr = Player()
	rat = BasicRat()

	try:
		while True:
			plr.RandomAction(rat)
			if not rat.is_alive():
				raise EndOfBattleException
			rat.RandomAction(plr)
			if not plr.is_alive():
				raise EndOfBattleException
	except EndOfBattleException:
		pass
	
	if plr.is_alive():
		print "Till won!"
	else:
		print "The rat won :("

if __name__ == '__main__':
	main()

