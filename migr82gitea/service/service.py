import abc

from urllib.parse import urlsplit

from gitback.service.session import Session
from gitback.blueprints import Repository


class GitService(abc.ABC):
    def __init__(self, url, username=None, secret=None):
        self.username = username
        self.secret = secret
        self.authenticated = bool(self.username or self.secret)

        urlscheme = urlsplit(url).scheme

        if urlscheme.lower() in ('local', 'file'):
            self.session = None
        else:
            self.session = Session(
                servertype=self.servertype,
                url=url,
                username=self.username,
                secret=self.secret
            )

    @abc.abstractproperty
    def servertype(self):
        pass

    @abc.abstractproperty
    def repositories(self) -> [Repository]:
        pass

    @abc.abstractmethod
    def get_namespace_repos(self):
        pass

    @abc.abstractmethod
    def get_namespaces(self):
        pass

    @abc.abstractmethod
    def create_namespace(self, parentns, name):
        pass

    @abc.abstractmethod
    def create_repository(self, namespace, name):
        pass

    def userid(self):
        return self.username
