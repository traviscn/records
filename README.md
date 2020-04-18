
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


### 全封装工具


CPython 开发GUIUI界面
界面收集的的数据与脚本进行整合
通

过批处理方式

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
