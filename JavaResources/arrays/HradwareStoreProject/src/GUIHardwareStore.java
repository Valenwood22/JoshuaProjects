//import static HardwareStoreClient.search;
import java.awt.Font;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;
import javax.swing.JFileChooser;
import javax.swing.JOptionPane;

/**
 *
 * @author lt2025vt
 */
public class GUIHardwareStore extends javax.swing.JFrame {

    final int SIZE = 15;

    Invenory[] itemList = new Invenory[SIZE];

    String inputFileName;

    public GUIHardwareStore() {
        initComponents();
    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jLabel1 = new javax.swing.JLabel();
        jScrollPane1 = new javax.swing.JScrollPane();
        outputArea = new javax.swing.JTextArea();
        SelectButton = new javax.swing.JButton();
        readButton = new javax.swing.JButton();
        outputButton = new javax.swing.JButton();
        totalButton = new javax.swing.JButton();
        lowButton = new javax.swing.JButton();
        highestButton = new javax.swing.JButton();
        searchButton = new javax.swing.JButton();
        clearButton = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jLabel1.setFont(new java.awt.Font("Tahoma", 1, 24)); // NOI18N
        jLabel1.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabel1.setText("Hardware Store Program");

        outputArea.setColumns(20);
        outputArea.setRows(5);
        jScrollPane1.setViewportView(outputArea);

        SelectButton.setFont(new java.awt.Font("Tahoma", 1, 11)); // NOI18N
        SelectButton.setText("Select Data File");
        SelectButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                SelectButtonActionPerformed(evt);
            }
        });

        readButton.setFont(new java.awt.Font("Tahoma", 1, 11)); // NOI18N
        readButton.setText("Read Data File");
        readButton.setEnabled(false);
        readButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                readButtonActionPerformed(evt);
            }
        });

        outputButton.setFont(new java.awt.Font("Tahoma", 1, 11)); // NOI18N
        outputButton.setText("Output Inventory");
        outputButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                outputButtonActionPerformed(evt);
            }
        });

        totalButton.setFont(new java.awt.Font("Tahoma", 1, 11)); // NOI18N
        totalButton.setText("Total In-Stock Value");
        totalButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                totalButtonActionPerformed(evt);
            }
        });

        lowButton.setFont(new java.awt.Font("Tahoma", 1, 11)); // NOI18N
        lowButton.setText("Low Stock Product");
        lowButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                lowButtonActionPerformed(evt);
            }
        });

        highestButton.setFont(new java.awt.Font("Tahoma", 1, 11)); // NOI18N
        highestButton.setText("Highest");
        highestButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                highestButtonActionPerformed(evt);
            }
        });

        searchButton.setFont(new java.awt.Font("Tahoma", 1, 11)); // NOI18N
        searchButton.setText("Search");
        searchButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                searchButtonActionPerformed(evt);
            }
        });

        clearButton.setFont(new java.awt.Font("Tahoma", 1, 11)); // NOI18N
        clearButton.setText("Clear");
        clearButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                clearButtonActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGap(108, 108, 108)
                        .addComponent(jLabel1, javax.swing.GroupLayout.PREFERRED_SIZE, 576, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(38, 38, 38)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 732, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(readButton, javax.swing.GroupLayout.PREFERRED_SIZE, 121, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(SelectButton, javax.swing.GroupLayout.PREFERRED_SIZE, 121, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addGap(34, 34, 34)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                                    .addComponent(outputButton, javax.swing.GroupLayout.PREFERRED_SIZE, 147, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(totalButton))
                                .addGap(26, 26, 26)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                    .addComponent(lowButton, javax.swing.GroupLayout.PREFERRED_SIZE, 187, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(highestButton, javax.swing.GroupLayout.PREFERRED_SIZE, 187, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addGap(33, 33, 33)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                    .addComponent(searchButton, javax.swing.GroupLayout.DEFAULT_SIZE, 184, Short.MAX_VALUE)
                                    .addComponent(clearButton, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))))))
                .addContainerGap(38, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jLabel1, javax.swing.GroupLayout.PREFERRED_SIZE, 53, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 351, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(SelectButton)
                    .addComponent(outputButton)
                    .addComponent(lowButton)
                    .addComponent(searchButton))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(readButton)
                    .addComponent(totalButton)
                    .addComponent(highestButton)
                    .addComponent(clearButton))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void lowButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_lowButtonActionPerformed
        // TODO add your handling code here:
        outputArea.append("Low In-Stock Items: \n");

        for (int i = 0; i < itemList.length; i++) {
            if (itemList[i].getNumberOfPrices() < 10) {
                outputArea.append(itemList[i] + "\n");
            }
        }
    }//GEN-LAST:event_lowButtonActionPerformed

    private void SelectButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_SelectButtonActionPerformed
        // TODO add your handling code here:
        JFileChooser open = new JFileChooser("./");

        int status = open.showOpenDialog(null);

        if (status == JFileChooser.APPROVE_OPTION) {
            //open button is a clicked
            inputFileName = open.getSelectedFile().getAbsolutePath();

            outputArea.append(inputFileName + " is seected.");
            
            readButton.setEnabled(true);
            
        } else {
            outputArea.append("No file is selected.");
        }
    }//GEN-LAST:event_SelectButtonActionPerformed

    private void readButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_readButtonActionPerformed
        // TODO add your handling code here://remove the data file headings

        try {
            Scanner inFile = new Scanner(new FileReader(inputFileName));
            for (int i = 0; i < 4; i++) {
                inFile.next();
            }

            int pid;
            String pName;
            int pieces;
            double unitPrice;

            int x = 0;
            //read data, create objects, and populate the array
            while (inFile.hasNext()) {
                pid = inFile.nextInt();
                pName = inFile.next();
                pieces = inFile.nextInt();
                unitPrice = inFile.nextDouble();

                //create an instant (object) of Inventory
                itemList[x] = new Invenory(pid, pName, pieces, unitPrice);
                x++;
            }

            outputArea.append("\nThe array is populated.\n");

        }//end try
        catch (IOException e) {
            outputArea.append("Error to read data file.");
        }
    }//GEN-LAST:event_readButtonActionPerformed

    private void outputButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_outputButtonActionPerformed
        // TODO add your handling code here:
        outputArea.setFont( new Font("Monospaced", Font.PLAIN, 12));
        
        for (int i = 0; i < itemList.length; i++) {
            outputArea.append(itemList[i] + "\n");
        }
    }//GEN-LAST:event_outputButtonActionPerformed

    private void totalButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_totalButtonActionPerformed
        // TODO add your handling code here:
        double sum = 0.0;
        for (int i = 0; i < itemList.length; i++) {
            sum += itemList[i].calculateInStockValue();
        }

        outputArea.append(String.format("%nTotal In-Stock Value: $ %.2f %n", sum) + "\n");

    }//GEN-LAST:event_totalButtonActionPerformed

    private void highestButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_highestButtonActionPerformed
        // TODO add your handling code here:
        int maxIndex = 0;

        for (int i = 0; i < itemList.length; i++) {
            if (itemList[maxIndex].calculateInStockValue()
                    < itemList[i].calculateInStockValue()) {

                maxIndex = i;
            }
        }

        outputArea.append("\nThe Highest In-Stock Value Item:\n");
        outputArea.append(itemList[maxIndex] + "\n");


    }//GEN-LAST:event_highestButtonActionPerformed

    private void searchButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_searchButtonActionPerformed
        // TODO add your handling code here:
        

        String searched = JOptionPane.showInputDialog("\nEnter a product to search");

        int foundIndex = search(itemList, searched);

        if (foundIndex == -1) {
            outputArea.append(searched + " is not found.\n");
        } else {
            outputArea.append(itemList[foundIndex] + "\n");
        }
    }//GEN-LAST:event_searchButtonActionPerformed
    //seach method
    private static int search(Invenory[] itemList, String searched) {

        for (int i = 0; i < itemList.length; i++) {
            if (itemList[i].getItemName().equalsIgnoreCase(searched)) {
                return i;
            }
        }

        return -1;
    }
    
    private void clearButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_clearButtonActionPerformed
        // TODO add your handling code here:
        outputArea.setText("");//clear text area
        
    }//GEN-LAST:event_clearButtonActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(GUIHardwareStore.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(GUIHardwareStore.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(GUIHardwareStore.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(GUIHardwareStore.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new GUIHardwareStore().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton SelectButton;
    private javax.swing.JButton clearButton;
    private javax.swing.JButton highestButton;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JButton lowButton;
    private javax.swing.JTextArea outputArea;
    private javax.swing.JButton outputButton;
    private javax.swing.JButton readButton;
    private javax.swing.JButton searchButton;
    private javax.swing.JButton totalButton;
    // End of variables declaration//GEN-END:variables
}
