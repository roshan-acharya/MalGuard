import pandas as pd 
import numpy as np
import re
from urllib.parse import * 

def count_domain_length(url):
    if not isinstance(url, str):
        return 0

    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    hostname = urlparse(url).hostname
    return len(hostname) if hostname else 0

def clean_safe_data(file_path):
    df=pd.read_csv(file_path,header=None,names=['url'])
    suspicious_words = ['login', 'signin', 'verify', 'update', 'banking', 'account', 'secure', 'ebayisapi', 'webscr', 'paypal','esewa','account']

        
    for url in df['url']:
        parse_url = urlparse(url)
        domain = parse_url.netloc
        scheme= parse_url.scheme
        path = parse_url.path

        #Suspicious check
        df['Suspicious_word_count'] = df['url'].apply(lambda x: 1 if any(word in x for word in suspicious_words) else 0)

        df["domain_length"] = df["url"].apply(count_domain_length)
        df['count_dots']=df['url'].apply(lambda x: x.count('.'))
        df['count_dashes']=df['url'].apply(lambda x: x.count('-'))
        df['https']=df['url'].apply(lambda x: 1 if 'https' in scheme else 0)
        df['count_at_symbol']=df['url'].apply(lambda x: x.count('@'))
        df['count_digits']=df['url'].apply(lambda x: sum(c.isdigit() for c in x))
        df['has_ip'] = int(bool(re.search(r'\d+\.\d+\.\d+\.\d+', domain)))
        df['subdomain_count'] = df['url'].apply(lambda x: len(urlparse(x).netloc.split('.')) - 2)
        df['query_length'] = df['url'].apply(lambda x: len(urlparse(x).query))
        df['num_params'] = df['url'].apply(lambda x: len(parse_qs(urlparse(x).query)))
        df['num_slashes'] = df['url'].apply(lambda x: x.count('/'))
        df['entropy'] = df['url'].apply(lambda x: -sum([ (x.count(c)/len(x)) * np.log2(x.count(c)/len(x)) for c in set(x)]))
        df['has_tld_in_path'] = df['url'].apply(lambda x: 1 if re.search(r'\.(com|org|net|info|biz|co|us|uk|io|gov)(/|$)', urlparse(x).path) else 0)
        df.dropna(inplace=True)
        print("Cleaned ",url)
    df.drop(columns=['url'],inplace=True) 
    return df


def save_data(df,file_path):
    df.to_csv(file_path, index=False)

def url_to_df(url):
        parse_url = urlparse(url)
        domain = parse_url.hostname
        scheme= parse_url.scheme
        path=parse_url.path
        suspicious_words = ['login', 'signin', 'verify', 'update', 'banking', 'account', 'secure', 'ebayisapi', 'webscr', 'paypal','esewa','account']
        data = {
            'Suspicious_word_count': 1 if any(word in url for word in suspicious_words) else 0,
            'domain_length': len(domain),
            'count_dots': url.count('.'),
            'count_dashes': url.count('-'),
            'https': 1 if 'https' in scheme else 0,
            'count_at_symbol': url.count('@'),
            'count_digits': sum(c.isdigit() for c in url),
            'has_ip': int(bool(re.search(r'\d+\.\d+\.\d+\.\d+', domain))),
            'subdomain_count': len(domain.split('.')) - 2,
            'query_length': len(urlparse(url).query),
            'num_params': len(parse_qs(parse_url.query)),
            'num_slashes': url.count('/'),
            'entropy': -sum([ (url.count(c)/len(url)) * np.log2(url.count(c)/len(url)) for c in set(url)]),
            'has_tld_in_path': 1 if re.search(r'\.(com|org|net|info|biz|co|us|uk|io|gov)(/|$)', path) else 0
        }
        return pd.DataFrame([data])