"""
读取配置文件中的数据，获取测试用例的执行命令，获取allure报告的生成命令，通过os.system("命令")执行测试并生成测试报告
把测试报告进行压缩后打包通过邮件发送
"""
import os
import py_yaml
import traceback
from Toolbox.Log import Logger
from Toolbox.zip_file import zip_files
from Toolbox.send_email import SendEmail

logging = Logger(__name__).get_logger()


def run_cases():
    test_allure = "pytest ./test_cases/ -s -q --clean-alluredir --alluredir=./result/"
    os.system(test_allure)  # 通过pytest 结合allure执行测试用例
    make_report = "allure generate ./result/ -o ./allure-report/ --clean"
    os.system(make_report)  # 通过测试数据生成测试报告
    dir_path = r'./allure-report'
    zip_path = r'./report_zip/report.zip'
    zip_report = zip_files(dir_path, zip_path)
    if zip_report:
        file_name = r'./config.yaml'
        file_path = zip_path
        content = "测试执行结束，Allure测试报告在邮件附件中，请使用Pycharm打开查看。"
        Subject = '陈强接口场景式自动化测试报告'  # 邮件标题
        From = "陈强的QQ邮箱"  # 邮件主体中发送者名称
        To = "领导的163邮箱"  # 邮件主体中接收者名称
        try:
            with open(file_name, "r", encoding="UTF-8") as f:
                config = yaml.safe_load(f)
                config_email = config["Email"]
            send = SendEmail(mail_host=config_email['mail_host'],
                             mail_user=config_email['mail_user'],
                             mail_pass=config_email['mail_pass'],
                             sender=config_email['sender'],
                             receives=config_email['receives']
                             )
            send.make_email_by_att(content, file_path, Subject, From, To)
            logging.info(f"邮件发送成功，邮件标题：{Subject}")
        except Exception as e:
            error_inf = traceback.format_exc()
            logging.error(f"读取配置文件::{file_name}并发送邮件::失败::{e}::失败详情:{error_inf}")


if __name__ == '__main__':
    run_cases()