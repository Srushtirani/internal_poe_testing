from app import app

def test_prediction():
    client = app.test_client()

    response = client.post(
        "/predict",
        json={
            "features": [
                0.038, 0.051, 0.062, 0.022, -0.044,
                -0.034, -0.043, -0.003, 0.020, -0.017
            ]
        }
    )

    assert response.status_code == 200
    assert "prediction" in response.get_json()