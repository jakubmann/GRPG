import os
import sys

from item import *
from enemy import *
from npc import *
from tilemap import *


#system
def clear():
	os.system('clear')


def show_help():
	print("Help:")
	print("You complete the game by winning")


#map
tilemap_current = tilemap_dev
tiles_current = tiles_basic
pickups_current = pickups_dev

def print_tilemap(tilemap, tiles):
	for y in range(0, len(tilemap)):
		for x in range(0, len(tilemap[y])):
			if y == player_ypos and x == player_xpos:
				print("@", end="")
			else:
				print(tiles[tilemap[y][x]], end="")
		print("", end="\n")

def show_map():
	print_tilemap(tilemap_current, tiles_current)

#player
name = "Beff"
health = 100
atk = 0
arm = 0
karma = 0
gold = 0

inventory = []
inventory_maxsize = 5
inventory_maxweight = 10
inventory_currentweight = 0

player_xpos = 1
player_ypos = 1

#inventory
def show_inventory():
	print("Inventory\n=====")
	for item in inventory:
		print(item.name)

def add_item(item):
	global inventory_currentweight
	if len(inventory) + 1 <= inventory_maxsize:
		if inventory_currentweight + item.weight <= inventory_maxweight:
			inventory.append(item)
			inventory_currentweight += item.weight
			print("You got a {}!".format(item.name))
		else:
			print("That item is too heavy.")
	else:
		print("Inventory full.")

def remove_item(item):
	global inventory_currentweight
	if item in inventory:
		inventory_currentweight -= item.weight
		inventory.remove(item)
	else:
		print("You don't have this item.")

#player functions
def stats():
	print("{}\n=====\nHealth: {}\nStrength: {}\nArmour: {}\nKarma: {}\nGold: {}\n".format(name, health, atk, arm, karma, gold))

def say(word):
	print("You said {}".format(word))

def go(direction):
	global player_xpos
	global player_ypos
	if direction == "up":
		if tilemap_current[player_ypos-1][player_xpos] not in solid:
			player_ypos -= 1
			print("You moved {}".format(direction))
		else:
			print("Blocked.")
	elif direction == "down":
		if tilemap_current[player_ypos+1][player_xpos] not in solid:
			player_ypos += 1
			print("You moved {}".format(direction))
		else:
			print("Blocked.")
	elif direction == "left":
		if tilemap_current[player_ypos][player_xpos-1] not in solid:
			player_xpos -= 1
			print("You moved {}".format(direction))
		else:
			print("Blocked")
	elif direction == "right":
		if tilemap_current[player_ypos][player_xpos+1] not in solid:
			player_xpos += 1
			print("You moved {}".format(direction))
		else:
			print("Blocked.")
	else:
		print("That's not a direction.")
	#collisions
	if pickups_current[player_ypos][player_xpos] == 1:
		add_item(leaf)
		pickups_current[player_ypos][player_xpos] = 0
	show_map()


def inspect(thing_name):
	if thing_name in Item.objects:
		if Item.objects[thing_name] in inventory:
			Item.objects[thing_name].get_info()
		else:
			print("You don't have that item.")
	elif thing_name in Enemy.objects:
		Enemy.objects[thing_name].get_desc()
	else:
		print("There is no {} here.".format(thing_name))

def drop(item_name):
	if item_name in Item.objects:
		if Item.objects[item_name] in inventory:
			item = Item.objects[item_name]
			remove_item(item)
			print("You dropped the {}".format(item.name))
		else:
			print("You don't have a {}".format(item_name))
	else:
		print("{} is not an Item.".format(item_name))

#player input
def get_input():
	user_input = input(": ").split()
	if len(user_input) == 1:
		if user_input[0] in commands_simple:
			command = commands_simple[user_input[0]]
			command()
		else:
			print("{} is not a valid command.".format(user_input[0]))
	elif len(user_input) >= 2:
		if user_input[0] in commands_complex:
			command_first = commands_complex[user_input[0]]
			command_second = user_input[1]
			command_first(command_second)
		else:
			print("{} is not a valid command.".format(user_input[0]))
	else:
		print("You must enter a command.")

commands_simple = {
	"help" : show_help,
	"map" : show_map,
	"inventory" : show_inventory,
	"stats" : stats

}

commands_complex = {
	"say" : say,
	"go" : go,
	"drop" : drop,
	"inspect" : inspect
}

#objekty
leaf = Item("Leaf", "A leaf you would find in a forest. Nothing much special about it.", 0.1, 0.01)
anvil = Item("Anvil", "It's pretty fucking heavy.", 25, 10)
potion = Potion("Potion", "potion", 0, 0, 0)


#game loop
clear()
add_item(anvil)
while True:

	try:
		get_input()
	except KeyboardInterrupt:
		print("Bye")
		sys.exit()
