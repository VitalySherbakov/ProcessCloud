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
		github="https://github.com/VitalySherbakov/HashcatCloud.git"
		com=f"install cmake build-essential -y && apt install checkinstall git -y && git clone {github} && cd hashcat && git submodule update --init && make && make install"
		return com
	def DirInit(dir_hc=WIFI_Init()):
		"""Иницилизация создание необходимых директорий"""
		dir_home=f"{current_dir}//{dir_hc.DirHomeHC22000}"
		dir_dicts=f"{current_dir}//{dir_hc.DirHomeDicts}"
		WIFI_Cloud.CreatDir(dir_home)
		WIFI_Cloud.CreatDir(dir_dicts)
		for li in dir_hc.DirWIFI:
			dir_new=f"{current_dir}//{dir_hc.DirHomeHC22000}//{li}"
			WIFI_Cloud.CreatDir(dir_new)
	def GoogleDisk1_Extract(dir_hc=WIFI_Init()):
		"""Распаковка Первого Пакета Словарей zip"""
		command=""
		for i,li in enumerate(dir_hc.GoogleDisk1):
			if(i<len(dir_hc.GoogleDisk1)-1):
				command+=f"{li}.zip -d {dir_hc.DirHomeDicts} && "
			if(i==len(dir_hc.GoogleDisk1)-1):
				command+=f"{li}.zip -d {dir_hc.DirHomeDicts}"
		return command
	def GoogleDisk2_Extract(dir_hc=WIFI_Init()):
		"""Распаковка Второй Пакета Словарей zip"""
		command=""
		for i,li in enumerate(dir_hc.GoogleDisk2):
			if(i<len(dir_hc.GoogleDisk2)-1):
				command+=f"{li}.zip -d {dir_hc.DirHomeDicts} && "
			if(i==len(dir_hc.GoogleDisk2)-1):
				command+=f"{li}.zip -d {dir_hc.DirHomeDicts}"
		return command
	def GoogleDisk3_Extract(dir_hc=WIFI_Init()):
		"""Распаковка Третий Пакета Словарей zip"""
		command=""
		for i,li in enumerate(dir_hc.GoogleDisk3):
			if(i<len(dir_hc.GoogleDisk3)-1):
				command+=f"{li}.zip -d {dir_hc.DirHomeDicts} && "
			if(i==len(dir_hc.GoogleDisk3)-1):
				command+=f"{li}.zip -d {dir_hc.DirHomeDicts}"
		return command
	def CreatDir(dirnew):
		"""Создать Директорию"""
		if os.path.exists(dirnew)==False:
			os.mkdir(dirnew)
	def RunProcess(dir_hc=WIFI_Init(),reng_two=WIFI_Three()):
		"""Запуск Процеса Перебора WIFI"""
		#-------------------Иницилизация---------------------
		selectfilespath,dir_wifi,one_string_dicts="","",""
		url_convert="https://hashcat.net/cap2hashcat/"
		#Словари Папка
		try:
			dirs = os.listdir(dir_hc.DirHomeHC22000)
			filesdicts = os.listdir(dir_hc.DirHomeDicts)
			print(f"--------Словари {dir_hc.DirHomeDicts}-------")
			for i,li in enumerate(filesdicts):
			  print(f"Номер: {i}|Словарь: {li}")
			print(f"-------Захваты {dir_hc.DirHomeHC22000}--------")
			for i,li in enumerate(dirs):
			  print(f"Номер: {i}|Папка: {li}")
			print("---------------")
			#-------Этапы 3--------
			three_mass=["",
			            "",
			            ""]
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
			for i,di in enumerate(dir_hc.DictsProces):
			  if(i<len(dir_hc.DictsProces)-1):
			    one_string_dicts+=f"{di} "
			  if(i==len(dir_hc.DictsProces)-1):
			    one_string_dicts+=f"{di}"
			#----------------------------------------------------
			indexspeed=dir_hc.Speed
			if (indexspeed>3):
				print(f"Вы выбрали Скорость {indexspeed} за приделы 1-3, по умолчанию выставлено 1")
				indexspeed=1
			selectdir=input("Укажы Номер Папки с Файлом *.hc22000: ")
			indexdir=int(selectdir)
			for i,li in enumerate(dirs):
				if(indexdir==i):
					dir_wifi=li
					pathdir=f"{dir_hc.DirHomeHC22000}/{li}"
					files=os.listdir(pathdir)
					if len(files)>0:
						selectfilespath=f"{pathdir}/{files[0]}"
					else:
						print(f"Нету Сконвентированого файла {url_convert} из формата *.cap в *.hc22000")
			print(f"Файл Перебора: {selectfilespath}")
			print(f"-----------------Выбор Метода 1-Полный 2-Тройной 3-Кусками-----------------")
			etap_select=input("Выбор Метода: ")
			index_etap_select=int(etap_select)
			if index_etap_select<4:
				if(index_etap_select==1):
					#Единый Процес в Одном
					print(f"---------------Единый Процес в Одном (Полный Этап)---------------")
					print(f"Скорость-{dir_hc.Speed}")
					print(f"Папка Сеть WIFI: {dir_wifi}")
					print(f"Файл WIFI: {selectfilespath}")
					input(f"Запустить Процес........................")
					return f"-m 22000 -a 0 -w {dir_hc.Speed} {selectfilespath} {one_string_dicts}"
				if(index_etap_select==2):
					pod_etap_select=input("Выбрать 1-3 Этапов: ")
					index_pod_etap_select=int(pod_etap_select)
					if(index_pod_etap_select<4):
						print(f"---------------Этапов 3---------------")
						print(f"Скорость-{dir_hc.Speed}")
						print(f"Папка Сеть WIFI: {dir_wifi}")
						print(f"Файл WIFI: {selectfilespath}")
						if(index_pod_etap_select==1):
							input(f"Запустить Этап ({index_pod_etap_select}) Процес........................")
							return f"-m 22000 -a 0 -w {dir_hc.Speed} {selectfilespath} {three_mass[0]}"
						if(index_pod_etap_select==2):
							input(f"Запустить Этап ({index_pod_etap_select}) Процес........................")
							return f"-m 22000 -a 0 -w {dir_hc.Speed} {selectfilespath} {three_mass[1]}"
						if(index_pod_etap_select==3):
							input(f"Запустить Этап ({index_pod_etap_select}) Процес........................")
							return f"-m 22000 -a 0 -w {dir_hc.Speed} {selectfilespath} {three_mass[2]}"
				if(index_etap_select==3):
					print(f"---------------Процес Кусками---------------")
					print(f"Скорость-{dir_hc.Speed}")
					print(f"Папка Сеть WIFI: {dir_wifi}")
					print(f"Файл WIFI: {selectfilespath}")
					pod_etap_select2=input(f"Выбрать 1-{len(dir_hc.DictsProces)} Этапов: ")
					index_pod_etap_select2=int(pod_etap_select2)
					if (index_pod_etap_select2<len(dir_hc.DictsProces)):
						for i2,li2 in enumerate(dir_hc.DictsProces):
							if ((i2+1)==index_pod_etap_select2):
								input(f"Запустить Этап ({index_pod_etap_select2}) Процес........................")
								return f"-m 22000 -a 0 -w {dir_hc.Speed} {selectfilespath} {dir_hc.DictsProces[i2]}"
					else:
						print(f"Вы выбрали {index_pod_etap_select2}, за границы доступности 19")
			else:
				print(f"Вы выбрали {index_etap_select} Метод вышло за приделы 1-3")
		except Exception as ex:
			print(f"ERROR: {ex}!")