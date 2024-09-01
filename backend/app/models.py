from pydantic import BaseModel
from typing import Optional

class CorporatePurchase(BaseModel):
    id: int
    purchase_cardId: Optional[str]
    purchase_id: Optional[str]
    purchase_status: Optional[str]
    purchase_created: Optional[str]
    purchase_holderId: Optional[str]
    purchase_amount: Optional[float]
    purchase_merchantName: Optional[str]
    purchase_merchantCategoryType: Optional[str]
    purchase_workspaceId: Optional[str]

class Transaction(BaseModel):
    id: int
    source: Optional[str]
    externalId: Optional[str]
    created: Optional[str]
    amount: Optional[float]
    fee: Optional[float]
    balance: Optional[float]
    description: Optional[str]
    workspaceId: Optional[str]

class Transfer(BaseModel):
    id: int
    transfer_id: Optional[str]
    transfer_status: Optional[str]
    transfer_created: Optional[str]
    transfer_amount: Optional[float]
    transfer_name: Optional[str]
    transfer_taxId: Optional[str]
    transfer_bankCode: Optional[str]
    transfer_branchCode: Optional[str]
    transfer_accountNumber: Optional[str]
    transfer_workspaceId: Optional[str]

class Invoice(BaseModel):
    id: int
    invoice_id: Optional[str]
    invoice_status: Optional[str]
    invoice_created: Optional[str]
    invoice_nominalAmount: Optional[float]
    invoice_amount: Optional[float]
    invoice_due: Optional[str]
    invoice_fine: Optional[float]
    invoice_interest: Optional[float]
    invoice_expiration: Optional[str]
    invoice_name: Optional[str]
    invoice_taxId: Optional[str]
    invoice_workspaceId: Optional[str]
    invoice_brcode: Optional[str]
