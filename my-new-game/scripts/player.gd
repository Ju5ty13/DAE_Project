extends CharacterBody2D

const SPEED = 130.0
const JUMP_VELOCITY = -300.0
const MAX_JUMPS = 2
const GLIDE_GRAVITY = 150.0

@export var max_health: int = 100
@export var double_jump_effect: PackedScene  # Optional effect, drag into inspector if using

var current_health: int
var gravity = ProjectSettings.get_setting("physics/2d/default_gravity")
var jump_count = 0
var is_gliding = false

@onready var animated_sprite: AnimatedSprite2D = $AnimatedSprite2D

func _ready():
	current_health = max_health
	animated_sprite.animation_finished.connect(_on_animation_finished)

func _physics_process(delta: float) -> void:
	# Add gravity
	if not is_on_floor():
		if Input.is_action_pressed("jump") and velocity.y > 0:
			is_gliding = true
		else:
			is_gliding = false

		if is_gliding:
			velocity.y += GLIDE_GRAVITY * delta
		else:
			velocity += get_gravity() * delta
	else:
		is_gliding = false
		jump_count = 0

	# Handle jump
	if Input.is_action_just_pressed("jump") and jump_count < MAX_JUMPS:
		velocity.y = JUMP_VELOCITY
		jump_count += 1

		if jump_count == 2 and double_jump_effect:
			var effect_instance = double_jump_effect.instantiate()
			effect_instance.position = global_position
			get_parent().add_child(effect_instance)

	# Handle movement and direction
	var direction := Input.get_axis("move_left", "move_right")

	if direction > 0:
		animated_sprite.flip_h = false
	elif direction < 0:
		animated_sprite.flip_h = true

	# Set animation state
	if is_on_floor():
		if direction == 0:
			animated_sprite.play("idle")
		else:
			animated_sprite.play("run")
	else:
		if is_gliding:
			animated_sprite.play("glide")  # Add this animation if using gliding
		else:
			animated_sprite.play("jump")

	# Horizontal movement
	if direction:
		velocity.x = direction * SPEED
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)

	move_and_slide()

# Damage and death
func take_damage(amount: int) -> void:
	current_health -= amount
	if current_health <= 0:
		die()

func die() -> void:
	velocity = Vector2.ZERO
	set_physics_process(false)  # Only stop physics, not everything
	animated_sprite.play("die")
	print("Player has died!")

# Wait for animation to finish
func _on_animation_finished():
	if animated_sprite.animation == "die":
		get_tree().reload_current_scene()

# Kill zone detection
func _on_area_entered(area: Area2D) -> void:
	if area.is_in_group("player"):
		var player = area
		player.take_damage(player.max_health)
