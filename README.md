
# records


## 开发形式


### 脚本工具


在软件界面


增加功能按钮，点击弹出GUI，内置的IronPython 的

WinFormMSDN 。Net4.0 帮助文档
开发
不用每次打开脚本编辑，把要修改的参数放到界面中
脚

本 脚本封装到GUI
脚本开发（脚本参数化函数化封装）结合IronPython界面开

发，界面控件绑定脚本，发布到工具组
平台
Script Editor

import clr

clr.AddReference(‘System.Windows.Form')
clr.AddReference(‘System.Drawing’)

import System.Windows.Form
import System.Drawing

from System.Windows.Form import *

类编写窗体

SharpDevelop工具 可以实现IronPython的可视化界面编程，

可以通过拖拽控件实现，适当修改，MainForm

().showdialog()

脚本参数化函数封装
def BrigeGen(brgLength):
	pass

事件绑定
self._btnGenClick += self.btnGenClicked

def btnClicked(self,sender ,event):
	brgLength = float(self._txtLength.Text)

	BrigeGen(brgLength)
	
	


### ACT插件


在软件界面
XML技术
脚本技术
操作向导
半封装，界面操作ACT

向导同时操

脚本化的ACT插件= XML文件+ IronPython脚本文件=编译=二

进制的WwX文件

Optional （HEML）自定义说明帮助文档

脚本文件夹 与 XML文件 放在同一个文件夹 并且要同名

XML文件：定义UI界面内容，插件属性，事件与脚本函数绑定 

回调函数

标记语言 携带数据 如材料属性的定义
标记 不同程序都有自己的标记 ACT也有自己的标记
标签 <> </>
节点 
元素
元素属性
注释<!--    -->
'''
<extension>定义
   <wizard>定义
	<step>定义
		<property>
		<propertyGroup>
			<Control>
<callbacks>
'''
XML 文件结构不熟悉 编写不方便

可以通过可视化Appbuild创建
高级的空间 可以通过 在当前界面显示XML编辑器,在当前窗

口显，有一点显示差异

OptionalAttributes: 
Caption  
Property

回调函数绑定脚本代码


IronPython 脚本
实现插件的功能书写，定义事件的调用函数（事件驱动），

支持外部库的访问

保存 导出脚本扩展 xxx.XML

简化XML文件删除无效代码 为了后期的维护

xml文件中 

<script src="main.py"/>
同名文件夹下，Image文件夹 Help文件夹 用户帮助文档HTML

界面美化

图标位置 

<interface context= "SpaceClaim">
<images> images</images>
</interface>

注意相对路径

<callbacks>
 <onupdate> onundateGeoStep</onupdate>
 <onreset> <> 上一步
</callbacks>



main.py
封装
morenbianma shi ASCII 
# encoding: utf-8
ACT Console 默认没有导入，需要重新定义
def clearAll():


def CreateGeo(length windth)：


def onupdateGeoStep(step):
获取界面值
bladeWindth = step.Propertities

["grp/bladewindth"].Value
调用函数
CreateGeo(bladeWindth)



def onupdateNsStep(step):

获取值判断

Application.Helper.ReportInformation("OK")

加载到WB 打开log 可以记录提示,
ShareTolopoly.FindANdFix（）

ACT console类 与 解释器类 不一致
涉及到API调用
打开ACTconsole
clr.reference ACT控制台引用的类库
SpaceClame V17API 涉及到新功能
clr.AppReference("spaceClaim.Api.V18")

From spaceClaim.ApiV18 import 
缺库补充

Build 3rd
'''<script src="main.py" compiled=True/>'''


### 
### 全封装工具


CPython 开发GUIUI界面
1.获取界面输入 2.修改脚本参数 3.批处理调用 4.用户体验的状态显示框
5.测试 6.打包发布

Tkinter Classes 获取常用控件的帮助
结构： 根窗体root 菜单栏 状态栏 控件 容器


面向过程的不利于代码管理
面对对象的封装 类编程

'''
# encoding：utf-8




'''



界面收集的的数据与脚本进行整合
通过批处理方式
设计到GUI开发多线程问题




### Workbench集成
workflow

全流程
WB 架构（提供接口 通过WBPython集成应用 扩展程序类似于

插件形式？）     工作区（内部操作的修改都会被WB脚本录

制记录）

WB结构 与工作区区别？？工作区不就是WB打开的界面吗？？

？？

数据集成软件（NAtive script language （CCL））

script 跟 journal区别？？？



WB 支持脚本录制 File Script records WBPython脚本

录制WB操作，内部的集成软件就不支持录制了

录制脚本适当修改

SendCommand  在WB界面发送脚本到集成软件执行，驱动集成

软件

交互性有待提高，执行过程中看不到过程 一行一行复制脚本
可以执行F5吗？？


geometry(SCDM) mechanical
geometry fluentmeshing 


WB平台以ACT插件形式封装

混合向导？WB向导 转到 SCDM向导
可以调试过程找原因？？通过调试执行
