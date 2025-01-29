import requests

url = "https://tarotoo.com/wp-json/openai/v1/chat-message"

# Указываем прокси
proxies = {
    "http": "http://user132581:schrvd@45.88.15.215:5085",
    "https": "http://user132581:schrvd@45.88.15.215:5085",
}

headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'content-length': '967',
    'content-type': 'application/json',
    'cookie': '_gcl_au=1.1.1604451826.1736844860; _ga=GA1.1.1544900680.1736844860; cookie_notice_accepted=true; csrf_token=bd32dc7a-7307-4bdb-abc5-2c150717dc23; _ga_XNM8ZL4LSH=GS1.1.1738173530.2.1.1738173657.0.0.0; cf_clearance=QIo5vebWJNXB.rbH_e3sjWMsk0UhcKW99Gc3ugd6Lzc-1738173658-1.2.1.1-L76JCLZx6bsSt7beLjVU0svjkeqM7ooA0qWTnAYWtcXaywIgnXiUIQpjl_rG8SGA1E4mfn5OpSIOsiuG6UNE3nkVCcRmheJJ.oPl5c70WwIlKX8qCPlqjcDmd7AWxQaXt1BiXBlPgSwK8wt6SG_nDPwSYK5s.SpeeYBvzcD2dCcBPJRb1sFSaFWQOqN.eS_C2AVYIuP19GQy1Hea3UBLBgKuHMFURz7IUyrnqgELZVvaetwhIniajFSx_8xrNf7ntWzMDfY8wmVDFNbXAEzT7SRYrHz3V2fyTS7piE2oCm4',
    'origin': 'https://tarotoo.com',
    'priority': 'u=1, i',
    'referer': 'https://tarotoo.com/psychic',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0'
}

data = {
    "messages": [
        {
            "role": "assistant",
            "content": "Hello, I’m Tarotoo’s AI psychic. You can ask me anything about astrology, numerology, spirituality, tarot, or dreams, or we can just chat. Don’t forget to try our free tarot readings by visiting the homepage. Or check out live psychic readings with real psychics by scrolling down a little."
        },
        {
            "role": "user",
            "content": "привет! помоги"
        },
        {
            "role": "assistant",
            "content": "Привет! С удовольствием помогу. Что именно тебя беспокоит или интересует? Может быть, ты хочешь поговорить о своей жизни, узнать о своей numerologической карте или судьбе по знаку зодиака? Или, возможно, тебе нужны советы по медитации или аффирмациям? Дай знать!"
        },
        {
            "role": "user",
            "content": "как дела"
        }
    ],
    "currentSiteLang":"en"
}

response = requests.post(url, headers=headers, json=data, proxies=proxies)

print(response.json())