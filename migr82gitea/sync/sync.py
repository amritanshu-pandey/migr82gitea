from gitback.service.service import GitService


class Sync:
    def __init__(
            self,
            source: GitService,
            destination: GitService,
            ):
        self.source = source
        self.destination = destination

    def sync(self, dryrun=False):
        source_namespaces = self.source.get_namespaces()
        for ns in source_namespaces:
            print(f'Processing namespace: {ns.name}')
            destns = self.destination.create_namespace(
                parentns=ns.parent or '',
                name=ns.name)
            for repo in ns.repositories:
                print(f'Processing repository: {repo}')
                repo.clone_or_update(
                    base_path=self.destination.root / destns.name)