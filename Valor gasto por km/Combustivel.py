from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image
import requests




# calcular a
class Km_litro():
    def __init__(self ,km, litro):

        self.km = km
        self.litro = litro

    def resultado(self):

        self.conta = self.km / self.litro

        return self.conta




class Combustivel(App):

    def funcao(self, instance):

        try:

            km = float(self.km.text)
            lt = float(self.consumo.text)
            kmlitro = Km_litro(km,lt)
            b = str('{0:.2f}'.format(kmlitro.resultado()))
            self.texto.text="Valor gasto por km é R${0}".format(b)
        except ValueError:
                self.texto.text="Por favor Digite Número ex 0.00 !!"
        else:

            km = float(self.km.text)
            lt = float(self.consumo.text)
            kmlitro = Km_litro(km, lt)
            b = str('{0:.2f}'.format(kmlitro.resultado()))
            self.texto.text = "Valor gasto por km é R${0}".format(b)

    def build(self):
        self.tela = GridLayout(

            size_hint = (0.4,0.5) ,
            pos_hint = {'center_x':0.5,'center_y':0.5},
            cols = 1
            )
        self.texto = Label(
            text = "Gasto médio de combustível por KM",
            bold = True,
            italic = True,
            font_size = 25,
            color = '#343dc3'
        )
        self.km = TextInput(

            hint_text = "Valor do ComBustivel EX: 9.99",
            pos_hint = {'top':1},
            font_size = 12,


        )
        self.consumo = TextInput(
            hint_text = "Consumo Médio do seu Veiculo EX:9.99",
            pos_hint={'top': 1},
            font_size=12,

        )
        self.calcular = Button(
            text = "Calcular",
            bold = True,
            background_color = '#7234C3',
            on_press = self.funcao

        )
        self.gaso = Image(
            source ='3273.jpg',
            size = (20,20)
            )
        self.tela.add_widget(self.gaso)
        self.tela.add_widget(self.texto)
        self.tela.add_widget(self.km)
        self.tela.add_widget(self.consumo)
        self.tela.add_widget(self.calcular)
        return self.tela
if __name__ == "__main__":
    Combustivel().run()
