import os
import time
import re
import json
from xlsxlib import Excel


class Sendlist():

    def __init__(self):

        return

    def load_list(self):

        loaded_list = []

        sendlist = Excel()

        sendlist.open_workbook("sendlist")

        list_len = sendlist.get_row_number()

        for i in range(1, list_len+1):
            phone_number = sendlist.read_cell(i, 1)
            loaded_list.append(phone_number)

        sendlist.save_workbook()

        return loaded_list

    def update_list(self, new_phone_list):

        sendlist = Excel()

        sendlist.open_workbook("sendlist")

        row_to_print = sendlist.get_row_number() + 1

        for i in range(0, len(new_phone_list)):
            sendlist.write_cell(row_to_print, 1, new_phone_list[i])
            row_to_print = row_to_print+1

        sendlist.save_workbook()

        return

if __name__ == "__main__":



