async function fetchExpenses() {
  const response = await fetch("/get_expenses");
  const expenses = await response.json();
  const expenseList = document.getElementById("expense-list");
  expenseList.innerHTML = "";
  expenses.forEach((expense) => {
    expenseList.innerHTML += `
            <tr>
                <td>${expense.description}</td>
                <td>${expense.amount}</td>
                <td><button onclick="removeExpense('${expense.description}')">Remove</button></td>
            </tr>
        `;
  });
}

async function addExpense() {
  const description = document.getElementById("description").value;
  const amount = document.getElementById("amount").value;

  if (description && amount) {
    await fetch("/add_expense", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ description, amount }),
    });
    document.getElementById("description").value = "";
    document.getElementById("amount").value = "";
    fetchExpenses();
  }
}

async function removeExpense(description) {
  await fetch("/remove_expense", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ description }),
  });
  fetchExpenses();
}

window.onload = fetchExpenses;
