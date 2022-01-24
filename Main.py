from Process_Cloud import WIFI_Init, WIFI_Cloud, WIFI_Three
import os


test = WIFI_Init()
test.DirHomeHC22000="Caps"
test.DirHomeDicts="Dicts"
test.DirGoogleDisk=""
test.DirWIFI=["Wifi1","Wifi2","Wifi3","Wifi4"]
test.GoogleDisk1=["GoogleDisk/Oup/Dicts/Wps1",
"GoogleDisk/Oup/Dicts/Wps2","GoogleDisk/Oup/Dicts/Wps3"]
test.Speed=1
test.DictsProces=["Dicts/00000000-99999999.txt Dicts/000000000-999999999.txt",
                    "Dicts/5_5.txt Dicts/6_6.txt Dicts/Datas.txt Dicts/Datas_X.txt",
                    "Dicts/Imena_1.txt",
                    "Dicts/Imena_2.txt",
                    "Dicts/Imena_3.txt",
                    "Dicts/Imena_4.txt",
                    "Dicts/Imena_5.txt",
                    "Dicts/domru_dir300.dic Dicts/domru_dir615.dic Dicts/domru_wnr612ert_1.dic Dicts/domru_wnr612ert_2.dic Dicts/domru_wnr612ert_3.dic Dicts/domru_zxhn_h118n.dic Dicts/zxhn_h118n.dic",
                    "Dicts/RUS_MOB_9XXXXXXXXXX.txt Dicts/RUS_MOB_89XXXXXXXXXX.txt",
                    "Dicts/UKR_MOB_0XXXXXXXXX.txt Dicts/UKR_MOB_380XXXXXXXXX.txt",
                    "Dicts/UZB_MOB_9XXXXXXXX.txt Dicts/UZB_MOB_9989XXXXXXXX.txt",
                    "Dicts/BEL_MOB.txt Dicts/KAZ_MOB_7XXXXXXXXX.txt",
                    "Dicts/KAZ_MOB_77XXXXXXXXX.txt Dicts/KAZ_MOB_87XXXXXXXXX.txt",
                    "Dicts/WPS_Pins.txt Dicts/TOP_VK-100M_WPA.txt",
                    "Dicts/Nummer_DB.Top_WPA.txt",
                    "Dicts/UKrtelecom.dic",
                    "Dicts/Hashkiller_WPA.txt",
                    "Dicts/InsideProFull.txt",
                    "Dicts/Top306Million-WPA.txt"]

WIFI_Cloud.DirInit(test)

res=WIFI_Cloud.GoogleDisk1_Extract(test)
print(res)

test2=WIFI_Three()
test2.One=3
test2.Two=12

while True:
    res2=WIFI_Cloud.RunProcess2(test,test2)
    print(res2)