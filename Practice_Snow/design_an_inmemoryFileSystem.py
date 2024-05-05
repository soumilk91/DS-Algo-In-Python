"""
Author: Soumil Ramesh Kulkarni
Date: 05.04.2024

Question:

Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:

FileSystem() Initializes the object of the system.
List<String> ls(String path)
If path is a file path, returns a list that only contains this file's name.
If path is a directory path, returns the list of file and directory names in this directory.
The answer should in lexicographic order.
void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
void addContentToFile(String filePath, String content)
If filePath does not exist, creates that file containing given content.
If filePath already exists, appends the given content to original content.
String readContentFromFile(String filePath) Returns the content in the file at filePath.

Input
["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
[[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
Output
[null, [], null, null, ["a"], "hello"]

Explanation
FileSystem fileSystem = new FileSystem();
fileSystem.ls("/");                         // return []
fileSystem.mkdir("/a/b/c");
fileSystem.addContentToFile("/a/b/c/d", "hello");
fileSystem.ls("/");                         // return ["a"]
fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"
"""

from collections import defaultdict
from typing import *

class FileSystem:
    def __init__(self):
        self.files = defaultdict(str) # store file content
        self.dirs = {} # store file system struture

    def __isFile(self, path) -> bool:
        return path in self.files # it is a file

    # O(n + m log m), where m is the number of the file entities in the director
    def ls(self, path: str) -> List[str]:
        res = []
        pathList = path.split('/')

        if self.__isFile(path):
            return [pathList[-1], ]

        cur = self.dirs
        for fileName in pathList:
            if fileName:
                cur = cur.get(fileName)
        if cur:
            for fn in cur.keys():
                res.append(fn)
            res.sort()
        return res

    # O(n)
    def mkdir(self, path: str) -> None:
        pathList = path.split('/')
        cur = self.dirs
        for symb in pathList:
            if symb:
                cur = cur.setdefault(symb, {})

    # O(n)
    def addContentToFile(self, filePath: str, content: str) -> None:
        self.mkdir(filePath)
        self.files[filePath] += content # store file content in a hash map

    # O(1)
    def readContentFromFile(self, filePath: str) -> str:
        return self.files.get(filePath)