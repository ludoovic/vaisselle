import sys
from PySide2.QtWidgets import (QApplication, QWidget, QMainWindow, QAbstractSlider)
from ui_vaisselle import Ui_MainWindow
from PySide2.QtCore import QUrl, QTime
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lecture.clicked.connect(self.lectureClicked)
        self.mediaPlayer = QMediaPlayer()
        self.mediaPlayer.setVideoOutput(self.ui.ecran)

        self.ui.pause.clicked.connect(self.pauseClicked)
        self.ui.suivant.clicked.connect(self.suivantClicked)
        self.ui.stop.clicked.connect(self.stopClicked)
        self.ui.precedent.clicked.connect(self.precedentClicked)

        self.ui.dialVol.valueChanged.connect(self.dVol)

        self.ui.slider.sliderMoved.connect(self.sliderMov)

        mediaContent = QMediaContent(QUrl.fromLocalFile("big_buck_bunny.avi"))
        self.mediaPlayer.setMedia(mediaContent)
        self.mediaPlayer.positionChanged.connect(self.mediaDurationChange)
        self.mediaPlayer.positionChanged.connect(self.mediapositionChange)

    def lectureClicked(self):
        print("Lecture !!!")
        self.mediaPlayer.play()
        #self.sliderMov.connect()

    def pauseClicked(self):
        print("Pause !!!")
        if self.mediaPlayer.state() == QMediaPlayer.PausedState:
            self.mediaPlayer.play()
        else:
            self.mediaPlayer.pause()

    def stopClicked(self):
        print("----------------stooooooop-----------------!")
        self.mediaPlayer.stop()

    def precedentClicked(self):
        print("Précédent !")

    def suivantClicked(self):
        print("Suivant !")

    def sliderMov(self):
        print("Slide .....")
        self.mediaPlayer.setPosition(self.ui.slider.value())

    def onceu(self):
        ttalTimeMedia = self.mediaPlayer.duration()

    def mediaDurationChange(self):
        print("medialoaded")
        mediaDuration = self.mediaPlayer.duration()
        ttalTimeMedia = QTime(0, 0, 0)
        ttalTimeMedia = ttalTimeMedia.addMSecs(mediaDuration)
        self.ui.toBe.setText(ttalTimeMedia.toString("HH:mm:ss"))
        #self.ui.slider.setValue(mediaPosition)

    def mediapositionChange(self):
        mediaPosition = self.mediaPlayer.position()
        currentTimeMedia = QTime(0, 0, 0)
        currentTimeMedia = currentTimeMedia.addMSecs(mediaPosition)

        self.ui.onceU.setText(currentTimeMedia.toString("HH:mm:ss"))
        self.ui.slider.setRange(0, self.mediaPlayer.duration())
        self.ui.slider.setValue(self.mediaPlayer.position())

    def dVol(self):
        self.ui.pourcent.setText(str(self.ui.dialVol.value())+"%")
        self.mediaPlayer.setVolume(self.ui.dialVol.value())

        #X = 3
        #if True
        #    else 7
        #tps = QTime(0,0,0)
        #tps = tps.add

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())