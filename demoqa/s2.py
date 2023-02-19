from selenium import webdriver

def open_files():
    file_names = ['file1.txt', 'file2.txt', 'file3.txt']
    files = []

    for file_name in file_names:
        try:
            file = open(file_name, 'r')
            files.append(file)
        except FileNotFoundError:
            print(f"{file_name} not found.")
            return None

    return files

def main():
    files = open_files()

    if files is None:
        # If one of the files is missing, do not perform the web automation tasks
        print("Exiting due to missing file.")
        return

    # Use the contents of the opened files in the web automation tasks
    driver = webdriver.Firefox()
    driver.get("http://www.google.com")
    search_input = driver.find_element_by_name("q")

    for file in files:
        search_query = file.readline().strip()
        search_input.send_keys(search_query)
        search_input.submit()

    driver.quit()

    # Close the opened files
    for file in files:
        file.close()

if __name__ == '__main__':
    main()
