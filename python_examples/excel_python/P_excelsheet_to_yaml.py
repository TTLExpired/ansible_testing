import sys
import yaml
from pudb import set_trace
from xlrd import open_workbook


def convert_data_to_dict(sheet, nrows, ncols):
    '''
    Function to convert raw Excell Data into a dictionary format. With Python
    3.6 and above, Dictionaries are no longer random! We make use of that to
    trim our code.
    '''

    # set_trace()
    initial_dict = {}
    sheet_dict = {}
    initial_list = []

    # Lets start with some data gathering.
    for section_key in range(0, nrows):
        row_key_value = (sheet.cell(section_key, 0).value)
        if row_key_value != '':
            key = str(row_key_value)
            for col in range(1, ncols):
                cell_col_value = (sheet.cell(section_key, col).value)
                if cell_col_value != '':
                    initial_list.append(cell_col_value)
                    initial_dict = {key: initial_list}

        initial_dict[key].append(initial_list)

        sheet_dict[sheet.name] = initial_dict

    return sheet_dict


def convert_rows_to_yaml():
    pass


def main():
    '''
    The main function to take spreadsheet name. And send it to appropriate
    functions for processing.
    '''

    book = open_workbook(sys.argv[1])
    sheet = book.sheet_by_index(0)

    number_of_rows = sheet.nrows
    number_of_cols = sheet.ncols

    global_dict = convert_data_to_dict(sheet, number_of_rows, number_of_cols)

    print(global_dict)


if __name__ == "__main__":
    main()
