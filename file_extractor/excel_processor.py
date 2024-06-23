import pandas as pd

def process_excel_file(file_path):
    processed_data = []
    try:
        excel_file = pd.ExcelFile(file_path)
        for sheet_name in excel_file.sheet_names:
            worksheet = pd.read_excel(excel_file, sheet_name=sheet_name)
            for row_num, row in worksheet.iterrows():
                for col_num, value in enumerate(row):
                    if pd.notnull(value):
                        column_name = worksheet.columns[col_num]
                        processed_data.append({
                            'name': str(column_name),
                            'value': str(value),
                            'sheet_name': sheet_name,
                            'row_number': row_num + 1,
                            'column_number': col_num + 1
                        })
    except Exception as e:
        raise ValueError(f'Error reading Excel file: {e}')

    return processed_data