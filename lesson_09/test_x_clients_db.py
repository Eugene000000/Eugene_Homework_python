from CompanyApi import CompanyApi
from CompanyTable import CompanyTable

api = CompanyApi("http://5.101.50.27:8000")
db = CompanyTable("postgres://qa:skyqa@5.101.50.27:5432/x_clients")

def test_add_new_company():
    body = api.get_company_list()
    len_before = len(body)

    name = "Company"
    descr = "Descr"
    result = api.get_company(name, descr)
    new_id = result["id"]

    body = api.get_company_list()
    len_after = len(body)

    db.delete(new_id)

    assert len_after - len_before == 1
    for company in body:
        if company["id"] == new_id:
           assert company["name"] == name
           assert company["description"] == descr
           assert company["id"] == new_id

def test_edit_company():
    name = "Company"
    db.create(name)
    max_id = db.get_max_id()

    new_name = "Updated"
    new_descr = "_upd_"
    edited = api.edit(max_id, new_name, new_descr)

    db.delete(max_id)

    assert edited["id"] == max_id
    assert edited["name"] == new_name
    assert edited["description"] == new_descr
    assert edited["isActive"] == True

def test_delete():
    name = "Company to be deleted"
    db.create(name)
    max_id = db.get_max_id()

    deleted = api.deleted(max_id)

    assert deleted["name"] == name
    assert deleted["id"] == max_id
    assert deleted["isActive"] == True

    rows = db.get_company_by_id(max_id)
    assert len(rows) == 0

    body = api.get_company_list()
    len_before = len(body)

    api.delete_company(max_id)

    body = api.get_company_list()
    len_after = len(body)
    assert len_before- len_after == 1

    deleted = api.get_company(max_id)
    assert deleted['detail'] == 'Компания не найдена'