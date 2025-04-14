import subprocess
import signal
import sys

def run_server():
    """启动 Gunicorn 服务器"""
    try:
        # 使用 gunicorn 配置文件启动服务器
        cmd = [
            "gunicorn",
            "main:app",  # FastAPI 应用实例
            "-c",
            "gunicorn_config.py",  # 配置文件
        ]
        
        # 启动服务器进程
        process = subprocess.Popen(cmd)
        
        # 设置信号处理
        def signal_handler(sig, frame):
            print("\nShutting down gracefully...")
            process.terminate()
            process.wait()
            sys.exit(0)
        
        # 注册信号处理器
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        
        # 等待进程结束
        process.wait()
        
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_server()