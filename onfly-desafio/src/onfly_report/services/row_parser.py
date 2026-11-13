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
        """
            Se se o usuario fez checkin e saiu no mesmo dia, a validação dá problema e dias 
            vão para 0, mas para não interferir nas regras de negóicio, vou apenas deixar o aviso!
            
            porém dava para colocar uma verificação para impedir que o checkout seja no mesmo dia do checkin
            ou se for no mesmo dia, contar como um dia inteiro.
        """

        try:
            checkin = date.fromisoformat((values.get("checkin_date") or "").strip())
            checkout = date.fromisoformat((values.get("checkout_date") or "").strip())
            rooms = int((values.get("rooms") or "").strip()) 
            
            if checkout < checkin:
                logger.warning("Checkout não pode ser menor que Checkin! Linha %s", raw.line_number)
                return None
            if rooms <= 0:
                logger.warning("Não pode existir reserva com 0 ou menos quartos! Linha %s", raw.line_number)
                return None
            return Reservation(
                reservation_id=(values.get("reservation_id") or "").strip(),
                traveler_name=(values.get("traveler_name") or "").strip(),
                company_id=(values.get("company_id") or "").strip(),
                hotel_id=(values.get("hotel_id") or "").strip(),
                hotel_name=(values.get("hotel_name") or "").strip(),
                city=(values.get("city") or "").strip(),
                country=(values.get("country") or "").strip(),
                checkin=checkin,
                checkout=checkout,
                rooms=rooms,
                status=(values.get("status") or "").strip(),
                currency=(values.get("currency") or "").strip(),
                amount=Decimal((values.get("amount") or "").strip()),
                payment_method=(values.get("payment_method") or "").strip(),
                line_number=raw.line_number,
            )
        except (ValueError, InvalidOperation) as err:
            raise InputFileError(f"linha {raw.line_number} inválida: {err}") from err
