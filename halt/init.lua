

minetest.register_node("halt:unbreakable", {
	description = "unbreakable",
	tiles = {"halt_unbreakable.png"},
	sounds = default.node_sound_defaults(),
	groups = {forbidden=1, very_hard = 1, creative = 1},
})

