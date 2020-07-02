import os


class Program():
  def __init__():
    print("Jakub Owczarczyk")
  def rozmiary():
    sciezka = "."

    lista_plikow = []
    l_ext = []
    for files in os.listdir(path=sciezka):
        if os.path.isfile(files):
          lista_plikow.append(files)

    i = 0
    while i < len(lista_plikow):
      tmp1 = lista_plikow[i].find(".")
      tmp2 = lista_plikow[i]
      if tmp2[tmp1:] not in l_ext:
        l_ext.append(tmp2[tmp1:])
      i+=1
    print("Lista plikow:")
    for pliki in lista_plikow: 
      print(pliki)

    print("\nLista rozszerzen:")  
    for rozszerzenia in l_ext:
     print(rozszerzenia)


    l_ext_dict = dict.fromkeys(l_ext,0)

    i = 0

    while i < len(lista_plikow):
      a = 0
      while a < len(l_ext):
        if l_ext[a] in lista_plikow[i]:
            l_ext_dict[l_ext[a]] = l_ext_dict[l_ext[a]] + os.path.getsize(lista_plikow[i]) 
        a+=1
      i+=1
    print("\nSumaryczna wielkosc dla kazdego z rozszerzen")
    print("Typ pliku      Rozmiar")
    for key,val in l_ext_dict.items():
        print(key, "          ", val, "kB")

program = Program.rozmiary()