import pytest

def test_sucess_rate():
    from api_metrics import success_rate as sr
    metrics = {
        "total_requests": 100,
        "failed_requests": 10
    }
    assert sr(metrics) == 90
    with pytest.raises(ValueError):
        sr({"total_requests": 0, "failed_requests": 0})

def test_failed_rate():
    from api_metrics import failed_rate as fr
    metrics = {
        "total_requests": 100,
        "failed_requests": 10
    }
    assert fr(metrics) == 10
    with pytest.raises(ValueError):
        fr({"total_requests": 0, "failed_requests": 0})

def test_latency_change():
    from api_metrics import latency_change as lc
    metrics = {
        "previous_latency": 200,
        "current_latency": 250
    }
    assert lc(metrics) == 25
    with pytest.raises(ValueError):
        lc({"previous_latency": 0, "current_latency": 250})

def test_throughput():
    from api_metrics import throughput as tp
    metrics = {
        "total_requests": 100,
        "processing_timer": 10
    }
    assert tp(metrics) == 10
    with pytest.raises(ValueError):
        tp({"total_requests": 100, "processing_timer": 0})

def test_success_requests():
    from api_metrics import success_requests as sreq
    metrics = {
        "total_requests": 100,
        "failed_requests": 10
    }
    assert sreq(metrics) == 90
    with pytest.raises(ValueError):
        sreq({"total_requests": 0, "failed_requests": 0})