from datetime import datetime

import pytest
from pytz import timezone

from api.config import Config

from .datetime import now


@pytest.mark.order(1)
def test_now():
    app_result = now()
    sys_result = datetime.now(tz=timezone(Config.TIMEZONE))
    assert app_result.tzinfo.zone == Config.TIMEZONE
    assert app_result.year == sys_result.year
    assert app_result.month == sys_result.month
    assert app_result.day == sys_result.day
    assert app_result.hour == sys_result.hour
