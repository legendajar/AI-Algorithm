def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)

        if left_height > right_height:
            return left_height + 1
        
        else: 
            return right_height + 1

def process_current_level(root, l):
    if root is None:
        return
    
    if l == 0:
        print(root.data)

    elif l > 0:
        process_current_level(root.left, l - 1)
        process_current_level(root.right, l - 1)

def recursive_level_order(root):
    h = height(root)
    for l in range(h):
        process_current_level(root, l)