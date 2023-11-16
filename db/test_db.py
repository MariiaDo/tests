def test_get_all_goods(good_repo):
    db = good_repo
    all_goods = db.get_all()
    for good in all_goods:
        print(good)


def test_insert_good(good_repo, fake_good):
    db = good_repo
    db.insert_one(**fake_good)
    good = db.get_by_filter("artikul", fake_good["artikul"])
    assert good == tuple(fake_good.values())


def test_get_by_filter(good_repo, field="brand", value="zara"):
    db = good_repo
    good = db.get_by_filter(field, value)
    assert tuple(good).__contains__(value)


def test_get_by_filter_negative(good_repo, field="brand", value="adidas"):
    db = good_repo
    good = db.get_by_filter(field, value)
    try:
        res = tuple(good).__contains__(value)
    except:
        res = "There are no this such products in the store"
        print(res)
    assert res == "There are no this such products in the store"


def test_update_by_filter(good_repo, filter_field="size", filter_value="s", condition_field="brand", condition_value="zara"):
    db = good_repo
    db.update_by_filter(filter_field, filter_value, condition_field, condition_value)
    good = db.get_by_filter(condition_field, condition_value)
    assert tuple(good).__contains__(filter_value)


def test_update_by_filter_negative(good_repo, filter_field="size", filter_value="s", condition_field="brand", condition_value="adidas"):
    db = good_repo
    db.update_by_filter(filter_field, filter_value, condition_field, condition_value)
    good = db.get_by_filter(condition_field, condition_value)
    try:
        res = tuple(good).__contains__(filter_value)
    except:
        res = "Updating is not possible"
        print(res)
    assert res == "Updating is not possible"


def test_delete_by_filter(good_repo, field="size", value="s"):
    db = good_repo
    db.delete_by_filter(field, value)
    good = db.get_by_filter(field, value)
    try:
        res = tuple(good).__contains__(value)
    except:
        res = "product does not exist"
        print(res)
    assert res == "product does not exist"
