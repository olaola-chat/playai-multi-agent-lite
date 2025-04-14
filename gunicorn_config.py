# gunicorn_config.py
import multiprocessing
import os

# 获取 CPU 核心数
workers_per_core_str = os.getenv("WORKERS_PER_CORE", "1")
cores = multiprocessing.cpu_count()
workers_per_core = float(workers_per_core_str)
default_web_concurrency = workers_per_core * cores

# Gunicorn 配置
bind = "0.0.0.0:18090"  # 绑定地址和端口
workers = int(os.getenv("WEB_CONCURRENCY", default_web_concurrency))  # worker 进程数
worker_class = "uvicorn.workers.UvicornWorker"  # 使用 Uvicorn 的 worker 类
keepalive = 300  # 连接保持时间
errorlog = "logs/error.log"  # 错误日志
accesslog = "logs/access.log"  # 访问日志
loglevel = "error"  # 只记录错误级别的日志

# 进程命名
proc_name = "playai-multi-agent"

# 启动前和启动后的钩子
def on_starting(server):
    """在 Gunicorn 启动前执行"""
    # 确保日志目录存在
    os.makedirs("logs", exist_ok=True)

def post_fork(server, worker):
    """在 worker 进程创建后执行"""
    server.log.info(f"Worker spawned (pid: {worker.pid})")