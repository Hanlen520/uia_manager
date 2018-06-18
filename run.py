import config as cf
import subprocess
import os
import shutil
import stat


def remove_readonly(func, path, _):
    os.chmod(path, stat.S_IWRITE)
    func(path)


def pull_modules():
    print('Trying to get latest modules ...')
    os.chdir(cf.WORKSPACE_PATH)
    pull_process_list = []
    for each_module_name, each_module_git_url in cf.MODULE_DICT.items():
        if os.path.exists(each_module_name):
            git_cmd = 'cd {} && ' \
                      'git reset --hard HEAD^ && ' \
                      'git pull --rebase'.format(each_module_name)
        else:
            git_cmd = 'git clone {}'.format(each_module_git_url)
        cur_process = subprocess.Popen(
            git_cmd.format(each_module_name),
            shell=True,
        )
        pull_process_list.append(cur_process)
    for _ in pull_process_list:
        _.communicate()

    os.chdir(cf.PROJECT_PATH)
    print('Modules already latest.')


def insert_cases():
    shutil.rmtree(cf.TARGET_CASE_DIR_PATH, onerror=remove_readonly)
    shutil.copytree(cf.SOURCE_CASE_DIR_PATH, cf.TARGET_CASE_DIR_PATH)
    print('Cases ready.')


def insert_api_file():
    shutil.copyfile(cf.SOURCE_API_FILE_PATH, cf.TARGET_API_FILE_PATH)
    print('Api file ready.')


def init_device():
    cmd = '{} -m uiautomator2 init'.format(cf.PYTHON_PATH)
    return_code = os.system(cmd)
    if return_code:
        raise SystemError('error happened in {}'.format(cmd))
    else:
        print('Device init ok.')


def start_test(task_name):
    print('Environment init ok. Start test ...')
    task_name = str(task_name)
    init_device()
    for each_device in cf.DEVICE_LIST:
        run_cmd = '{} {} -d {} -t {}'.format(
            cf.PYTHON_PATH,
            cf.FRAMEWORK_ENTRY_FILE,
            each_device,
            task_name,
        )
        print(run_cmd)
        # TODO: 多设备同步
        subprocess.run(run_cmd, shell=True)


if __name__ == '__main__':
    if not cf.DEBUG_SWITCH:
        pull_modules()
        insert_cases()
        insert_api_file()
    start_test(cf.TASK_NAME)
    print('Task [ {} ] finished.')
