

minetest.register_node(":lucky_block:lucky_block", {
  description = "Christmas Present (openable december 25th)",
  tiles = {
    "gift_rainbow.png^gift_bow_top.png",
    "gift_rainbow.png^gift_bow_bottom.png",
    "gift_rainbow.png^gift_bow_side.png"},
  is_ground_content = true,
  groups = {crumbly=3}
})
minetest.register_craft({
	output = "lucky_block:lucky_block",
	recipe = {
		{"wool:black", "wool:blue", "wool:red"},
		{"wool:green", "", "wool:yellow"},
		{"wool:white", "wool:brown", "wool:grey"},
	}
})
--minetest.register_alias("lucky_block:lucky_block","gift:gift")