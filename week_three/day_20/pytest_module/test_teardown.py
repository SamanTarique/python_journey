import pytest
from teardown import checking_db_connection


@pytest.fixture
def db_conn():
    print("\nConnecting DB...")
    yield "DB Connected"
    print("\nClosing DB connection ..")


def test_check_db_conn(db_conn):
    assert db_conn == "DB Connected"
    assert checking_db_connection() == "SUCCESS"
    # assert some_db_operation() == <Expected result>
