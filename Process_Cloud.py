import sys, os

current_dir = os.getcwd()
current_dir = current_dir.replace("\\","//")
#print(f"D: {current_dir}")

class WIFI_Init:
	DirHomeHC22000=""
	DirHomeDicts=""
	DirWIFI=[],
	Speed=1,
	GoogleDisk1=[],
	GoogleDisk2=[],
	GoogleDisk3=[],
	DictsProces=[]

class WIFI_Three:
	One=7,
	Two=12

class WIFI_Cloud:
	"""WIFI Cloud"""
	def LibInit():
		"""Иницилизациия Библиотек"""
		com="!apt install cmake build-essential -y && apt install checkinstall git -y && git clone https://github.com/hashcat/hashcat.git && cd hashcat && git submodule update --init && make && make install"
		return com
	def DirInit(dir_hc=WIFI_Init()):
		dir_home=f"{current_dir}//{dir_hc.DirHomeHC22000}"
		WIFI_Cloud.CreatDir(dir_home)
		for li in dir_hc.DirWIFI:
			dir_new=f"{current_dir}//{dir_hc.DirHomeHC22000}//{li}"
			WIFI_Cloud.CreatDir(dir_new)
	def GoogleDisk1_Extract(dir_hc=WIFI_Init()):
		command=""
		for li in dir_hc.GoogleDisk1:
			command+=f"!unzip {li} -d {dir_hc.DirHomeDicts}\n"
		return command
	def GoogleDisk2_Extract(dir_hc=WIFI_Init()):
		command=""
		for li in dir_hc.GoogleDisk2:
			command+=f"!unzip {li} -d {dir_hc.DirHomeDicts}\n"
		return command
	def GoogleDisk3_Extract(dir_hc=WIFI_Init()):
		command=""
		for li in dir_hc.GoogleDisk3:
			command+=f"!unzip {li} -d {dir_hc.DirHomeDicts}\n"
		return command
	def CreatDir(dirnew):
		if os.path.exists(dirnew)==False:
			os.mkdir(dirnew)
	def RunProcess2(dir_hc=WIFI_Init(),reng_two=WIFI_Three()):
		#-------------------Иницилизация---------------------
		selectfilespath,dir_wifi="",""
		url_convert="https://hashcat.net/cap2hashcat/"
		#Словари Папка
		dirs = os.listdir(dir_hc.DirHomeHC22000)
		  filesdicts = os.listdir(dir_hc.DirHomeDicts)
		  print(f"--------Словари {dir_hc.DirHomeDicts}-------")
		  for i,li in enumerate(filesdicts):
		    print(f"Номер: {i}|Словарь: {li}")
		  print(f"-------{dir_hc.DirHomeDicts}--------")
		  for i,li in enumerate(dirs):
		    print(f"Номер: {i}|Папка: {li}")
		  print("---------------")
		  #-------Этапы 3--------
		  three_mass=["",
		              "",
		              ""]
		  three_rang=reng_two.Three.split("-")
		  for i,di in enumerate(dir_hc.DictsProces):
		    if(i<reng_two.One):
		      three_mass[0]+=f"{di} "
		    if(i==reng_two.One):
		      three_mass[0]+=f"{di}"
		    if(i>reng_two.One and i<reng_two.Two):
		      three_mass[1]+=f"{di} "
		    if(i>reng_two.One and i==reng_two.Two):
		      three_mass[1]+=f"{di}"
		    if(i>reng_two.Two and i<len(dir_hc.DictsProces)-1):
		      three_mass[2]+=f"{di} "
		    if(i==len(dir_hc.DictsProces)-1):
		      three_mass[2]+=f"{di}"
		  #-------Этапы Единий-----
		  one_string_dicts=""
		  for i,di in enumerate(dir_hc.DictsProces):
		    if(i<len(dir_hc.DictsProces)-1):
		      one_string_dicts+=f"{di} "
		    if(i==len(dir_hc.DictsProces)-1):
		      one_string_dicts+=f"{di}"
		  #----------------------------------------------------
		  indexspeed=dir_hc.Speed
	def RunProcess(dir_hc=WIFI_Init(),reng_two=WIFI_Three()):
		#-------------------Иницилизация---------------------
		selectfilespath,dir_wifi="",""
		url_convert="https://hashcat.net/cap2hashcat/"
		#Словари Папка
		ExistFlag=True
		while ExistFlag==True:
		  dirs = os.listdir(dir_hc.DirHomeHC22000)
		  filesdicts = os.listdir(dir_hc.DirHomeDicts)
		  print(f"--------Словари {dir_hc.DirHomeDicts}-------")
		  for i,li in enumerate(filesdicts):
		    print(f"Номер: {i}|Словарь: {li}")
		  print(f"-------{dir_hc.DirHomeDicts}--------")
		  for i,li in enumerate(dirs):
		    print(f"Номер: {i}|Папка: {li}")
		  print("---------------")
		  #-------Этапы 3--------
		  three_mass=["",
		              "",
		              ""]
		  three_rang=reng_two.Three.split("-")
		  for i,di in enumerate(dir_hc.DictsProces):
		    if(i<reng_two.One):
		      three_mass[0]+=f"{di} "
		    if(i==reng_two.One):
		      three_mass[0]+=f"{di}"
		    if(i>reng_two.One and i<reng_two.Two):
		      three_mass[1]+=f"{di} "
		    if(i>reng_two.One and i==reng_two.Two):
		      three_mass[1]+=f"{di}"
		    if(i>reng_two.Two and i<len(dir_hc.DictsProces)-1):
		      three_mass[2]+=f"{di} "
		    if(i==len(dir_hc.DictsProces)-1):
		      three_mass[2]+=f"{di}"
		  #-------Этапы Единий-----
		  one_string_dicts=""
		  for i,di in enumerate(dir_hc.DictsProces):
		    if(i<len(dir_hc.DictsProces)-1):
		      one_string_dicts+=f"{di} "
		    if(i==len(dir_hc.DictsProces)-1):
		      one_string_dicts+=f"{di}"
		  #----------------------------------------------------
		  indexspeed=dir_hc.Speed
		  if indexspeed<4:
		    selectdir=input("Укажы Номер Папки с Файлом *.hc22000: ")
		    indexdir=int(selectdir)
		    for i,li in enumerate(dirs):
		      if(indexdir==i):
		        dir_wifi=li
		        pathdir=f"{caps_path}/{li}"
		        files=os.listdir(pathdir)
		        if len(files)>0:
		          selectfilespath=f"{pathdir}/{files[0]}"
		        else:
		          print(f"Нету Сконвентированого файла {url_convert} из формата *.cap в *.hc22000")
		          ExistFlag=False
		          break
		        break
		    print(f"Файл Перебора: {selectfilespath}")
		  else:
		    print(f"Вы выбрали Скорость {indexspeed} за приделы 1-3")
		    ExistFlag=False
		    break
		  print(f"-----------------Выбор Метода 1-Полный 2-Тройной 3-Кусками-----------------")
		  etap_select=input("Выбор Метода: ")
		  index_etap_select=int(etap_select)
		  if index_etap_select<4:
		    if(index_etap_select==1):
		      #Единый Процес в Одном
		      print(f"---------------Единый Процес в Одном (Полный Этап)---------------")
		      print(f"Скорость-{speed}")
		      print(f"Папка Сеть WIFI: {dir_wifi}")
		      print(f"Файл WIFI: {selectfilespath}")
		      input(f"Запустить Процес........................")
		      return f"!hashcat -m 22000 -a 0 -w {speed} {selectfilespath} {one_string_dicts}"
		      print("---------------Конец Работы Единого в Одном---------------")
		      input(".............................................................")
		    if(index_etap_select==2):
		      pod_etap_select=input("Выбрать 1-3 Этапов: ")
		      index_pod_etap_select=int(pod_etap_select)
		      if(index_pod_etap_select<4):
		        print(f"---------------Этапов 3---------------")
		        print(f"Скорость-{speed}")
		        print(f"Папка Сеть WIFI: {dir_wifi}")
		        print(f"Файл WIFI: {selectfilespath}")
		        if(index_pod_etap_select==1):
		          input(f"Запустить Этап 1({index_pod_etap_select}) Процес........................")
		          # Перебор по Словарей (Этап 1)
		          return f"!hashcat -m 22000 -a 0 -w {speed} {selectfilespath} {three_mass[0]}"
		          print(f"---------------Конец Работы Этапа 1({index_pod_etap_select})---------------")
		          input(".............................................................")
		        if(index_pod_etap_select==2):
		          input(f"Запустить Этап 2 Процес........................")
		          # Перебор по Словарей (Этап 2)
		          return f"!hashcat -m 22000 -a 0 -w {speed} {selectfilespath} {three_mass[1]}"
		          print(f"---------------Конец Работы Этапа 2({index_pod_etap_select})---------------")
		          input(".............................................................")
		        if(index_pod_etap_select==3):
		          input(f"Запустить Этап 3({index_pod_etap_select}) Процес........................")
		          # Перебор по Словарей (Этап 3)
		          return f"!hashcat -m 22000 -a 0 -w {speed} {selectfilespath} {three_mass[2]}"
		          print(f"---------------Конец Работы Этапа 3({index_pod_etap_select})---------------")
		          input(".............................................................")
		        else:
		          print(f"Вы выбрали {index_pod_etap_select}, за приделы границ 1-3 Этапов")
		          input(".............................................................")
		          ExistFlag=False
		          break
		        print("---------------Конец Работы (3)Тройного Метода---------------")
		        input(".............................................................")
		    if(index_etap_select==3):
		      print(f"---------------Этапов 3 (1=1-8); (2=(9-13)); (3=(14-19))---------------")
		      print(f"Скорость-{speed}")
		      print(f"Папка Сеть WIFI: {dir_wifi}")
		      print(f"Файл WIFI: {selectfilespath}")
		      pod_etap_select2=input("Выбрать 1-19 Этапов: ")
		      index_pod_etap_select2=int(pod_etap_select2)
		      if(index_pod_etap_select2<len(dir_hc.DictsProces)):
		      	for i2,li2 in enumerate(dir_hc.DictsProces):
		      		print(li)
		      		input(".............................................................")
                    #if(i2==index_pod_etap_select2):
			          # input(f"Запустить Этап ({index_pod_etap_select2}) Процес........................")
			          # # Перебор по Словарей (Этап)
			          # return f"!hashcat -m 22000 -a 0 -w {speed} {selectfilespath} {dir_hc.DictsProces[i]}"
			          # print(f"---------------Конец Работы Этапа {index_pod_etap_select2}---------------")
		      else:
		        print(f"Вы выбрали {index_pod_etap_select2}, за границы доступности 19")
		        input(".............................................................")
		        ExistFlag=False
		        break
		      print("---------------Конец Работы Много Этапного Кусками---------------")
		      input(".............................................................")
		  else:
		    print(f"Вы выбрали {index_etap_select} Метод вышло за приделы 1-3")
		    input(".............................................................")
		    ExistFlag=False
		    break