# Powcode Weekly no. 1
# Owo auto bot
import pyautogui as pag;
import time as t

gems_effect = {
  'c' : 1, 'u' : 3, 'r' : 4,'e' : 5,'m' : 6,'l' : 7,'f' : 9
}
gems_list = ['c', 'u', 'r', 'e', 'm', 'l', 'f']
hunt_dur_list = {'c' : 25, 'u' : 25, 'r' : 50,'e' : 75,'m' :75 ,'l' : 100,'f' : 100}
enpower_dur_list = {'c' : 50, 'u' : 100, 'r' : 250,'e' : 450,'m' :525 ,'l' : 800,'f' : 1000}
lucky_dur_list = {'c' : 50, 'u' : 100, 'r' : 250,'e' : 450,'m' :525 ,'l' : 800,'f' : 1000}

hunting_type = input("Hunting gems type(c, u, r, e, m, l, f ) : ")
hunting_dur = int(input("Hunting durability : "))

enpowering_type = input("Enpowering gems type(c, u, r, e, m, l, f) : ")
enpowering_dur = int(input("Enpowering durability : "))

lucky_type = input("Lucky gems type(c, u, r, e, m, l, f) : ")
lucky_dur = int(input("Lucky durability : "))

hunting = [hunting_type, hunting_dur]
enpowering = [enpowering_type, enpowering_dur]
lucky = [lucky_type, lucky_dur]

hunting_id =(51 + gems_list.index(hunting_type))
enpower_id = (65+gems_list.index(enpowering_type))
lucky_id = (72+gems_list.index(lucky_type))

message = ["owoh", "owob"]
animal_get_total = 0
count = 0
t.sleep(3)

try :
  while(True):
    if(count == 16):
      count = 0
      t.sleep(60)
      
    if(hunting_dur <= 0):
      pag.typewrite("owo equip " + str(hunting_id) + "\n")
      hunting_dur = hunt_dur_list[hunting_type]
      t.sleep(5)
      
    if(enpowering_dur <= 0):
      pag.typewrite("owo equip " + str(enpower_id) + "\n")
      enpowering_dur = enpower_dur_list[enpowering_type]
      t.sleep(5)
      
    if(lucky_dur <= 0):
      pag.typewrite("owo equip " + str(lucky_id) + "\n")
      lucky_dur = lucky_dur_list[enpowering_type]
      t.sleep(5)
        
    for msg in message :
      t.sleep(1)
      pag.typewrite(msg + "\n")
      
    animal_get = gems_effect[hunting_type] * 2 +2
    animal_get_total += animal_get
    hunting_dur -= 1
    enpowering_dur -= animal_get
    lucky_dur -=  animal_get 
    count += 1 
    t.sleep(20)
  
except KeyboardInterrupt:
  print("Program Berhenti")

  
print("Total Animal : " + str(animal_get_total))







