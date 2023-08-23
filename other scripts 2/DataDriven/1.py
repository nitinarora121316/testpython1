from XLUtils import XLUtils


if __name__ == "__main__":

    file = "other scripts 2/DataDriven/1.xlsx"  # Replace with your Excel file name
    xlutils = XLUtils(file)

    sheetName = "Sheet1"
    all_data = xlutils.fetchAllData(sheetName)

    for row_num, row_data in enumerate(all_data, start=2):
        for col_num, cell_value in enumerate(row_data, start=1):
            print(f"Data at row {row_num}, column {col_num}: {cell_value}")
