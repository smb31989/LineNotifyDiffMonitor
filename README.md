# LineNotifyDiffMonitor
-ดาวน์โหลด Python3: https://www.python.org/downloads
-ใน File config.config: True = แจ้งเตือน False = ไม่แจ้งเตือน
-ติดตั้ง line_notify
> pip install line_notify

       [MonitorCoins]
       mineRVN = True
       mineETH = False
       mineETC = False
       
-กำหนดช่วงของค่า diff 

       [tarDiff_High]
       tarDiffRVN = 12000
       tarDiffETH = 3522206773042161
       tarDiffETC = 206456480047318

-กำหนด Line Token

        [TOKEN]
        Acc_TOKEN = 0jySON3X6UMpQ1ADWuluGgClzbdhmrNohmnHj42CTzm
       
-กำหนด loop time

       [looptime]
       timescan = 1800
###1800 sec = 30 min

-เปิด python
>Start->Python 3.6 ->IDLE(Python 3.6 64 bit)
>เมนู File->Open->CryptoSwitc.py
>เมนู Run->Run Module
