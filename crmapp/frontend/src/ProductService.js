import axios from 'axios';

const API_URL = 'http://localhost:8000';

export default class ProductService{

    constructor(){}

    getProducts() {
        const url = `${API_URL}/api/products/`;
        return axios.get(url).then(response => response.data);
    }
    getProductssByURL(link) {
        const url = `${API_URL}${link}`;
        return axios.get(url).then(Response => Response.data);
    }
    getProduct(pk) {
        const url = `${API_URL}/api/products/${pk}`;
        return axios.get(url).then(Response => Response.data);
    }
    deleteProduct(product) {
        const url = `${API_URL}/api/products/${product.pk}`;
        return axios.delete(url);
    }
    createProduct(product) {
        const url = `${API_URL}/api/products/`;
        return axios.post(url,product, {
            headers: {
                'Content-Type': 'application/json'
            }
        });
    }
    updateCustomers(product) {
        const url = `${API_URL}/api/products/${product.pk}`;
        return axios.put(url,product,{
            headers: {
                'Content-Type': 'application/json'
            }
        });
    }
}