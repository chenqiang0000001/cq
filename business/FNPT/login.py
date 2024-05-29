import requests
from Public.FNPT.address import *
from Public.FNPT.veriables import *


class Login:
    """
        登陆登出相关模块
        """

    def login_firm(self, account=account,headers= "", password=password):
        """
        :param account: 账号
        :param password: 密码
        :return:
        """
        url = firm_url + login_api
        uploads = {
                      "account": account,
                      "password": password
                  },
        requests.post(url=url, headers=headers, json=uploads)


if __name__ == '__main__':
    res = Login.login_firm()
    print(res)
