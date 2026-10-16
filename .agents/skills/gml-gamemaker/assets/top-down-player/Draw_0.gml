// obj_player / Draw（新規）
// スプライト画像なしで、プレイヤーを円として描きます。
var _previous_colour = draw_get_color();
draw_set_color(c_aqua);
draw_circle(x, y, player_radius, false);
draw_set_color(_previous_colour);
