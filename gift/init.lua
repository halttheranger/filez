

minetest.register_node(":lucky_block:lucky_block", {
  description = "Christmas Present (openable december 25th)",
  tiles = {
    "gift_rainbow.png^gift_bow_top.png",
    "gift_rainbow.png^gift_bow_bottom.png",
    "gift_rainbow.png^gift_bow_side.png"},
  is_ground_content = true,
  groups = {crumbly=3}
})