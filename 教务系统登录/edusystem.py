import logging
import sys

from bs4 import BeautifulSoup
from ddddocr import DdddOcr
from requests import Session, Response

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
)


class SessionRouter:
    def __init__(self, root: str):
        """会话路由器

        接收 root 作为会话的根网址，并提供 get post 方法用于发送会话网络请求
        """
        self._root = root
        with Session() as session:
            self._session = session

    def get(self, route: str, params: dict | None = None) -> Response:
        """返回 Session.get"""
        return self._session.get(f"{self._root}/{route}", params=params)

    def post(
            self,
            route: str,
            params: dict | None = None,
            data: dict | None = None,
    ) -> Response:
        """返回 Session.post"""
        return self._session.post(f"{self._root}/{route}", params=params, data=data)


def beautiful_soup(response: Response, features: str="html.parser") -> BeautifulSoup:
    """返回解析 response.text 后的 BeautifulSoup 对象"""
    return BeautifulSoup(response.text, features)


class EduSystem(SessionRouter):
    def __init__(self, username: int, password: str):
        """教务系统

        接收 username（学号）和 password（门户密码），并进行登录
        """
        super().__init__("http://jwxt.gdufe.edu.cn")

        self.username = username
        self._password = password
        self._login()

    def _login(self):
        """教务系统递归（验证码错误时）登录"""
        logging.info(f"{self.username} 正在登录")
        # 获取、识别验证码
        content = self.get("jsxsd/verifycode.servlet").content
        data = {
            "USERNAME": self.username,
            "PASSWORD": self._password,
            "RANDOMCODE": DdddOcr(show_ad=False).classification(content)
        }

        # 发送登录请求
        soup = beautiful_soup(self.post("jsxsd/xk/LoginToXkLdap", data=data))

        # 检验登录结果
        title = soup.find("title").text

        if title == "学生个人中心":
            # 重定向到个人中心，登录成功
            return logging.info(f"{self.username} 登录成功")
        elif title == "广东财经大学综合教务管理系统-强智科技":
            # 还在登录页面，有提示信息
            tip = soup.find("font").text

            if tip != "验证码错误!!":
                logging.error(f"登录失败: {tip}")
                sys.exit(1)

            # 验证码错误，重新登录
            logging.info(f"{self.username} 验证码错误")
            self._login()
        else:
            # 重定向到未知位置
            logging.error(f"登录失败：{title}")
            sys.exit(1)


if __name__ == "__main__":
    EduSystem(21251107799, "abcd1234")
