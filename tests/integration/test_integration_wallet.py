"""Integration tests for Wallet package"""
import pytest
from tests.fixtures.wallet_fixtures import empty_wallet, wallet_with_50_balance
from src.wallet import Wallet, InsufficientAmount


# TODO: Implémenter la fonction de test test_deferred_payment
# Transférer 20 de wallet_with_50_balance à empty_wallet
# Faire un paiement de 10 avec empty_wallet
# faire un paiement différé de 10 avec empty_wallet
# Transférer 10 de wallet_with_50_balance à empty_wallet
# vérifier que la balance de empty_wallet est 20
# vérifier que la balance de wallet_with_50_balance est 20
# Executer les paiements différés
# Vérifier que la balance de empty_wallet est 10
def test_deferred_payment(empty_wallet: Wallet, wallet_with_50_balance: Wallet):
    """Tests a usecase of deferred payment and transfers between 2 wallets"""
    assert False
