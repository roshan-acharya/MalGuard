import pandas as pd 
import numpy as np
import re
from urllib.parse import * 
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer


def clean_safe_data(file_path):
    df=pd.read_csv(file_path,header=None,names=['url'])
    suspicious_words = ['login', 'signin', 'verify', 'update', 'banking', 'account', 'secure', 'ebayisapi', 'webscr', 'paypal','esewa','account']

        
    for url in df['url']:
        parse_url = urlparse(url)
        domain = parse_url.netloc
        scheme= parse_url.scheme
        path = parse_url.path

        #Suspicious check
        df['suspicious'] = df['url'].apply(lambda x: 1 if any(word in x for word in suspicious_words)else 0)
        
        #Length check of domain
        df['length_domain'] = df['url'].apply(lambda x: len(urlparse(x).netloc))
        df['count_dots']=df['url'].apply(lambda x: x.count('.'))
        df['count_dashes']=df['url'].apply(lambda x: x.count('-'))
        df['https']=df['url'].apply(lambda x: 1 if 'https' in scheme else 0)
        df['count_at_symbol']=df['url'].apply(lambda x: x.count('@'))
        df['count_digits']=df['url'].apply(lambda x: sum(c.isdigit() for c in x))
        df['has_ip'] = int(bool(re.search(r'\d+\.\d+\.\d+\.\d+', domain)))
        df['subdomain_count'] = df['url'].apply(lambda x: len(urlparse(x).netloc.split('.')) - 2)
    return df


def save_data(df):
    df.to_csv('..\Data\safe_links.csv', index=False)

def url_to_df(url):
        parse_url = urlparse(url)
        domain = parse_url.netloc
        scheme= parse_url.scheme
        path=parse_url.path
        suspicious_words = ['login', 'signin', 'verify', 'update', 'banking', 'account', 'secure', 'ebayisapi', 'webscr', 'paypal','esewa','account']
        data = {
            'url': url,
            'suspicious': 1 if any(word in url for word in suspicious_words) else 0,
            'length_domain': len(domain),
            'count_dots': url.count('.'),
            'count_dashes': url.count('-'),
            'https': 1 if 'https' in scheme else 0,
            'count_at_symbol': url.count('@'),
            'count_digits': sum(c.isdigit() for c in url),
            'has_ip': int(bool(re.search(r'\d+\.\d+\.\d+\.\d+', domain))),
            'subdomain_count': len(domain.split('.')) - 2
        }
        print(data)
        return pd.DataFrame([data])