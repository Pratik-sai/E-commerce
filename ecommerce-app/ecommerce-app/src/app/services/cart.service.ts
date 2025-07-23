import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CartService {
  private apiUrl = 'http://127.0.0.1:8000/od_app/carts';  // Replace with your Django API URL

  constructor(private http: HttpClient) { }

  // Get cart items
  getCartItems(): Observable<any> {
    return this.http.get(this.apiUrl);
  }

  // Add item to the cart
  addToCart(cartData: any): Observable<any> {
    return this.http.post(this.apiUrl, cartData);
  }

  // Remove item from the cart (if applicable)
  removeFromCart(cartItemId: number): Observable<any> {
    const url = `${this.apiUrl}/${cartItemId}/`;
    return this.http.delete(url);
  }
}
