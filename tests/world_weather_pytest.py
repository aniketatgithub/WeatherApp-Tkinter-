import pytest
from world_weather import mtr_per_sec_to_km_per_hour, format_date_long, format_date_short

def test_mtr_per_sec_to_km_per_hour():
    assert mtr_per_sec_to_km_per_hour(3) == pytest.approx(10.8), "Should convert meters per second to kilometers per hour"

def test_format_date_long():
    assert format_date_long("2023-05-24") == "Wed, 24 May", "Should format date to weekday, day month format"

def test_format_date_short():
    assert format_date_short("2023-05-24") == "24 May", "Should format date to day month format"
