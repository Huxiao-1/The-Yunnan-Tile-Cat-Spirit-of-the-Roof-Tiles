screen say(who, what):
    # 确保对话框在屏幕底部，更窄一些
    window:
        id "window"
        xalign 0.5
        yalign 0.95  # 稍微向上移动一点
        xsize 750   # 宽度进一步变窄 (从900改为750)
        ysize 200    # 高度保持不变
        background Frame("textbox2", 12, 12)
        padding (30, 30, 30, 40)  # 上、右、下、左内边距
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 10
            xmaximum 690  # 容器宽度 = 窗口宽(750) - 左右内边距(30+30)
            
            # 根据角色显示不同位置的名字
            if who is not None:
                if who == "瓦福福":
                    hbox:
                        xfill True
                        use namebox_left(who)
                elif who == "瓦彩彩":
                    hbox:
                        xfill True
                        use namebox_right(who)
                else:
                    # 默认居中显示
                    text who id "who" style "say_label_cute" xalign 0.5
            
            # 对话文本
            text what id "what" style "say_dialogue_cute" xalign 0.5 xmaximum 690 color "#000000"

# 左侧名字框
screen namebox_left(who):
    frame:
        style "namebox_left"
        text who style "say_label_left_cute"

# 右侧名字框
screen namebox_right(who):
    frame:
        style "namebox_right"
        text who style "say_label_right_cute"
    
screen choice(items):
    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5
        vbox:
            style "menu"
            spacing 10
            for i in items:
                textbutton i.caption action i.action

screen main_menu():
    tag menu
    add "gui/main_menu.png"  # 请替换为您的背景图片路径
    
    frame:
        style "main_menu_frame"
        xalign 0.5
        yalign 0.5
        vbox:
            style "main_menu_vbox"
            spacing 20
            textbutton _("开始游戏") action Start()
            textbutton _("加载游戏") action ShowMenu("load")
            textbutton _("设置") action ShowMenu("preferences")
            textbutton _("退出") action Quit(confirm=False)

# 导航屏幕 - 使用图片按钮，固定在屏幕顶部
screen navigation():
    zorder 300  # 提高层级确保在最上层
    
    # 左上角返回景点选择按钮
    imagebutton:
        xpos 10
        ypos 10
        idle "shouye"
        hover "shouye"
        action Jump("choose_attraction")
        tooltip "返回景点选择"
        xysize (40, 40)
    
    # 右上角背景音乐控制按钮
    if renpy.music.get_playing("background") and not renpy.music.get_pause("background"):
        imagebutton:
            xpos 1200
            ypos 10
            idle "yinliang_open"
            hover "yinliang_open"
            action PauseAudio("background")  # 暂停音乐
            tooltip "暂停音乐"
            xysize (40, 40)
    else:
        imagebutton:
            xpos 1200
            ypos 10
            idle "yinliang_close"
            hover "yinliang_close"
            action PlayAudio("background")  # 播放音乐
            tooltip "播放音乐"
            xysize (40, 40)

# 设置屏幕
screen preferences():
    tag menu
    window:
        style "gm_root"
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            label _("设置")
            
            null height 20
            
            # 显示模式
            hbox:
                label _("显示模式:")
                textbutton _("窗口") action Preference("display", "window")
                textbutton _("全屏") action Preference("display", "fullscreen")
            
            null height 20
            
            # 音量设置
            vbox:
                label _("音量")
                hbox:
                    bar value Preference("music volume")
                    label _("音乐")
                hbox:
                    bar value Preference("sound volume")
                    label _("音效")
                hbox:
                    bar value Preference("voice volume")
                    label _("语音")
            
            null height 20
            
            # 文字速度
            hbox:
                bar value Preference("text speed")
                label _("文字速度")
            
            null height 40
            
            # 返回按钮
            textbutton _("返回") action Return()

# 加载游戏屏幕
screen load():
    tag menu
    use navigation
    frame:
        style "file_picker_frame"
        vbox:
            label _("加载游戏")
            null height 20
            grid 2 3:
                transpose False
                xfill True
                for i in range(1, 7):
                    button:
                        action FileLoad(i)
                        has vbox
                        add FileScreenshot(i)
                        text FileTime(i, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("空存档")):
                            style "file_picker_text"
                        text FileSaveName(i):
                            style "file_picker_text"
            null height 20
            textbutton _("返回") action Return()

# 保存游戏屏幕
screen save():
    tag menu
    use navigation
    frame:
        style "file_picker_frame"
        vbox:
            label _("保存游戏")
            null height 20
            grid 2 3:
                transpose False
                xfill True
                for i in range(1, 7):
                    button:
                        action FileSave(i)
                        has vbox
                        add FileScreenshot(i)
                        text FileTime(i, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("空存档")):
                            style "file_picker_text"
                        text FileSaveName(i):
                            style "file_picker_text"
            null height 20
            textbutton _("返回") action Return()

# 游戏菜单屏幕 (替代原来的game_menu)
screen game_menu(title):
    tag menu
    use navigation
    frame:
        style "gm_root"
        vbox:
            label title
            textbutton _("返回") action Return()
            textbutton _("主菜单") action MainMenu()
            textbutton _("退出") action Quit()

# 跳过指示器
screen skip_indicator():
    zorder 100
    style_prefix "skip"
    
    frame:
        hbox:
            spacing 6
            
            text _("正在跳过")
            
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

# 通知屏幕
screen notify(message):
    zorder 100
    style_prefix "notify"
    
    frame at notify_appear:
        text "[message!tq]"
    
    timer 3.0 action Hide('notify')

# 闪烁变换
transform delayed_blink(delay, cycle):
    alpha .5
    
    pause delay
    
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat

# 通知出现变换
transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

# 景点选择菜单屏幕 - 直接显示在背景图上
screen attraction_menu():
    zorder 10
    
    # 菜单选项容器 - 使用透明背景
    vbox:
        xalign 0.8  # 右侧位置
        yalign 0.5  # 垂直居中
        spacing 25
        
        # 分隔线
        null height 20
        
        # 选项按钮 - 透明背景
        textbutton "石林":
            action [Hide("attraction_menu"), Jump("stone_forest")]
            style "attraction_choice_button"
            xalign 0.5
            
        textbutton "玉龙雪山":
            action [Hide("attraction_menu"), Jump("yulong_xueshan")]
            style "attraction_choice_button"
            xalign 0.5
            
        textbutton "白水台":
            action [Hide("attraction_menu"), Jump("bai_shuitai")]
            style "attraction_choice_button"
            xalign 0.5
        
        # 添加魏家古镇选项
        textbutton "魏家古镇":
            action [Hide("attraction_menu"), Jump("weijia_ancient_town")]
            style "attraction_choice_button"
            xalign 0.5
            
        textbutton "退出游戏":
            action [Hide("attraction_menu"), Jump("end_game")]
            style "attraction_choice_button"
            xalign 0.5

# 景点介绍后的选择菜单屏幕 - 使用与初始菜单相同的样式
screen after_attraction_choice():
    modal True
    zorder 100
    
    # 菜单选项容器 - 使用透明背景，直接放在背景图的黄色区域上
    vbox:
        xalign 0.8  # 右侧位置，与初始菜单一致
        yalign 0.5  # 垂直居中
        spacing 25
        
        # 选项按钮 - 透明背景
        textbutton "返回景点选择":
            action Return("choose_attraction")
            style "attraction_choice_button"
            xalign 0.5
            
        textbutton "退出游戏":
            action Return("end_game")
            style "attraction_choice_button"
            xalign 0.5

# 小型选择按钮样式
style choice_button_small:
    background Solid("#fff")
    hover_background Solid("#e6e6e6")
    xsize 180
    ysize 45
    
style choice_button_small_text:
    color "#000"
    size 20
    bold True
    xalign 0.5
    yalign 0.5

# 确认退出对话框 - 居中显示
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    
    # 半透明背景
    add Solid("#0008")
    
    # 居中显示的确认对话框
    frame:
        style_prefix "confirm"
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 25
            
            # 标题
            label message:
                style "confirm_prompt"
                xalign 0.5
            
            # 按钮容器
            hbox:
                xalign 0.5
                spacing 100
                
                # 确定按钮
                textbutton "确定":
                    action yes_action
                    style "confirm_button"
                
                # 取消按钮
                textbutton "取消":
                    action no_action
                    style "confirm_button"

