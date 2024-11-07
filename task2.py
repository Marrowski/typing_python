from __future__ import annotations
from typing import List, Optional


class Directory:
    def __init__(self, name: str, root: Optional[Directory]):
        self.name: str = name
        self.root: Optional[Directory] = root
        self.files: List[File] = []
        self.sub_directories: List[Directory] = []

    def add_sub_directory(self, sub_directory: Directory):
        sub_directory.root = self
        self.sub_directories.append(sub_directory)

    def remove_sub_directory(self, sub_directory: Directory):
        sub_directory.root = None
        self.sub_directories.clear()

    def add_file(self, file: File):
        file.directory = self
        self.files.append(file)

    def remove_file(self, file: File):
        file.files = None
        self.files.clear()


class File:
    def __init__(self, name: str, directory: Optional[Directory]):
        self.name: str = name
        self.directory: Optional[Directory] = directory
