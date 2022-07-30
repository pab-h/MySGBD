import argparse
import configparser
import json
import os
import sys

from modules.folders import Folders
from modules.utils import print_json

class Cli:
    INI_PATH = "./database.ini"
    CLI_VERSION = "1.1.0"

    def __init__(self) -> None:
        self.settings = self.__load_ini_file()

        self.folders = Folders(
            path=self.settings.get(
                "settings", 
                "local_storage"
            )
        )

        self.__run()

    def __create_default_ini_file(self) -> None:
        parser = configparser.ConfigParser()

        parser["settings"] = { 
            "local_storage": "./tmp" 
        }

        with open(self.INI_PATH, "w+") as file:
            parser.write(file)

    def __load_ini_file(self) -> configparser.ConfigParser: 
        if not os.path.exists(self.INI_PATH):
            self.__create_default_ini_file()

        parser = configparser.ConfigParser()
        parser.read(self.INI_PATH)

        return parser

    def __create_folders_parser(self, subparsers):
        self.folders_parser = subparsers.add_parser(
            "folders", 
            help="Folders handler"
        )

        self.folders_parser.add_argument(
            "-c", 
            "--create", 
            help="Create a folder",
            type=str,
            required=False
        )

        self.folders_parser.add_argument(
            "-d", 
            "--delete", 
            help="Delete a folder by name",
            type=str,
            required=False
        )

        self.folders_parser.add_argument(
            "-l", 
            "--list", 
            help="list all folders",
            action="store_true",
            required=False
        )        

    def __create_documents_parser(self, subparsers):
        self.documents_parser = subparsers.add_parser(
            "documents",
            help="Folders handler"
        )
        
        self.documents_parser.add_argument(
            "folder",
            type=str
        )

        self.documents_parser.add_argument(
            "-l", 
            "--list", 
            help="List all documents",
            type=str,
            required=False
        )

        self.documents_parser.add_argument(
            "-g", 
            "--get", 
            help="Get document by id",
            type=str,
            required=False
        )

        self.documents_parser.add_argument(
            "-c", 
            "--create", 
            help="Create document",
            type=str,
            required=False
        )

        self.documents_parser.add_argument(
            "-d", 
            "--delete", 
            help="Delete document",
            type=str,
            required=False
        )

        self.documents_parser.add_argument(
            "-u", 
            "--update", 
            help="Update document",
            type=str,
            required=False
        )

    def __run(self) -> None:

        self.parser = argparse.ArgumentParser(
            prog="My sgbd",
            description="Estava com tempo sobrando e...",
            epilog="Desenvolvido por https://github.com/pab-h"
        )

        self.parser.version = self.CLI_VERSION
        self.parser.add_argument("-v", "--version", action="version")

        subparsers = self.parser.add_subparsers(
            dest="command",
            help="Actions folders"
        )

        self.__create_folders_parser(subparsers)
        self.__create_documents_parser(subparsers)

        args = self.parser.parse_args()

        try:
            if args.command == "folders":

                if args.create:
                    self.folders.create(args.create)

                    print_json({ 
                        "ok": True,
                        "mensage": f"Folder { args.create } created"
                    })

                if args.delete:
                    self.folders.delete(args.delete)

                    print_json({ 
                        "ok": True,
                        "mensage": f"Folder { args.delete } deleted"
                    })

                if args.list:
                    folders = self.folders.list()

                    print_json({ 
                        "ok": True,
                        "folders": folders
                    })
            if args.command == "documents":
                folder = self.folders.get(args.folder)

                if args.create:
                    json_parsed = json.loads(args.create)
                    document = folder.create(json_parsed)

                    print_json({
                        "ok": True,
                        "document_id": document.id
                    })

                if args.get and not args.update:
                    document = folder.get(args.get)

                    print_json({
                        "ok": True,
                        "document": document.read()
                    })

                if args.get and args.update:
                    document = folder.get(args.get)
                    
                    json_parsed = json.loads(args.update)
                    document.update(json_parsed)

                    print_json({ "ok": True })
                    
            sys.exit(0)
                
        except Exception as e:
            print_json({ 
                "ok": False,
                "mensage": e.args[0]
            })    

            sys.exit(1)
Cli()