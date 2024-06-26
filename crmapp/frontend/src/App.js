import  React, { Component } from  'react';
import { BrowserRouter, Routes, Route } from  'react-router-dom'
import  CustomersList  from  './components/CustomersList'
import  CustomerCreateUpdate  from  './components/CustomerCreateUpdate'
import  './App.css';


const BaseLayout = () => (
  <div className="container-fluid">
  <nav className="navbar navbar-expand-lg navbar-light bg-light">
  <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
    <span className="navbar-toggler-icon"></span>
  </button>
  <a className="navbar-brand" href="#">CRM</a>
  <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
    <div className="navbar-nav">
      <a className="nav-item nav-link" href="/">CUSTOMERS</a>
      <a className="nav-item nav-link" href="/customer">CREATE CUSTOMER</a>
    </div>
    <div className="navbar-nav ml-auto">
      <li className="nav-item">
        <a className="nav-link" href="/dashboard">Dashboard</a>
      </li>
      <li className="nav-item">
        <a className="nav-link" href="/customers">Customers</a>
      </li>
      <li className="nav-item">
        <a className="nav-link" href="/products">Products</a>
      </li>
      <li className="nav-item">
        <a className="nav-link" onClick={() => { localStorage.removeItem('token'); window.location.href = '/'; }}>Logout</a>
      </li>
    </div>
  </div>
</nav>

    <div className="content">
      <Routes>
        <Route path="/" exact element={<CustomersList/>} />
        <Route path="/customer/:pk?"  element={<CustomerCreateUpdate/>} />
        <Route path="/customer/" exact element={<CustomerCreateUpdate/>} />
      </Routes>

    </div>

  </div>
)

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <BaseLayout/>
      </BrowserRouter>
    );
  }
}

export default App;
