#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
HTTP可用性检测脚本
"""

import requests
import sys
import time

def check_url(url,timeout=5):
    if not url.startswith(("http://","https://")):
        url = "http://" + url

    start_time = time.time()
    try:
        response = requests.get(url,timeout=5)
        response_time = round(time.time() - start_time,3)
        reachable = response.status_code == 200
        return {
            "url": url,
            "status": response.status_code,
            "reachable": reachable,
            "response_time": response_time,
            "error": None
        }

    except requests.exceptions.Timeout:
        return{
            "url": url,
            "status": None,
            "reachable": False,
            "response_time": None,
            "error": "请求超时"
        }

    except requests.exceptions.ConnectionError:
        return{
            "url": url,
            "status": None,
            "reachable": False,
            "response_time": None,
            "error": "连接失败(DNS、拒绝连接等)"
        }
        
    except requests.exceptions.InvalidURL:
        return{
            "url": url,
            "status": None,
            "reachable": False,
            "response_time": None,
            "error": "无效的url"
        }

    except Exception as e:
        return{
            "url": url,
            "status": None,
            "reachable": False,
            "response_time": None,
            "error": f"未知错误:{str(e)}"
        }

def main():
    if len(sys.argv) > 1:
        urls = sys.avgv[1:]
    else:
        urls = [
            "https://www.baidu.com",
            "https://github.com",
            "https://www.google.com",
            "https://www.bing.com",
            "https://x.com"
        ]
    print("未提供URL,使用默认测试列表...")
    
    print(f"\n正在检测{len(urls)}个网站...\n")
    print(f"{'URL':<40} | {'可达':<6} | {'状态码':<8} | {'响应时间(s)':<12} | 错误信息")
    print("-" * 50)

    for url in urls:
        result = check_url(url,timeout=5)
        status_str = str(result['status']) if result['status'] else "N/A"
        time_str = str(result['response_time']) if result['response_time'] else "N/A"
        reachable_str = "是" if result['reachable'] else "否"
        error_str = result['error'] if ['error'] else ""
        print(f"{result['url']:<40} | {reachable_str:<6} | {status_str:<8} | {time_str:<12} | {error_str}")

if __name__ == "__main__":
    main()

