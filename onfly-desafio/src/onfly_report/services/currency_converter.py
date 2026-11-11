"""Conversão de valores para BRL."""

from __future__ import annotations

from decimal import Decimal

"""Converte um valor na moeda informada para BRL usando a taxa da tabela."""
def convert_to_brl(amount: Decimal, currency: str, rates: dict[str, Decimal]) -> Decimal:
    rate = rates[currency]
    return amount * rate 
