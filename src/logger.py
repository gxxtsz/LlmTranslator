import logging
import os
from datetime import datetime

# 创建 logs 目录（如果不存在）
logs_dir = 'logs'
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# 生成带有时间戳的日志文件名
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
log_filename = os.path.join(logs_dir, f'app_{timestamp}.log')

# 配置日志记录器
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()
    ]
)

# 创建固定名字的全局 logger
logger = logging.getLogger('LlmTranslatorLogger')


if __name__ == "__main__":
    logger.info("This is a test log message.")
