from my_project.auth.dao import transactions_dao
from my_project.auth.service.general_service import GeneralService


class TransactionsService(GeneralService):

    _dao = transactions_dao