
/**
 * @author lt2025vt Date: 4/16/18 Program: Description:
 */

public class BinarySearchTree<E extends Comparable<E>> {

    private TreeNode<E> root;

    //constructor
    public BinarySearchTree() {
        root = null;
    }

    //setters and getter
    public TreeNode<E> getRoot() {
        return root;
    }

    public void setRoot(TreeNode<E> root) {
        this.root = root;
    }

    //insert node method
    public void insertNode(E obj) {
        if (root == null) {
            root = new TreeNode(obj);
        } else {
            root.insert(obj, root);
        }
    }

    //in-order traverse
    public void inorderTraverse() {
        inorderHelper(root);
    }

    private void inorderHelper(TreeNode<E> node) {
        if (node == null) {
            return;
        } else {
            inorderHelper(node.getLeftChild());
            System.out.print(node.toString() + " ");
            inorderHelper(node.getRightChild());
        }
    }

    //pre-order
    //post-order
    //search method
    public TreeNode treeSearch(E key, TreeNode<E> node) {

        try {
            if (key.compareTo(node.getElement()) == 0) {
                return node;
            } else if (key.compareTo(node.getElement()) > 0) {
                //further search on he right subtree
                return treeSearch(key, node.getRightChild());
            } else {
                //further search on the left subtree
                return treeSearch(key, node.getLeftChild());
            }
        }
        catch(Exception e) {
            return null;
        }
    }// end method
}//end class
