from YGApi import YG

api = YG('https://ru.yougile.com')

def test_get_projects_list():
    res = api.get_project_list()
    status = res.status_code
    json = res.json()
    count = json['paging']['count']
    assert status == 200
    assert count > 0

def test_negative_get_projects_list():
    res = api.get_project_list(token='000')
    status = res.status_code
    assert status == 401

def test_add_projects():
    res_before = api.get_project_list()
    json = res_before.json()
    count_before = json['paging']['count']
    res_add = api.add_project('Project')
    status = res_add.status_code
    json_add = res_add.json()
    res_after = api.get_project_list()
    json_after = res_after.json()
    count_after = json_after['paging']['count']
    assert status == 201
    assert count_after - count_before == 1
    assert json_add['id'] is not None

def test_negative_add_project():
    res_before = api.get_project_list()
    json = res_before.json()
    count_before = json['paging']['count']
    res_add = api.add_project('Project', token='123')
    status = res_add.status_code
    json_add = res_add.json()
    res_after = api.get_project_list()
    json_after = res_after.json()
    count_after = json_after['paging']['count']
    assert status == 401
    assert count_after - count_before == 0

def test_get_project_with_id():
    new_title = 'New_title'
    new_project = api.add_project(new_title)
    json = new_project.json()
    new_id = json['id']
    desired_project = api.get_project_with_id(new_id)
    status = desired_project.status_code
    json = desired_project.json()
    assert status == 200
    assert json['id'] == new_id
    assert json['title'] == new_title

def test_negative_get_project_with_id():
    new_title = 'New_title'
    new_project = api.add_project(new_title)
    json = new_project.json()
    new_id = json['id']
    desired_project = api.get_project_with_id('123')
    status = desired_project.status_code
    assert status == 404

def test_change_project_title():
    add_title = 'Added_title'
    new_project = api.add_project(add_title)
    json = new_project.json()
    new_id = json['id']
    new_title = 'New_title'
    modified_project = api.change_project_title(new_id, new_title)
    modified_project_status = modified_project.status_code
    modified_project_json = modified_project.json()
    desired_project = api.get_project_with_id(new_id)
    desired_project_json = desired_project.json()
    assert modified_project_status == 200
    assert modified_project_json['id'] == new_id
    assert desired_project_json['title'] == new_title

def test_negative_change_project_title():
    add_title = 'Added_title'
    api.add_project(add_title)
    new_title = 'New_title'
    modified_project = api.change_project_title('123', new_title)
    modified_project_status = modified_project.status_code
    assert modified_project_status == 404