extends Node2D

const SPEED = 60
var direction = 1

@onready var ray_cast_right: RayCast2D = $RayCastRight
@onready var ray_cast_left: RayCast2D = $RayCastLeft
@onready var animated_sprite: AnimatedSprite2D = $AnimatedSprite2D
@onready var killzone: Area2D = $Killzone

func _ready():
	killzone.body_entered.connect(_on_body_entered)

func _process(delta: float) -> void:
	# Reverse direction when hitting a wall or edge
	if ray_cast_right.is_colliding():
		direction = -1
		animated_sprite.flip_h = true
	elif ray_cast_left.is_colliding():
		direction = 1
		animated_sprite.flip_h = false

	# Move slime manually since we're using Node2D
	position.x += direction * SPEED * delta

func _on_body_entered(body: Node2D) -> void:
	if body.is_in_group("player"):
		# Check if the player is falling onto the slime (like a stomp)
		if body.velocity.y > 0:
			queue_free()
			body.velocity.y = -200  # Bounce the player up
		else:
			body.take_damage(20)
