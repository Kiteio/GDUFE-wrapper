@echo off
setlocal enabledelayedexpansion
ping -n 1 www.bilibili.com >nul

if errorlevel 1 (
    set name=你的学号
    set pwd=你的密码
    set ip=你的电脑ip
    curl "http://100.64.13.17:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=%%2C0%%2C!name!&user_password=!pwd!&wlan_user_ip=!ip!&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=100.64.13.18&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=5545&lang=zh"
)

pause
