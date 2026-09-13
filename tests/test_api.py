from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'ok'

def test_generate_episode():
    response = client.post('/api/episodes', json={'topic':'Sharing a toy','lesson':'kindness','scene_count':6})
    assert response.status_code == 201
    data = response.json()
    assert data['status'] == 'ready'
    assert len(data['scenes']) == 6
    assert all(s['duration_seconds'] >= 3 for s in data['scenes'])
