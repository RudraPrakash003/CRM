import React, { Component } from 'react';
import CustomerService from '../CustomerService';

const  customersService  =  new  CustomerService();

class CustomersList extends Component{

    constructor(props){
        super(props);
        this.state = {
            customers: [],
        };
        this.handleDelete = this.handleDelete.bind(this);
    }
    
    
    componentDidMount(){
        var  self  =  this;
	    customersService.getCustomers().then(function (result) {
		    self.setState({ customers:result})
        });
    }   
    handleDelete(e,pk){
        var  self  =  this;
        customersService.deleteCustomer({pk: pk}).then(()=>{
            var newArr = self.state.customers.filter(function(obj) {
                return obj.pk !==pk;
            });
            this.setState({customers: newArr})
        });
    }


    render() {
    
        return (
            <div  className="customers--list">
                <table  className="table">
                <thead  key="thead">
                <tr>
                    <th>#</th>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Email</th>
                    <th>Phone</th>
                    <th>Address</th>
                    <th>Actions</th>
                </tr>
                </thead>
                <tbody>
                {this.state.customers.map( c  =>
                    <tr  key={c.pk}>
                    <td>{c.pk}  </td>
                    <td>{c.first_name}</td>
                    <td>{c.last_name}</td>
                    <td>{c.email}</td>
                    <td>{c.phone_num}</td>
                    <td>{c.address}</td>
                    <td>
                    <button  onClick={(e)=>  this.handleDelete(e,c.pk) }> Delete</button>
                    <a  href={"/customer/" + c.pk}> Update</a>
                    </td>
                </tr>)}
                </tbody>
                </table>
            </div>
        );
    }
}


export default CustomersList;
