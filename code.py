from queue import Queue

class newNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def maxNode(root):
    if(root==None):
        return -1
    q=Queue()
    q.put(root)
    level=0
    Max=-99999999999
    level_no=0
    while(1):
        NodeCount=q.qsize()
        if(NodeCount==0):
            break
        if(NodeCount>Max):
            Max=NodeCount
            level_no=level
        while(NodeCount>0):
            Node=q.queue[0]
            q.get()
            if(Node.left!=None):
                q.put(Node.left)
            if(Node.right!=None):
                q.put(Node.right)
            NodeCount-=1
        level+=1
    return level_no
def insert(root,node):
    if(root is None):
        root=node
    else:
        if root.data<node.data:
            if root.right is None:
                root.right=node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left=node
            else:
                insert(root.left,node)
                
        
if __name__=='__main__':
    qwe=int(input())
    
    j=0
    for i in range(0,qwe):
        mn=int(input())
        asd=list(map(int,input().split()))
        r=newNode(asd[j])
        for j in range(1,mn):
            insert(r,newNode(asd[j]))
        s=maxNode(r)
        print(s)
                   
