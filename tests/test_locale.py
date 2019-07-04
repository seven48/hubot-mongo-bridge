
async def test_for_existing_user(client):
    resp = await client.get("/locale?user_id=rocket.cat")
    assert resp.status == 200
    data = await resp.json()
    assert "ru" in data["locale"]


async def test_for_nonexistent_user(client):
    resp = await client.get("/locale?user_id=qwerty")
    assert resp.status == 404


async def test_for_bad_request(client):
    resp = await client.get("/locale?test=qwerty")
    assert resp.status == 400
    text = await resp.text()
    assert "user_id not found" in text
