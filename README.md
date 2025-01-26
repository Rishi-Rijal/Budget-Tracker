<h1>Budget Tracker System</h1>

<p>A simple Python-based budget tracker that allows users to create and manage budget accounts, add transactions, and keep track of their financials. The system also validates emails and provides basic operations like changing user information.</p>

<h2>Features</h2>
<ul>
    <li>Email validation for users using <code>email_validator</code>.</li>
    <li>Create and manage budget accounts.</li>
    <li>Add and remove transactions for each account.</li>
    <li>Track account balance (income and expenses).</li>
    <li>Modify user information such as name and email.</li>
</ul>

<h2>Requirements</h2>
<ul>
    <li>Python 3.x</li>
    <li>email_validator library (Install via <code>pip install email-validator</code>)</li>
</ul>

<h2>Installation</h2>
<p>Clone the repository and install the dependencies:</p>
<pre><code>git clone https://github.com/Rishi-Rijal/Budget-Tracker.git
cd budget-tracker
pip install -r requirements.txt</code></pre>

<h2>Usage</h2>
<p>To use the Budget Tracker system, you can follow the steps below:</p>

<pre><code># Example usage:

# Create a new Person
person = Person("John Doe", "john.doe@example.com")

# Create a Budget Account for the person
account = BudgetAccount("Personal Expenses", person)

# Add transactions to the account
transaction1 = Transaction(100, "income", "Salary", account)
transaction2 = Transaction(50, "expense", "Groceries", account)

# Print account balance
print("Account Balance: $", account.get_balance())

# Get all transactions
account.get_transactions()

# Change user's email
person.change_email("new.email@example.com")
</code></pre>

<h2>Classes</h2>
<h3>Person</h3>
<p>The <code>Person</code> class represents a user with a name, email, and associated budget accounts. You can change a person's name, email, and manage their budget accounts.</p>

<h3>BudgetAccount</h3>
<p>The <code>BudgetAccount</code> class represents an individual budget account. It allows you to add and remove transactions, track the account's balance, and view the transaction history.</p>

<h3>Transaction</h3>
<p>The <code>Transaction</code> class represents a financial transaction (either income or expense). You can add a description and specify the amount of the transaction.</p>

<h2>Contributing</h2>
<p>If you'd like to contribute to the project, please fork the repository, create a branch, and submit a pull request. All contributions are welcome!</p>

