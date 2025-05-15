extends CharacterBody2D

const SPEED = 130.0
const JUMP_VELOCITY = -300.0
const MAX_JUMPS = 2
const GLIDE_GRAVITY = 150.0
const STOMP_BOUNCE_VELOCITY = -250.0

@export var max_health: int = 100
@export var double_jump_effect: PackedScene

var current_health: int
var jump_count = 0
var is_gliding = false
var can_double_jump := false
var can_glide := false

@onready var animated_sprite: AnimatedSprite2D = $AnimatedSprite2D

func _ready():
	current_health = max_health
	animated_sprite.animation_finished.connect(_on_animation_finished)

func _physics_process(delta: float) -> void:
	# Gravity and glide
	if not is_on_floor():
		if can_glide and Input.is_action_pressed("jump") and velocity.y > 0:
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

	# Jumping
	var max_jumps_allowed := 1
	if can_double_jump:
		max_jumps_allowed = MAX_JUMPS

	if Input.is_action_just_pressed("jump") and jump_count < max_jumps_allowed:
		velocity.y = JUMP_VELOCITY
		jump_count += 1

		if jump_count == 2:
			if double_jump_effect:
				var effect_instance = double_jump_effect.instantiate()
				effect_instance.position = global_position
				get_parent().add_child(effect_instance)

	# Movement
	var direction := Input.get_axis("move_left", "move_right")

	if direction != 0:
		velocity.x = direction * SPEED
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)

	# Flip sprite
	if direction > 0:
		animated_sprite.flip_h = false
	elif direction < 0:
		animated_sprite.flip_h = true

	# Set animations
	if is_on_floor():
		if direction == 0:
			animated_sprite.play("idle")
		else:
			animated_sprite.play("run")
	else:
		if is_gliding:
			animated_sprite.play("glide")
		elif jump_count == 2:
			animated_sprite.play("double_jump")
		else:
			animated_sprite.play("jump")

	move_and_slide()

# Called by unlock pickups
func unlock_ability(ability_name: String) -> void:
	match ability_name:
		"double_jump":
			can_double_jump = true
		"glide":
			can_glide = true
	print("Unlocked: " + ability_name)

func show_ability_notification(message: String) -> void:
	print("NOTIFICATION: " + message)
	# You can add UI code here later

# Health and death
func take_damage(amount: int) -> void:
	current_health -= amount
	if current_health <= 0:
		die()

func die() -> void:
	velocity = Vector2.ZERO
	set_physics_process(false)
	animated_sprite.play("die")
	print("Player has died!")

func _on_animation_finished():
	if animated_sprite.animation == "die":
		get_tree().reload_current_scene()

# Stomp enemies
func _on_body_entered(body: Node) -> void:
	if body.is_in_group("enemy") and velocity.y > 0:
		if global_position.y < body.global_position.y:
			# Stomp the slime
			if body.has_method("die"):
				body.die()
			velocity.y = STOMP_BOUNCE_VELOCITY
		else:
			take_damage(20)

# Kill zone death
func _on_area_entered(area: Area2D) -> void:
	if area.is_in_group("kill_zone"):
		take_damage(max_health)
