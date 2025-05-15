extends Area2D

@export var ability_to_unlock: String = "double_jump"

func _ready():
	connect("body_entered", Callable(self, "_on_body_entered"))

func _on_body_entered(body):
	if body is CharacterBody2D and body.has_method("unlock_ability"):
		body.unlock_ability(ability_to_unlock)
		queue_free() 
