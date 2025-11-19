import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}



def get_data_file(headers):
    # url = 'https://www.landingfolio.com/'
    # response = requests.get(url =url,headers=headers)
    #
    # with open('index.html', 'w') as file:
    #     file.write(response.text)
    offset = 0
    img_count = 0
    result_list = []
    while True:
        url = f'https://landingfolio.com/api/v1/inspiration/?offset={offset}&color=%23undefined'
        response = requests.get(url=url, headers= headers)
        data = response.json()
        for  item in  data:
            if 'description' in item:

                images = item.get('images')
                img_count += len(images)

                for img in  images:
                    img.update({'url': f'https://landingfoliocom.imgix.net/{img.get('url')}'})

                result_list.append(
                    {
                        'title': item.get('title'),
                        'description': item.get('description'),
                        'url': item.get('url'),
                        'images': images
                    }
                )
            else:
                with open('result_list.json', 'a') as file:
                    json.dump(result_list, file, indent=4, ensure_ascii= False)
                return f'[INFO] Work finished. Images count  is {img_count}\n{'='*20}'

        print(f'[+] Processed {offset}')
        offset +=  1

def download_images(file_path):
    pass

def main():
    print(get_data_file(headers=headers))


if __name__== '__main__':
    main()
