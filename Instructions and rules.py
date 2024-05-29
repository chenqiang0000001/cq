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

#--Instructions and rules  # 本文件，自动化测试框架说明及维护规则#

#维护规则
# 1.各类型文件应该按分类放在文件夹里
# 2.做好注释，方便使用，格式如：
# def zip_files(dir_path, zip_path):
#     '''
# 	:param dir_path: 需要压缩的文件夹地址  例：'D:\Buyer_test_code\apipotest_jcmall\report'
# 	:param zip_path: 压缩后的文件存在地址+压缩文件名  例：'D:\Buyer_test_code\apipotest_jcmall\report_zip\report.zip'
# 	:return: 0  压缩失败  1 压缩成功
# 	'''
#     try:
#         with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as f:
#             for dirpath, dirnames, filenames in os.walk(dir_path):
#                 fpath = dirpath.replace(dir_path, '')
#                 fpath = fpath and fpath + os.sep or ''
#                 for filename in filenames:
#                     f.write(os.path.join(dirpath, filename), fpath + filename)
#             logging.info(f"文件：{dir_path} 压缩成功")
#     except Exception as e:
#         logging.error(f"文件：{dir_path} 压缩失败，错误：{e}")
#         return 0
#     else:
#         return 1
# 3.协商好分支，以免分支冲突
