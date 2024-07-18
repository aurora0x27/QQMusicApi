from .ApiException import ApiException


class CredentialNoMusickeyException(ApiException):
    def __init__(self):
        super().__init__("Credential 未提供 musickey 或为空")
