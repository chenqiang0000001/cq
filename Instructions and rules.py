# 自动化测试框架说明及维护规则
#
# 文件说明：
# -EmergenAutomate  # 智昌接口自动化测试框架
# --AllurData  # 生成Allur报告
#
# --AllureReport  # 调试Allur报告
#
# --business  # 业务函数封装模块，按系统分模块
# ---WKY
# ---MES
# ---FNPT
# ---X2server
#
# --Logs  # 日志信息存放模块
#
# --Public  # 公共数据存放模块，按系统分模块
# ---WKY
# ----address.py  # url集中存放模块
# ----common.py  # 项目特定函数存放模块，如：get_token
# ----veriables.py  # 数据，变量集中存放模块
# ---MES
# ----address.py
# ----common.py
# ----veriables.py
# ---FNPT
# ----address.py
# ----common.py
# ----veriables.py
# ---X2server
# ----address.py
# ----common.py
# ----veriables.py
#
# --py_yaml  # 数据存放模块，yaml格式，备用
#
# --testCase  # 用例封装模块，按系统分模块
# ---testWKY
# ---testX2server
# ---testFNPT
# ---testMES
#
# --Toolbox  # 工具箱
# ---ConnDB.py  # 数据库连接及查询工具
# ---dateTool.py  # 时间戳处理及处理方法
# ---log_module.py  # 日志工具
# ---packaging_fixture.py  # 夹具封装
# ---send_email.py  # 自动发送邮件工具
# ---zip_file.py  # 文件压缩工具
#
# --markers.py  # 优先级设定模块
#
# --pytest.ini  # 配置文件
#
# --main.py  # 主执行文件

--Instructions and rules  # 本文件，自动化测试框架说明及维护规则#
