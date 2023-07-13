import requests

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.'

def pre_create(ndus, path):
    endpoint = 'https://www.terabox.com/api/precreate'
    cookies = {'ndus': ndus}
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': USER_AGENT
    }
    data = {
        'path': path,
        'autoinit': '1',
        'block_list': '["5910a591dd8fc18c32a8f3df4fdc1761"]'
    }

    res = requests.post(endpoint, cookies=cookies, headers=headers, data=data)
    res_data = res.json()
    if not res_data['errno']:
        return res.json()
    raise Exception(res_data)
    
def superfile2(ndus, file_path, upload_id, file_obj):
    endpoint = 'https://c-jp.terabox.com/rest/2.0/pcs/superfile2'
    cookies = {'ndus': ndus}
    headers = {
        'Accept': '*/*',
        'User-Agent': USER_AGENT
    }
    params = {
        "method":"upload",
        "app_id":"250528",
        "path":file_path,
        "uploadid":upload_id,
        "uploadsign":"0",
        "partseq":"0"
    }

    res = requests.post(endpoint, params=params, cookies=cookies, headers=headers, files={'blob':file_obj})
    res_data = res.json()
    if 'error_code' not in res_data:
        return res.json()
    raise Exception(res_data)

def create(ndus, file_path, md5, upload_id, size, is_dir=False):
    endpoint = 'https://www.terabox.com/api/create'
    cookies = {'ndus': ndus}
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': USER_AGENT
    }
    params = {'isdir': str(int(is_dir))}
    data = {
        'path': file_path,
        'size': str(size),
        'uploadid': upload_id,
        'block_list': f'["{md5}"]'
    }
    res = requests.post(endpoint, params=params, cookies=cookies, headers=headers, data=data)
    return(res.json())