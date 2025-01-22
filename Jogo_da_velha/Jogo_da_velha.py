import random
import time
class Game():
    
    def _init_(self):
          pass
    def inicio(self):
        
        self.play = ['''
        
                __|  |__
                __|  |__
                  |  |
          
         ''','''
                0 |1 | 2
                3 |4 | 5 
                6 |7 | 8
        ''','''
        
          
        '''
        ]
        
        print(self.play[0],self.play[1])
        self.op = ["  ","  ","  ","  ","  ","  ","  ","  ","  "]
        self.cont = 0
        self.a = []
    def final(self):
        
        
        if self.op[0]==self.op[1]==self.op[2]==self.cor:
            print('\nVOCÊ VENCEU !!')
            exit()
        elif  self.op[0]==self.op[1]==self.op[2]==self.co2:
            print('\nVOCÊ PERDEU !!')
            exit()
            
        if self.op[3]==self.op[4]==self.op[5]==self.cor:
            print('\nVOCÊ VENCEU !!')
            exit()
            
        elif  self.op[3]==self.op[4]==self.op[5]==self.co2:
            print('\nVOCÊ PERDEU !!')
            exit()
            
        if self.op[6]==self.op[7]==self.op[8]==self.cor:
            print('\nVOCÊ VENCEU !!')
            exit()
        elif  self.op[6]==self.op[7]==self.op[8]==self.co2:
            print('\nVOCÊ PERDEU !!')
            exit()
            
        
        if self.op[0]==self.op[4]==self.op[8]==self.cor:
            print('\nVOCÊ VENCEU !!')
            exit()
            
        elif  self.op[0]==self.op[4]==self.op[8]==self.co2:
            print('\nVOCÊ PERDEU !!')
            exit()
            
            
        if self.op[2]==self.op[4]==self.op[6]==self.cor:
            print('\nVOCÊ VENCEU !!')
            exit()
        elif  self.op[2]==self.op[4]==self.op[6]==self.co2:
            print('\nVOCÊ PERDEU !!')
            exit()
        
               
        if self.op[0]==self.op[3]==self.op[6]==self.cor:
            print('\nVOCÊ VENCEU !!')
            exit()
        elif  self.op[0]==self.op[3]==self.op[6]==self.co2:
            print('\nVOCÊ PERDEU !!')
            exit()
            
            
        if self.op[1]==self.op[4]==self.op[7]==self.cor:
            print('\nVOCÊ VENCEU !!')
            exit()
        elif  self.op[1]==self.op[4]==self.op[7]==self.co2:
            print('\nVOCÊ PERDEU !!')
            exit()
        if self.op[2]==self.op[5]==self.op[8]==self.cor:
            print('\nVOCÊ VENCEU !!')
            exit()
        elif  self.op[2]==self.op[5]==self.op[8]==self.co2:
            print('\nVOCÊ PERDEU !!')
            exit()
        
        
    def menu1(self):
       
        print('\n\n\n\n\n\n\n             JOGO DA VELHA 👵🏽#🎮\n')
        print('_______________________________________\n')
        jg = input('\n           SELECIONE TIPO DE JOGO\n[1]🎮\n[2]🎮🎮\n-> ')
        if jg=='1':
            self.select_cor()
            self.inicio()
            self.start()
        elif jg=='2':
            print('Em Contrução 🛠️')
            
    def select_cor(self):
        
        self.cor = input('\n           SELECIONE TIPO DE PLAY\n[1]❌\n[2]⚪\n-> ')
        if self.cor =='1':
            self.cor = '❌'
            self.co2 = '⚪'
        elif self.cor =='2':
            self.cor = '⚪'
            self.co2 = '❌'
        
    def start(self):      
        while True:
                         
    
            self.menu = int(input("Sua vez: "))
                     
            self.op[self.menu] = self.cor
            if len(self.a)>=8:
                print('velha')
                exit()
            self.a.append((self.menu))
            
            game.cycle()
                 
    def cycle(self):
        
        self.alto = random.randint(0,8)
            
        self.r = self.alto not in self.a
            
        #print(self.alto)     
               
        if self.r == True:
                
            self.a.append(self.alto)   
             
            self.op[self.alto] = self.co2
            
                
        else:
            #print("retorno")
            game.cycle()
    
                      
        print(self.play[1])
       
        print("                {}|{}|{}".format(self.op[0],self.op[1],self.op[2]))
        print("                {}|{}|{}".format(self.op[3],self.op[4],self.op[5]))
        print("                {}|{}|{}".format(self.op[6],self.op[7],self.op[8]))
        self.final()
        self.start()      
        
game = Game()
game.menu1()
game.select_cor()
game.inicio()

game.cycle()