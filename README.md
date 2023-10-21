# final_project

"My Ex Libris" is a website where you can store the data of your personal library in an easy, straight-forward application. Users can create accounts to view their own dashboards which display the books they own as well as the locations of them. i.e. the hall bookcase, bedroom, or if it's on loan to a friend. This is a site meant for all bibliophiles who wish they could remember where they put their copy of Great Expectations or if they own that specific copy of Fahrenheit 451 while visiting their local bookstore.

The users of My Ex Libris will be able to:

    Add books to their library, which consists of:
        *The title
        *The author
        ISBN
        Book cover for their edition (we will use an API from OpenLibrary for calling book cover images based on the ISBN number)
        Genre
        Personal reviews
        If they would recommend the book to others
        Location of book (Specific room of house or on loan)
            If the book is on loan
            Who the book is loaned to
            Date book was loaned out
        Favorite quote
    Edit books
    View each author with their books that the user owns
    Delete books from library

This will have two tables, Users and Books, utilizing a one to many relationship. There will be a page to login and register, a homepage/dashboard which lists the books in a user's library starting with the most recent additions at the top, a page to view one book, a page to edit a book, and a page to view an author and their books.

Future developments to My Ex Libris would be an interactive site where users could become friends and view each other's libraries. Users could set certain books in a private list and others for their friends to see which would have the options to loan out to them. It could be a scaled back social media just for seeing each other's reviews on books and sharing with each other new books they just bought. There would also be an option for uploading their own photos of the books they add to their library, such as antique copies that are not listed with an isbn or sbn.

This project is a collaboration between @MollyDahl and Anna Dahl.
