"""
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

Example1:

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

import collections
from typing import *
class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.isFile = False
        self.content = ""
        self.name = ""

class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        res = []
        path = path.split('/')[1:]
        cur = self.root
        if path[0] != '':
            for p in path:
                cur = cur.child[p]
        if cur.isFile:
            return [cur.name]
        for ch in cur.child:
            res.append(ch)
        return sorted(res)

    def mkdir(self, path: str) -> None:
        cur = self.root
        paths = path.split('/')[1:]
        for p in paths:
            cur = cur.child[p]
            cur.name = p

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.root
        filePath = filePath.split('/')[1:]
        for p in filePath:
            cur = cur.child[p]
            cur.name = p
        cur.isFile = True
        cur.content += content

    def readContentFromFile(self, filePath: str) -> str:
        cur = self.root
        filePath = filePath.split('/')[1:]
        for p in filePath:
            cur = cur.child[p]
        if cur.isFile:
            return cur.content

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)