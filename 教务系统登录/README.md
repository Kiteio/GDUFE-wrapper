# 教务系统登录

<p>

[![](https://img.shields.io/static/v1?label=Python&message=3.12.x&labelColor=white&color=white&logo=python)](https://www.python.org/downloads/)

</p>

**本脚本只是使用 Python 模拟用户登录，非专业人员请不要继续**

## 用法

使用 pip 下载依赖：

```
pip install bs4 ddddocr requests
```

实例化`EduSystem`即可登录：

```py
if __name__ == "__main__":
    EduSystem(21251107799, "abcd1234")
```

你可以在`EduSystem`中定义一些其他方法，获取教务系统中的信息（相关的 API 请自行前往控制台获取）：

```py
class EduSystem(SessionRouter):
    # ...

    def get_timetable(self):
        self.get("route/to/timetable")

if __name__ == "__main__":
    eduSystem = EduSystem(21251107799, "abcd1234")

    eduSystem.get_timetable()
```

## 文档

- `SessionRouter`

主要负责管理 API 路由和会话。

| 名称                                | 类型                 | 描述                                                     |
|-----------------------------------|--------------------|--------------------------------------------------------|
| `_root`                           | `str`              | API 根路径                                                |
| `_session`                        | `requests.Session` | 会话支持                                                   |
| `get(self, route, params)`        | `Function`         | 使用会话发送 GET 请求，与`requests.Session.get`类似，但`url`参数改为路由   |
| `post(self, route, params, data)` | `Function`         | 使用会话发送 POST 请求，与`requests.Session.post`类似，但`url`参数改为路由 |

- `EduSystem`(`SessionRouter`)

教务系统

| 名称             | 类型         | 描述     |
|----------------|------------|--------|
| `username`     | `int`      | 学号     |
| `_password`    | `str`      | 密码     |
| `_login(self)` | `Function` | 登录教务系统 |