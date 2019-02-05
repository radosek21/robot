# -*- coding: utf-8 -*-


futuraInputRegisters = {
'serial_number0': 1,    #s�riov� ��slo za��zen�, bity 0..15
'serial_number1': 2,    #s�riov� ��slo za��zen�, bity 16..31
'mac_address0': 3,    #MAC adresa za��zen�
'mac_address1': 4,    #MAC adresa za��zen�
'mac_address2': 5,    #MAC adresa za��zen�
'hw_version0': 6,    #verze hardware
'hw_version1': 7,    #verze hardware
'fw_version0': 8,    #verze firmware
'fw_version1': 9,    #verze firmware
'sys_build_number0': 10,    #fw build number
'sys_build_number1': 11,    #fw build number
'sys_regmap_version0': 12,    #verze mapy registr�
'sys_regmap_version1': 13,    #verze mapy registr�
'sys_options': 14,    #varianta za��zen� (0=Futura L, 1=Futura M)
'sys_config': 15,    #mo�nosti za��zen� (b0=int. heating, b1=CB cooling, b2=CB heating)
'sys_mode0': 16,    #aktu�ln� re�im za��zen�
'sys_mode1': 17,    #aktu�ln� re�im za��zen�, zat�m nevyu�ito
'sys_error0': 18,    #poruchy za��zen�
'sys_error1': 19,    #poruchy za��zen�
'sys_warning0': 20,    #v�strahy za��zen�
'sys_warning1': 21,    #v�strahy za��zen�
'temp_ambient': 30,    #teplota venkovn�ho vzduchu
'temp_fresh': 31,    #teplota dod�van�ho vzduchu do domu
'temp_indoor': 32,    #teplota ods�van�ho vzduchu z domu
'temp_waste': 33,    #teplota odpadn�ho vzduchu
'humi_ambient': 34,    #relativn� vlhkost venkovn�ho vzduchu
'humi_fresh': 35,    #relativn� vlhkost dod�van�ho vzduchu do domu
'humi_indoor': 36,    #relativn� vlhkost ods�van�ho vzduchu z domu
'humi_waste': 37,    #relativn� vlhkost odpadn�ho vzduchu
'fut_t_out': 38,    #teplota extern�ho NTC senzoru venkovn� teploty
'filter_wear_level': 40,    #hodnota zanesen� filtr� 0-100%
'power_consumption': 41,    #aktu�ln� p��kon jednotky
'heat_recovering': 42,    #aktu�ln� hodnota zp�tn� z�sk�van�ho tepla
'heating_power': 43,    #v�kon topen� doh�evu
'air_flow': 44,    #aktu�ln� pr�tok vzduchu
'fan_pwm_supply': 45,    #v�kon ventil�toru pro p��vod vzduchu
'fan_pwm_exhaust': 46,    #v�kon ventil�toru pro odtah vzduchu
'fan_rpm_supply': 47,    #ot��ky ventil�toru pro p��vod vzduchu
'fan_rpm_exhaust': 48,    #ot��ky ventil�toru pro odtah vzduchu
'voltage_input1': 49,    #nap�t� vstupu UIN1
'voltage_input2': 50,    #nap�t� vstupu UIN2
'digital_inputs': 51,    #digit�ln� vstupy (bit0 - user button, bit1 - fact button, bit2 - boost input, bit3 - uint1, bit4 � uint2)
'sys_battery_voltage': 52,    #napt� z�lo�n� baterie pro RTC
# Sb�rnice periferi� Modbus RTU
'mbdev_reads0': 60,    #statistika, po�et �ten�
'mbdev_reads1': 61,    #statistika, po�et �ten�
'mbdev_writes0': 62,    #statistika, po�et z�pis�
'mbdev_writes1': 63,    #statistika, po�et z�pis�
'mbdev_fails0': 64,    #statistika, po�et chyb
'mbdev_fails1': 65,    #statistika, po�et chyb
'mbdev_mk_ui': 66,    #p�ipojen� ovlada�e UI, bity 0..2 (bity p�edstavuj� jednotliv� ovlada�e )
'mbdev_mk_sens0': 67,    #p�ipojen� CO2 senzory, bity 0..15
'mbdev_mk_sens1': 68,    #p�ipojen� CO2 senzory, bity 16..31
'mbdev_coolbreeze': 69,    #p�ipojen� coolbreeze, bit 0
'mbdev_valve_sup0': 70,    #p�ipojen� klapky na p��vodu, bity 0..15
'mbdev_valve_sup1': 71,    #p�ipojen� klapky na p��vodu, bity 16..31
'mbdev_valve_exh0': 72,    #p�ipojen� klapky na odtahu, bity 0..15
'mbdev_valve_exh1': 73,    #p�ipojen� klapky na odtahu, bity 16..31
'mbdev_buttons': 74,    #p�ipojen� tla��tka boost, bity 0..7
# Ovlada�e UI Mikroklima
'mk_ui_mb_address_0': 100,    #Ovlada� 0 � MB RTU adresa
'mk_ui_options_0': 101,    #Ovlada� 0 � bit0=nepou��vat v auto. re�imu
'mk_ui_co2_0': 102,    #Ovlada� 0 � m��en� hodnota CO2
'mk_ui_temp_0': 103,    #Ovlada� 0 � m��en� teplota
'mk_ui_humi_0': 104,    #Ovlada� 0 � m��en� relativn� vlhkost
'mk_ui_mb_address_1': 105,    #Ovlada� 1 � MB RTU adresa
'mk_ui_options_1': 106,    #Ovlada� 1 � bit0=nepou��vat v auto. re�imu
'mk_ui_co2_1': 107,    #Ovlada� 1 � m��en� hodnota CO2
'mk_ui_temp_1': 108,    #Ovlada� 1 � m��en� teplota
'mk_ui_humi_1': 109,    #Ovlada� 1 � m��en� relativn� vlhkost
'mk_ui_mb_address_2': 110,    #Ovlada� 2 � MB RTU adresa
'mk_ui_options_2': 111,    #Ovlada� 2 � bit0=nepou��vat v auto. re�imu
'mk_ui_co2_2': 112,    #Ovlada� 2 � m��en� hodnota CO2
'mk_ui_temp_2': 113,    #Ovlada� 2 � m��en� teplota
'mk_ui_humi_2': 114,    #Ovlada� 2 � m��en� relativn� vlhkost
# CO2 senzory Mikroklima
'mk_sens_mb_address_0': 115,    #Senzor 0 � MB RTU adresa
'mk_sens_options_0': 116,    #Senzor 0 � bit0=nepou��vat v auto. re�imu
'mk_sens_co2_0': 117,    #Senzor 0 � m��en� hodnota CO2
'mk_sens_temp_0': 118,    #Senzor 0 � m��en� teplota
'mk_sens_humi_0': 119,    #Senzor 0 � m��en� relativn� vlhkost
# � dal��ch 7 senzor�
# Tepeln� v�m�n�k
'exchanger_status': 900,
'exchanger_valve_pos0': 901,
'exchanger_valve_pos1': 902,
'exchanger_valve_pos2': 903,
'exchanger_valve_pos3': 904,
'exchanger_maxopen0': 905,
'exchanger_maxopen1': 906,
'exchanger_maxopen2': 907,
'exchanger_maxopen3': 908,
'in_position': 909,
'switch_tm': 910,
'period1': 911,
'period2': 912,
'switch_count0': 913,
'switch_count1': 914,
'valve_fail_count_0': 915,
'valve_fail_count_1': 916,
'valve_fail_count_2': 917,
'valve_fail_count_3': 918,
# Skute�n� hodnoty �idel
't_ambient': 930,    #teplota venkovn�ho vzduchu
't_fresh': 931,    #teplota dod�van�ho vzduchu do domu
't_indoor': 932,    #teplota ods�van�ho vzduchu z domu
't_waste': 933,    #teplota odpadn�ho vzduchu
'rh_ambient': 934,    #relativn� vlhkost venkovn�ho vzduchu
'rh_fresh': 935,    #relativn� vlhkost dod�van�ho vzduchu do domu
'rh_indoor': 936,    #relativn� vlhkost ods�van�ho vzduchu z domu
'rh_waste': 937,    #relativn� vlhkost odpadn�ho vzduchu
't_ntc': 938,    #teplota extern�ho NTC senzoru venkovn� teploty
# Coolbreeze
'cb_mode': 950,
'cb_power': 951,
'cb_temp_indoor': 952,
'cb_humi_indoor': 953,
'cb_temp_ntc': 954,
'cb_temp_exch': 955,
'cb_temp_out': 956,
'cb_out_status': 957,
'cb_status': 958,
'cb_cur_power': 959,
'cb_errcode': 960,
'cb_fw_version': 961,
'cb_power_consumption': 962,
}

futuraHoldingRegisters = {
'boost_tm': 1,    #Funkce Boost �ten�: zb�vaj�c� �as z�pis: �as 0 � 7200 s
'circulation_tm': 2,    #Funkce Cirkulace �ten�: zb�vaj�c� �as z�pis: �as 0 � 7200 s
'overpressure_tm': 3,    #Funkce P�etlak �ten�: zb�vaj�c� �as z�pis: �as 0 � 7200 s
'night_tm': 4,    #Funkce Noc �ten�: zb�vaj�c� �as z�pis: �as 0 � 7200 s
'party_tm': 5,    #Funkce Party �ten�: zb�vaj�c� �as z�pis: �as 0 � 28800 s
'away_begin0': 6,    #Funkce Dovolen� - za��tek, unix timestamp, local time, 0=off
'away_begin1': 7,    #Funkce Dovolen� - za��tek, unix timestamp, local time, 0=off
'away_end0': 8,    #Funkce Dovolen� - konec, unix timestamp, local time, 0=off
'away_end1': 9,    #Funkce Dovolen� - konec, unix timestamp, local time, 0=off
'cfg_temp_set': 10,    #Preferovan� teplota
'cfg_humi_set': 11,    #Preferovan� vlhkost
'func_time_prog': 12,    #Zapnut�/vypnut� �asov�ho programu
'func_antiradon': 13,    #Povolen� protiradonov� ochrany
'cfg_bypass_enable': 14,    #Povolen� automatick�ho ��zen� bypasu
'cfg_heating_enable': 15,    #Povolen� topen� doh�evu
'cfg_cooling_enable': 16,    #Povolen� topen� doh�evu
'cfg_comfort_enable': 17,    #Povolen� komfortn�ho doh�evu
'access_code': 900,    #povolen� p��stupu k servisn�m registr�m �ten�: povolen� p��stup 0/1 Z�pis: spr�vn� k�d povoluje p��stup, jin� hodnota zakazuje
'fut_control': 901,    #registr pro ��d�c� p��kazy �ten�: odpov�� na p��kaz, pouze 16 bit� Z�pis: p��kaz, pouze 16 bit�
'fut_parametr0': 902,    #parametr pro ��d�c� p��kaz, spodn�ch 16 bit�
'fut_parametr1': 903,    #parametr pro ��d�c� p��kaz, horn�ch 16 bit�
'fut_fan_pwm_supply': 904,    #aktu�ln� nastaven� ventil�tor�, b�hem servisn�ho re�imu umo��uje p��m� ovl�d�n�
'fut_fan_pwm_exhaust': 905,    #aktu�ln� nastaven� ventil�tor�, b�hem servisn�ho re�imu umo��uje p��m� ovl�d�n�
'exch_mode': 906,    #aktu�ln� re�im v�m�n�ku (0, 1..8), b�hem servisn�ho re�imu umo��uje p��m� ovl�d�n�
'exch_period1': 907,    #periody p�ekl�p�n� v�m�n�ku
'exch_period2': 908,    #periody p�ekl�p�n� v�m�n�ku
'fut_flaps': 909,    #stav klapek bypass a vysou�en�
'fut_heating_pwm': 910,    #aktu�ln� v�kon vnit�n�ho topen�
'cb_mode': 911,    #aktu�ln� re�im coolbreezu: b0=cool, b1=heat
'cb_power': 912,    #aktu�ln� v�kon coolbreezu: 0..30
}

