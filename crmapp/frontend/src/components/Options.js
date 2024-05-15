import Options from './components/Options';

const BaseLayout = () => (
  <div className="container-fluid">
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span className="navbar-toggler-icon"></span>
      </button>
      <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div className="navbar-nav">
          <a className="nav-item nav-link" href="/">CUSTOMERS</a>
          <a className="nav-item nav-link" href="/customer">CREATE CUSTOMER</a>
        </div>
        <div className="navbar-nav ml-auto">
          <Options />
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