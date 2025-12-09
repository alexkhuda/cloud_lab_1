from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Transactions


class TransactionsDAO(GeneralDAO):
    _domain_type = Transactions
