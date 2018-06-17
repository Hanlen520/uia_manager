import os


# --- PIPELINE ---
PROJECT_PATH = os.path.dirname(__file__)
WORKSPACE_PATH = '/home/fengzhangchi/ui_auto_workspace'
PYTHON_PATH = '/usr/bin/python3'

# --- GIT ---
CASE_PROJECT_NAME = 'IPEntryAutoTest'
CASE_DIR_NAME = 'cases'
API_FILE_NAME = 'extend_api.py'

FRAMEWORK_PROJECT_NAME = 'basic_uia'

CASE_GIT_URL = 'https://github.com/williamfzc/uia_case_sample.git'
FRAMEWORK_GIT_URL = 'https://github.com/williamfzc/basic_uia.git'

MODULE_DICT = {
    CASE_PROJECT_NAME: CASE_GIT_URL,
    FRAMEWORK_PROJECT_NAME: FRAMEWORK_GIT_URL,
}

# --- OTHER ---
FRAMEWORK_ENTRY_FILE = os.path.join(WORKSPACE_PATH, FRAMEWORK_PROJECT_NAME, 'run.py')
TARGET_CASE_DIR_PATH = os.path.join(WORKSPACE_PATH, FRAMEWORK_PROJECT_NAME, CASE_DIR_NAME)
SOURCE_CASE_DIR_PATH = os.path.join(WORKSPACE_PATH, CASE_PROJECT_NAME, CASE_DIR_NAME)

TARGET_API_FILE_PATH = os.path.join(WORKSPACE_PATH, FRAMEWORK_PROJECT_NAME, API_FILE_NAME)
SOURCE_API_FILE_PATH = os.path.join(WORKSPACE_PATH, CASE_PROJECT_NAME, API_FILE_NAME)

# --- DEVICE ---
DEVICE_LIST = ['QGTKH6MFVWRODU8T']

# --- DEBUG MODE ---
DEBUG_SWITCH = True
