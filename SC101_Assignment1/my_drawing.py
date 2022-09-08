"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow

window = GWindow(1200, 600, "pic")


def main():
    """
    Title: 如何不使用GLine製造斜線

    第一眼看過去會覺得圖片中的線是斜的或彎的，但其如果仔細看的話會發現其實他們都是直線!
    這個現象就叫視覺錯覺! 希望有騙到你~
    """
    rect01()
    square02()
    square103()
    square204()
    square305()
    square406()
    square507()
    rect108()
    square2009()
    square2110()
    square2211()
    square2312()
    square2413()
    square2514()
    rect215()
    square3016()
    square3117()
    square3218()
    square3319()
    square3420()
    square3521()
    rect322()
    square4023()
    square4124()
    square4225()
    square4326()
    square4427()
    square4528()
    rect429()
    square5030()
    square5131()
    square5232()
    square5333()
    square5434()
    square5535()
    rect536()
    square6037()
    square6138()
    square6239()
    square6340()
    square6441()
    square6542()
    rect643()


def rect01():
    rect = GRect(1200, 5, x=0, y=0)
    rect.filled = True
    rect.fill_color = 'grey'
    rect.color = 'grey'
    window.add(rect)


def square02():
    square = GRect(100, 100, x=30, y=5)
    square.filled = True
    square.fill_color = 'black'
    square.color = 'grey'
    window.add(square)


def square103():
    square1 = GRect(100, 100, x=230, y=5)
    square1.filled = True
    square1.fill_color = 'black'
    square1.color = 'grey'
    window.add(square1)


def square204():
    square2 = GRect(100, 100, x=430, y=5)
    square2.filled = True
    square2.fill_color = 'black'
    square2.color = 'grey'
    window.add(square2)


def square305():
    square3 = GRect(100, 100, x=630, y=5)
    square3.filled = True
    square3.fill_color = 'black'
    square3.color = 'grey'
    window.add(square3)


def square406():
    square4 = GRect(100, 100, x=830, y=5)
    square4.filled = True
    square4.fill_color = 'black'
    square4.color = 'grey'
    window.add(square4)


def square507():
    square5 = GRect(100, 100, x=1030, y=5)
    square5.filled = True
    square5.fill_color = 'black'
    square5.color = 'grey'
    window.add(square5)


def rect108():
    rect1 = GRect(1200, 5, x=0, y=100)
    rect1.filled = True
    rect1.fill_color = 'grey'
    rect1.color = 'grey'
    window.add(rect1)


def square2009():
    square = GRect(100, 100, x=60, y=105)
    square.filled = True
    square.fill_color = 'black'
    square.color = 'grey'
    window.add(square)


def square2110():
    square21 = GRect(100, 100, x=260, y=105)
    square21.filled = True
    square21.fill_color = 'black'
    square21.color = 'grey'
    window.add(square21)


def square2211():
    square22 = GRect(100, 100, x=460, y=105)
    square22.filled = True
    square22.fill_color = 'black'
    square22.color = 'grey'
    window.add(square22)


def square2312():
    square23 = GRect(100, 100, x=660, y=105)
    square23.filled = True
    square23.fill_color = 'black'
    square23.color = 'grey'
    window.add(square23)


def square2413():
    square24 = GRect(100, 100, x=860, y=105)
    square24.filled = True
    square24.fill_color = 'black'
    square24.color = 'grey'
    window.add(square24)


def square2514():
    square25 = GRect(100, 100, x=1060, y=105)
    square25.filled = True
    square25.fill_color = 'black'
    square25.color = 'grey'
    window.add(square25)


def rect215():
    rect2 = GRect(1200, 5, x=0, y=200)
    rect2.filled = True
    rect2.fill_color = 'grey'
    rect2.color = 'grey'
    window.add(rect2)


def square3016():
    square30 = GRect(100, 100, x=90, y=205)
    square30.filled = True
    square30.fill_color = 'black'
    square30.color = 'grey'
    window.add(square30)


def square3117():
    square31 = GRect(100, 100, x=290, y=205)
    square31.filled = True
    square31.fill_color = 'black'
    square31.color = 'grey'
    window.add(square31)


def square3218():
    square32 = GRect(100, 100, x=490, y=205)
    square32.filled = True
    square32.fill_color = 'black'
    square32.color = 'grey'
    window.add(square32)


def square3319():
    square33 = GRect(100, 100, x=690, y=205)
    square33.filled = True
    square33.fill_color = 'black'
    square33.color = 'grey'
    window.add(square33)


def square3420():
    square34 = GRect(100, 100, x=890, y=205)
    square34.filled = True
    square34.fill_color = 'black'
    square34.color = 'grey'
    window.add(square34)


def square3521():
    square35 = GRect(100, 100, x=1090, y=205)
    square35.filled = True
    square35.fill_color = 'black'
    square35.color = 'grey'
    window.add(square35)


def rect322():
    rect3 = GRect(1200, 5, x=0, y=300)
    rect3.filled = True
    rect3.fill_color = 'grey'
    rect3.color = 'grey'
    window.add(rect3)


def square4023():
    square40 = GRect(100, 100, x=60, y=305)
    square40.filled = True
    square40.fill_color = 'black'
    square40.color = 'grey'
    window.add(square40)


def square4124():
    square41 = GRect(100, 100, x=260, y=305)
    square41.filled = True
    square41.fill_color = 'black'
    square41.color = 'grey'
    window.add(square41)


def square4225():
    square42 = GRect(100, 100, x=460, y=305)
    square42.filled = True
    square42.fill_color = 'black'
    square42.color = 'grey'
    window.add(square42)


def square4326():
    square43 = GRect(100, 100, x=660, y=305)
    square43.filled = True
    square43.fill_color = 'black'
    square43.color = 'grey'
    window.add(square43)


def square4427():
    square44 = GRect(100, 100, x=860, y=305)
    square44.filled = True
    square44.fill_color = 'black'
    square44.color = 'grey'
    window.add(square44)


def square4528():
    square45 = GRect(100, 100, x=1060, y=305)
    square45.filled = True
    square45.fill_color = 'black'
    square45.color = 'grey'
    window.add(square45)


def rect429():
    rect4 = GRect(1200, 5, x=0, y=400)
    rect4.filled = True
    rect4.fill_color = 'grey'
    rect4.color = 'grey'
    window.add(rect4)


def square5030():
    square50 = GRect(100, 100, x=30, y=405)
    square50.filled = True
    square50.fill_color = 'black'
    square50.color = 'grey'
    window.add(square50)


def square5131():
    square51 = GRect(100, 100, x=230, y=405)
    square51.filled = True
    square51.fill_color = 'black'
    square51.color = 'grey'
    window.add(square51)


def square5232():
    square52 = GRect(100, 100, x=430, y=405)
    square52.filled = True
    square52.fill_color = 'black'
    square52.color = 'grey'
    window.add(square52)


def square5333():
    square53 = GRect(100, 100, x=630, y=405)
    square53.filled = True
    square53.fill_color = 'black'
    square53.color = 'grey'
    window.add(square53)


def square5434():
    square54 = GRect(100, 100, x=830, y=405)
    square54.filled = True
    square54.fill_color = 'black'
    square54.color = 'grey'
    window.add(square54)


def square5535():
    square55 = GRect(100, 100, x=1030, y=405)
    square55.filled = True
    square55.fill_color = 'black'
    square55.color = 'grey'
    window.add(square55)


def rect536():
    rect5 = GRect(1200, 5, x=0, y=500)
    rect5.filled = True
    rect5.fill_color = 'grey'
    rect5.color = 'grey'
    window.add(rect5)


def square6037():
    square60 = GRect(100, 100, x=60, y=505)
    square60.filled = True
    square60.fill_color = 'black'
    square60.color = 'grey'
    window.add(square60)


def square6138():
    square61 = GRect(100, 100, x=260, y=505)
    square61.filled = True
    square61.fill_color = 'black'
    square61.color = 'grey'
    window.add(square61)


def square6239():
    square62 = GRect(100, 100, x=460, y=505)
    square62.filled = True
    square62.fill_color = 'black'
    square62.color = 'grey'
    window.add(square62)


def square6340():
    square63 = GRect(100, 100, x=660, y=505)
    square63.filled = True
    square63.fill_color = 'black'
    square63.color = 'grey'
    window.add(square63)


def square6441():
    square64 = GRect(100, 100, x=860, y=505)
    square64.filled = True
    square64.fill_color = 'black'
    square64.color = 'grey'
    window.add(square64)


def square6542():
    square65 = GRect(100, 100, x=1060, y=505)
    square65.filled = True
    square65.fill_color = 'black'
    square65.color = 'grey'
    window.add(square65)


def rect643():
    rect6 = GRect(1200, 5, x=0, y=595)
    rect6.filled = True
    rect6.fill_color = 'grey'
    rect6.color = 'grey'
    window.add(rect6)

if __name__ == '__main__':
    main()
