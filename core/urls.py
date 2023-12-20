from django.urls import path
from .views import index
from .transfer import search_users_account_number,AmountTransfer,AmountTransferProcess,TransferConfirmation,TransferProcess,TransferCompleted
from .transaction import transaction_lists,transaction_detail
from .payment_request import SearchUsersRequest,AmountRequest,AmountRequestProcess,AmountRequestConfirmation,AmountRequestFinalProcess,RequestCompleted,settlement_confirmation,settlement_processing,SettlementCompleted,deletepaymentrequest
from .credit_card import card_detail,fund_credit_card,withdraw_fund,delete_card
app_name='core'
urlpatterns=[
    path('',index,name='index'),
    #Transfers
    path('search-account/',search_users_account_number,name="search-account"),
    path('amount-transfer/<account_number>/',AmountTransfer,name="amount-transfer"),
    path('amount-transfer-process/<account_number>/',AmountTransferProcess,name="amount-transfer-process"),
    path('transfer-confirmation/<account_number>/<transaction_id>/',TransferConfirmation,name="transfer-confirmation"),
    path('transfer-process/<account_number>/<transaction_id>/',TransferProcess,name="transfer-process"),
    path('transfer-completed/<account_number>/<transaction_id>/',TransferCompleted,name="transfer-completed"),
    

    #transactiion
    path('transactions/',transaction_lists,name="transactions"),
    path('transaction-detail/<transaction_id>/',transaction_detail,name="transaction-detail"),

    #paymentRequest
    path('request-search-account/',SearchUsersRequest,name="request-search-account"),
    path('amount-request/<account_number>/',AmountRequest,name="amount-request"),
    path('amount-request-process/<account_number>/',AmountRequestProcess,name="amount-request-process"),
    path('amount-request-confirmation/<account_number>/<transaction_id>/',AmountRequestConfirmation,name="amount-request-confirmation"),
    path('amount-request-final-process/<account_number>/<transaction_id>/',AmountRequestFinalProcess,name="amount-request-final-process"),
    path('amount-request-completed/<account_number>/<transaction_id>/',RequestCompleted,name="amount-request-completed"),

    #Request Settlement
    path('settlement-confirmation/<account_number>/<transaction_id>/',settlement_confirmation,name="settlement-confirmation"),
    path('settlement-processing/<account_number>/<transaction_id>/',settlement_processing,name="settlement-processing"),
    path('settlement-completed/<account_number>/<transaction_id>/',SettlementCompleted,name="settlement-completed"),
    path('delete-request/<account_number>/<transaction_id>/',deletepaymentrequest,name="delete-request"),

    #Credit Cards URLS
    path("card/<card_id>/", card_detail, name="card-detail"),
    path("fund-credit-card/<card_id>/", fund_credit_card, name="fund-credit-card"),
    path("withdraw_fund/<card_id>/", withdraw_fund, name="withdraw_fund"),
    path("delete_card/<card_id>/", delete_card, name="delete_card"),








    




]