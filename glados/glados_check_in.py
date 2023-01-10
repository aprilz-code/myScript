"""GLaDOS自动打卡"""
import os
import sys

import requests
from requests import Timeout


class Gladosci:
    """GLaDOS自动打卡"""

    def __init__(self) -> None:
        self.fail = False
        self.title: str
        self.content: str

    def __call__(self) -> None:
        try:
            self.check_in()
        except Timeout:
            print("GLaDOS响应超时，打卡失败")
            self.title = self.content = "GLaDOS响应超时，打卡失败"
            self.fail = True

        try:
            self.notify()
        except Timeout:
            sys.exit("pushplus响应超时")

    def check_in(self) -> None:
        """打卡"""
        cookie = os.environ["GLADOS_COOKIE"]
        data = {"token": "glados.network"}
        url = "https://glados.rocks/api/user/checkin"
        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit\
    /537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50",
            "cookie": cookie,
        }

        response = requests.post(url, headers=headers, data=data, timeout=10).json()

        if response["message"] in [
            "Checkin! Get 1 Day",
            "Please Try Tomorrow",
            "Checkin! Get 0 day(Your lucky chance is 33%),try next time.",
        ]:
            print(response["message"])
            self.title = "GLaDOS打卡成功"
        else:
            print("返回未知响应，按打卡失败处理")
            print(response["message"])
            self.title = "GLaDOS返回未知响应"
            self.fail = True

        self.content = response["message"]

    def notify(self) -> None:
        """推送打卡成功与否的消息"""
        pushplus = os.environ["PUSH_PLUS_TOKEN"]
        if pushplus:
            print(f"推送{self.title}的消息")

            data = {
                "token": pushplus,
                "title": self.title,
                "content": self.content,
            }
            url = "http://www.pushplus.plus/send/"
            print(requests.post(url, data=data, timeout=5).text)
        elif self.fail:
            sys.exit("GLaDOS打卡失败")


if __name__ == "__main__":
    gci = Gladosci()
    gci()