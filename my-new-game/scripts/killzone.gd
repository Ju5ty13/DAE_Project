extends Area2D

@onready var timer: Timer = $Timer

func _ready():
	# Connect the body_entered signal if not done in the editor
	connect("body_entered", Callable(self, "_on_body_entered"))

func _on_body_entered(body: Node2D) -> void:
	if body.is_in_group("player"):
		print("KillZone triggered by player!")
		body.take_damage(body.max_health)  # Instantly kills the player

		# Optional: Slow-mo effect and scene reload after short delay
		Engine.time_scale = 0.5
		timer.start()

func _on_timer_timeout() -> void:
	Engine.time_scale = 1.0
	get_tree().reload_current_scene()
