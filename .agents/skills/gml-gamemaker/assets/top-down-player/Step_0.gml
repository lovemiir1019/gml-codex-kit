// obj_player / Step（新規）
var _input_x = keyboard_check(vk_right) - keyboard_check(vk_left);
var _input_y = keyboard_check(vk_down) - keyboard_check(vk_up);
var _input_length = sqrt(_input_x * _input_x + _input_y * _input_y);

// 斜めでも移動距離を同じにします。入力がないときは割りません。
if (_input_length > 0) {
    x += (_input_x / _input_length) * move_speed;
    y += (_input_y / _input_length) * move_speed;
}

// この例はルーム全体を表示する想定です。
x = clamp(x, player_radius, room_width - player_radius);
y = clamp(y, player_radius, room_height - player_radius);
