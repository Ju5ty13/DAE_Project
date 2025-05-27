extends Area2D

@export var target_position: Vector2

func _on_body_entered(body):
	if body.name == "Player":  # Match your player node name
		body.global_position = target_position
