## 下载 https://shareclash.github.io/ 上的节点链接文件

# 导入网络请求库：用于发送HTTP请求下载文件
import requests
# 导入日期时间库：用于获取当前日期、计算昨天日期
from datetime import datetime, timedelta
# 导入YAML解析库：用于处理YAML格式的配置文件
import yaml

# ---------------------- 1. 日期处理模块 ----------------------
# 获取当前系统日期时间
current_date = datetime.now()
# 格式化当前日期：提取 年份（4位数字，如2026）
year = current_date.strftime('%Y')
# 格式化当前日期：提取 月份（2位数字，如03）
month = current_date.strftime('%m')
# 格式化当前日期：拼接为 年月日（8位数字，如20260330）
day = current_date.strftime('%Y%m%d')
# 计算昨天的日期（当前日期 - 1天）
yesterday_date = current_date - timedelta(days=1)
# 格式化昨天日期：拼接为 年月日（8位数字）
y_day = yesterday_date.strftime('%Y%m%d')

# ---------------------- 1. 处理下载链接 ----------------------
# 定义需要下载的文件URL（自动嵌入当天的年、月、日）
url = f"https://clashgithub.github.io/uploads/{year}/{month}/0-{day}.txt"

# ---------------------- 1. 核心下载函数 ----------------------
# 定义一个gets函数
def gets():
    try:
        # 发送GET请求下载文件（verify=False：关闭SSL证书验证，解决部分网站报错）
        response = requests.get(url, verify=False)
        # 判断请求是否成功（状态码200=成功）
        if response.status_code == 200:
            # 将下载的内容用GBK编码解码（适配中文文本）
            decoded_text = response.content.decode('gbk')
            # 以写入模式打开文件，保存到本地
            with open("clashgithub", 'w', encoding='gbk') as file:
                file.write(decoded_text)
            # 打印成功提示
            print(f"✅ 下载成功：{url}")
        else:
            print(f"❌ 连接失败，状态码：{response.status_code},URL:{url}")  
    except Exception as e:
        print("❌ 下载出错：{str(e)}")

# ---------------------- 1. 调用 gets 函数 ----------------------
# 调用函数，执行下载任务
gets()