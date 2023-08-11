class TrieNode:
    def __init__(self):
        self.ref_child = {}
        self.flag = False
        self.value = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key, value):
        node = self.root
        for char in key:
            if char not in node.ref_child:
                node.ref_child[char] = TrieNode()
            node = node.ref_child[char]
        node.flag = True
        node.value = value

    def search(self, key):
        node = self.root
        for char in key:
            if char not in node.ref_child:
                return None
            node = node.ref_child[char]
        if node.flag:
            return node.value
        return None

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.ref_child:
                return False
            node = node.ref_child[char]
        return True

    def delete(self, key):
        def _delete_helper(node, key, index):
            if index == len(key):
                if not node.flag:
                    return False
                node.flag = False
                node.value = None
                return len(node.ref_child) == 0

            char = key[index]
            if char not in node.ref_child:
                return False

            should_delete = _delete_helper(node.ref_child[char], key, index + 1)
            if should_delete:
                del node.ref_child[char]
                return len(node.ref_child) == 0

            return False

        _delete_helper(self.root, key, 0)



