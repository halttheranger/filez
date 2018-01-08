minetest.register_node("killfield:killfield", {
	description = ("killfield"),
	sunlight_propagates = true,
        damage_per_second = 20,
        walkable = false,
        is_ground_content = false,
	drawtype = "glasslike",
	groups = {radioactive=3},
	paramtype = "light",
	light_source = default.LIGHT_MAX,
	diggable = false,
	drop = '',
	tiles = {{
		name = "killfield_killfield_animated.png",
		animation = {
			type = "vertical_frames",
			aspect_w = 16,
			aspect_h = 16,
			length = 1.0,
		},
	}},
})


