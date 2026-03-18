#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
文件读写，系统信息获取
"""

import os
import subprocess
from datetime import datetime

def run_command(cmd):
    try:
        result = subprocess.run(cmd,capture_output=True,text=True,check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"命令执行失败:{e}\n"


def collect_system_info():
    info = []
    info.append("=" * 50)
    info.append(f"系统信息收集时间:{datetime.now().strftime('%Y-%m-%d %H:%M%S')}")
    info.append("=" * 50)

    info.append(f"主机名:{os.uname().nodename}")
    info.append(f"当前用户:{os.getlogin()}")
    info.append(f"当前工作目录:{os.getcwd()}")

    info.append("\n--- 磁盘使用情况 (df -h) ---")
    info.append(run_command(['df','-h']))

    info.append("--- 内存使用情况 (free -h) ---")
    info.append(run_command(['free','-h']))

    info.append("--- CPU核心数 ---")
    info.append(f"逻辑cpu核心数:{os.cpu_count()}")

    info.append("=" * 50 + "\n")
    return "\n".join(info)

def write_to_log(content,filename="sysinfo.log"):
    with open(filename,'a',encoding="utf-8") as f:
        f.write(content)
    print(f"系统信息已追加写入{filename}")

def main():
    sys_info = collect_system_info()
    write_to_log(sys_info)

if __name__ == "__main__":
    main()
