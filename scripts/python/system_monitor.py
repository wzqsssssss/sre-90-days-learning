#!/usr/bin/env python3
#-*- coding:utf -*-

"""
系统监控脚本
"""

import shutil
import psutil
import os
import sys
import time
import requests
from datetime import datetime

# HTTP服务健康检查
USE_HTTP_CHECK = True
HTTP_TARGETS = ['http://localhost']

# 获取指定路径磁盘使用率%
def get_disk_usage(path="/"):
    usage = shutil.disk_usage(path)
    total = usage.total
    used = usage.used
    percent = (used / total) * 100
    return round(percent,1)

# 获取内存使用率%
def get_memory_usage():
    mem = psutil.virtual_memory()
    return mem.percent

# 检查HTTP服务是否返回200
def check_http_service(url,timeout=3):
    try:
        headers = {'User-Agent':'SystemMonitor/1.0'}
        response = requests.get(url,timeout = timeout,headers = headers)
        return response.status_code == 200
    except Exception:
        return False

# 告警信息写入日志
def log_alert(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[ALERT] {timestamp} - {message}\n"
    with open("monitor.log","a",encoding="utf-8") as f:
        f.write(log_line)

def main():
    print("=" * 60)
    print("系统健康状态检察")
    print("=" * 60)

    alters = []

    # 磁盘检查
    try:
        disk_pct = get_disk_usage("/")
        disk_status = "正常" if disk_pct <= 80 else "告警"
        print(f"磁盘(/)使用率:{disk_pct}% ({disk_status})")
        if disk_pct > 80:
            msg = f"磁盘使用率过高:{disk_pct}% (80%)"
            alerts.append(msg)
            log_alert(msg)
    except Exception as e:
        err_msg = f"磁盘检查失败:{e}"
        print(f"磁盘使用率:错误 - {e}")
        alerts.append(err_msg)
        log_alert(err_msg)

    # 内存检查
    try:
        mem_pct = get_memory_usage()
        mem_status = "正常" if mem_pct <= 90 else "告警"
        print(f"内存使用率:{mem_pct}% ({mem_status})")
        if mem_pct > 90:
            msg = f"内存使用率过高:{mem_pct}% (90%)"
            alerts.append(msg)
            log_alert(msg)
    except Exception as e:
        err_msg = f"内存检查失败:{e}"
        print(f"内存使用率:错误 - {e}")
        alerts.append(err_msg)
        log_alert(err_msg)

    # HTTP服务检查
    if USE_HTTP_CHECK:
        print("\nHTTP服务健康度检查")
        for url in HTTP_TARGETS:
            is_ok = check_http_service(url)
            status = "正常" if is_ok else "不可达"
            print(f"  - {url} : {status}")
            if not is_ok:
                msg = f"HTTP服务不可达:{url}"
                alerts.append(msg)
                log_alert(msg)

    print("\n" + "=" * 60)
    if alters:
        print(f"发现以下问题，请及时处理: ")
        for alter in alters:
            print(f"  * {alter}")
    else:
        print("系统一切正常!")
    print("=" * 60)

if __name__ == "__main__":
    main()

    

