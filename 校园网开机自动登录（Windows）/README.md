# 校园网开机自动登录（Windows）

**请勿轻信从别人那里得到的脚本**

该脚本使用 VBScript 编写，利用其源代码`.vbs`文件能被 Windows 直接运行的特点（双击运行，并且不像`.cmd`有黑窗口），将其放置到`启动`目录中，开机时便会运行该脚本并登录校园网（前提是开机登录后已经连上校园网）。

## 快速上手

1. 参照[如何获取本机 IP](#如何获取本机-ip)，得到你的 Windows 的 ip 地址。

2. 保存 [network.vbs](network.vbs)，使用记事本打开，将脚本中第六行开始的`你的学号`、`你的校园网密码`和`你的电脑ip`改为你自己的信息。
    ```vbscript
    Set WshShell = CreateObject("WScript.Shell")

    result = WshShell.Run("ping www.bilibili.com", 0, True)

    If result <> 0 Then
        name = "21251107799"
        pwd = "123456"
        ip = "192.168.1.1"

        url = "http://100.64.13.17:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=%2C0%2C" & name & "&user_password=" & pwd & "&wlan_user_ip=" & ip & "&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=100.64.13.18&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=5545&lang=zh"

        WShShell.Run "curl " & """" & url & """", 0
    End If

    ```

3. 将编辑好的 [network.vbs](network.vbs) 保存，并存放到下方的目录里：
    ```
    C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
    ```

    大功告成！在你下次启动电脑时，该脚本便会自动运行并登录校园网。

## 调试

如果你不清楚自己配置的信息是否正确，可以保存 [debug.cmd](debug.cmd)（请不要把它也放到`启动`里），将你在 [network.vbs](network.vbs) 中的配置填到其中（第六行开始），双击运行该脚本查看运行信息。

```cmd
@echo off
setlocal enabledelayedexpansion
ping -n 1 www.bilibili.com >nul

if errorlevel 1 (
    set name=21251107799
    set pwd=123456
    set ip=192.168.1.1
    curl "http://100.64.13.17:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=%%2C0%%2C!name!&user_password=!pwd!&wlan_user_ip=!ip!&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=100.64.13.18&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=5545&lang=zh"
)

pause

```

## 如何获取本机 IP

### 方法 1：从网站获取（推荐）

1. 连接校园网，打开 http://100.64.13.17/drcom/chkstatus?callback=dr1002 （校园网官方接口）
2. 按下键盘组合键`Ctrl`+`F`，在输入框输入`v46ip`，在它的右侧有一串数字

### 方法 2：从设置获取

1. 连接校园网
2. 按下键盘组合键`Win（Windows 图标）`+`I`打开 Windows 设置
3. 在左侧选择`网络和 Internet`
4. 在右侧点击`属性`
5. 找到`IPv4 地址`

### 方法 3：从命令行获取

1. 连接校园网
2. 按下键盘组合键`Win（Windows 图标）`+`R`，输入`cmd`并确定，打开命令行黑窗口
3. 在黑窗口输入`ipconfig`，按下`Enter`
4. 找到`IPv4 地址`