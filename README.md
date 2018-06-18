# UI自动化 流程管理

## 使用

- 在config.py中配置
    - WORKSPACE_PATH
        - 工作区（文件夹，需要先创建），所有工作将会在该文件夹内进行 
    - PYTHON_PATH
        - 你的python安装位置（需要安装有uiautomator2）
    - CASE_GIT_URL
        - 用例git仓库
    - FRAMEWORK_GIT_URL 
        - 框架git仓库，如无修改使用默认即可
    - DEVICE_LIST
        - 测试使用的机器列表。用例将会在他们上执行
    - TASK_NAME
        - 测试的任务名称
- 执行run.py
- (TODO) 将结果汇总到本目录下

## 作用

- 框架与用例完全隔离管理，保障信息安全
- 框架开发与测试脚本彼此不会互相影响，提高效率与安全性
- 比较强的可扩展性，可在此基础上新增功能

## 流程

- 拉取最新的 框架、用例
- 将用例插入到框架内
- 启动框架开始测试