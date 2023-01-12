def check_binary_search_tree_(root):
    if not root:
        return False
    
    data_set = {root.data}
    
    def check(node, min_ = None, max_ = None):
        if not node:
            return True
        
        if node.data in data_set:
            return False
        else:
            data_set.add(node.data)
        print("what")
        if not min_:
            if node.data < max_:
                return (check(node.left, min_ = min_, max_ = node.data)
                        and 
                        check(node.right, min_ = node.data, max_ = max_))
            else:
                return False
            
        if not max_:
            if node.data > min_:
                return (check(node.left, min_ = min_, max_ = node.data)
                        and 
                        check(node.right, min_ = node.data, max_ = max_))
            else:
                return False   
        
        if node.data < min_ or node.data > max_:
            return False
        
        return check(node.left, min_ = min_, max_ = node.data) and check(node.right, min_ = node.data, max_ = max_)
    
    return check(root.left, max_ = root.data) and check(root.right, min_ = root.data)