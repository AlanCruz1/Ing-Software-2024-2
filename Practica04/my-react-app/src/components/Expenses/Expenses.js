import React from 'react';
import './Expenses.css'
import ExpenseItem from '../ExpenseItem/';
const Expenses = (props) => {
    const renderExpenses = ({concept,amount}) => {

    }
    return (
        <div>
            <ul>
                {props.expensesList.map((/expense) => {
                    <ExpenseItem expense ={expense}/>
                })}
            </ul>
        </div>
    );
}
export default Expenses;