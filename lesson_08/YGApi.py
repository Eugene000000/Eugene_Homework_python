import requests

class YG():

    def __init__(self, url):
        self.url = url
    
    def get_project_list(self, token='Bearer j-iDnUeA48Hi2lIiI--lNoWZLT3AB4bxyV953mWcMoTXxUYuv4IoKn5Mi7H2P96v'):
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer undefined"
        }
        my_headers["Authorization"] = token
        result = requests.get(self.url + '/api-v2/projects', headers=my_headers)
        return result

    def add_project(self, title, user_id='280fd7cf-c501-4e6d-9264-9145dd0498ed', user_role='admin', token='Bearer j-iDnUeA48Hi2lIiI--lNoWZLT3AB4bxyV953mWcMoTXxUYuv4IoKn5Mi7H2P96v'):
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer undefined"
        }
        my_headers["Authorization"] = token
        body = {
            "title": title,
            "users":
            {user_id: user_role}
        }
        result = requests.post(self.url + '/api-v2/projects', json=body, headers=my_headers)
        return result

    def get_project_with_id(self, id, token='Bearer j-iDnUeA48Hi2lIiI--lNoWZLT3AB4bxyV953mWcMoTXxUYuv4IoKn5Mi7H2P96v'):
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer undefined"
        }
        my_headers["Authorization"] = token
        result = requests.get(self.url + '/api-v2/projects/' + id, headers=my_headers)
        return result

    def change_project_title(self, id, new_title, token='Bearer j-iDnUeA48Hi2lIiI--lNoWZLT3AB4bxyV953mWcMoTXxUYuv4IoKn5Mi7H2P96v'):
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer undefined"
        }
        my_headers["Authorization"] = token
        body = {'title': new_title}
        result = requests.put(self.url + '/api-v2/projects/' + id, json=body, headers=my_headers)
        return result