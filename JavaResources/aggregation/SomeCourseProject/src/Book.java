/**
 *
 * @author hm0481jg
 */
public class Book {
    private String isbn;
    private String title;
    private String author;
    private String publisher;
    private double price;

    public Book() {
    }

    public Book(String isbn, String title, String author, String publisher, double price) {
        this.isbn = isbn;
        this.title = title;
        this.author = author;
        this.publisher = publisher;
        this.price = price;
    }

    public String getIsbn() {
        return isbn;
    }

    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public String getPublisher() {
        return publisher;
    }

    public double getPrice() {
        return price;
    }

    @Override
    public String toString() {
        return isbn + " " + title + " " + author + " " + publisher + "$" + price;
    }
   
}
