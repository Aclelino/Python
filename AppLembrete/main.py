import sys
import time
import sqlite3
from PyQt5 import uic,QtWidgets
from PyQt5.QtCore import QTime,QDate
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem


def dado():
    conn = sqlite3.connect("dado.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS lembrete(id INTEGER NOT NULL PRIMARY KEY,texto STRING NOT NULL,hora STRING NOT NULL,data STRING NOT NULL )")


    l = texto.toPlainText()
    h = horas.text()
    d = data.text()
    c.execute("INSERT INTO lembrete(texto,hora,data)VALUES(?,?,?)",(l, h, d))


    v = c.execute("SELECT * FROM lembrete")


    conn.commit()
    for row in v:
        t = c.fetchall()
        print(t)
        tabela.setRowCount(len(t))
        tabela.setColumnCount(3)
        tabela.setItem((row[1]))#id
        tabela.setItem(0,1,QTableWidgetItem(row[1]))#texto
        tabela.setItem(1,0,QTableWidgetItem(row[2]))#hora
        tabela.setItem(1,1,QTableWidgetItem(row[3]))#data

def btsalvar ():
    p = texto.toPlainText()
    g = horas.text()
    d = data.text()
    print(p ,g,)
    func()
def func():
    p = texto.toPlainText()
    g = horas.text()
    d = data.text()
    
    while True:
        time.sleep(60)
        h = time.strftime("%H:%M")
        print(h)



        if g <= h:
            QMessageBox.about(qt,"LEMBRETE !",p)
            break

app=QtWidgets.QApplication([])
qt=uic.loadUi("main.ui")

#ELEMENTOS DA MAIN UI

salvar = qt.btsavar.clicked.connect(dado)
horas = qt.horas
hora_atual = qt.horas.setTime(QTime.currentTime())
data_atual = qt.data.setDate(QDate.currentDate())
tabela = qt.tableWidget

texto = qt.caixa
data = qt.data

# CARREGA APP
qt.show()
app.exec_()
