import argparse
from modules.folders import Folders

class Cli:
    SGBD_LOCAL_STORAGE = './tmp'

    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(description="CLI")
        self.folders = Folders(
            path=Cli.SGBD_LOCAL_STORAGE
        )

        self.__run()

    def __set_args_folders(self) -> None:
        self.parser.add_argument(
            "--folders-create",
            type=str,
            required=False
        )

        self.parser.add_argument("--folders-get", required=False)

    def __run(self) -> None:
        self.__set_args_folders()

        args = self.parser.parse_args()

        if args.folders_create:
            self.folders.create(args.folders_create)


Cli()