# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QPixmap, QDesktopServices

from . import wx,alipay

class Ui_infoform(object):
    def setupUi(self, infoform):
        infoform.setObjectName("infoform")
        infoform.setWindowModality(QtCore.Qt.NonModal)
        infoform.resize(800, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(infoform.sizePolicy().hasHeightForWidth())
        infoform.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(infoform)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(infoform)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.anchorClicked.connect(self.openExternalLink)
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.retranslateUi(infoform)
        QtCore.QMetaObject.connectSlotsByName(infoform)
    def openExternalLink(self, url):
        # Open the link in the system browser
        QDesktopServices.openUrl(url)

    def retranslateUi(self, infoform):
        _translate = QtCore.QCoreApplication.translate
        infoform.setWindowTitle(_translate("infoform", "捐助该软件以便持续维护"))
        self.textBrowser.setHtml(_translate("infoform", """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;">
<h1 style=" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:xx-large; font-weight:600;">捐助该软件以便能够持续维护 Donate to this project and support</span></h1>
<hr />
<p><a href="https://ko-fi.com/jianchang512"> 👑 Donate buy me a coffee </a></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">本项目基于兴趣创建，在可预期的未来都没有商业计划，也就是你可以一直免费使用，或者fork后自己修改。不用担心收费问题。</p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">至于维护问题呢，开源嘛都是用爱发电，闲时就多花些精力在这上面，忙时可能就一段时间顾不上。当然了，如果觉得该项目对你有价值，并希望该项目能一直稳定持续维护，也欢迎小额捐助。</p>
<hr />
<h2 style=" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:x-large; font-weight:600;">如何捐助</span></h2>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">你可以向微信或支付宝二维码付款，备注你的github名称</p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src=":/png/wx.png" width="240" /></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src=":/png/alipay.png" width="240" /></p>
<hr />
<h2 style=" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:x-large; font-weight:600;">感谢所有捐助者</span></h2>
<h2 style="-qt-paragraph-type:empty; margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:x-large; font-weight:600;"><br /></h2>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style="margin:5px;padding:5px;">wonyes 2023-11-20 捐助100元 </span> /  
<span style="margin:5px;padding:5px;">yuppiesnotzhuhao  2023-12-01 捐助10元 </span> /  
<span style="margin:5px;padding:5px;">9*9  2023-12-02 捐助10元 </span> /  
<span style="margin:5px;padding:5px;">*s  2023-12-7 捐助 10 元 </span> /  
<span style="margin:5px;padding:5px;">汪*X  2023-12-10 捐助 0.6 元 </span> /  
<span style="margin:5px;padding:5px;">*兄  2023-12-12 捐助 1 元 </span> /  
<span style="margin:5px;padding:5px;">*辰  2023-12-13 捐助 5 元 </span> /  
<span style="margin:5px;padding:5px;">喵の左爪/19225866  2023-12-18 捐助5元 </span> / 
<span style="margin:5px;padding:5px;">ID:BigD-a-yi2023-12-20  捐助10元 </span> /  
<span style="margin:5px;padding:5px;">*D  2023-12-20 捐助 10 元 </span> /  
<span style="margin:5px;padding:5px;">*溪  2023-12-22 捐助 5 元 </span> /  
<span style="margin:5px;padding:5px;">*星  2023-12-23 捐助 66 元 </span> /  
<span style="margin:5px;padding:5px;">F*f  2023-12-24 捐助 10 元 </span> /  
<span style="margin:5px;padding:5px;">*玲  2023-12-25 捐助 10 元 </span> /  
<span style="margin:5px;padding:5px;">laowangtou-888  2023-12-25 100 元 </span> /  
<span style="margin:5px;padding:5px;">铁*  2023-12-29 捐助 5 元 </span> /  
<span style="margin:5px;padding:5px;">dingsmart  2024-1-1 捐助 100 元 </span> /  
<span style="margin:5px;padding:5px;">*王  2024-1-1 捐助 50 元 </span> /  
<span style="margin:5px;padding:5px;">*想  2024-1-2 捐助 2.88 元 </span> /  
<span style="margin:5px;padding:5px;">*)  2024-1-6 捐助 50 元 </span> /  
<span style="margin:5px;padding:5px;">*道  2024-1-6 捐助 20 元 </span> /  
<span style="margin:5px;padding:5px;">*剑  2024-1-6 捐助 8 元 </span> /  
<span style="margin:5px;padding:5px;">o*u  2024-1-9 捐助 100 元 </span> /  
<span style="margin:5px;padding:5px;"><a href="https://github.com/qxk2005">qxk2005</a>  2024-1-9 捐助 100 元 </span> /  
<span style="margin:5px;padding:5px;"><a href="https://space.bilibili.com/19225866">喵の左爪 2024-1-11 捐助10元</a></span> /
<span style="margin:5px;padding:5px;">*泉 2024-1-11 捐助 6.6 元</span> /
<span style="margin:5px;padding:5px;">*匐 2024-1-11 捐助 20 元</span> /
<span style="margin:5px;padding:5px;">m*o 2024-1-11 捐助 1.0 元</span> /
<span style="margin:5px;padding:5px;">*工 2024-1-12 捐助 10 元</span> /
<span style="margin:5px;padding:5px;"><a href="https://github.com/maotouying0102">maotouying0102 2024-1-12 捐助 10 元</a></span> /
<span style="margin:5px;padding:5px;"><a href="https://github.com/super5hunz1">super5hunz1 2024-1-13 捐助 16.66 元</a></span> /
<span style="margin:5px;padding:5px;"><a href="https://github.com/zhulinzhao">zhulinzhao 2024-1-14 捐助 5 元</a></span> /
<span style="margin:5px;padding:5px;"><a href="https://github.com/darksiderlyd">darksiderlyd 2024-1-14 捐助 20 元</a></span> /
<span style="margin:5px;padding:5px;"><a href="https://github.com/againstthewindtofly">againstthewindtofly 2024-1-15 捐助 50 元</a></span> /
<span style="margin:5px;padding:5px;"><a href="https://github.com/wxxvc">wxxvc 2024-1-16 捐助 10 元</a></span> /
<span style="margin:5px;padding:5px;"><a href="https://space.bilibili.com/19225866">喵の左爪 2024-1-16 捐助5元</a></span> /

<span style="margin:5px;padding:5px;"> *眼  2024-1-20 捐助 8.88 元</span> / 
<span style="margin:5px;padding:5px;"> *工  2024-1-21 捐助 10 元</span> / 
<span style="margin:5px;padding:5px;"> D*t  2024-1-21 捐助 10 元</span> / 
<span style="margin:5px;padding:5px;"> L*N  2024-1-23 捐助 5 元</span> / 
<span style="margin:5px;padding:5px;"> M*  2024-1-24 捐助 10 元</span> / 
<span style="margin:5px;padding:5px;"> m*l  2024-1-24 捐助 10 元</span> / 
<span style="margin:5px;padding:5px;"> *生  2024-1-25 捐助 18.88 元</span> / 
<span style="margin:5px;padding:5px;">w*d  2024-1-26 捐助 6.66 元</span> / 
<span style="margin:5px;padding:5px;">*.  2024-1-27 捐助 0.15 元</span> / 
<span style="margin:5px;padding:5px;">*明  2024-1-29 捐助 20 元</span> / 
<span style="margin:5px;padding:5px;">5*)  2024-1-30 捐助 10 元</span> / 
<span style="margin:5px;padding:5px;">rqi14(U*d)  2024-1-30 捐助 200 元</span> / 
<span style="margin:5px;padding:5px;">*明   2024-1-29 捐助 20 元</span> / 
<span style="margin:5px;padding:5px;">*骁(支付宝)   2024-1-29 捐助 2 元</span> / 
<span style="margin:5px;padding:5px;">5*)   2024-1-30 捐助 10 元</span> / 
<span style="margin:5px;padding:5px;">rqi14(U*d)   2024-1-30 捐助 200 元</span> / 
<span style="margin:5px;padding:5px;">*正  2024-1-30 捐助 10 元</span> / 
<span style="margin:5px;padding:5px;">i*8   2024-1-31 捐助 18 元</span> / 
<span style="margin:5px;padding:5px;">*.   2024-2-1 捐助 10 元</span> / 
<span style="margin:5px;padding:5px;">*途   2024-2-1 捐助 30 元</span> / 
<span style="margin:5px;padding:5px;">*甜(bingsunny0730)   2024-2-2 捐助 1.68 元</span> / 
<span style="margin:5px;padding:5px;">k*v   2024-2-2 捐助 10 元</span> / 
<span style="margin:5px;padding:5px;">*林(xjsszl)   2024-2-2 捐助 10 元</span> / 
<span style="margin:5px;padding:5px;">**宇(支付宝)   2024-2-2 捐助 10 元</span> / 
<span style="margin:5px;padding:5px;">*彦  2024-2-3 捐助 10 元</span> | 
<span style="margin:5px;padding:5px;">*遡  2024-2-6 捐助 20 元</span> | 
<span style="margin:5px;padding:5px;">*程(支付宝)  2024-2-6 捐助 50 元</span> | 
<span style="margin:5px;padding:5px;">*豪(支付宝)  2024-2-7 捐助 8.8 元</span> | 
<span style="margin:5px;padding:5px;">*u  2024-2-8 捐助 20 元</span> | 
<span style="margin:5px;padding:5px;">*哦  2024-2-8 捐助 10 元</span> | 
<span style="margin:5px;padding:5px;">*u  2024-2-9 捐助 30 元</span> | 
<span style="margin:5px;padding:5px;">*许  2024-2-10 捐助 10 元</span> | 
<span style="margin:5px;padding:5px;">*伟(支付宝)  2024-2-10 捐助 88.88 元</span> | 

</p>
<p><a href="https://github.com/jianchang512/pyvideotrans/blob/main/about.md">全部捐助列表</a></p>
<p style="-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#00aa00;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#00aa00;"><br /></p></body></html>
"""))
