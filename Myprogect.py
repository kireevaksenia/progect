import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QColor


class Sun_system(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(50, 50, 900, 300)
        self.setWindowTitle('Солнечная система')

        self.label = QLabel(self)
        self.label.setText("Зажми курсор на белом поле и наведи на планету, информацию о которой хочешь узнать")
        self.label.move(40, 30)
        self.label.resize(self.label.sizeHint())

        self.labeldown = QLabel(self)
        self.labeldown.setText("Космос намного больше, чем ты думаешь "
                               "(попробуй немного расширить границы окна)")
        self.labeldown.move(60, 260)
        self.labeldown.resize(self.labeldown.sizeHint())

        self.label = QLabel(self)
        self.label.setText("Какая-нибудь из этих звез, возможно,"
                           " будет названа твоим именем!")
        self.label.move(60, 400)
        self.label.resize(self.label.sizeHint())

        self.Mer = QLabel(self)
        self.Mer.setText("Меркурий")
        self.Mer.move(780, 175)

        self.Ven = QLabel(self)
        self.Ven.setText("Венера")
        self.Ven.move(710, 80)

        self.Ear = QLabel(self)
        self.Ear.setText("Земля")
        self.Ear.move(620, 180)

        self.Mars = QLabel(self)
        self.Mars.setText("Марс")
        self.Mars.move(535, 90)

        self.Jup = QLabel(self)
        self.Jup.setText("Юпитер")
        self.Jup.move(420, 195)

        self.Sat = QLabel(self)
        self.Sat.setText("Сатурн")
        self.Sat.move(290, 80)

        self.Ur = QLabel(self)
        self.Ur.setText("Уран")
        self.Ur.move(180, 200)

        self.Nep = QLabel(self)
        self.Nep.setText("Нептун")
        self.Nep.move(65, 90)
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawPlanet(qp)
        qp.end()

    def drawPlanet(self, qp):
        qp.setBrush(QColor(229, 83, 0))  # создаум солнце
        qp.drawEllipse(850, 20, 250, 250)

        qp.setBrush(QColor(169, 169, 169))  # создаем Меркурий
        qp.drawEllipse(780, 120, 40, 40)

        qp.setBrush(QColor(248, 222, 126))  # создаем Венеру
        qp.drawEllipse(690, 105, 70, 70)

        qp.setBrush(QColor(102, 185, 52))  # создаем Землю
        qp.drawEllipse(600, 105, 70, 70)

        qp.setBrush(QColor(165, 30, 35))  # создаем Марс
        qp.drawEllipse(520, 110, 60, 60)

        qp.setBrush(QColor(218, 165, 32))  # создаем Юпитер
        qp.drawEllipse(390, 90, 100, 100)

        qp.setBrush(QColor(253, 165, 15))  # создаем Сатурн
        qp.drawEllipse(265, 100, 85, 85)

        qp.setBrush(QColor(0, 128, 255))  # сщздаем Уран
        qp.drawEllipse(155, 110, 75, 75)

        qp.setBrush(QColor(101, 147, 245))  # сщздаем Нептун
        qp.drawEllipse(50, 120, 65, 65)

        qp.setBrush(QColor(184, 15, 10))
        qp.drawEllipse(320, 300, 20, 20)

        qp.setBrush(QColor(0, 142, 204))
        qp.drawEllipse(100, 320, 10, 10)

        qp.setBrush(QColor(238, 130, 238))
        qp.drawEllipse(30, 370, 30, 30)

        qp.setBrush(QColor(0, 142, 204))
        qp.drawEllipse(190, 305, 10, 10)

        qp.setBrush(QColor(184, 15, 10))
        qp.drawEllipse(240, 350, 40, 40)

        qp.setBrush(QColor(0, 142, 204))
        qp.drawEllipse(308, 310, 5, 5)

        qp.setBrush(QColor(0, 142, 204))
        qp.drawEllipse(400, 360, 10, 10)

        qp.setBrush(QColor(238, 130, 238))
        qp.drawEllipse(450, 310, 20, 20)

        qp.setBrush(QColor(0, 142, 204))
        qp.drawEllipse(470, 340, 10, 10)

        qp.setBrush(QColor(0, 142, 204))
        qp.drawEllipse(520, 300, 30, 30)

        qp.setBrush(QColor(0, 142, 204))
        qp.drawEllipse(600, 380, 15, 15)

        qp.setBrush(QColor(184, 15, 10))
        qp.drawEllipse(620, 400, 20, 20)

        qp.setBrush(QColor(238, 130, 238))
        qp.drawEllipse(650, 390, 10, 10)

        qp.setBrush(QColor(184, 15, 10))
        qp.drawEllipse(690, 310, 40, 40)

        qp.setBrush(QColor(0, 142, 204))
        qp.drawEllipse(750, 400, 20, 20)

        qp.setBrush(QColor(0, 142, 204))
        qp.drawEllipse(800, 350, 5, 5)

        qp.setBrush(QColor(0, 142, 204))
        qp.drawEllipse(890, 340, 15, 15)

    def mouseMoveEvent(self, event):
        if 50 < event.x() < 115:
            if 120 < event.y() < 185:  # определяем рамки, с помощью которых можно будет открывать новые окна
                Neptune.show()
        elif 155 < event.x() < 190:
            if 110 < event.y() < 185:
                Uranus.show()
        elif 265 < event.x() < 350:
            if 100 < event.y() < 185:
                Saturn.show()
        elif 390 < event.x() < 490:
            if 90 < event.y() < 190:
                Jupiter.show()
        elif 520 < event.x() < 580:
            if 110 < event.y() < 170:
                Mars.show()
        elif 600 < event.x() < 670:
            if 105 < event.y() < 175:
                Earth.show()
        elif 690 < event.x() < 760:
            if 105 < event.y() < 175:
                Venus.show()
        elif 780 < event.x() < 820:
            if 120 < event.y() < 160:
                Mercury.show()
        elif 850 < event.x() < 1000:
            if 20 < event.y() < 270:
                Sun.show()


class Neptune(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Солнечная система')

        self.label = QLabel(self)
        self.label.setText("Непту́н — восьмая и самая дальняя от Земли\n"
                           " планета Солнечной системы. Нептун также\n"
                           " является четвёртой по диаметру и третьей\n"
                           " по массе планетой. Масса Нептуна в 17,2 раза,\n"
                           " а диаметр экватора в 3,9 раза больше земных.\n"
                           " Планета была названа в честь римского\n"
                           " бога морей. Её астрономический символ Neptune\n"
                           "— стилизованная версия трезубца Нептуна.\n"
                           "\n"
                           "Вы можете посмотреть информацию о ближайших\n"
                           "планетах:")
        self.label.move(40, 30)
        self.label.resize(self.label.sizeHint())

        self.btn = QPushButton('Уран', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 190)
        self.btn.clicked.connect(self.uran)

    def uran(self):
        Uranus.show()
        Neptune.hide()


class Uranus(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Солнечная система')

        self.label = QLabel(self)
        self.label.setText("Ура́н — планета Солнечной системы, седьмая\n"
                           " по удалённости от Солнца, третья по диаметру\n"
                           " и четвёртая по массе. Была открыта в 1781 году\n"
                           " английским астрономом Уильямом Гершелем и\n"
                           " названа в честь греческого бога неба Урана.\n "
                           "Уран стал первой планетой, обнаруженной в\n"
                           " Новое время и при помощи телескопа. Его\n"
                           " открыл Уильям Гершель 13 марта 1781 года,\n"
                           " тем самым впервые со времён античности\n"
                           " расширив границы Солнечной системы в\n"
                           " глазах человека. Несмотря на\n"
                           " то, что порой Уран различим невооружённым\n"
                           " глазом, более ранние наблюдатели принимали\n"
                           " его за тусклую звезду.\n"
                           "\n"
                           "Вы можете посмотреть информацию о ближайших\n"
                           "планетах:")
        self.label.move(40, 30)
        self.label.resize(self.label.sizeHint())

        self.btn = QPushButton('Cатурн', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(30, 260)
        self.btn.clicked.connect(self.sat)

        self.btn = QPushButton('Нептун', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(200, 260)
        self.btn.clicked.connect(self.nep)

    def sat(self):
        Saturn.show()
        Uranus.hide()

    def nep(self):
        Neptune.show()
        Uranus.hide()


class Saturn(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Солнечная система')

        self.label = QLabel(self)
        self.label.setText("Сату́рн — шестая планета от Солнца и вторая\n"
                           " по размерам планета в Солнечной системе\n"
                           " после Юпитера. Сатурн, а также Юпитер,\n"
                           " Уран и Нептун, классифицируются как газовые\n"
                           " гиганты. Сатурн назван в честь римского бога\n"
                           " земледелия.Символ Сатурна — серп.")
        self.label.move(40, 30)
        self.label.resize(self.label.sizeHint())

        self.label1 = QLabel(self)
        self.label1.setText("Вы можете посмотреть информацию о ближайших\n"
                            "планетах:")

        self.label1.move(40, 230)
        self.label1.resize(self.label1.sizeHint())

        self.btn = QPushButton('Уран', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(30, 260)
        self.btn.clicked.connect(self.uran)

        self.btn = QPushButton('Юпитер', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(200, 260)
        self.btn.clicked.connect(self.jup)

    def uran(self):
        Saturn.hide()
        Uranus.show()

    def jup(self):
        Jupiter.show()
        Saturn.hide()


class Jupiter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Солнечная система')

        self.label = QLabel(self)
        self.label.setText("Юпи́тер — крупнейшая планета Солнечной\n"
                           " системы, пятая по удалённости от Солнца.\n"
                           " Наряду с Сатурном, Ураном и Нептуном,\n"
                           " Юпитер классифицируется как газовый гигант.\n"
                           "Планета была известна людям с глубокой\n"
                           " древности, что нашло своё отражение в\n"
                           " мифологии и религиозных верованиях\n"
                           " различных культур: месопотамской,\n"
                           " вавилонской, греческой и других. Современное\n"
                           " название Юпитера происходит от имени\n"
                           " древнеримского верховного бога-громовержца.")
        self.label.move(40, 30)
        self.label.resize(self.label.sizeHint())

        self.label1 = QLabel(self)
        self.label1.setText("Вы можете посмотреть информацию о ближайших\n"
                            "планетах:")

        self.label1.move(40, 230)
        self.label1.resize(self.label1.sizeHint())

        self.btn = QPushButton('Сатурн', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(30, 260)
        self.btn.clicked.connect(self.sat)

        self.btn = QPushButton('Марс', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(200, 260)
        self.btn.clicked.connect(self.mars)

    def sat(self):
        Saturn.show()
        Jupiter.hide()

    def mars(self):
        Mars.show()
        Jupiter.hide()


class Mars(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Солнечная система')

        self.label = QLabel(self)
        self.label.setText("Марс — четвёртая по удалённости от Солнца\n"
                           " и седьмая по размерам планета Солнечной\n системы;"
                           " масса планеты составляет 10,7 %\n массы Земли."
                           " Названа в честь Марса — \nдревнеримского бога"
                           " войны, соответствующего\n древнегреческому Аресу."
                           " Иногда Марс называют\n «красной планетой» из-за"
                           " красноватого оттенка\n"
                           " поверхности, придаваемого ей минералом\n"
                           " маггемитом — γ-оксидом железа(III).\n"
                           "Марс — планета земной группы\n"
                           " с разреженной атмосферой. Особенностями\n"
                           " поверхностного рельефа Марса можно считать\n"
                           " ударные кратеры наподобие лунных, а также\n"
                           " вулканы, долины, пустыни и полярные\n"
                           " ледниковые шапки наподобие земных.")

        self.label.move(40, 30)
        self.label.resize(self.label.sizeHint())

        self.label1 = QLabel(self)
        self.label1.setText("Вы можете посмотреть информацию о ближайших\n"
                            "планетах:")

        self.label1.move(40, 230)
        self.label1.resize(self.label1.sizeHint())

        self.btn = QPushButton('Юпитер', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(30, 260)
        self.btn.clicked.connect(self.jup)

        self.btn = QPushButton('Земля', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(200, 260)
        self.btn.clicked.connect(self.earth)

    def jup(self):
        Jupiter.show()
        Mars.hide()

    def earth(self):
        Earth.show()
        Mars.hide()


class Earth(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Солнечная система')

        self.label = QLabel(self)
        self.label.setText("Земля́ — третья по удалённости от Солнца\n"
                           " планета Солнечной системы. Самая плотная,\n"
                           " пятая по диаметру и массе среди всех планет\n"
                           " и крупнейшая среди планет земной группы,\n"
                           " в которую входят также Меркурий,\n"
                           " Венера и Марс.")
        self.label.move(40, 30)
        self.label.resize(self.label.sizeHint())

        self.label1 = QLabel(self)
        self.label1.setText("Вы можете посмотреть информацию о ближайших\n"
                            "планетах:")

        self.label1.move(40, 230)
        self.label1.resize(self.label1.sizeHint())

        self.btn = QPushButton('Марс', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(30, 260)
        self.btn.clicked.connect(self.mars)

        self.btn = QPushButton('Венера', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(200, 260)
        self.btn.clicked.connect(self.ven)

    def mars(self):
        Mars.show()
        Earth.hide()

    def ven(self):
        Venus.show()
        Earth.hide()


class Venus(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Солнечная система')

        self.label = QLabel(self)
        self.label.setText("Вене́ра — вторая по удалённости от\n"
                           " Солнца планета Солнечной системы,\n"
                           " наряду с Меркурием, Землёй и Марсом\n"
                           " принадлежит к семейству планет земной\n"
                           " группы. Названа в честь древнеримской\n"
                           " богини любви Венеры. Венерианский год\n"
                           " составляет 224,7 земных суток. Она имеет\n"
                           " самый длинный период вращения вокруг своей\n"
                           " оси (243 земных суток) среди всех планет\n"
                           " Солнечной системы и вращается в направлении,\n"
                           " противоположном направлению вращения\n"
                           " большинства планет. Венера не имеет\n"
                           " естественных спутников. Это третий по яркости\n"
                           " объект на небе Земли, после Солнца и Луны.\n"
                           " Изредка Венера видна невооружённым глазом\n"
                           " и в светлое время суток.\n"
                           "\n"
                           "Вы можете посмотреть информацию о ближайших\n"
                           "планетах:")
        self.label.move(40, 10)
        self.label.resize(self.label.sizeHint())

        self.btn = QPushButton('Земля', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(30, 260)
        self.btn.clicked.connect(self.earth)

        self.btn = QPushButton('Меркурий', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(200, 260)
        self.btn.clicked.connect(self.mer)

    def earth(self):
        Earth.show()
        Venus.hide()

    def mer(self):
        Mercury.show()
        Venus.hide()


class Mercury(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Солнечная система')

        self.label = QLabel(self)
        self.label.setText("Мерку́рий — ближайшая к Солнцу планета\n Солнечной системы,  "
                           "наименьшая из планет\n земной группы."
                           " Названа в честь\n древнеримского бога торговли — быстрого\n Меркурия,"
                           " поскольку она движется по\n небесной сфере быстрее других планет.")
        self.label.move(40, 30)
        self.label.resize(self.label.sizeHint())

        self.label1 = QLabel(self)
        self.label1.setText("Вы можете посмотреть информацию о ближайших\n"
                            "космических объектах:")

        self.label1.move(40, 230)
        self.label1.resize(self.label1.sizeHint())

        self.btn = QPushButton('Венера', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(30, 260)
        self.btn.clicked.connect(self.ven)

        self.btn = QPushButton('Солнце', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(200, 260)
        self.btn.clicked.connect(self.sun)

    def ven(self):
        Venus.show()
        Mercury.hide()

    def sun(self):
        Sun.show()
        Mercury.hide()


class Sun(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Солнечная система')

        self.label = QLabel(self)
        self.label.setText("Со́лнце — одна из звёзд нашей\n"
                           " Галактики (Млечный Путь) и единственная\n"
                           " звезда Солнечной системы. Вокруг Солнца\n"
                           " обращаются другие объекты этой системы:\n"
                           " планеты и их спутники, карликовые планеты\n"
                           " и их спутники, астероиды, метеороиды, кометы\n"
                           " и космическая пыль.")
        self.label.move(40, 30)
        self.label.resize(self.label.sizeHint())

        self.label1 = QLabel(self)
        self.label1.setText("Вы можете посмотреть информацию о ближайших\n"
                            "космических объектах:")

        self.label1.move(40, 140)
        self.label1.resize(self.label1.sizeHint())

        self.btn = QPushButton('Меркурий', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 190)
        self.btn.clicked.connect(self.mer)

    def mer(self):
        Mercury.show()
        Sun.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Sun_system()
    Mercury = Mercury()
    Venus = Venus()
    Earth = Earth()
    Mars = Mars()
    Jupiter = Jupiter()
    Saturn = Saturn()
    Uranus = Uranus()
    Neptune = Neptune()
    Sun = Sun()
    sys.exit(app.exec_())
