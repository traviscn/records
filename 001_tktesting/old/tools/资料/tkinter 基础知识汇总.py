
选项	含义
anchor	1. 对齐方式，左对齐”w”，右对齐”e”，顶对齐”n”，底对齐”s”
        2. “n”, “s”, “w”, “e”, “nw”, “sw”, “se”, “ne”, “center” (默认为” center”)
expand	1. 当值为“yes”时，side选项无效，组件显示在父配件中心位置；若fill选项为”both”,则填充父组件的剩余空间。
        2. 默认值是 False
fill	1. 填充x(y)方向上的空间
        2. 当属性side=”top”或”bottom”时，填充x方向；
        3. 当属性side=”left”或”right”时，填充”y”方向；
        4. 当expand选项为”yes”时，填充父组件的剩余空间。
        5. 默认值是 NONE，表示保持子组件的原始尺寸
        6. 还可以使用的值有："x"（水平填充），"y"（垂直填充）和 "both"（水平和垂直填充）
in_	    1. 将该组件放到该选项指定的组件中
        2. 指定的组件必须是该组件的父组件
ipadx	组件内部在x(y)方向上填充的空间大小，默认单位为像素，可选单位为c（厘米）、m（毫米）、 i（英寸）、p（打印机的点，即1/27英寸），用法为在值后加以上一个后缀既可。
ipady   组件内部在x(y)方向上填充的空间大小，默认单位为像素，可选单位为c（厘米）、m（毫米）、 i（英寸）、p（打印机的点，即1/27英寸），用法为在值后加以上一个后缀既可。
padx    组件外部在x(y)方向上填充的空间大小，默认单位为像素，可选单位为c（厘米）、m（毫米）、 i（英寸）、p（打印机的点，即1/27英寸），用法为在值后加以上一个后缀既可。
pady	组件外部在x(y)方向上填充的空间大小，默认单位为像素，可选单位为c（厘米）、m（毫米）、 i（英寸）、p（打印机的点，即1/27英寸），用法为在值后加以上一个后缀既可。
side	1. 指定组件的放置位置
        2. 默认值是 "top"
        3. 还可以设置的值有："left"，"bottom"，"right"

column      组件所置单元格的列号。	自然数（起始默认值为0，而后累加）
columnspan	从组件所置单元格算起在列方向上的跨度。	自然数（起始默认值为0）
ipadx, ipady	组件内部在x(y)方向上填充的空间大小，默认单位为像素，可选单位为c（厘米）、m（毫米）、 i（英寸）、p（打印机的点，即1/27英寸），用法为在值后加以上一个后缀既可。	非负浮点数（默认值为0.0）
padx, pady	组件外部在x(y)方向上填充的空间大小，默认单位为像素，可选单位为c（厘米）、m（毫米）、 i（英寸）、p（打印机的点，即1/27英寸），用法为在值后加以上一个后缀既可。	非负浮点数（默认值为0.0）
row	        组件所置单元格的行号。	自然数（起始默认值为0，而后累加）
rowspan	    从组件所置单元格算起在行方向上的跨度。	自然数（起始默认值为0）
in_	        将本组件作为所选组建对象的子组件，类似于指定本组件的master为选定组件。	已经pack后的组件对象
sticky	    组件紧靠所在单元格的某一边角。	“n”, “s”, “w”, “e”, “nw”, “sw”, “se”, “ne”, “center” (默认为” center”)

控件	描述
Canvas	画布控件；显示图形元素如线条或文本
Button	按钮控件；在程序中显示按钮。
Checkbutton	多选框控件；用于在程序中提供多项选择框
Radiobutton	单选按钮控件；显示一个单选的按钮状态

Entry	输入控件；用于显示简单的文本内容
Spinbox	输入控件；与Entry类似，但是可以指定输入范围值

LabelFrame	labelframe 是一个简单的容器控件。常用与复杂的窗口布局。
PanedWindow	PanedWindow是一个窗口布局管理的插件，可以包含一个或者多个子控件。
Frame	框架控件；在屏幕上显示一个矩形区域，多用来作为容器
Toplevel	容器控件；用来提供一个单独的对话框，和Frame比较类似

Menu	菜单控件；显示菜单栏,下拉菜单和弹出菜单
Menubutton	菜单按钮控件，由于显示菜单项。
Message	消息控件；用来显示多行文本，与label比较类似
Label	标签控件；可以显示文本和位图
Listbox	列表框控件；在Listbox窗口小部件是用来显示一个字符串列表给用户
Text	文本控件；用于显示多行文本
Scale	范围控件；显示一个数值刻度，为输出限定范围的数字区间
Scrollbar	滚动条控件，当内容超过可视化区域时使用，如列表框。.

tkMessageBox	用于显示你应用程序的消息框。

标准属性
属性	描述
Dimension	控件大小；
Color	控件颜色；
Font	控件字体；
Anchor	锚点；
Relief	控件样式；
Bitmap	位图；
Cursor	光标
text    显示文本内容
state   设置组件状态为正常（normal），激活（active）或禁用（disable）


（font family, size ,modifiers）
例:
for ft in (('Arial',('Times New Roman','3','italic'))
    Label(win,text='Hello,my dream world',font=ft)


ft=tkFont.Font((family='Fixdays',size=20,weight='bold',slant='italic',underline=1，overstrik=1))
family  字体名
size    大小
weight  粗体：bold或normal或不写
slant   斜体：italic或normal或不写
underline   下划线
overstrik   删除线


例：
<Button-1>      按下鼠标左键
<KeyPress-A>    按下键盘上的A
<Control-Shift-KeyPress-A>  同时按下Control、Shift和A三个键

键盘事件：KeyPress、KeyRelease
鼠标事件：ButtonPres或Button、ButtonReleas、Motion(点击组件并拖拽)、Enter、Leave、MouseWheel
窗体事件：Visibility、Unmap、Map、Expose、FocusIn、FocusOut、Configure、Property、Destroy、Activate、Deactivate
组合键修饰符：Alt、Any、Control、Double、Lock（Caps Lock键）、Shift、Triple

activebackground, activeforeground, anchor,
background, bitmap, borderwidth, cursor,
disabledforeground, font, foreground,
highlightbackground, highlightcolor,
highlightthickness, image, justify,
padx, pady, relief, takefocus, text,
textvariable, underline, wraplength
height, state, widt
# Booleans
NO=FALSE=OFF=0
YES=TRUE=ON=1
# -anchor and -sticky
N='n'
S='s'
W='w'
E='e'
NW='nw'
SW='sw'
NE='ne'
SE='se'
NS='ns'
EW='ew'
NSEW='nsew'
CENTER='center'
# -fill
NONE='none'
X='x'
Y='y'
BOTH='both'
# -side
LEFT='left'
TOP='top'
RIGHT='right'
BOTTOM='bottom'
# -relief
RAISED='raised'
SUNKEN='sunken'
FLAT='flat'
RIDGE='ridge'
GROOVE='groove'
SOLID = 'solid'
# -orient
HORIZONTAL='horizontal'
VERTICAL='vertical'
# -tabs
NUMERIC='numeric'
# -wrap
CHAR='char'
WORD='word'
# -align
BASELINE='baseline'
# -bordermode
INSIDE='inside'
OUTSIDE='outside'
# Special tags, marks and insert positions
SEL='sel'
SEL_FIRST='sel.first'
SEL_LAST='sel.last'
END='end'
INSERT='insert'
CURRENT='current'
ANCHOR='anchor'
ALL='all' # e.g. Canvas.delete(ALL)
# Text widget and button states
NORMAL='normal'
DISABLED='disabled'
ACTIVE='active'
# Canvas state
HIDDEN='hidden'
# Menu item types
CASCADE='cascade'
CHECKBUTTON='checkbutton'
COMMAND='command'
RADIOBUTTON='radiobutton'
SEPARATOR='separator'
# Selection modes for list boxes
SINGLE='single'
BROWSE='browse'
MULTIPLE='multiple'
EXTENDED='extended'
# Activestyle for list boxes
# NONE='none' is also valid
DOTBOX='dotbox'
UNDERLINE='underline'
# Various canvas styles
PIESLICE='pieslice'
CHORD='chord'
ARC='arc'
FIRST='first'
LAST='last'
BUTT='butt'
PROJECTING='projecting'
ROUND='round'
BEVEL='bevel'
MITER='miter'
# Arguments to xview/yview
MOVETO='moveto'
SCROLL='scroll'
UNITS='units'
PAGES='pages'
