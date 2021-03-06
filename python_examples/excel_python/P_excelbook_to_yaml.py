import sys
import yaml
from xlrd import open_workbook


def convert_sheet_list(sheet, xrows, ycolumns):
    '''
    A function to convert the spreadsheet into a nested list.
    '''
    rows = []
    for row in range(1, xrows):
        values = []
        for col in range(ycolumns):
            value = (sheet.cell(row, col).value)
            if value != '':
                try:
                    value = str(int(value))
                except ValueError:
                    pass
                finally:
                    values.append(value)
        rows.append(values)
    
    return rows


def convert_list_dictionary(sheet, nested_list):
    '''
    A function to convert the list created earlier into a nested dictionary.
    '''
    global_dict = {}
    curr_dict = {}
    first_key = sheet.name

    for row in nested_list:
        curr_values_list = []
        if len(row) >= 1:
            key = str(row[0])
            for i in range(1, len(row)):
                if row[i] != '':
                    curr_values_list.append(row[i])
            curr_dict[key] = curr_values_list
    global_dict[first_key] = curr_dict

    return global_dict


def print_in_yaml_format(dictionary):
    '''
    Function to simply print dictinary in Yaml Format
    '''
    print(yaml.dump(dictionary, default_flow_style=False))


def get_output_file_name():
    '''
    Function to create Yaml format into a file based on sheet name.
    '''
    book_name = sys.argv[1]
    book_name = book_name.split('.')
    book_name = book_name[0]

    return book_name


def input_to_file(book_name, dictionary):

    with open(book_name, 'a') as f:
        f.write(yaml.dump(dictionary, default_flow_style=False))


def main():
    '''
    the main function is simply taking the file name and sending it to
    convert it to a list, followed by a dictionary.
    '''
    book = open_workbook(sys.argv[1])
    number_of_sheets = book.sheet_names()

    # Let's make up a book name
    book_name = get_output_file_name()

    for i in range(len(number_of_sheets)):
        sheet = book.sheet_by_index(i) 
        number_of_rows = sheet.nrows
        number_of_columns = sheet.ncols

        rows = convert_sheet_list(sheet, number_of_rows, number_of_columns)
        global_dict = convert_list_dictionary(sheet, rows)

        # Let's test by printing rows
        input_to_file(book_name, global_dict)

    print("Data copied to {} ".format(book_name))


if __name__ == "__main__":
    main()
