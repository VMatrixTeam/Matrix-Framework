# Matrix Tornado Framework

> create by yejq Nov 8, 2016

## Description

本项目是Matrix使用的Python Tornado下搭建的MVC（model-view-controller）快速开发框架。

后台采用:

- Python Tornado (non-blocking network I/O aync web server)
- Pyjade (jade template engine for python)
- Asynctorndb (mysql wrapper for python)

前端采用:

- Bootflat (web front-end components bases on bootstrap)

本项目架构运行于:

- Matrix Community (https://community.vmatrix.org.cn)
- Matrix Console

## Dependencies

- python 2.7
- pip
- python development tools
- python mysql

## 运行命令

```
cd /path/to/project
sudo pip install -r requirements.txt
python server.py development
```
