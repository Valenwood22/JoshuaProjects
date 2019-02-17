/**
 * @author lt2025vt
 * Date: 4/16/18
 * Program:
 * Description:
 */

public class TreeNode<E extends Comparable<E> > {
    
    //data members
    private E element;
    private TreeNode<E> parent;
    private TreeNode<E> leftChild;
    private TreeNode<E> rightChild;
    
    //constructor
    public TreeNode (E element) {
        this.element = element;
        this.parent = null;
        this.leftChild = null;
        this.rightChild = null;
    }
    
    //getter and setters

    public E getElement() {
        return element;
    }

    public void setElement(E element) {
        this.element = element;
    }

    public TreeNode<E> getParent() {
        return parent;
    }

    public void setParent(TreeNode<E> parent) {
        this.parent = parent;
    }

    public TreeNode<E> getLeftChild() {
        return leftChild;
    }

    public void setLeftChild(TreeNode<E> leftChild) {
        this.leftChild = leftChild;
    }

    public TreeNode<E> getRightChild() {
        return rightChild;
    }

    public void setRightChild(TreeNode<E> rightChild) {
        this.rightChild = rightChild;
    }
    
        //insert a new node into the tree
    public void insert(E obj, TreeNode<E> node) {
        
        if( obj.compareTo(node.getElement())<0) { //it goes to the left
            
            if(leftChild == null) { //insert it here
                leftChild = new TreeNode( obj );
                leftChild.setParent(node);
                node.setLeftChild(leftChild);
            } 
            else{ //continue down the through the tree
                leftChild.insert(obj, node.getLeftChild());
            }
        }
        else{ //it goes to the right
            if(rightChild == null) {
                rightChild = new TreeNode(obj);
                rightChild.setParent(node);
                node.setRightChild(rightChild);
            }
            else {
                rightChild.insert(obj, node.getRightChild());
                
            }
            
        }
        
    }

    @Override
    public String toString() {
        return "" + this.element;
    }     
}