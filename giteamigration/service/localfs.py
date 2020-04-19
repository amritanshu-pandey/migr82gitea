import pathlib

import git

from urllib.parse import urlsplit

from giteamigration.service.service import GitService
from giteamigration.blueprints import Repository, Namespace
from giteamigration.blueprints.repositories import is_git_repo


class LocalFS(GitService):
    def __init__(self, url, username=None, secret=None):
        super().__init__(url, username, secret)
        self.root = pathlib.Path(urlsplit(url).path)

    @property
    def servertype(self):
        return "localfs"

    @staticmethod
    def _get_path_stem(path):
        return pathlib.Path(path).absolute().parts[-1]

    @property
    def repositories(self) -> Repository:
        all_repos = []
        for directory in self.root.iterdir():
            if is_git_repo(directory):
                all_repos.append(directory)

        for repo in all_repos:
            yield Repository(
                name=self._get_path_stem(repo),
                namespace=Namespace("root"),
                ssh_url=None,
                http_url=None,
                localfs_url=repo.absolute(),
                description=repo.name,
            )

    def get_namespace_repos(self, namespace: Namespace):
        namespace_path = self.root / namespace

        if namespace == "root":
            for repo in self.repositories:
                yield repo
        else:
            for directory in namespace_path.iterdir():
                if is_git_repo(directory):
                    yield Repository(
                        name=self._get_path_stem(directory),
                        namespace=Namespace,
                        ssh_url=None,
                        http_url=None,
                        localfs_url=directory.absolute(),
                        description=directory.name,
                    )

    def get_namespaces(self, namespace: Namespace = None) -> Namespace:
        namespaces = []

        namespace_path = ""
        if namespace:
            namespace_path = namespace.fspath
        for directory in (self.root / namespace_path).iterdir():
            if not is_git_repo(directory):
                namespaces.append(directory)

        for ns in namespaces:
            yield Namespace(
                name=self._get_path_stem(ns),
                parent=namespace or Namespace("root"),
                repositories=self.get_namespace_repos(ns),
            )

    def create_namespace(self, parentns: str, name: str):
        namespace = self.root / parentns / name
        namespace.mkdir()

        return namespace

    def create_repository(self, namespace: Namespace, name: str):
        repo_path = self.root / namespace.fspath / name
        repo_path.mkdir(parents=True)

        git.Git().init(repo_path)
        return Repository(
            name=name,
            namespace=namespace,
            ssh_url=None,
            http_url=None,
            localfs_url=repo_path.absolute(),
            description=name,
        )

    @property
    def userid(self):
        return None
