import requests

def check_link(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

def verify_links(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Unable to access website.")
        return
    
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [link.get('href') for link in soup.find_all('a')]

    for link in links:
        if link is None:
            continue
        if not link.startswith('http'):
            link = url + link
        if check_link(link):
            print(f"{link} is working.")
        else:
            print(f"{link} is not working.")

verify_links("https://google.com")
