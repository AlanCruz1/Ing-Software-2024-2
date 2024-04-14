import React from "react";
import './ExpenseItem.css';

function ExpenseItem ({concept, amount}){

    return(
        <li>
            <h2>Expense Item</h2>
            <div>{concept}</div>
            <div>${amount}</div>
        </li>
    )
}
export default ExpenseItem;