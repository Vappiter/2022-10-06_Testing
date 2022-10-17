documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

def My_input():
  
  """Function input processing"""
  
  print (f'\n ДОБРЫЙ! \n Данное приложение поддерживает следующие команды: \n 1. p - команда выводящая ФИО человека по № введеного документа \n 2. s - команда выводящая № полки, где хранится документ, по № введеного документа \n 3. l - команда выводит все документы из БД с наименованием документа, № документа и ФИО \n 4. a - команда добавления нового документа \n 5. d - команда удаления документа \n 6. m - команда перемещения документа на другую полку \n 7. as - команда добавления полки \n 8. q - выход из приложения')
  var_input = input ("\n Введите команду: ")
  var_input = var_input.upper()
  if var_input == 'P':
    number_doc(documents)
  elif var_input == 'S':
    number_shelf(directories)
  elif var_input == 'L':
    list_doc(documents)
  elif var_input == 'A':
    doc_add(documents,directories)
  elif var_input == 'D':
    doc_del(documents,directories)
  elif var_input == 'M':
    doc_move_shelf(directories)  
  elif  var_input == 'AS':
    shelf_add ()
  elif var_input == 'Q':
    exit()
  else:
    print (f'\n Вы ввели не правильную команду. \n Данное приложение поддерживает следующие команды: \n 1. p - команда выводящая ФИО человека по № введеного документа \n 2. s - команда выводящая № полки, где хранится документ, по № введеного документа \n 3. l - команда выводит все документы из БД с наименованием документа, № документа и ФИО \n 4. a - команда добавления нового документа \n 5. d - команда удаления документа \n 6. m - команда перемещения документа на другую полку \n 7. as - команда добавления полки \n 8. q - выход из приложения')  

def number_doc(doc):
  
  """Function output Name after # documents """
  
  print ('ИМЯ, КОМУ ПРИНАДЛЕЖИТ ДОКУМЕНТ')
  print ('Существуют такие документы')
  for var1 in range (0,len(doc)):
    print (doc[var1]['number']) 
  var_number = input ("\n Введите № документа: ")
  Doc_True = False
  for i1 in range (0,len(doc)):
    if var_number in doc[i1].values():
     Doc_True = True   
    #  print (doc[i1]['name'])
     return (doc[i1]['name']) 
  if Doc_True == False:   
   print('\n Нет такого документа')  
   return None

def number_shelf(shelf):
  
  """Function output # shelf after # documents """
  
  print ('ПОЛКА, ГДЕ НАХОДИТСЯ ДОКУМЕНТ')
  var_number = input ("\n Введите № документа: ")
  Doc_True = False
  for key,i1 in shelf.items():
    if var_number in i1:
     Doc_True = True   
     print ('Полка на которой хранится документ имеет №:', key)
     return () 
  if Doc_True == False:   
   print('\n Нет такого документа')  
   return None         

def list_doc(doc):
  """Function output list type document, number document, name  """
  for i1 in range (0,len(doc)):
    dist_val = list(doc[i1].values())
    print (f'Документ: {dist_val[0]} Документ №: {dist_val[1]} Имя: {dist_val[2]}\n')
  return () 

def doc_add(doc, shelf):
  """Function add type document, number document, name and shelf"""
  print ('ДОБАВЛЕНИЕ ДОКУМЕНТА В КАТАЛОГ')  
  var_type = input ('\n Введите тип документа: ')
  var_number = input ('\n Введите № документа: ')
  var_name = input ('\n Введите владельца документа: ')
  shelf_false = False
  while shelf_false != True: 
    var_shelf = int(input ('\n Введите № полки, куда нужно поместить документ: '))
    if var_shelf > len(shelf):
     print (f'Такой полки не существует, извиняйте \n Давайте повторим ввод (число не более {len(shelf)})')
    else:
       shelf_false = True
  doc.append ({"type": var_type, "number":var_number, "name":var_name})
  shelf[str(var_shelf)].append(var_number) 

def doc_del(doc, shelf):
  """Function delete type document, number document, name and shelf"""
  print ('УДАЛЕНИЕ ДОКУМЕНТА ИЗ КАТАЛОГА')  
  var_number = input ('\n Введите № документа: ')
  Doc_True = False
  for i1 in range (0,len(doc)):
    if var_number in doc[i1].values():
     Doc_True = True  
     doc.pop(i1) 
     break
  for key,var_i1 in shelf.items():
    if var_number in var_i1:
     shelf [key].remove(var_number)
     break
  if Doc_True == False:   
   print('Нет такого документа')  
  return None 

def doc_move_shelf(shelf):
  """Function move document shelf"""
  print ('ПЕРЕМЕЩЕНИЕ ДОКУМЕНТА НА ДРУГУЮ ПОЛКУ')  
  var_number = input ('\n Введите № документа: ')
  Doc_True = False
  shelf_false = False
  while shelf_false != True: 
    var_shelf = input ('\n Введите № полки, куда нужно поместить документ: ')
    if var_shelf not in shelf:
     print (f'Такой полки не существует, извиняйте \n')
    else:
       shelf_false = True
  for key,i1 in shelf.items():
    if var_number in i1:
     Doc_True = True   
     shelf [key].remove(var_number)
     shelf[str(var_shelf)].append(var_number) 
     print (f'\n Документ перемещен с полки № {key} на полку № {var_shelf}')
     return () 
  if Doc_True == False:   
   print('Нет такого документа')  

def shelf_add():
  """Function add shelf"""
  print ('ДОБАВЛЕНИЕ ПОЛКИ')  
  global directories
  # var_dist_shelf = shelf
  # print(directories)
  var_key = list(directories.keys())
  shelf_false = False
  var_shelf = input(f'\n Введите № полки, который нужно добавить \n (сейчас есть полки {" ".join(var_key)}): ')
  while shelf_false != True: 
    if var_shelf in directories:
     var_shelf = input(f'\n Такая полочка существует, извиняйте \n Давайте повторим (сейчас есть полки {" ".join(var_key)})')
    else:
      directories[var_shelf] = []
      shelf_false = True
      return()
  return()    
      
 
# var_str = input(f'\n Введите № полки, который нужно добавить (сейчас есть полки ): ')
# directories[var_str] = [] 
# print (directories)

if __name__ == '__main__':
 while My_input() != "Q":
     My_input()
