"""Conversão de uma linha do CSV para o modelo de reserva."""

from __future__ import annotations

import logging
from datetime import date
from decimal import Decimal, InvalidOperation

from ..exceptions import InputFileError
from ..models import RawRow, Reservation

logger = logging.getLogger(__name__)


class RowParser:
    """Converte a linha crua em Reservation.

    O arquivo de entrada é consistente; falhas de formato são erro de arquivo, não dado a
    ser descartado.
    """

    def parse(self, raw: RawRow) -> Reservation | None:
        values = raw.values

        try:
            reservation_id=(values.get("reservation_id") or "").strip()
            traveler_name=(values.get("traveler_name") or "").strip()
            company_id=(values.get("company_id") or "").strip()
            hotel_id=(values.get("hotel_id") or "").strip()
            hotel_name=(values.get("hotel_name") or "").strip()
            city=(values.get("city") or "").strip()
            country=(values.get("country") or "").strip()
            checkin = date.fromisoformat((values.get("checkin_date") or "").strip())
            checkout = date.fromisoformat((values.get("checkout_date") or "").strip())
            rooms = int((values.get("rooms") or "").strip())
            status=(values.get("status") or "").strip()
            currency=(values.get("currency") or "").strip()
            amount=Decimal((values.get("amount") or "").strip())
            payment_method=(values.get("payment_method") or "").strip()

            validacoes = [
                (checkout < checkin, "Checkout deve ser posterior ao Checkin!"),
                (rooms <= 0, "Não pode existir reserva com 0 ou menos quartos!"),
                (amount < 0, "Valor da reserva deve ser positivo!"),
            ]
            
            for invalido, mensagem in validacoes:
                if invalido:
                    logger.warning("%s Linha %s", mensagem, raw.line_number)
                    return None

            return Reservation(
                reservation_id=reservation_id,
                traveler_name=traveler_name,
                company_id=company_id,
                hotel_id=hotel_id,
                hotel_name=hotel_name,
                city=city,
                country=country,
                checkin=checkin,
                checkout=checkout,
                rooms=rooms,
                status=status,
                currency=currency,
                amount=amount,
                payment_method=payment_method,
                line_number=raw.line_number,
            )
        except (ValueError, InvalidOperation) as err:
            raise InputFileError(f"linha {raw.line_number} inválida: {err}") from err
