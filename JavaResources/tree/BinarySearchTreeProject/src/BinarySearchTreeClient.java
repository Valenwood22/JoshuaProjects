/**
 * @author lt2025vt
 * Date: 4/16/18
 * Program:
 * Description:
 */

import java.util.Scanner;

public class BinarySearchTreeClient {
    
    public static void main( String [] args) {
        
        Scanner console = new Scanner(System.in);
        
        //create a BinarySearchTree object
        BinarySearchTree<Integer> myTree = new BinarySearchTree<Integer>();
        
        myTree.insertNode(8);
        myTree.insertNode(4);
        myTree.insertNode(32);
        myTree.insertNode(7);
        myTree.insertNode(3);
        myTree.insertNode(37);
        myTree.insertNode(2);
        myTree.insertNode(11);
        myTree.insertNode(12);
        
        System.out.println("\nInorder Travers: ");
        
        myTree.inorderTraverse();

        System.out.println();
        
        System.out.print("Enter key to search: " );
        int key = console.nextInt();
        
        TreeNode temp = myTree.treeSearch(key, myTree.getRoot());
        
        if(temp == null) {
            System.out.println("Not Found");
            
        }
        else {
            System.out.println("Found");
            
            if(temp.getParent() != null) {
                System.out.println("parent: " + temp.getParent());
            }
            else {
                System.out.println("No parnt, so it is the root");
            }
            if(temp.getLeftChild() != null) {
                System.out.println("Left child: " + temp.getLeftChild());
                System.out.println("Right child: " + temp.getRightChild());
            }
            else{
                System.out.println("No left Child");
            }
        }
    }
}
