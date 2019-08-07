# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 16:41:08 2019

@author: xiang
"""
"""
# 二叉搜索树的建立，删除等
"""

        
class BinarySearchTree(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def find(self, x):
        if x == self.key:
            return True
        elif x < self.key and self.left:  # 如果x小，则去左子树找
            return self.left.find(x)
        elif x > self.key and self.right:  # 如果x大，则去右子树找
            return self.right.find(x)
        else:
            return None  # 找不到返回None

    def findMin(self):
        if self.left:  # 如果左节点存在，最小值一定在左节点的最深处
            return self.left.findMin()
        else:
            return self.key  # 如果左节点没有，那么根节点最小

    def findMax(self):
        if self.right:  # 如果右节点存在，最大值一定在右节点的最深处
            return self.right.findMax()
        else:
            return self.key  # 如果右节点没有，那么根节点最大

    def insert(self, x):
        if self.find(x):  # 如果找到了该节点，则什么也不做
            return None
        else:  # 如果没有找到则开始插入
            if x < self.key:  # 如果插入值小，则插入左子树
                if self.left:  # 先判断左子树是否存在
                    return self.left.insert(x)
                else:
                    newTree = BinarySearchTree(x)
                    self.left = newTree  # 如果左子树不存在，则把该节点设为左子树
            elif x > self.key:  # 如果插入值大，则插入右子树
                if self.right:
                    return self.right.insert(x)
                else:
                    newTree = BinarySearchTree(x)
                    self.right = newTree

    def delete(self, x):
        if self.find(x):  # 首先判断该节点是否存在
            if x < self.key:  # 如果要删的数据比该数据self.key小，从左子树删起
                self.left = self.left.delete(x)
                return self
            elif x > self.key:  # 如果要删的数据比self.key大，从右子树删起
                self.right = self.right.delete(x)
                return self
            else:  # 如果就是该数据，判断他是否有左右子树
                if self.left and self.right:  # 如果左右子树都存在
                    minkey = self.right.findMin().key  # 把右子树中最小的点连接原来x的父节点, 并且右子树中删除该点
                    self.key = minkey
                    self.right = self.right.delete(minkey)
                    return self
                else:  # 如果左右节点不全存在
                    if self.left:
                        return self.left
                    else:
                        return self.right
        else:
            return self


bst = BinarySearchTree(17)
node_list = [17, 5, 29, 38, 35, 2, 9, 8, 16, 11]
for l in node_list:
    bst.insert(l)

print(bst.findMax())
print(bst.findMin())
print(bst.find(10))
print(bst.delete(11))
