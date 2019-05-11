# -*- coding: utf-8 -*-

__author__ = 'Jace Xu'
__version__ = "0.4"

from .autoit import options, properties, commands
from .autoit import AutoItError

from .autoit import error
from .autoit import auto_it_set_option
from .autoit import clip_get
from .autoit import clip_put
from .autoit import is_admin
from .autoit import drive_map_add
from .autoit import drive_map_del
from .autoit import drive_map_get
from .autoit import mouse_click
from .autoit import mouse_click_drag
from .autoit import mouse_down
from .autoit import mouse_get_cursor
from .autoit import mouse_get_pos
from .autoit import mouse_move
from .autoit import mouse_up
from .autoit import mouse_wheel
from .autoit import opt
from .autoit import pixel_checksum
from .autoit import pixel_get_color
from .autoit import pixel_search
from .autoit import send
from .autoit import tooltip

from .process import run
from .process import run_wait
from .process import process_close
from .process import process_exists
from .process import process_set_priority
from .process import process_wait
from .process import process_wait_close
from .process import run_as
from .process import run_as_wait
from .process import shutdown

from .win import win_activate
from .win import win_activate_by_handle
from .win import win_active
from .win import win_active_by_handle
from .win import win_close
from .win import win_close_by_handle
from .win import win_exists
from .win import win_exists_by_handle
from .win import win_get_caret_pos
from .win import win_get_class_list
from .win import win_get_class_list_by_handle
from .win import win_get_client_size
from .win import win_get_client_size_by_handle
from .win import win_get_handle
from .win import win_get_handle_as_text
from .win import win_get_pos
from .win import win_get_pos_by_handle
from .win import win_get_process
from .win import win_get_process_by_handle
from .win import win_get_state
from .win import win_get_state_by_handle
from .win import win_get_text
from .win import win_get_text_by_handle
from .win import win_get_title
from .win import win_get_title_by_handle
from .win import win_kill
from .win import win_kill_by_handle
from .win import win_menu_select_item
from .win import win_menu_select_item_by_handle
from .win import win_minimize_all
from .win import win_minimize_all_undo
from .win import win_move
from .win import win_move_by_handle
from .win import win_set_on_top
from .win import win_set_on_top_by_handle
from .win import win_set_state
from .win import win_set_state_by_handle
from .win import win_set_title
from .win import win_set_title_by_handle
from .win import win_set_trans
from .win import win_set_trans_by_handle
from .win import win_wait
from .win import win_wait_by_handle
from .win import win_wait_active
from .win import win_wait_active_by_handle
from .win import win_wait_close
from .win import win_wait_close_by_handle
from .win import win_wait_not_active
from .win import win_wait_not_active_by_handle

from .control import control_click
from .control import control_click_by_handle
from .control import control_command
from .control import control_command_by_handle
from .control import control_list_view
from .control import control_list_view_by_handle
from .control import control_disable
from .control import control_disable_by_handle
from .control import control_enable
from .control import control_enable_by_handle
from .control import control_focus
from .control import control_focus_by_handle
from .control import control_get_focus
from .control import control_get_focus_by_handle
from .control import control_get_handle
from .control import control_get_handle_as_text
from .control import control_get_pos
from .control import control_get_pos_by_handle
from .control import control_get_text
from .control import control_get_text_by_handle
from .control import control_hide
from .control import control_hide_by_handle
from .control import control_move
from .control import control_move_by_handle
from .control import control_send
from .control import control_send_by_handle
from .control import control_set_text
from .control import control_set_text_by_handle
from .control import control_show
from .control import control_show_by_handle
from .control import control_tree_view
from .control import control_tree_view_by_handle
from .control import statusbar_get_text
from .control import statusbar_get_text_by_handle