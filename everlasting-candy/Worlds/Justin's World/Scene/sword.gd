extends Node2D

# constant reference to player
var player: Player

# called when the sword node is first loaded
func _ready():
	var parents := get_tree().get_nodes_in_group("player")
	player = parents[0]

	get_parent().remove_child(self)
	player.add_child(self)

# called every frame (_delta is the time since last frame)
func _process(_delta: float):
	# setting the horizontal scale to a negative number will "invert" the node horiozntally.
	# we use this to flip the sword to face right or left
	
	# if the player's horizontal velocity (x) is greater than x (moving right)
	if player.velocity.x > 0:
		scale.x = 1
	# if the player's horizontal velocity (x) is less than x (moving left)
	elif player.velocity.x < 0:
		scale.x = -1

# this function is called whenever a body enters into the area2d
# "body: Node2D" is a reference to the interacted body
func _on_area_2d_body_entered(body:Node2D):
	# checks if the body entered is a Player type node
	if body is Goober:
		# emits signal from player to "stomp" body/goober
		player.stomped.emit(body)
