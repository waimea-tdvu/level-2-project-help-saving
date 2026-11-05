# Project Final Review and Reflection

## Addressing Relevant Implications

### Usability

During the project, I focused on making the Savings and Expense Tracker simple and easy to use, as my main end-users are my mum and my sister. I created separate pages for the homepage, expense list, adding expenses and setting a weekly savings target. I also used clear labels, buttons and navigation links so users could access the main features without confusion. The forms allow users to enter expense information and savings targets directly.

However, further improvements could be made to make the system more convenient on mobile devices and reduce the time needed to record expenses.

### Privacy

The system stores personal financial information, including expense records, spending amounts and weekly savings targets in an SQLite database. I used parameterised SQL queries when inserting and retrieving information to help protect the database from unsafe user input.

However, the final system does not include a login or authentication feature. This means it does not yet provide separate private accounts for my mum and sister. If I developed the application further, I would add user authentication and access controls to protect each user's financial information.

### Functionality

I developed the main features based on the requirements identified in Sprint 0. Users can add daily expenses, view their expense records, filter expenses by date, delete unwanted records and set a weekly savings target. The homepage also provides an overview of savings information.

Some proposed features were not fully completed. For example, the automatic weekly summary, warning notifications and the smile face changing to a sad face when users approach or fall below their savings target were not fully implemented. The weekly expense summary also required further development to ensure that the correct information was displayed. These are important improvements I would consider in the future.



### Ethical

I considered the ethical impact of the application because its purpose is to encourage users to develop better financial habits. I wanted the system to help users understand their spending rather than make them feel guilty when they do not achieve their savings goals.

The use of a friendly smile face image on the homepage was intended to make the application feel more welcoming. I also aimed to present financial information clearly so users could make their own spending decisions. In the future, I would make sure that any warning messages use supportive language and encourage users to improve their financial habits instead of making them feel pressured.

### Legal

During development, I used technologies such as Python, Flask, SQLite, HTML, Jinja and CSS to build the application. I also used images in the website design. I considered the importance of using software, libraries and visual resources responsibly and respecting copyright and licensing requirements.

Because the application stores personal financial information, privacy and data protection are also important legal considerations. The current system would need stronger privacy and security features, such as user authentication and clearer information about how financial data is stored and used, before being used by multiple people.

## Overall Review

Overall, I successfully developed the main features of my Savings and Expense Tracker, including adding, viewing and deleting expenses, and setting weekly savings targets. I also improved my programming skills using Flask, SQLite, HTML and CSS.

One challenge was connecting the database to the webpages and displaying information correctly. Some proposed features, such as automatic notifications and the changing smile face, were not completed.

Testing helped me identify errors and improve the system's functionality and layout. If I could do this project again, I would plan more carefully, test each feature earlier and manage my time better.

Overall, the project helped me improve my coding, problem-solving and testing skills

