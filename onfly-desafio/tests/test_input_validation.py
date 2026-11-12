"""Testes adicionais: validação de registros."""

from helpers import run_cli


def test_checkin_after_checkout_is_ignored(tmp_path):
    report = run_cli(
        tmp_path,
        [
            {
                "reservation_id": "RSV-1",
                "checkin_date": "2025-01-15",
                "checkout_date": "2025-01-10",
            }
        ],
    )
    assert report["summary"]["total_reservations"] == 0


def test_rooms_less_than_or_equal_zero_is_ignored(tmp_path):
    report = run_cli(
        tmp_path,
        [
            {
                "reservation_id": "RSV-1",
                "rooms": "0",
            }
        ],
    )
    assert report["summary"]["total_reservations"] == 0
