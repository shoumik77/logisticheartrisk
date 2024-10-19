import os.path
import pickle
import sys

from PyQt5 import QtWidgets

from GUI import Ui_MainWindow


class App:

    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        self.ui.pushButton.clicked.connect(self.predict)

        # Check for the support file to be available or not
        if os.path.exists("support.pickle"):
            self.support = pickle.load(open("support.pickle", 'rb'))
        else:
            print("No Support file avaliable unable to load the Application")
            sys.exit(1)

    def predict(self):

        # Input values
        Age = self.ui.spinBox.value()
        if self.ui.radioButton_2.isChecked():
            Sex = 'M'
        else:
            Sex = 'F'

        ChestPainType = self.ui.comboBox_2.currentText()
        RestingBP = self.ui.spinBox_2.value()
        Cholesterol = self.ui.spinBox_3.value()
        FastingBS = self.ui.spinBox_4.value()
        RestingECG = self.ui.comboBox.currentText()
        MaxHR = self.ui.spinBox_5.value()
        if self.ui.radioButton_3.isChecked():
            ExerciseAngina = 'Y'
        else:
            ExerciseAngina = 'N'
        Oldpeak = self.ui.doubleSpinBox.value()
        ST_Slope = self.ui.comboBox_3.currentText()

        # Transform the labels into number
        Sex = self.support['Sex'].transform([Sex])[0]
        ChestPainType = self.support['ChestPainType'].transform([ChestPainType])[0]
        RestingECG = self.support['RestingECG'].transform([RestingECG])[0]
        ExerciseAngina = self.support['ExerciseAngina'].transform([ExerciseAngina])[0]
        ST_Slope = self.support['ST_Slope'].transform([ST_Slope])[0]

        # Scale the data again
        rec = self.support['Scaler'].transform(
            [[Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR,
              ExerciseAngina, Oldpeak, ST_Slope]])

        # Predict the label
        prediction = self.support['Model'].predict(rec)[0]

        if prediction == 0:
            self.ui.label_13.setText("Normal")
        else:
            self.ui.label_13.setText("Heart Risk")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = App()
    application.MainWindow.show()
    sys.exit(app.exec_())
