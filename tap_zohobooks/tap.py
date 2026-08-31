"""ZohoBooks tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_zohobooks.streams import (
    OrganizationIdStream,
    InvoicesStream,
    JournalsIdStream,
    JournalStream,
    ChartOfAccountsStream,
    SalesOrdersStream,
    SalesOrdersDetailsStream,
    ItemsStream,
    ContactsStream,
    BillsStream,
    PurchaseOrdersStream,
    PurchaseOrderDetailsStream,
    VendorsStream,
    ItemsDetailStream,
    EstimatesStream,
    EstimatesDetailsStream,
    AccountTransactionsStream,
    BillsDetailsStream,
    InvoiceDetailsStream,
    ExpensesStream,
    ExpensesDetailsStream,
    CreditNotesIDStream,
    CreditNoteDetailsStream,
    VendorCreditIDSStream,
    VendorCreditDetailsStream,
    ProfitAndLossStream,
    ReportAccountTransactionsStream,
    ProfitAndLossCashStream,
    ReportAccountTransactionsCashStream,
    ReportAgingDetailStream,
    ReportAgingSummaryStream,
    CurrencyStream,
)

STREAM_TYPES = [
    OrganizationIdStream,
    JournalsIdStream,
    InvoicesStream,
    JournalStream,
    ChartOfAccountsStream,
    SalesOrdersStream,
    SalesOrdersDetailsStream,
    ItemsStream,
    ContactsStream,
    BillsStream,
    PurchaseOrdersStream,
    PurchaseOrderDetailsStream,
    VendorsStream,
    ItemsDetailStream,
    EstimatesStream,
    EstimatesDetailsStream,
    AccountTransactionsStream,
    BillsDetailsStream,
    InvoiceDetailsStream,
    ExpensesStream,
    ExpensesDetailsStream,
    CreditNotesIDStream,
    CreditNoteDetailsStream,
    VendorCreditIDSStream,
    VendorCreditDetailsStream,
    ProfitAndLossStream,
    ReportAccountTransactionsStream,
    ProfitAndLossCashStream,
    ReportAccountTransactionsCashStream,
    ReportAgingDetailStream,
    ReportAgingSummaryStream,
    CurrencyStream,
]


class TapZohoBooks(Tap):
    """ZohoBooks tap class."""

    name = "tap-zohobooks"

    def __init__(
        self,
        config=None,
        catalog=None,
        state=None,
        parse_env_config=False,
        validate_config=True,
        **kwargs
    ) -> None:
        self.config_file = config[0] if config else None
        super().__init__(config=config, catalog=catalog, state=state, parse_env_config=parse_env_config, validate_config=validate_config, **kwargs)

    config_jsonschema = th.PropertiesList(
        th.Property(
            "client_id",
            th.StringType,
            required=True,
            secret=True,
            description="The client ID for OAuth 2.0 authentication",
        ),
        th.Property(
            "client_secret",
            th.StringType,
            required=True,
            secret=True,
            description="The client secret for OAuth 2.0 authentication",
        ),
        th.Property(
            "access_token",
            th.StringType,
            required=True,
            secret=True,
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "refresh_token",
            th.StringType,
            required=True,
            secret=True,
        ),
        th.Property(
            "accounts-server",
            th.StringType,
            default="https://accounts.zoho.com",
            description="The Zoho accounts server URL for your region (e.g., https://accounts.zoho.eu for EU)",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapZohoBooks.cli()