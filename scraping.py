MAX_THREADS=30

combined=[]

def scrape_image_url(page_number):
    number_view=90
    if page_number != 1:
        url = f'page={page_number}&view={number_view}'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs_main = soup.find_all('a', class_ = 'css-n5nq0d-ProductCardLink e4l1wga0')
    

    for idx, job in enumerate(jobs_main):

        scraped_data={}

        print(f'idx {idx} page_number {page_number}')
        
        new_url='https://www.farfetch.com' + job['href']

        scraped_data['url'] = new_url
        
        print(new_url)
        
        html_text = requests.get(new_url).text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs_1 = soup.select('') #CSS type selector
        
        jobs2 = soup.select('') #CSS type selector

        try:
            children = jobs_attr[0].findChildren("li" , recursive=False)  #Finding in case of lists that have children
            for child in children:
                print(child.text)
                scraped_data['attributes'].append(child.text)
        except:
            pass
        
        combined.append(scraped_data)
    time.sleep(0.25)

            
def download_them(page_num):
    threads = min(MAX_THREADS, len(page_num))
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(scrape_image_url, page_num)
        
download_them() #Pass list
