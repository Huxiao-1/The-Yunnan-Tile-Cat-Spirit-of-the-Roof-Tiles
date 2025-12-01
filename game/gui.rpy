
init -1 python:
    gui.init(1280, 720)
    gui.text_font = "fonts/cute_font3.ttf"
    gui.name_text_font = "fonts/cute_font3.ttf"
    gui.interface_text极="fonts/cute_font3.ttf"
    gui.button_text_font = "fonts/cute_font3.ttf"
    gui.choice_button_text_font = "fonts/cute_font极.ttf"
    
    gui.nav_button_size = 60
    
    cute_orange = "#FF9E6D"  
    cute_pink = "#FF6B9D"   
    cute_purple = "#B28DFF" 

style namebox_left:
    background None
    xalign 0.0 
    yalign 0.0  
    xoffset 40  
    yoffset -25  
style namebox_right:
    background None
    xalign 1.0  
    yalign 0.0  
    xoffset -40  
    yoffset -25 

style say_label_left_cute:
    color cute_orange  
    font gui.name_text_font
    bold True
    size 30
    outlines [(2, "#FFFFFF", 0, 0)]  


style say_label_right_cute:
    color cute_pink  
    font gui.name_text_font
    bold True
    size 30
    outlines [(2, "#FFFFFF", 0, 0)] 


style say_label_cute:
    color cute_purple  
    font gui.name_text_font
    bold True
    size 30
    outlines [(2, "#FFFFFF", 0, 0)]  

style say_dialogue_cute:
    color "#000000" 
    font gui.text_font
    size 26
    text_align 0.5
    xalign 0.5
    xmaximum 1040
    line_spacing 8
    layout "subtitle"

style window:
    xalign 0.5
    yalign 0.98  
    xsize 1100   
    ysize 250    
    background Frame("textbox2", 12, 12)
    padding (30, 30, 30, 40)

# 定义基本样式
style default:
    font gui.text_font
    size 24

# 景点选择按钮样式 - 透明背景
style attraction_choice_button:
    background None
    hover_background Solid("#ffdd00aa")  
    xsize 200
    ysize 50
    
style attraction_choice_button_text:
    color "#000"
    size 26
    bold True
    xalign 0.5
    yalign 0.5
    hover_color "#fff"  

# 菜单样式
style menu_window:
    xalign 0.5
    yalign 0.5
    
style menu_vbox:
    xalign 0.7
    yalign 0.5
    spacing 10
    
style menu_button:
    background Frame("gui/button/idle.png", 12, 12)
    hover_background Frame("gui/button/hover.png", 12, 12)
    padding (20, 10)
    xsize 200
    
style menu_button_text:
    color "#000"
    hover_color "#fff"
    size 24
    text_align 0.5
    
style gm_root:
    background "#0008"
    
# 确认对话框样式
style confirm_frame:
    background Frame("gui/frame.png", 12, 12)
    xalign 0.5
    yalign 0.5
    xpadding 30
    ypadding 30
    xminimum 400
    yminimum 200

style confirm_prompt:
    color "#000"
    size 28
    text_align 0.5
    xalign 0.5

style confirm_button:
    background Solid("#fff")
    hover_background Solid("#e6e6e6")
    xsize 100
    ysize 40

style confirm_button_text:
    color "#000"
    size 22
    bold True
    xalign 0.5
    yalign 0.5