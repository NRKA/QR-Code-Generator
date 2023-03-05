import qrcode as qr
import requests


def getting_valid_link(url: str) -> str:
    while True:
        try:
            if ('https://' or 'http://') not in url:
                url = 'http://www.' + url
            if requests.head(url).status_code != 404:
                return url
        except:
            url = input('URL is not valid, please enter a valid URL ')
    return url


if __name__ == '__main__':
    url = input('Enter URL, please ')
    url = getting_valid_link(url)

    img = qr.make(url)
    img.save('qr.png')
    print('Thank you for using QR Code Generator, your QR Code is ready')
