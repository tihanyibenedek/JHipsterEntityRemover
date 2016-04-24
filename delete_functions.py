
import os
import re
import os.path
from os.path import exists
import shutil

BasePath = "D:\Bence\Code\JHipster\BaseApp\\"


def delete_selected_item(global_list, post_fix, expansion):
    """

    :param global_list:
    :param post_fix:
    :param expansion:
    :return:
    """

    file_list = [name for name in os.listdir(BasePath + post_fix) if name.endswith(expansion)]

    for entity in global_list:
        for file_l in file_list:
            match_obj = re.match(entity, file_l)
            if match_obj:
                delete_f = BasePath + post_fix + file_l
                if exists(delete_f):
                    os.remove(delete_f)
                    if not exists(delete_f):
                        return True


def delete_selected_item_with_lower(global_list, post_fix, expansion):
    """

    :param global_list:
    :param post_fix:
    :param expansion:
    :return:
    """

    file_list = [name for name in os.listdir(BasePath + post_fix) if name.endswith(expansion)]

    for entity in global_list:
        for file_l in file_list:
            list_e = list(entity)
            list_e[0] = list_e[0].lower()
            entity = "".join(list_e)
            match_obj = re.match(entity, file_l)
            if match_obj:
                delete_f = BasePath + post_fix + file_l
                if exists(delete_f):
                    shutil.rmtree(delete_f)
                    if not exists(delete_f):
                        return  True

