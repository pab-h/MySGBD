import argparse
import json
import sys
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

        self.parser.add_argument(
            "--folders-get",
            type=str,
            required=False
        )

        self.parser.add_argument(
            "--folders-delete",
            type=str,
            required=False
        )

        self.parser.add_argument(
            "--folders-list",
            action='store_true',
            required=False
        )

    def __set_args_documents(self) -> None:
        self.parser.add_argument(
            "--documents-create",
            type=str,
            required=False
        )



    def __run(self) -> None:
        self.__set_args_folders()
        self.__set_args_documents()

        args = self.parser.parse_args()

        if args.folders_create:
            folder = self.folders.create(args.folders_create)
            self.current_folder = args.folders_create
            print(json.dumps({
                "ok": True
            }))

        if args.folders_get:
            folder = self.folders.get(args.folders_get)
            print(json.dumps({
                "ok": True
            }))

        if args.folders_list:
            print(json.dumps({
                "ok": True,
                "folders": self.folders.list()
            }))

        if args.folders_delete:
            self.folders.delete(args.folders_delete)
            print(json.dumps({
                "ok": True
            }))

        # if args.
        sys.exit(0)


Cli()