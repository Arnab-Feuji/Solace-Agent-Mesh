"""Acceptance tests generated from BRD criteria."""
from fastapi.testclient import TestClient
import importlib.util, os
spec = importlib.util.spec_from_file_location('genapp', os.path.join(os.path.dirname(__file__),'main.py'))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
client = TestClient(m.app)

def test_health():
    assert client.get('/health').status_code == 200

def test_predict_endpoint_exists():
    r = client.post('/predict', json={})
    assert r.status_code == 200
