init python:
    # 自定义动作：暂停指定通道的音频
    class PauseAudio(Action):
        def __init__(self, channel):
            self.channel = channel
            
        def __call__(self):
            renpy.music.set_pause(True, channel=self.channel)
            # 强制刷新导航屏幕
            renpy.restart_interaction()
    
    # 自定义动作：继续播放指定通道的音频
    class PlayAudio(Action):
        def __init__(self, channel):
            self.channel = channel
            
        def __call__(self):
            renpy.music.set_pause(False, channel=self.channel)
            # 如果音乐没有在播放，则重新开始播放
            if not renpy.music.get_playing(self.channel):
                renpy.music.play("audio/background_music.mp3", channel=self.channel, loop=True)
            # 强制刷新导航屏幕
            renpy.restart_interaction()
            
# 定义角色
define c = Character("瓦彩彩", color="#FF6B9D", image="caicai", who_style="say_label_right_cute")
define f = Character("瓦福福", color="#FF9E6D", image="fufu", who_style="say_label_left_cute")
define narrator = Character(None, what_style="say_dialogue_cute")

# 游戏开始
label start:
    scene black
    
    # 播放开场视频
    play movie "audio/opening.webm"
    
    # 显示跳过按钮
    show screen skip_video_button
    
    # 等待视频结束或用户点击跳过
    $ renpy.pause(delay=None)  
    
    # 隐藏跳过按钮
    hide screen skip_video_button
    
    # 停止视频
    stop movie
    
    # 直接进入景点选择
    jump choose_attraction

# 跳过视频按钮屏幕
screen skip_video_button():
    zorder 100
    button:
        xalign 1.0
        yalign 0.0
        xoffset -20
        yoffset 20
        background None
        action Jump("skip_opening")
        
        text "跳过":
            size 24
            color "#fff"
            hover_color "#ff0"

# 跳过视频的标签
label skip_opening:
    # 停止视频
    stop movie
    # 继续游戏
    jump choose_attraction

label choose_attraction:
    if not renpy.music.get_playing("background"):
        $ renpy.music.play("audio/background_music.mp3", channel="background", loop=True, fadein=1.0)
    else:
        $ renpy.music.set_pause(False, channel="background")
    scene background with fade
    show screen navigation
    show screen attraction_menu
    pause
    hide screen attraction_menu
    hide screen navigation
    return

# 石林景点介绍
label stone_forest:
    hide screen attraction_menu
    scene shilin with fade
    show screen navigation
    show caicai at right_bottom with dissolve 
    c "欢迎来到石林！这里是云南最著名的自然奇观之一。"
    
    hide caicai with dissolve
    show fufu at left_bottom with dissolve  # 左下角
    f "喵~这里是世界自然遗产，被誉为'天下第一奇观'！"
    
    hide fufu with dissolve
    show caicai at right_bottom with dissolve  # 右下角
    c "石林形成于2.7亿年前，是典型的喀斯特地貌，这些石柱形态各异，非常壮观。"
    
    hide caicai with dissolve
    show fufu at left_bottom with dissolve  # 左下角
    f "看那些奇形怪状的石头，有的像动物，有的像人物，非常神奇！"
    
    hide fufu with dissolve
    show caicai at right_bottom with dissolve  # 右下角
    c "这里还是撒尼人的故乡，有着丰富的民族文化，他们的传统服饰和歌舞表演很值得一看。"
    
    hide caicai with dissolve
    show fufu at left_bottom with dissolve  # 左下角
    f "每年农历六月二十四，这里会举办盛大的火把节，热闹极了！"
    
    hide fufu with dissolve
    jump after_attraction

# 玉龙雪山景点介绍
label yulong_xueshan:
    hide screen attraction_menu
    scene yulongxueshan with fade
    
    # 显示导航按钮
    show screen navigation
    
    show caicai at right_bottom with dissolve  # 右下角
    c "欢迎来到玉龙雪山！这是北半球最南端的大雪山，海拔5596米。"
    
    hide caicai with dissolve
    show fufu at left_bottom with dissolve  # 左下角
    f "喵~雪山有13座山峰，宛如一条巨龙腾越飞舞，所以叫'玉龙'。"
    
    hide fufu with dissolve
    show caicai at right_bottom with dissolve  # 右下角
    c "这里有高山雪域风景、水域风景和森林风景，景观非常丰富多样。"
    
    hide caicai with dissolve
    show fufu at left_bottom with dissolve  # 左下角
    f "玉龙雪山是纳西族的神山，传说中是纳西族保护神'三多'的化身。"
    
    hide fufu with dissolve
    show caicai at right_bottom with dissolve  # 右下角
    c "可以乘坐缆车到达海拔4506米的观景台，欣赏壮丽的雪山风光，视野非常开阔。"
    
    hide caicai with dissolve
    show fufu at left_bottom with dissolve  # 左下角
    f "山下的蓝月谷也很漂亮，湖水是蓝色的，像仙境一样！"
    
    hide fufu with dissolve
    jump after_attraction

# 白水台景点介绍
label bai_shuitai:
    hide screen attraction_menu
    scene baishuitai with fade
    
    # 显示导航按钮
    show screen navigation
    
    show caicai at right_bottom with dissolve  # 右下角
    c "欢迎来到白水台！这是中国最大的华泉台地，有'仙人遗田'的美称。"
    
    hide caicai with dissolve
    show fufu at left_bottom with dissolve  # 左下角
    f "喵~白水台是由于碳酸钙溶解于泉水中而形成的自然奇观。"
    
    hide fufu with dissolve
    show caicai at right_bottom with dissolve  # 右下角
    c "层层叠叠的白色梯田，在阳光下闪烁着银光，非常壮观，像是大自然雕刻的艺术品。"
    
    hide caicai with dissolve
    show fufu at left_bottom with dissolve  # 左下角
    f "这里也是纳西族东巴教的发源地，有'东巴圣地'之称。"
    
    hide fufu with dissolve
    show caicai at right_bottom with dissolve  # 右下角
    c "每年农历二月初八，纳西族会在这里举行传统的朝白水活动，场面很隆重。"
    
    hide caicai with dissolve
    show fufu at left_bottom with dissolve  # 左下角
    f "这里的泉水据说有神奇的功效，很多人都会来取水祈福。"
    
    hide fufu with dissolve
    jump after_attraction

# 魏家古镇景点介绍
label weijia_ancient_town:
    # 只隐藏景点选择菜单，但保留导航按钮
    hide screen attraction_menu
    scene weijiaguzhen with fade
    
    # 显示导航按钮
    show screen navigation
    
    show caicai at right_bottom with dissolve  # 右下角
    c "欢迎来到魏家古镇！这里是云南保存最完好的古镇之一，也是瓦猫文化的发源地。"
    
    hide caicai with dissolve
    show fufu at left_bottom with dissolve  # 左下角
    f "喵~这里就是我的家乡！魏家古镇有几百年的历史，是我们瓦猫的故乡。"
    
    hide fufu with dissolve
    show caicai at right_bottom with dissolve  # 右下角
    c "古镇的建筑很有特色，青石板路、古色古香的民居，漫步其中仿佛穿越回了古代。"
    
    hide caicai with dissolve
    show fufu at left_bottom with dissolve  # 左下角
    f "你看那些屋顶上的瓦猫雕像，那就是我们瓦猫家族的象征，守护着家家户户的平安。"
    
    hide fufu with dissolve
    show caicai at right_bottom with dissolve  # 右下角
    c "魏家古镇的瓦猫制作工艺是省级非物质文化遗产，每一只瓦猫都是手工精心制作的。"
    
    hide caicai with dissolve
    show fufu at left_bottom with dissolve  # 左下角
    f "古镇里还有瓦猫博物馆，展示了各种造型的瓦猫，从传统到现代，形态各异。"
    
    hide fufu with dissolve
    show caicai at right_bottom with dissolve  # 右下角
    c "每年农历三月三，这里会举办盛大的瓦猫文化节，吸引很多游客前来参观体验。"
    
    hide caicai with dissolve
    show fufu at left_bottom with dissolve  # 左下角
    f "你可以亲手体验制作瓦猫的乐趣，带一只回家保平安，很有纪念意义。"
    
    hide fufu with dissolve
    jump after_attraction

# 景点介绍后的选择
label after_attraction:
    scene background with fade
    # 显示导航按钮
    show screen navigation
    # 显示选择菜单 - 使用与初始菜单相同的样式
    call screen after_attraction_choice
    
    # 根据选择跳转
    if _return == "choose_attraction":
        jump choose_attraction
    elif _return == "end_game":
        jump end_game

# 退出游戏
label end_game:
    stop music channel "background"  # 停止背景音乐
    scene ending with fade
    narrator "感谢您游玩云南景点介绍，期待下次再会！"
    return