import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import CustomerService from '../CustomerService';

const customersService = new CustomerService();

const CustomerCreateUpdate = () => {
    const { pk } = useParams();
    const [customer, setCustomer] = useState({
        first_name: '',
        last_name: '',
        email: '',
        phone_num: '',
        address: ''
    });

    useEffect(() => {
        if (pk) {
            customersService.getCustomer(pk)
                .then((customerData) => {
                    setCustomer(customerData);
                })
                .catch((error) => {
                    console.error('Error fetching customer data:', error);
                });
        }
    }, [pk]);

    const handleChange = (event) => {
        const { name, value } = event.target;
        setCustomer(prevCustomer => ({
            ...prevCustomer,
            [name]: value
        }));
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        if (pk) {
            // Handle update
            customersService.updateCustomers(customer)
                .then((result) => {
                    console.log(result);
                    alert("Customer updated!");
                })
                .catch((error) => {
                    console.error('Error updating customer:', error);
                    alert('There was an error! Please re-check your form.');
                });
        } else {
            // Handle create
            customersService.createCustomer(customer)
                .then((result) => {
                    console.log(result);
                    alert("Customer created!");
                })
                .catch((error) => {
                    console.error('Error creating customer:', error);
                    alert('There was an error! Please re-check your form.');
                });
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <div className="form-group">
                <label>First Name:</label>
                <input className="form-control" type="text" name="first_name" value={customer.first_name} onChange={handleChange} />
                
                <label>Last Name:</label>
                <input className="form-control" type="text" name="last_name" value={customer.last_name} onChange={handleChange} />
                
                <label>Email:</label>
                <input className="form-control" type="text" name="email" value={customer.email} onChange={handleChange} />
                
                <label>Phone:</label>
                <input className="form-control" type="text" name="phone_num" value={customer.phone_num} onChange={handleChange} />
              
                <label>Address:</label>
                <input className="form-control" type="text" name="address" value={customer.address} onChange={handleChange} />
                
                <input className="btn btn-primary" type="submit" value="Submit" />
            </div>
        </form>
    );
};

export default CustomerCreateUpdate;
