shader_type spatial;

uniform vec4 emission_color : hint_color = vec4(1.0, 0.0, 0.0, 1.0);  // Default to red neon
uniform float emission_strength : hint_range(0.0, 10.0) = 2.0; // Control emission intensity

void fragment() {
    vec4 tex_color = texture(TEXTURE, UV);
    ALBEDO = tex_color.rgb;  // Set the object's base color
    EMISSION = emission_color.rgb * emission_strength;  // Apply emission
}