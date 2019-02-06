# -*- coding: utf-8 -*-

futuraInputRegisters = {
'fact_device_id': {'regNr': 0, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #identifikace zařízení, pro Futuru2 vždy 39
'fact_serial_number': {'regNr': 1, 'size': 2, 'format': 'UINT', 'power': '', 'min': 2, 'max': ''},    #sériové číslo zařízení, bity 0..15
'fact_ethernet_mac': {'regNr': 3, 'size': 3, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #MAC adresa zařízení
'fact_hw_revision': {'regNr': 6, 'size': 2, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #verze hardware
'firm_revision': {'regNr': 8, 'size': 2, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #verze firmware
'sys_build_number': {'regNr': 10, 'size': 2, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #fw build number
'sys_regmap_version': {'regNr': 12, 'size': 2, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #verze mapy registrů
'sys_options': {'regNr': 14, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #varianta zařízení (0=Futura L, 1=Futura M)
'fut_config': {'regNr': 15, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #možnosti zařízení (b0=int. heating, b1=CB cooling, b2=CB heating)
'fut_mode': {'regNr': 16, 'size': 2, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #aktuální režim zařízení
'fut_error': {'regNr': 18, 'size': 2, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #poruchy zařízení
'fut_warning': {'regNr': 20, 'size': 2, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #výstrahy zařízení
'fut_temp_ambient': {'regNr': 30, 'size': 1, 'format': 'SINT', 'power': 10, 'min': '', 'max': ''},    #teplota venkovního vzduchu
'fut_temp_fresh': {'regNr': 31, 'size': 1, 'format': 'SINT', 'power': 10, 'min': '', 'max': ''},    #teplota dodávaného vzduchu do domu
'fut_temp_indoor': {'regNr': 32, 'size': 1, 'format': 'SINT', 'power': 10, 'min': '', 'max': ''},    #teplota odsávaného vzduchu z domu
'fut_temp_waste': {'regNr': 33, 'size': 1, 'format': 'SINT', 'power': 10, 'min': '', 'max': ''},    #teplota odpadního vzduchu
'fut_humi_ambient': {'regNr': 34, 'size': 1, 'format': 'SINT', 'power': 10, 'min': 0, 'max': 100},    #relativní vlhkost venkovního vzduchu
'fut_humi_fresh': {'regNr': 35, 'size': 1, 'format': 'SINT', 'power': 10, 'min': 0, 'max': 100},    #relativní vlhkost dodávaného vzduchu do domu
'fut_humi_indoor': {'regNr': 36, 'size': 1, 'format': 'SINT', 'power': 10, 'min': 0, 'max': 100},    #relativní vlhkost odsávaného vzduchu z domu
'fut_humi_waste': {'regNr': 37, 'size': 1, 'format': 'SINT', 'power': 10, 'min': 0, 'max': 100},    #relativní vlhkost odpadního vzduchu
'fut_t_out': {'regNr': 38, 'size': 1, 'format': 'SINT', 'power': 10, 'min': '', 'max': ''},    #teplota externího NTC senzoru venkovní teploty
'fut_filter_wear_level': {'regNr': 40, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #hodnota zanesení filtrů 0-100%
'fut_power_consumption': {'regNr': 41, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #aktuální příkon jednotky
'fut_heat_recovering': {'regNr': 42, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #aktuální hodnota zpětně získávaného tepla
'fut_heating_power': {'regNr': 43, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #výkon topení dohřevu
'fut_air_flow': {'regNr': 44, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #aktuální průtok vzduchu
'fut_fan_pwm_supply': {'regNr': 45, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #výkon ventilátoru pro přívod vzduchu
'fut_fan_pwm_exhaust': {'regNr': 46, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #výkon ventilátoru pro odtah vzduchu
'fut_fan_rpm_supply': {'regNr': 47, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #otáčky ventilátoru pro přívod vzduchu
'fut_fan_rpm_exhaust': {'regNr': 48, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #otáčky ventilátoru pro odtah vzduchu
'fut_uin1_voltage': {'regNr': 49, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #napětí vstupu UIN1
'fut_uin2_voltage': {'regNr': 50, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #napětí vstupu UIN2
'fut_dig_inputs': {'regNr': 51, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #digitální vstupy (bit0 - user button, bit1 - fact button, bit2 - boost input, bit3 - uint1, bit4 – uint2)
'sys_battery_voltage': {'regNr': 52, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #naptí záložní baterie pro RTC
'mbdev_stat_reads': {'regNr': 60, 'size': 2, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #statistika, počet čtení
'mbdev_stat_writes': {'regNr': 62, 'size': 2, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #statistika, počet zápisů
'mbdev_stat_fails': {'regNr': 64, 'size': 2, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #statistika, počet chyb
'mbdev_connected_mk_ui': {'regNr': 66, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #připojené ovladače UI, bity 0..2 (bity představují jednotlivé ovladače )
'mbdev_connected_mk_sens': {'regNr': 67, 'size': 2, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #připojené CO2 senzory, bity 0..15
'mbdev_connected_coolbreeze': {'regNr': 69, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #připojený coolbreeze, bit 0
'mbdev_connected_valve_supply': {'regNr': 70, 'size': 2, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #připojené klapky na přívodu, bity 0..15
'mbdev_connected_valve_exhaust': {'regNr': 72, 'size': 2, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #připojené klapky na odtahu, bity 0..15
'mbdev_connected_button': {'regNr': 74, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #připojené tlačítka boost, bity 0..7
'mbuimk_mb_address_0': {'regNr': 100, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #Ovladač 0 – MB RTU adresa
'mbuimk_options_0': {'regNr': 101, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #Ovladač 0 – bit0=nepoužívat v auto. režimu
'mbuimk_co2_0': {'regNr': 102, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #Ovladač 0 – měřená hodnota CO2
'mbuimk_temp_0': {'regNr': 103, 'size': 1, 'format': 'SINT', 'power': 10, 'min': '', 'max': ''},    #Ovladač 0 – měřená teplota
'mbuimk_humi_0': {'regNr': 104, 'size': 1, 'format': 'UINT', 'power': 10, 'min': '', 'max': ''},    #Ovladač 0 – měřená relativní vlhkost
'mbuimk_mb_address_1': {'regNr': 105, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #Ovladač 1 – MB RTU adresa
'mbuimk_options_1': {'regNr': 106, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #Ovladač 1 – bit0=nepoužívat v auto. režimu
'mbuimk_co2_1': {'regNr': 107, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #Ovladač 1 – měřená hodnota CO2
'mbuimk_temp_1': {'regNr': 108, 'size': 1, 'format': 'SINT', 'power': 10, 'min': '', 'max': ''},    #Ovladač 1 – měřená teplota
'mbuimk_humi_1': {'regNr': 109, 'size': 1, 'format': 'UINT', 'power': 10, 'min': '', 'max': ''},    #Ovladač 1 – měřená relativní vlhkost
'mbuimk_mb_address_2': {'regNr': 110, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #Ovladač 2 – MB RTU adresa
'mbuimk_options_2': {'regNr': 111, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #Ovladač 2 – bit0=nepoužívat v auto. režimu
'mbuimk_co2_2': {'regNr': 112, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #Ovladač 2 – měřená hodnota CO2
'mbuimk_temp_2': {'regNr': 113, 'size': 1, 'format': 'SINT', 'power': 10, 'min': '', 'max': ''},    #Ovladač 2 – měřená teplota
'mbuimk_humi_2': {'regNr': 114, 'size': 1, 'format': 'UINT', 'power': 10, 'min': '', 'max': ''},    #Ovladač 2 – měřená relativní vlhkost
'mbsemk_mb_address_0': {'regNr': 115, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #Senzor 0 – MB RTU adresa
'mbsemk_options_0': {'regNr': 116, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #Senzor 0 – bit0=nepoužívat v auto. režimu
'mbsemk_co2_0': {'regNr': 117, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #Senzor 0 – měřená hodnota CO2
'mbsemk_temp_0': {'regNr': 118, 'size': 1, 'format': 'SINT', 'power': 10, 'min': '', 'max': ''},    #Senzor 0 – měřená teplota
'mbsemk_humi_0': {'regNr': 119, 'size': 1, 'format': 'UINT', 'power': 10, 'min': '', 'max': ''},    #Senzor 0 – měřená relativní vlhkost
'exch_state': {'regNr': 900, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'exch_valve_position_0': {'regNr': 901, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'exch_valve_position_1': {'regNr': 902, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'exch_valve_position_2': {'regNr': 903, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'exch_valve_position_3': {'regNr': 904, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'exch_valve_maxopen_0': {'regNr': 905, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'exch_valve_maxopen_1': {'regNr': 906, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'exch_valve_maxopen_2': {'regNr': 907, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'exch_valve_maxopen_3': {'regNr': 908, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'exch_in_position': {'regNr': 909, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'exch_switch_tm': {'regNr': 910, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'exch_period1': {'regNr': 911, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'exch_period2': {'regNr': 912, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'exch_switch_count, bytes 0, 1': {'regNr': 913, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'exch_switch_count, bytes 2, 3': {'regNr': 914, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'exch_valve_fail_count_0': {'regNr': 915, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'exch_valve_fail_count_1': {'regNr': 916, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'exch_valve_fail_count_2': {'regNr': 917, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'exch_valve_fail_count_3': {'regNr': 918, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'fut_t_amb': {'regNr': 930, 'size': 1, 'format': 'SINT', 'power': 10, 'min': '', 'max': ''},    #teplota venkovního vzduchu
'fut_t_fre': {'regNr': 931, 'size': 1, 'format': 'SINT', 'power': 10, 'min': '', 'max': ''},    #teplota dodávaného vzduchu do domu
'fut_t_ind': {'regNr': 932, 'size': 1, 'format': 'SINT', 'power': 10, 'min': '', 'max': ''},    #teplota odsávaného vzduchu z domu
'fut_t_was': {'regNr': 933, 'size': 1, 'format': 'SINT', 'power': 10, 'min': '', 'max': ''},    #teplota odpadního vzduchu
'fut_rh_amb': {'regNr': 934, 'size': 1, 'format': 'SINT', 'power': 10, 'min': '', 'max': ''},    #relativní vlhkost venkovního vzduchu
'fut_rh_fre': {'regNr': 935, 'size': 1, 'format': 'SINT', 'power': 10, 'min': '', 'max': ''},    #relativní vlhkost dodávaného vzduchu do domu
'fut_rh_ind': {'regNr': 936, 'size': 1, 'format': 'SINT', 'power': 10, 'min': '', 'max': ''},    #relativní vlhkost odsávaného vzduchu z domu
'fut_rh_was': {'regNr': 937, 'size': 1, 'format': 'SINT', 'power': 10, 'min': '', 'max': ''},    #relativní vlhkost odpadního vzduchu
'fut_t_out': {'regNr': 938, 'size': 1, 'format': 'SINT', 'power': 10, 'min': '', 'max': ''},    #teplota externího NTC senzoru venkovní teploty
'cb_mode': {'regNr': 950, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'cb_power': {'regNr': 951, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'cb_temp_indoor': {'regNr': 952, 'size': 1, 'format': 'SINT', 'power': 10, 'min': '', 'max': ''},    #
'cb_humi_indoor': {'regNr': 953, 'size': 1, 'format': 'SINT', 'power': 10, 'min': '', 'max': ''},    #
'cb_temp_ntc': {'regNr': 954, 'size': 1, 'format': 'SINT', 'power': 10, 'min': '', 'max': ''},    #
'cb_temp_exch': {'regNr': 955, 'size': 1, 'format': 'SINT', 'power': 10, 'min': '', 'max': ''},    #
'cb_temp_out': {'regNr': 956, 'size': 1, 'format': 'SINT', 'power': 10, 'min': '', 'max': ''},    #
'cb_out_status': {'regNr': 957, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'cb_status': {'regNr': 958, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'cb_cur_power': {'regNr': 959, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'cb_errcode': {'regNr': 960, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'cb_fw_version': {'regNr': 961, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
'cb_power_consumption': {'regNr': 962, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #
}

futuraHoldingRegisters = {
'func_ventilation': {'regNr': 0, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': 0.0, 'max': 6.0},    #nastavený výkon větrání 0 – vypnuto 1..5 – přednastavená úroveň 1 až 5 6 – automatické větrání podle hodnoty CO2 nebo ext. vstupu
'func_boost_tm': {'regNr': 1, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': 0.0, 'max': 7200.0},    #Funkce Boost čtení: zbývající čas zápis: čas 0 – 7200 s
'func_circulation_tm': {'regNr': 2, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': 0.0, 'max': 7200.0},    #Funkce Cirkulace čtení: zbývající čas zápis: čas 0 – 7200 s
'func_overpressure_tm': {'regNr': 3, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': 0.0, 'max': 7200.0},    #Funkce Přetlak čtení: zbývající čas zápis: čas 0 – 7200 s
'func_night_tm': {'regNr': 4, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': 0.0, 'max': 7200.0},    #Funkce Noc čtení: zbývající čas zápis: čas 0 – 7200 s
'func_party_tm': {'regNr': 5, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': 0.0, 'max': 28800.0},    #Funkce Party čtení: zbývající čas zápis: čas 0 – 28800 s
'func_away_begin': {'regNr': 6, 'size': 2.0, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #Funkce Dovolená - začátek, unix timestamp, local time, 0=off
'func_away_end': {'regNr': 8, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #Funkce Dovolená - konec, unix timestamp, local time, 0=off
'func_away_end': {'regNr': 9, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #Funkce Dovolená - konec, unix timestamp, local time, 0=off
'cfg_temp_set': {'regNr': 10, 'size': 1.0, 'format': 'UINT', 'power': 10.0, 'min': 50.0, 'max': 300.0},    #Preferovaná teplota
'cfg_humi_set': {'regNr': 11, 'size': 1.0, 'format': 'UINT', 'power': 10.0, 'min': 0.0, 'max': 100.0},    #Preferovaná vlhkost
'func_time_prog': {'regNr': 12, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': 0.0, 'max': 255.0},    #Zapnutí/vypnutí časového programu
'func_antiradon': {'regNr': 13, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': 0.0, 'max': 255.0},    #Povolení protiradonové ochrany
'cfg_bypass_enable': {'regNr': 14, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': 0.0, 'max': 255.0},    #Povolení automatického řízení bypasu
'cfg_heating_enable': {'regNr': 15, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': 0.0, 'max': 255.0},    #Povolení topení dohřevu
'cfg_cooling_enable': {'regNr': 16, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': 0.0, 'max': 255.0},    #Povolení topení dohřevu
'cfg_comfort_enable': {'regNr': 17, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': 0.0, 'max': 255.0},    #Povolení komfortního dohřevu
'access_code': {'regNr': 900, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #povolení přístupu k servisním registrům Čtení: povolený přístup 0/1 Zápis: správný kód povoluje přístup, jiná hodnota zakazuje
'fut_control': {'regNr': 901, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': 0.0, 'max': '0xFFFF'},    #registr pro řídící příkazy Čtení: odpověď na příkaz, pouze 16 bitů Zápis: příkaz, pouze 16 bitů
'fut_parameter': {'regNr': 902, 'size': 2.0, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #parametr pro řídící příkaz, spodních 16 bitů
'fut_fan_pwm_supply': {'regNr': 904, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': 0.0, 'max': 100.0},    #aktuální nastavení ventilátorů, během servisního režimu umožňuje přímé ovládání
'fut_fan_pwm_exhaust': {'regNr': 905, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': 0.0, 'max': 100.0},    #aktuální nastavení ventilátorů, během servisního režimu umožňuje přímé ovládání
'exch_mode': {'regNr': 906, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': 0.0, 'max': 8.0},    #aktuální režim výměníku (0, 1..8), během servisního režimu umožňuje přímé ovládání
'exch_period1': {'regNr': 907, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #periody překlápění výměníku
'exch_period2': {'regNr': 908, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #periody překlápění výměníku
'fut_flaps': {'regNr': 909, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #stav klapek bypass a vysoušení
'fut_heating_pwm': {'regNr': 910, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': 0.0, 'max': 100.0},    #aktuální výkon vnitřního topení
'cb_mode': {'regNr': 911, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': 0.0, 'max': 1.0},    #aktuální režim coolbreezu: b0=cool, b1=heat
'cb_power': {'regNr': 912, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': 0.0, 'max': 30.0},    #aktuální výkon coolbreezu: 0..30
'fut_t_amb': {'regNr': 930, 'size': 1.0, 'format': 'SINT', 'power': 10.0, 'min': '', 'max': ''},    #teplota přiváděného vzduchu z venku
'fut_rh_amb': {'regNr': 931, 'size': 1.0, 'format': 'SINT', 'power': 10.0, 'min': '', 'max': ''},    #relativní vlhkost přiváděného vzduchu z venku
'fut_t_fre': {'regNr': 932, 'size': 1.0, 'format': 'SINT', 'power': 10.0, 'min': '', 'max': ''},    #teplota dodávaného vzduchu do domu
'fut_rh_fre': {'regNr': 933, 'size': 1.0, 'format': 'SINT', 'power': 10.0, 'min': '', 'max': ''},    #relativní vlhkost dodávaného vzduchu do domu
'fut_t_ind': {'regNr': 934, 'size': 1.0, 'format': 'SINT', 'power': 10.0, 'min': '', 'max': ''},    #teplota odsávaného vzduchu z domu
'fut_rh_ind': {'regNr': 935, 'size': 1.0, 'format': 'SINT', 'power': 10.0, 'min': '', 'max': ''},    #relativní vlhkost odsávaného vzduchu z domu
'fut_t_was': {'regNr': 936, 'size': 1.0, 'format': 'SINT', 'power': 10.0, 'min': '', 'max': ''},    #teplota odpadního vzduchu
'fut_rh_was': {'regNr': 937, 'size': 1.0, 'format': 'SINT', 'power': 10.0, 'min': '', 'max': ''},    #relativní vlhkost odpadního vzduchu
'fut_t_out': {'regNr': 938, 'size': 1.0, 'format': 'SINT', 'power': 10.0, 'min': '', 'max': ''},    #teplota externího NTC senzoru venkovní teploty
'fut_fan_rpm_supply': {'regNr': 939, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #otáčky ventilátoru pro přívod vzduchu
'fut_fan_rpm_exhaust': {'regNr': 940, 'size': 1.0, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #otáčky ventilátoru pro odtah vzduchu
'fut_co2_ppm_max': {'regNr': 941, 'size': 2.0, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},    #maximální hodnota CO2 ze všech čidel
}

