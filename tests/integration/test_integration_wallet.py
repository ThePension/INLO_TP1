"""Integration tests for Wallet package"""
import pytest
from tests.fixtures.wallet_fixtures import empty_wallet, wallet_with_50_balance
from src.wallet import Wallet, InsufficientAmount


# TODO: Implémenter la fonction de test test_deferred_payment
def test_deferred_payment(empty_wallet: Wallet, wallet_with_50_balance: Wallet):
    """Tests a usecase of deferred payment and transfers between 2 wallets"""
    # Transférer 20 de wallet_with_50_balance à empty_wallet
    wallet_with_50_balance.transfer(empty_wallet, 20)

    # Faire un paiement de 10 avec empty_wallet
    empty_wallet.spend_cash(10)

    # faire un paiement différé de 10 avec empty_wallet
    empty_wallet.spend_cash(10, deferred=True)

    # Transférer 10 de wallet_with_50_balance à empty_wallet
    wallet_with_50_balance.transfer(empty_wallet, 10)

    # vérifier que la balance de empty_wallet est 20
    assert empty_wallet.balance == 20

    # vérifier que la balance de wallet_with_50_balance est 20
    assert wallet_with_50_balance.balance == 20

    # Executer les paiements différés
    empty_wallet.pay_deferred_payments()

    # Vérifier que la balance de empty_wallet est 10
    assert empty_wallet.balance == 10
